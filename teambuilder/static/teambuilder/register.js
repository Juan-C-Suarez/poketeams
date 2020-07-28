document.addEventListener('DOMContentLoaded', function(){
    let favorite_pokemon = document.querySelector('#favorite_pokemon');

    fetch('https://pokeapi.co/api/v2/pokemon?limit=807')
    .then(response => response.json())
    .then(result => {
        for(i = 0; i < 892; i++){
            let option = document.createElement('option');
            option.value = `${i+1}`;
            option.innerHTML = result.results[i].name;
            favorite_pokemon.append(option);
        }
    });
});