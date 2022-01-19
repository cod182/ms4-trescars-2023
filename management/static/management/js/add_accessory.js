let newImg = document.getElementById('new-image');
let imgContainer = document.getElementById('upload-image-container');
let img = document.createElement('img'); // creates and image
let removeBtn = document.createElement('a');

// on select image button change, get the image from files and display it
newImg.addEventListener('change', function () {
    imgContainer.innerHTML = '';

    removeBtn.classList.add('btn', 'red', 'fa', 'fa-remove', 'pointer');

    img.classList.add('img-thumb') // adds a class to the images
    img.setAttribute('alt', 'image of accessory'); //add al attribute to image
    img.setAttribute('src', URL.createObjectURL(newImg.files[0])); // adds src to image

    imgContainer.appendChild(img); // appends the label to the img container
    imgContainer.appendChild(removeBtn);

    // on load empties the mempry
    img.onload = function () {
        URL.revokeObjectURL(img.src) // free memory
    }
})

// when the remove button is clicked, the image is deleted from input files
removeBtn.addEventListener('click', function () {
    newImg.value = '';
    imgContainer.innerHTML = '';
})