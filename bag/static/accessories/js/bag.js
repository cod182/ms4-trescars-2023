// Update quantity on click
$('.btn--update-link').click(function(e) {
    var form = $(this).prev('.update-form');
    form.submit();
})

// Remove item and reload on click
$('.btn--remove-item').click(function(e) {
    var csrfToken = "{{ csrf_token }}";
    var itemId = $(this).attr('id').split('remove_')[1];
    var url = `/bag/remove/${itemId}/`;
    var data = {
        'csrfmiddlewaretoken': csrfToken,
    };

    $.post(url, data)
        .done(function() {
            location.reload();
        });
})