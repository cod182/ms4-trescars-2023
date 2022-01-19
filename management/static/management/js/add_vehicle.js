let loadFile = function (event) {
    let imgsContainer = document.getElementById('images-container')
    imgsContainer.innerHTML = ''
    for (let i = 0; i < event.target.files.length; i++) {
        let imgInputLabel = document.createElement('label');
        let imgInput = document.createElement('input');
        let img = document.createElement('img');

        imgInputLabel.appendChild(imgInput);
        imgInputLabel.appendChild(img);

        imgInput.setAttribute('type', 'radio');
        imgInput.setAttribute('name', 'main');
        imgInput.setAttribute('required', true);
        imgInput.setAttribute('value', event.target.files[i].name)

        img.classList.add('img-thumb')
        img.setAttribute('alt', 'image of vehicle');
        img.setAttribute('src', URL.createObjectURL(event.target.files[i]));

        imgsContainer.appendChild(imgInputLabel);

        img.onload = function () {
            URL.revokeObjectURL(img.src) // free memory
        }
    }
};