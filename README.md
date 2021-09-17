# Poketeams by Juan Carlos Suárez Jaimes
Poketeams is a web application that allows users to build teams for Pokemon games and also 
view the teams created by other users. This web application uses the API **PokeAPI** for getting
data about Pokemon, items, moves, etc.

## Features
1. **Teambuilder:** Logged in users can create a Pokemon team. Each team has six Pokemon
chosen by the user. The user chooses the ability, nature, held item and moves of each
of the team's Pokemon. All these choices are displayed using select elements that are populated
with the options fetched from PokeAPI. Additionally, the user is supposed to name the team
and describe their strategy in a textarea.

2. **Team Lists:** The index page, profile page and Pokemon page display lists of teams
created by users. The selection of teams displayed varies depending on the page, but all
share the following features:

    1. A select element is used to choose the ordering method. The options are most popular teams
first (teams with the most points), newest teams first and oldest teams first.

    2. Infinite Scroll: Only five teams are loaded at first, but as the user scrolls down, the next
five teams are loaded.

    3. If logged in, the user can click a button to like or unlike (if already liked) a team.
Liking a team increases its number of points.

3. **Profile Page:** Clicking on a username takes the user to the corresponding profile page.
The profile displays an image of the user's avatar, the user's total points (sum of the points
form all their posts) and a list of all the teams submitted by the user, as described in the
Team List feature.

4. **Stats:** The stats page displays a list of the top 10 most used Pokemon, along with the number
of teams that Pokemon was incluided in. The page also displays a selector the user can use
in order to go to that Pokemon's page.

5. **Pokemon Page:** Clicking on a Pokemon's name or searching it using the stats page takes the
user to that Pokemon's page, which displays a list of all the teams that include that Pokemon,
as described in the Team List Feature.

6. **Team Page:** Clicking on a team's name takes the user to that team's page, which displays
detailed information about the team and each of its Pokemon. It's also possible to like or unlike
the team using this page's like button.

7. **Accounts:** Users can login, register and logout from the website.

## What's contained in each file
* poketeams: project directory
    * urls.py: project urls, it was only modified to add the app's url.
    * settings.py: project settings, it was only modified to install the application.
    * (The rest of the files here were automatically created bu Django and were not manually modified.)
* teambuilder: application's directory
    * static/teambuilder: directory containing all the javascript and CSS files.
        * index.js: file containing the load function used for loading teams for the index page.
        * like.js: file containing the functions used for liking and unliking teams.
        * pokemon.js: file containing the load function used for loading teams for the Pokemon page. Also includes the code for fetching the Pokemon's name.
        * profile.js: file containing the load function used for loading teams for the profile page.
        * register.js: file containing the code used in the registration page for fetching Pokemon names and getting the Pokemon image.
        * stats.js: file containing the code used in the stats page for fetching Pokemon names and setting up event-handlers.
        * team.js: file containing the code used in the team page for fetching Pokemon names and setting up event-handlers.
        * team_list.js: file containing the code used in the index, profile and pokemon pages for fetching Pokemon teams taking into account the selected order and infinite scroll.
        * teambuilder.js: file containing the code used in the teambuilder page for populating the select elements.
        * style.css: CSS file used for the styling of the whole website.
    * teamplates/teambuilder: directory containing all HTML files.
        * error.html: HTML page for displaying errors.
        * index.html: HTML file for the index page.
        * layout.html: Layout file. The rest HTML files extend it.
        * login.html: HTML file for the login page.
        * pokemon.html: HTML file for the pokemon page.
        * profile.html: HTML file for the profile page.
        * register.html: HTML file for the register page.
        * stats.html: HTML file for the stats page.
        * team.html: HTML file for the team page.
        * teambuilder.html: HTML file for the teambuilder page.
    * models.py: file where the models are defined
    * urls.py: app's urls
    * views.py: views file with all the server-side code for all the views
    * (The rest of the files here were automatically created by Django and were not manually modified.)
* db.sqlite3: Database file.
* manage.py


