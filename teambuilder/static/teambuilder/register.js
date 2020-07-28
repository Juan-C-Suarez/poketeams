document.addEventListener('DOMContentLoaded', function(){
    let favorite_pokemon = document.querySelector('#favorite_pokemon');
    favorite_pokemon.addEventListener('change', () => {
        let image = document.querySelector('img');
        image.srcset = `https://pokeres.bastionbot.org/images/pokemon/${favorite_pokemon.value}.png`;
        image.style.display = 'block';
    });

    fetch('https://pokeapi.co/api/v2/pokemon?limit=807')
    .then(response => response.json())
    .then(result => {
        for(i = 0; i < 807; i++){
            let option = document.createElement('option');
            option.value = `${i+1}`;
            option.innerHTML = result.results[i].name.charAt(0).toUpperCase() + result.results[i].name.slice(1);
            favorite_pokemon.append(option);
        }
    });
});