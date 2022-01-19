let newImg = document.getElementById('new-image');
let imgContainer = document.getElementById('upload-image-container');

// on select image button change, get the image from files and display it
newImg.addEventListener('change', function () {
    let img = document.createElement('img'); // creates and image

    img.classList.add('img-thumb') // adds a class to the images
    img.setAttribute('alt', 'image of accessory'); //add al attribute to image
    img.setAttribute('src', URL.createObjectURL(newImg.files[0])); // adds src to image

    imgContainer.appendChild(img); // appends the label to the img container

    // on load empties the mempry
    img.onload = function () {
        URL.revokeObjectURL(img.src) // free memory
    }
})