let sortSelector = document.getElementById('sort-selector');
let deleteAccessoryBtn = document.getElementsByClassName('delete-accessory');

// when sort chaned submits to backend
sortSelector.addEventListener('change', function () {
    let currentUrl = new URL(window.location);
    let sortSelectorVal = sortSelector.value;
    if (sortSelectorVal != 'reset') {
        let sort = sortSelectorVal.split("_")[0];
        let direction = sortSelectorVal.split("_")[1];

        currentUrl.searchParams.set("sort", sort);
        currentUrl.searchParams.set("direction", direction);

        window.location.replace(currentUrl);
    } else {
        currentUrl.searchParams.delete("sort");
        currentUrl.searchParams.delete("direction");

        window.location.replace(currentUrl);
    }
});

// initial click prevents delete button from working and changes
// text to 'are you sure?
// second click completes button funciton
for (let i = 0; i < deleteAccessoryBtn.length; i++) {
    deleteAccessoryBtn[i].addEventListener('click', function (event) {
        if (deleteAccessoryBtn[i].innerText == "Are Your Sure?") {
            deleteAccessoryBtn[i].innerText = "Delete";
        } else {
            event.preventDefault();
            deleteAccessoryBtn[i].innerText = "Are Your Sure?";
        }
    });
}