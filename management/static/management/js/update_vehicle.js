let currImgCont = document.getElementsByClassName('current_image');
let main_list = 0;
let submitBtn = document.getElementById('updateBtnVehicle');
let messageCont = document.getElementById('warning-message');

for (x = 0; x < currImgCont.length; x++) {
    let check = currImgCont[x].children[3].children[0].children[0];
    let img = document.createElement('img');

    if (currImgCont[x].children[2].children[1].children[0].getAttribute('href')) {
        img.setAttribute('src', currImgCont[x].children[2].children[1].children[0].getAttribute(
            'href'));
        img.setAttribute('width', '100px');
        img.setAttribute('height', 'auto');

        currImgCont[x].children[2].prepend(img);
    }
    // on first loop, checks if a main image is selected
    if (check.checked) {
        main_list += 1
        console.log(main_list);
    }

    // When a main image checkbox is selected, adds 1 to main_image list
    check.addEventListener('change', function () {
        if (check.checked) {
            main_list += 1
            console.log(main_list);

        } else {
            main_list -= 1
            console.log(main_list);
        }
    })
}

// When the submit button is clicked, check if more that one main image is selected
submitBtn.addEventListener('click', function (event) {
    if (main_list > 1) {
        event.preventDefault();
        messageCont.innerHTML = `<p>Please only select 1 main image</P>`;
        messageCont.classList.add('red');
        messageCont.classList.add('text-center');
    } else if (main_list == 0) {
        event.preventDefault();
        console.log('')
        messageCont.innerHTML = `<p>Please select a main image</P>`;
        messageCont.classList.add('red');
        messageCont.classList.add('text-center');

    }
})