function load() {
    const id = document.querySelector('#username').dataset.id;
    const orderSelector = document.querySelector('#order-selector');
    const start = counter;
    const end = counter + teamsPerPage; //non-inclusive
    counter = end;
    //Fetch the teams with the most popular teams first
    fetch(`/teams?order=${orderSelector.value}&start=${start}&end=${end}&user=${id}`)
        .then(response => response.json())
        .then(data => {
            console.log(data);
            data.teams.forEach(add_team);
        });
}