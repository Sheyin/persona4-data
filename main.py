
from flask import Flask, render_template, request
from school import school_data
from link import link_data
from lunch import lunch
from scrape import get_info_for, get_url_for, format_persona_input
import re


app = Flask(__name__)
# This allows the server to reload when changes are detected
app.config['DEBUG'] = True


@app.route('/')
@app.route('/index.html', methods=['GET'])
def index():
    return render_template('index.html', title="Persona 4 Data Compendium")


@app.route('/school', methods=['GET'])
@app.route('/school.html', methods=['GET'])
def school_pick_date():
    return render_template('school.html', title="School Questions")


@app.route('/daily/<date>', methods=['GET'])
def daily(date="april_may"):
    if date in ['april_may', 'june_july', 'sept_oct', 'nov_dec', 'jan_feb']:
        data = school_data[date]
        return render_template('daily.html',
                               date=data["date"],
                               daily_questions=data["data_school"],
                               )
    else:
        return "Error! You didn't pick a date range!"


@app.route('/exam/<date>', methods=['GET'])
def exam(date="april_may"):
    if date in ['april_may', 'june_july', 'sept_oct', 'nov_dec', 'jan_feb']:
        data = school_data[date]
        exam_data = simplify_exam_data(school_data[date]["data_exam"])
        return render_template('exam.html',
                               date=data["date"],
                               exam_header=data["data_exam"]["header"],
                               exam_data=simplify_exam_data(
                                   school_data[date]["data_exam"]),
                               )
    else:
        return "Error! You didn't pick a date range!"

# rebuilding a better object/dictionary to render data in template
# returns an array where each element is a dict that holds two entries:
# date (of that day) and data (with an array of tuples for each q-a pairing)


def simplify_exam_data(exam_data):
    keys = exam_data.keys()
    days = []
    # key will refer to "header", "day1", "day2", etc
    for key in keys:
        if key == "header":
            pass
        else:
            # inside each 'day1', 'day2' block
            # simplifying variable name
            data_for_the_day = exam_data[key]
            day_keys = data_for_the_day.keys()
            # rebuilding a better object/dictionary to render data in template
            day_data = {}
            day_data["date"] = data_for_the_day["date"]
            day_questions = []
            # Most exam days have only the date entry, but final days have a note as well
            if "note" in day_keys:
                number_of_questions = int((len(day_keys) - 2) / 2)
                day_data["note"] = data_for_the_day["note"]
            else:
                number_of_questions = int((len(day_keys) - 1) / 2)

            for number in range(1, number_of_questions):
                question_header = "question" + str(number) + "_question"
                answer_header = "question" + str(number) + "_answer"
                question_pairing = (
                    data_for_the_day[question_header],
                    data_for_the_day[answer_header]
                )
                day_questions.append(question_pairing)
            day_data["data"] = day_questions
            days.append(day_data)
    return days


@app.route('/links', methods=['GET'])
def social_links():
    name_list = link_data.keys()
    names = []
    for name in name_list:
        arcana = link_data[name]["arcana"]
        name = name.capitalize()
        data = (name, arcana)
        names.append(data)
    return render_template('links.html', title="Social Links",
                           names=names
                           )


@app.route('/link/<name_choice>', methods=['GET'])
def link(name_choice):
    name = name_choice.lower()
    info = link_data[name]
    # data = tidy_link_data(info["data"])
    # mostly destructuring the data for easier use in template
    return render_template('link.html',
                           title="Social Links",
                           name=info["name"],
                           arcana=info["arcana"],
                           schedule=info["schedule"],
                           # data=tidy_link_data(info["data"])
                           data=info["data"]
                           )


@app.route('/fusion', methods=['GET'])
@app.route('/calculator', methods=['GET'])
@app.route('/fusion.html', methods=['GET'])
@app.route('/calculator.html', methods=['GET'])
def hello_world():
    return render_template('calculator.html', title="Fusion Calculator")


@app.route('/lunch', methods=['GET'])
def lunch_render():
    return render_template('lunch.html',
                           title=lunch["header"],
                           lunches=lunch["data"],
                           date_title=lunch["dates_header"],
                           lunch_dates=lunch["dates_data"]
                           )


# This is an idea - search and scrape data about a specific persona (skills, etc)
@app.route('/persona', methods=['GET'])
def persona_search(persona=""):
    persona = request.args.get('persona', '')
    print("persona: " + persona)
    if persona == "":
        print("No persona given")
        return render_template('persona_search.html', title="Search for Persona Information")
    else:
        print("Received: " + persona)
        persona = request.args.get('persona', '')
        result = str(get_info_for(persona))
        return render_template('persona_search.html',
                               title="Stats for " +
                               format_persona_input(persona),
                               # result=result
                               result=change_color(result),
                               url=get_url_for(persona)
                               )


# @app.route('/quests.html', methods=['GET'])
# def quests():
#    return render_template('quests.html', title="Quests")

# Tidies up and formats the social link data, returns
# Because Flask prevents html from being rendered from said data, a workaround
# is to split the data here and repackage the string as an array in the template.


def tidy_link_data():
    name_list = link_data.keys()
    for name in name_list:
        link_data[name]["schedule"] = link_data[name]["schedule"].split('\n')
        personal_link_info = link_data[name]["data"]
        # the data is an array of dicts with header/data properties each element
        for rank in personal_link_info:
            rank["data"] = rank["data"].split('\n')
    return


# for the tables in persona search - colors came predefined in scraped text
# and they are a little dark
def change_color(text):
    lighter_grey_old = "#282828"
    darker_grey_old = "#222"
    lighter_grey_new = "#757575"
    darker_grey_new = "#5c5c5c"

    # Taking control of the table's styling
    table_string = """<table align="center" style="min-width:650px;text-align:center; background: #222; border:2px solid #FFE600; border-radius:10px; font-size:75%; font-family:verdana;">"""
    text = text.replace(table_string, '<table class="persona-info-table">')

    # Replace the colors of the rows since they are too dark (and hardcoded by source)
    text = text.replace(lighter_grey_old, lighter_grey_new)
    text = text.replace(darker_grey_old, darker_grey_new)

    # replace links with plain text
    regex = re.compile('<a href=(.*?)>')
    matches = re.findall(regex, text, flags=0)
    print("Found " + str(len(matches)) + " matches: ")
    print(matches)
    for match in matches:
        string_to_remove = "<a href=" + match + ">"
        text = text.replace(string_to_remove, '')
        text = text.replace("</a>", '')
    return text


# I want this to run on startup every time so it prevents errors
tidy_link_data()


if __name__ == '__main__':
    #app.run(debug=True, port=81, host='0.0.0.0')
    app.run(debug=True)
