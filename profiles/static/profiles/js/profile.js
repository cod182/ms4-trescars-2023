let countryField = document.getElementById('id_default_country');

countryField.classList.add('greyed');

countryField.addEventListener('change', function() {
    if (countryField.value == '') {
        countryField.classList.remove('black');
        countryField.classList.add('greyed');
    } else {
        countryField.classList.remove('greyed');
        countryField.classList.add('black');
    }
})
