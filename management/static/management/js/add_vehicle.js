let imgsContainer = document.getElementById('images-container');


// called by click on image upload
let loadFile = function (event) {
    imgsContainer.innerHTML = ''; // empties the img container
    for (let i = 0; i < event.target.files.length; i++) {
        let imgInputLabel = document.createElement('label'); // Creates a label
        let imgInput = document.createElement('input'); // creates and input
        let img = document.createElement('img'); // creates and image

        imgInputLabel.appendChild(imgInput); // appends the input to the label
        imgInputLabel.appendChild(img); // appends the image to the label

        imgInput.setAttribute('type', 'radio'); // sets the lable type
        imgInput.setAttribute('name', 'main'); // sets the label name
        imgInput.setAttribute('required', true); // sets the label to required
        imgInput.setAttribute('value', event.target.files[i].name); // sets the label value

        img.classList.add('img-thumb'); // adds a class to the images
        img.setAttribute('alt', 'image of vehicle'); //add al attribute to image
        img.setAttribute('src', URL.createObjectURL(event.target.files[i])); // adds src to image

        imgsContainer.appendChild(imgInputLabel); // appends the label to the img container

        // on load empties the mempry
        img.onload = function () {
            URL.revokeObjectURL(img.src); // free memory
        };
    }
};