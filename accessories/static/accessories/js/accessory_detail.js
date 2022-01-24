let decremntbtn = document.getElementById('decrement-qty');
let incrementbtn = document.getElementById('increment-qty');

let qtyCont = document.getElementById('id_qty');

// when minus button clicked, checks if value of qty is less than 2
// if less, disabled minus btn
decremntbtn.addEventListener('click', function () {
    qtyPlusBtnEnable();
    if (qtyCont.value <= 2) {
        qtyMinusBtnDisable();
    }
});

// when plus button clicked, checks if value of qty is less than 2
// if less, disabled plus btn
incrementbtn.addEventListener('click', function () {
    qtyMinusBtnEnable();
    if (qtyCont.value == qtyCont.attributes.max.value - 1) {
        qtyPlusBtnDisable();
    }
});

// disables minus button
function qtyMinusBtnDisable() {
    decremntbtn.setAttribute('disabled', "");
}

// enables minus button
function qtyMinusBtnEnable() {
    decremntbtn.removeAttribute('disabled');
}

// disables plus button
function qtyPlusBtnDisable() {
    incrementbtn.setAttribute('disabled', "");
}

// enables plus button
function qtyPlusBtnEnable() {
    incrementbtn.removeAttribute('disabled');
}

// checks value of qty and disbales buttons if needed
window.addEventListener('load', function () {
    if (qtyCont.value == qtyCont.attributes.max.value - 1) {
        incrementbtn.setAttribute('disabled', "");
    }

    if (qtyCont.value <= 2) {
        decremntbtn.setAttribute('disabled', "");
    }
});

// Increment quantity
$('.increment-qty').click(function (e) {
    e.preventDefault();
    var closestInput = $(this).closest('.input-group').find('.qty_input')[0];
    var currentValue = parseInt($(closestInput).val());
    $(closestInput).val(currentValue + 1);
    var itemId = $(this).data('item_id');
});

// Decrement quantity
$('.decrement-qty').click(function (e) {
    e.preventDefault();
    var closestInput = $(this).closest('.input-group').find('.qty_input')[0];
    var currentValue = parseInt($(closestInput).val());
    $(closestInput).val(currentValue - 1);
    var itemId = $(this).data('item_id');
});