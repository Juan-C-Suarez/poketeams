document.addEventListener('DOMContentLoaded', function () {
    let names = document.querySelectorAll('.name').forEach(name => {
        //Fetch all items for the item selector
        fetch(`https://pokeapi.co/api/v2/pokemon/${name.dataset.id}`)
        .then(response => response.json())
        .then(data => {
            name.innerHTML = data.name.charAt(0).toUpperCase() + data.name.slice(1);
        });
    });
    let button =  document.querySelector('.like-button');
    console.log(button.dataset.liked);
    if (button.dataset.liked === 'True') {
        button.innerHTML = 'Unlike';
    }
    else {
        button.innerHTML = 'Like';
    }
    button.addEventListener('click', function() {
        if (this.innerHTML === 'Like') {
            like(this.dataset.id);
            let counter = document.querySelector('.point-counter');
            counter.dataset.count++;
            counter.innerHTML = `${counter.dataset.count} Points`;
            this.innerHTML = 'Unlike';
        }
        else {
            unlike(this.dataset.id);
            let counter = document.querySelector('.point-counter');
            counter.dataset.count--;
            counter.innerHTML = `${counter.dataset.count} Points`;
            this.innerHTML = 'Like';
        }
    })
});