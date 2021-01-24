import re

# for the tables in persona search - colors came predefined in scraped text
# and they are a little dark


def change_color(text):
    lighter_grey_old = "#282828"
    darker_grey_old = "#222"
    lighter_grey_new = "#757575"
    darker_grey_new = "#5c5c5c"

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


if __name__ == "__main__":
    text = """<td style="background:#282828">12 SP
</td>
<td style="background:#282828;text-align:left;padding-left:5px">Deals heavy Fire damage to 1 foe.
</td>
<td style="background:#282828">56
</td></tr>
<tr>
<th style="background:#000;color:#fff"><a href="/wiki/Endure_Light" title="Endure Light">Endure Light</a>
</th>
<td style="background:#222">Passive
</td>
<td style="background:#222;text-align:left;padding-left:5px">Automatically survive instant death 1 time<br>from a Light attack with 1 HP.
</td>
<td style="background:#222">57
</td></tr>
<tr>
<th style="background:#000;color:#fff"><a href="/wiki/Tetra_Break" title="Tetra Break">Tetra Break</a>
</th>
<td style="background:#282828">18 SP
</td>
<td style="background:#282828;text-align:left;padding-left:5px">Negates all foes' Tetrakarn.
</td>
<td style="background:#282828">60
</td></tr>"""
    print(change_color(text))
