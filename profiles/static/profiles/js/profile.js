let countryField = document.getElementById('id_default_country');

window.addEventListener('load', function() {
    if (countryField.value == '') {
        countryField.classList.add('greyed');
    }
})

countryField.addEventListener('change', function() {
    if (countryField.value == '') {
        countryField.classList.remove('black');
        countryField.classList.add('greyed');
    } else {
        countryField.classList.remove('greyed');
        countryField.classList.add('black');
    }
})
