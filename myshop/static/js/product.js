

$('#add-category-form').on('submit', function(event) {
  event.preventDefault();
  var formData = $(this).serialize();
  $.ajax({
    url: '/addcategory',
    type: 'POST',
    data: formData,
    success: function(data) {
      // Insert the flash message into the DOM
      $('.messages').html(
        '<div class="alert alert-' + data.flash_message[0][0] + '">' + data.flash_message[0][1] + '</div>'
      );
      // Fade out the message and then hide it
      $('.messages .alert').fadeOut(4000).delay(4000).hide(0);
      // If the category was added successfully, insert it into the list
      if (data.flash_message[0][0] === "success") {
        $('#categories-list ul').append(
          '<li>' + data.category + ' / ' + data.id + ' / ' + data.date_created + ' <a href="/editcategory/' + data.id + '">update</a></li>'
        );
      }
      // Reset the form
      $('#add-category-form')[0].reset();
    },
    error: function(data) {
      // Insert the flash message into the DOM
      $('.messages').html(
        '<div class="alert alert-' + data.flash_message[0][0] + '">' + data.flash_message[0][1] + '</div>'
      );
      // Fade out the message and then hide it
      $('.messages .alert').fadeOut(4000).delay(4000).hide(0);
    }
  });
});




