let counter = 0;
const teamsPerPage = 5;

document.addEventListener('DOMContentLoaded', function () {
    let orderSelector = document.querySelector('#order-selector');
    let teams = document.querySelector('#teams');
    load();
    //Whenever the order is changed, clear the teams div and fetch the teams in the new order
    orderSelector.addEventListener('change', () => {
        while (teams.firstChild) {
            teams.removeChild(teams.lastChild);
        }
        counter = 0;
        load();
    });
});

window.onscroll = () => {
    if (window.innerHeight + window.scrollY >= document.body.offsetHeight) {
        load();
    }
};

function add_team(team_data) {
    const team = document.createElement('div');
    team.className = 'team';
    const teams = document.querySelector('#teams');
    const name = document.createElement('h4');
    name.innerHTML = team_data.name;
    team.append(name);
    const username = document.createElement('h5');
    username.innerHTML = `by <a href="/profile/${team_data.username}">${team_data.username}</a>`;
    team.append(username);
    const row = document.createElement('div');
    row.className = 'row';
    team_data.members.forEach(pokemon => {
        const pkmn = document.createElement('div');
        pkmn.className = 'col-lg-2 col-sm-12';
        const image = document.createElement('img');
        image.className = "small-image";
        image.height = 125;
        image.width = 125;
        image.srcset = `https://pokeres.bastionbot.org/images/pokemon/${pokemon}.png`;
        pkmn.append(image);
        row.append(pkmn);
    });
    const points = document.createElement('p');
    points.className = 'point-counter';
    points.innerHTML = `${team_data.points} Points`;
    points.dataset.count = team_data.points;
    const likeButton = document.createElement('button');
    likeButton.dataset.id = team_data.id;
    if (team_data.liked) {
        likeButton.innerHTML = 'Unlike';
    }
    else {
        likeButton.innerHTML = 'Like';
    }
    likeButton.addEventListener('click', function () {
        let team = this.parentElement;
        if (this.innerHTML === 'Like') {
            like(this.dataset.id);
            for (i = 0; i < team.children.length; i++) {
                if (team.children[i].className === 'point-counter') {
                    team.children[i].dataset.count++;
                    team.children[i].innerHTML = `${team.children[i].dataset.count} Points`;
                }
            }
            this.innerHTML = 'Unlike';
        }
        else {
            unlike(this.dataset.id);
            for (i = 0; i < team.children.length; i++) {
                if (team.children[i].className === 'point-counter') {
                    team.children[i].dataset.count--;
                    team.children[i].innerHTML = `${team.children[i].dataset.count} Points`;
                }
            }
            this.innerHTML = 'Like';
        }
    });
    team.append(row);
    team.append(points);
    team.append(likeButton);
    teams.append(team);
}

function like(team_id) {
    let csrftoken = getCookie('csrftoken');
    fetch('/like', {
        method: 'PUT',
        body: JSON.stringify({
            like: true,
            team_id: team_id
        }),
        headers: { "X-CSRFToken": csrftoken }
    });
}

function unlike(team_id) {
    let csrftoken = getCookie('csrftoken');
    fetch('/like', {
        method: 'PUT',
        body: JSON.stringify({
            like: false,
            team_id: team_id
        }),
        headers: { "X-CSRFToken": csrftoken }
    });
}

// The following function was copied from the Django documentation at https://docs.djangoproject.com/en/dev/ref/csrf/#ajax
// It's used for getting the csrf token that is needed in order to send the PUT request
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}


