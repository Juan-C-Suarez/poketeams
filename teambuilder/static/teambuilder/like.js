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