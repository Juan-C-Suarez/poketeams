document.addEventListener('DOMContentLoaded', function () {
    const title = document.querySelector('#search-title');
    const number = title.dataset.id;
    fetch(`https://pokeapi.co/api/v2/pokemon/${number}`)
    .then(response => response.json())
    .then(data => {
        title.innerHTML = data.name.charAt(0).toUpperCase() + data.name.slice(1);
    });
});

function load() {
    const id = document.querySelector('#search-title').dataset.id;
    const orderSelector = document.querySelector('#order-selector');
    const start = counter;
    const end = counter + teamsPerPage; //non-inclusive
    counter = end;
    //Fetch the teams with the most popular teams first
    fetch(`/teams?order=${orderSelector.value}&start=${start}&end=${end}&pokemon=${id}`)
        .then(response => response.json())
        .then(data => {
            console.log(data);
            data.teams.forEach(add_team);
        });
}