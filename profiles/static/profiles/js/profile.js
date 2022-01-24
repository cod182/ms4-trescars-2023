let countryField = document.getElementById('id_default_country');
let hideSearchBtn = document.getElementById('hide-profile-info');
let profileInfo = document.getElementById('profile-info');
let storedProfileOption = localStorage.getItem('storedProfileOption');
const deleteProfileInfoBtn = document.getElementById('delete-profile-info');

//Checks if storedProfileOption is hidden in local storage
if (storedProfileOption === 'hidden') {
    hideProfileInfo();
}

// on window load, country is greyed if value empty
window.addEventListener('load', function () {
    if (countryField.value == '') {
        countryField.classList.add('greyed');
    }
});

// when country field is changed
// adds grey text if empty
// adds black text if option selected
countryField.addEventListener('change', function () {
    if (countryField.value == '') {
        countryField.classList.remove('black');
        countryField.classList.add('greyed');
    } else {
        countryField.classList.remove('greyed');
        countryField.classList.add('black');
    }
});

// hide profile info and stores setting in storage
function hideProfileInfo() {
    hideSearchBtn.innerText = 'Show Profile Info';
    profileInfo.classList.add('hidden');
    localStorage.setItem('storedProfileOption', 'hidden');
}

// hide profile info and stores setting in storage
function showProfileInfo() {
    hideSearchBtn.innerText = 'Hide Info';
    profileInfo.classList.remove('hidden');
    localStorage.setItem('storedProfileOption', 'visable');
}

// button clicked, hides/hide profile info
hideSearchBtn.addEventListener('click', function () {
    if (hideSearchBtn.innerText == 'Hide Info') {
        hideProfileInfo();
    } else {
        showProfileInfo();
    }
});

// initial click prevents delete button from working and changes
// text to 'are you sure?
// second click completes button funciton
deleteProfileInfoBtn.addEventListener('click', function (event) {
    if (deleteProfileInfoBtn.innerText == "Are Your Sure?") {
        deleteProfileInfoBtn.innerText = "Delete Info";
        deleteProfileInfoBtn.classList.remove('bg-red');
    } else {
        event.preventDefault();
        deleteProfileInfoBtn.innerText = "Are Your Sure?";
        deleteProfileInfoBtn.classList.add('bg-red');
    }
});