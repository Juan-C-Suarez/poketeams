document.addEventListener('DOMContentLoaded', function(){
    let speciesSelector1 = document.querySelector('#species1');
    let speciesSelector2 = document.querySelector('#species2');
    let speciesSelector3 = document.querySelector('#species3');
    let speciesSelector4 = document.querySelector('#species4');
    let speciesSelector5 = document.querySelector('#species5');
    let speciesSelector6 = document.querySelector('#species6');

    let natureSelector1 = document.querySelector('#nature1');
    let natureSelector2 = document.querySelector('#nature2');
    let natureSelector3 = document.querySelector('#nature3');
    let natureSelector4 = document.querySelector('#nature4');
    let natureSelector5 = document.querySelector('#nature5');
    let natureSelector6 = document.querySelector('#nature6');
    let itemSelector1 = document.querySelector('#item1');
    let itemSelector2 = document.querySelector('#item2');
    let itemSelector3 = document.querySelector('#item3');
    let itemSelector4 = document.querySelector('#item4');
    let itemSelector5 = document.querySelector('#item5');
    let itemSelector6 = document.querySelector('#item6');

    //Make visible all the selectors corresponding to the selected Pokemon and fetch their pokemon-specific options
    speciesSelector1.addEventListener('change', () => {
        initializeSelectors(speciesSelector1, natureSelector1, itemSelector1,
            document.querySelector('#ability1'), document.querySelector('#move1-1'), document.querySelector('#move1-2'),
            document.querySelector('#move1-3'), document.querySelector('#move1-4'), document.querySelector('#img1'), document.querySelector('#move-title1'))
        });

    speciesSelector2.addEventListener('change', () => {
        initializeSelectors(speciesSelector2, natureSelector2, itemSelector2,
            document.querySelector('#ability2'), document.querySelector('#move2-1'), document.querySelector('#move2-2'),
            document.querySelector('#move2-3'), document.querySelector('#move2-4'), document.querySelector('#img2'), document.querySelector('#move-title2'))
        });

    speciesSelector3.addEventListener('change', () => {
        initializeSelectors(speciesSelector3, natureSelector3, itemSelector3,
            document.querySelector('#ability3'), document.querySelector('#move3-1'), document.querySelector('#move3-2'),
            document.querySelector('#move3-3'), document.querySelector('#move3-4'), document.querySelector('#img3'), document.querySelector('#move-title3'))
        });

    speciesSelector4.addEventListener('change', () => {
        initializeSelectors(speciesSelector4, natureSelector4, itemSelector4,
            document.querySelector('#ability4'), document.querySelector('#move4-1'), document.querySelector('#move4-2'),
            document.querySelector('#move4-3'), document.querySelector('#move4-4'), document.querySelector('#img4'), document.querySelector('#move-title4'))
        });

    speciesSelector5.addEventListener('change', () => {
        initializeSelectors(speciesSelector5, natureSelector5, itemSelector5,
            document.querySelector('#ability5'), document.querySelector('#move5-1'), document.querySelector('#move5-2'),
            document.querySelector('#move5-3'), document.querySelector('#move5-4'), document.querySelector('#img5'), document.querySelector('#move-title5'))
        });
    
    speciesSelector6.addEventListener('change', () => {
        initializeSelectors(speciesSelector6, natureSelector6, itemSelector6,
            document.querySelector('#ability6'), document.querySelector('#move6-1'), document.querySelector('#move6-2'),
            document.querySelector('#move6-3'), document.querySelector('#move6-4'), document.querySelector('#img6'), document.querySelector('#move-title6'))
        });
    

    //Fetch all options for the pokemon selector
    fetch('https://pokeapi.co/api/v2/pokemon?limit=807')
    .then(response => response.json())
    .then(result => {
        for(i = 0; i < 807; i++){
            let option = document.createElement('option');
            option.value = i+1;
            option.innerHTML = result.results[i].name.charAt(0).toUpperCase() + result.results[i].name.slice(1);
            speciesSelector1.append(option);
            speciesSelector2.append(option.cloneNode(true));
            speciesSelector3.append(option.cloneNode(true));
            speciesSelector4.append(option.cloneNode(true));
            speciesSelector5.append(option.cloneNode(true));
            speciesSelector6.append(option.cloneNode(true));
        }
    });

    //Fetch all options for the nature selector
    fetch('https://pokeapi.co/api/v2/nature?limit=25')
    .then(response => response.json())
    .then(result => {
        result.results.forEach((nature) => {
            let option = document.createElement('option');
            option.value = nature.name;
            option.innerHTML = nature.name.charAt(0).toUpperCase() + nature.name.slice(1);
            natureSelector1.append(option);
            natureSelector2.append(option.cloneNode(true));
            natureSelector3.append(option.cloneNode(true));
            natureSelector4.append(option.cloneNode(true));
            natureSelector5.append(option.cloneNode(true));
            natureSelector6.append(option.cloneNode(true));
        });
    });

    //Fetch all items for the item selector
    fetch('https://pokeapi.co/api/v2/item?limit=954')
    .then(response => response.json())
    .then(result => {
        result.results.forEach((item) => {
            let option = document.createElement('option');
            option.value = item.name;
            option.innerHTML = item.name.charAt(0).toUpperCase() + item.name.slice(1);
            itemSelector1.append(option);
            itemSelector2.append(option.cloneNode(true));
            itemSelector3.append(option.cloneNode(true));
            itemSelector4.append(option.cloneNode(true));
            itemSelector5.append(option.cloneNode(true));
            itemSelector6.append(option.cloneNode(true));
        });
    });
});

