let make = document.getElementById('vehicle-make-search');
let model = document.getElementById('vehicle-model-search');
let hideSearchBtn = document.getElementById('hide-search');
let searchOptions = document.getElementsByClassName('detail-options');
let storedSearchOption = localStorage.getItem('searchOptions');
let sortSelector = document.getElementById('sort-selector');


//Checks if latest games is enabled in local storage
if (storedSearchOption === 'hidden') {
    hideSearchOptions();
};

// removes the disabled attribute from the model input
function makeEnteredAllowModel() {
    model.removeAttribute('disabled');
}

// if make not select, model is disabled
// if the make is selected, the model option is available
// data-vehicle-make on the model options is checked and only ones matching the make are shown
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

// 
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

function hideSearchOptions() {
    for (var i = 0; i < searchOptions.length; i++) {
        hideSearchBtn.innerText = 'Show'
        searchOptions[i].classList.add('less-options')
        localStorage.setItem('searchOptions', 'hidden');
    }
}

function showSearchOptions() {
    for (var i = 0; i < searchOptions.length; i++) {
        hideSearchBtn.innerText = 'Hide'
        searchOptions[i].classList.remove('less-options')
        localStorage.setItem('searchOptions', 'visable');
    }
}

hideSearchBtn.addEventListener('click', function() {
    if (hideSearchBtn.innerText == 'Hide'){
        hideSearchOptions();
    } else {
        showSearchOptions();
    }
})