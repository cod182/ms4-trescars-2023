let make = document.getElementById('make');
let model = document.getElementById('model');

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