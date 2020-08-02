document.addEventListener('DOMContentLoaded', function () {
    let names = document.querySelectorAll('.pokemon-name').forEach(name => {
        fetch(`https://pokeapi.co/api/v2/pokemon/${name.dataset.id}`)
        .then(response => response.json())
        .then(data => {
            name.innerHTML = data.name.charAt(0).toUpperCase() + data.name.slice(1);
        });
    });

    //Fetch all options for the pokemon selector
    fetch('https://pokeapi.co/api/v2/pokemon?limit=807')
    .then(response => response.json())
    .then(result => {
        let pokemonSelector = document.querySelector("#pokemon_selector");
        for(i = 0; i < 807; i++){
            let option = document.createElement('option');
            option.value = i+1;
            option.innerHTML = result.results[i].name.charAt(0).toUpperCase() + result.results[i].name.slice(1);
            pokemonSelector.append(option);
        }
    });

    document.querySelector('#search-button').addEventListener('click', () => {
        let pokemonSelector = document.querySelector("#pokemon_selector");
        if(pokemonSelector.value !== ''){
            document.location.href = `/pokemon/${pokemonSelector.value}`;
        }
    });
});