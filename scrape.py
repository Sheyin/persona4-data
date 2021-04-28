from bs4 import BeautifulSoup
import requests
from personadata import list_of_persona_names


def get_info_for(persona):
    # Format input, make sure it's spelled and capitalized correctly, etc
    persona = format_persona_input(persona)
    print("Persona received: ===" + persona + "===")

    # Double check it against a list of properly spelled names?
    if is_valid_persona(persona):
        # Here, we're just importing both Beautiful Soup and the Requests library
        page_link = 'https://megamitensei.fandom.com/wiki/' + persona
        # https://megamitensei.fandom.com/wiki/Kali#Persona_4
        # this is the url that we've already determined is safe and legal to scrape from.
        page_response = requests.get(page_link, timeout=5)
        # here, we fetch the content from the url, using the requests library
        soup = BeautifulSoup(page_response.content, "html.parser")

        p4header = soup.find_all(id='Persona_4')[0].parent
        stats = p4header.find_next('table')

        type(stats)
        """
        # Strip all the formatting
        for tag in stats:
            for attribute in ["class", "id", "name", "style"]:
                del tag[attribute]
        """
        return stats
    else:
        errorString = f'Sorry, {persona} is not a valid persona.  Please try again.'
        return errorString


# Helper function to populate the attribution url
# Should only be called after a valid result was already found and returned.
def get_url_for(persona):
    return 'https://megamitensei.fandom.com/wiki/' + format_persona_input(persona)


def is_valid_persona(input):
    if input in list_of_persona_names:
        return True
    else:
        return False


# This takes the name of a persona (input/string) and makes sure it is formatted
# to work correctly with the other functions (first letter of each word capitalized, no trailing spaces)
def format_persona_input(persona):
    persona = persona.rstrip()
    # in case of multi-word names
    namelist = persona.split(' ')
    formattedInput = ""
    for _ in namelist:
        if _ == namelist[0]:
            formattedInput = namelist[0].capitalize()
        else:
            formattedInput += " " + _.capitalize()
    return formattedInput.rstrip()


if __name__ == "__main__":
    #persona = input("Name of persona: ")
    # print(get_info_for(persona))
    print("Running")
    get_info_for("Kali")
