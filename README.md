# Persona 4 Data Site

This is a site made for personal use - I found it difficult to look up information on my aging iPad while playing due to non-mobile-friendly sites (many large images, small search boxes, ads slowing down loading time, etc.).  So my solution was to make a proxy site of sorts - some of the information is stored locally, some of it is pulled from a wiki.  This allowed me to centralize the information and make some visual/usability improvements.  This application is normally hosted on a raspberry pi and not available publicly.

Of course, it has taken me _much_ longer to work on this site than I have been actually playing the game... but I suppose I'll be ready for the next time I pick it up!

## Features
- Larger links / clickable areas
- High-contrast colors for better visibility
- No images - all the design is done with CSS
- Search will suggest names as they are entered into the search box.  The suggestions can then be clicked/tapped for faster searching.
- Search will scrape persona data from the wiki and display the stats / skills.
- Most of the heavy lifting is done server-side, with a minimum of javascript to aid with typing input.
- All the information/links I've needed to look up during a play session is all in one place, including social link guides, school questions, lunch ingredients, and the fusion calculator.
- No ads!

## Progress / Bugs
- All the links are functional, but some areas still need to be refined.  
- Lunch data needs to be formatted and organized.
- Some of the school questions may not be linked to the correct dates.  (This requires some testing)
- Search is working, but the results are sometimes improperly formatted. (Unsure if this is due to the source, formatting on my end, or both)
- Clipping on the calculator iframe.  I haven't figured out a solution to this yet.
- Some of the information may be incorrect (ex. lunch favorites/dates) - this was due to some scarcity of information (and really isn't that significant).  As this is an older/unchanging game, most of the data should be correct, assuming it was displayed correctly here.
- Quest data - no progress made on this yet.  
- Formatting may look odd depending on different orientation / resolution - I haven't properly tweaked this yet, but it's been good enough so far.


## Attribution
- https://arantius.github.io/persona-fusion-calculator/4golden.html#/list/level
- http://megamitensei.fandom.com/
- https://www.rpgsite.net/feature/9850-persona-4-golden-social-link-guide-dialogue-options-love-interests-and-full-s-link-walkthroughs
