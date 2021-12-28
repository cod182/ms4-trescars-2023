let make = document.getElementById('vehicle-make-search');
let model = document.getElementById('vehicle-model-search');

function makeEnteredAllowModel() {
    model.removeAttribute('disabled');
}

function checkCorrectMakesForModel() {
    for (var x=0; x < model.options.length; x++) {
        makeCheck = model.options[x].getAttribute('data-vehicle-make')
        if ( make.value.toLowerCase() == makeCheck ) {
            model.options[x].classList.remove('hidden');
            model.value = model.options[0].value;
        } else if (makeCheck != make.value.toLowerCase()){
            model.options[x].classList.add('hidden');
            model.value = model.options[0].value;
        }
    }
}

make.addEventListener('change', function() {
    makeEnteredAllowModel();
    checkCorrectMakesForModel();
    if (make.selectedOptions[0].innerHTML == 'Make') {
        make.classList.add('greyed');
        model.classList.add('greyed');
    } else {
        make.classList.remove('greyed');
        model.classList.remove('greyed');
    }
})

let sortSelector = document.getElementById('sort-selector');

sortSelector.addEventListener('change', function() {
    let currentUrl = new URL(window.location);
    let sortSelectorVal = sortSelector.value;
    if (sortSelectorVal != 'reset') {
        let sort = sortSelectorVal.split("_")[0];
        let direction = sortSelectorVal.split("_")[1];
    
        currentUrl.searchParams.set("sort", sort);
        currentUrl.searchParams.set("direction", direction);
    
        window.location.replace(currentUrl)
    } else {
        currentUrl.searchParams.delete("sort");
        currentUrl.searchParams.delete("direction");
    
        window.location.replace(currentUrl);
    }
})
