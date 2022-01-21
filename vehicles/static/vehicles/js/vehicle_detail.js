let deleteVehicleBtn = document.getElementById('delete-vehicle');
let motContainer = document.getElementById('mot-date');
let taxContaienr = document.getElementById('tax-date');


function myFunction(imgs) {
    // Get the expanded image
    var expandImg = document.getElementById("expandedImg");
    // Get the image text
    var imgText = document.getElementById("imgtext");
    // Use the same src in the expanded image as the image being clicked on from the grid
    expandImg.src = imgs.src;
    // Show the container element (hidden with CSS)
    expandImg.parentElement.style.display = "block";
}



function ChangeFormateDate(container, oldDate) {
    newDate = oldDate.toString().split("-").reverse().join("/");
    container.innerHTML = newDate
}
if (motContainer) {
    ChangeFormateDate(motContainer, motContainer
        .innerHTML); // Changes the date from DB format to readable for MOT date
}

if (taxContaienr) {
    ChangeFormateDate(taxContaienr, taxContaienr
        .innerHTML); // Changes the date from DB format to readable for Tax date
}

// initial click prevents delete button from working and changes
// text to 'are you sure?
// second click completes button funciton
deleteVehicleBtn.addEventListener('click', function (event) {
    if (deleteVehicleBtn.innerText == "Are Your Sure?") {
        deleteVehicleBtn.innerText = "Delete";
    } else {
        event.preventDefault();
        deleteVehicleBtn.innerText = "Are Your Sure?";
    }
})