function initializeSelectors(speciesSelector, natureSelector, itemSelector, abilitySelector, moveSelector1, moveSelector2, moveSelector3, moveSelector4, image, moveTitle){
    image.srcset = `https://pokeres.bastionbot.org/images/pokemon/${speciesSelector.value}.png`;
    image.style.display = 'block';
    abilitySelector.style.display = 'block';
    natureSelector.style.display = 'block';
    itemSelector.style.display = 'block';
    moveSelector1.style.display = 'block';
    moveSelector2.style.display = 'block';
    moveSelector3.style.display = 'block';
    moveSelector4.style.display = 'block';
    moveTitle.style.display = 'block';
    abilitySelector.required = true;
    natureSelector.required = true;
    itemSelector.required = true;
    moveSelector1.required = true;
    moveSelector2.required = true;
    moveSelector3.required = true;
    moveSelector4.required = true;
    fetch(`https://pokeapi.co/api/v2/pokemon/${speciesSelector.value}`)
    .then(response => response.json())
    .then(result => {  
        while (abilitySelector.firstChild) {
            abilitySelector.removeChild(abilitySelector.lastChild);
        }
        let defaultOption = document.createElement('option');
        defaultOption.selected = true;
        defaultOption.value = "";
        defaultOption.disabled = true;
        defaultOption.innerHTML = 'Choose an Ability';
        abilitySelector.append(defaultOption);
        abilitySelector.value = "";
        result.abilities.forEach(ability => {
            let option = document.createElement('option');
            option.value = ability.ability.name;
            option.innerHTML = ability.ability.name.charAt(0).toUpperCase() + ability.ability.name.slice(1);
            abilitySelector.append(option);
        });

        let defaultMove = document.createElement('option');
        defaultMove.selected = true;
        defaultMove.value = "";
        defaultMove.disabled = true;
        defaultMove.innerHTML = 'Choose a Move';
        
        while (moveSelector1.firstChild) {
            moveSelector1.removeChild(moveSelector1.lastChild);
        }
        moveSelector1.append(defaultMove);
        moveSelector1.value = "";
        
        while (moveSelector2.firstChild) {
            moveSelector2.removeChild(moveSelector2.lastChild);
        }
        moveSelector2.append(defaultMove.cloneNode(true));
        moveSelector2.value = "";
        
        while (moveSelector3.firstChild) {
            moveSelector3.removeChild(moveSelector3.lastChild);
        }
        moveSelector3.append(defaultMove.cloneNode(true));
        moveSelector3.value = "";
        
        while (moveSelector4.firstChild) {
            moveSelector4.removeChild(moveSelector4.lastChild);
        }
        moveSelector4.append(defaultMove.cloneNode(true));
        moveSelector4.value = "";

        result.moves.forEach(move => {
            let option = document.createElement('option');
            option.value = move.move.name;
            option.innerHTML = move.move.name.charAt(0).toUpperCase() + move.move.name.slice(1);
            moveSelector1.append(option);
            moveSelector2.append(option.cloneNode(true));
            moveSelector3.append(option.cloneNode(true));
            moveSelector4.append(option.cloneNode(true));
        })
    });
}