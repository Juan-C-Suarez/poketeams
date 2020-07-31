function load() {
    const orderSelector = document.querySelector('#order-selector');
    const start = counter;
    const end = counter + teamsPerPage; //non-inclusive
    counter = end;
    //Fetch the teams with the most popular teams first
    fetch(`/teams?order=${orderSelector.value}&start=${start}&end=${end}`)
        .then(response => response.json())
        .then(data => {
            console.log(data);
            data.teams.forEach(add_team);
        });
}