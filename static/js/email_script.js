
// Code adapted from eamil lesson from code instutite
function sendEmail(contactForm) {
    emailjs.send('gmail','codie',{
        "from_name": contactForm.name.value,
        "from_email": contactForm.email.value,
        "reason": contactForm.reason.value,
        "message": contactForm.message.value
    })
    .then(
        function(response) {
            console.log('SUCCESS',response);
            document.getElementById('message-status').innerHTML =`<span class='green bold message-status'><em>Message Sent!</em> <i class="green fas fa-check-circle"></i></span>`;
            document.getElementById('contact-submit').disabled = true;
            setTimeout(function(){ 
                document.getElementById('contact-modal-close').click();
                document.getElementById('contact-submit').disabled = false;
                document.getElementById('message-status').innerHTML =``;
                document.getElementById('contact-name').value = '';
                document.getElementById('contact-email').value = '';
                document.getElementById('contact-message').value = '';
            }, 2000);
        },
        function(error) {
            console.log('FAILED', error);
            document.getElementById('message-status').innerHTML =`<span class='red bold'><em>Error! Please try again.</em></span>`;
        });
    return false;
}