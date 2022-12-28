// visual validate email in registration form 👇


    $('.costumer_email_check').hide();
    $('#registration_email').on('input', function() {
      var email = $(this).val();
      var emailRegEx = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/;
      if(!emailRegEx.test(email) && email.length > 10) {
        $('.costumer_email_check').text("Prosím zadejte platný formát emailové adresy.").show();
        $('.check-tag').css('visibility', 'hidden');  // hide the "check-tag" element
        return false;
      } else {
        $('.costumer_email_check').hide();
        $.ajax({
          url: '/check-email',
          method: 'POST',
          data: {'email': email},
          success: function(data) {
            if (data == 'taken') {
              $('.costumer_email_check').text("Tento email je již zaregistrovaný v naší databázi.").show();
              $('.check-tag').css('visibility', 'hidden');  // hide the "check-tag" element
            } else {
              // show the "check-tag" element only if the email address is in a valid format and is not already in the database
              if (emailRegEx.test(email)) {
                $('.check-tag').css('visibility', 'visible');
              } else {
                $('.check-tag').css('visibility', 'hidden');
              }
            }
          }
        });
      }
    });

////////////////////////////////////////////////////////////////////////////////////////////





// visual validate username in registration form 👇

    $('.check-tag-username').css('visibility', 'hidden');
    $('#registration_username').on('input', function(){
        var username =  $(this).val();
        $('.costumer_username_check').hide(); // hide the message element before making the AJAX request
        if (username.length === 0) { // check if the form is empty
            $('.check-tag-username').css('visibility', 'hidden');
            return; // exit the function if the form is empty
        }
        if (username.length < 6) { // check if the username is longer than 5 characters
            $('.check-tag-username').css('visibility', 'hidden');
            $('.costumer_username_check').text("Uživatelské jméno musí obsahovat alespoň 6 znaků.").show();
            return; // exit the function if the username is too short
        }
        $.ajax({
        url: '/check-username',
        method: 'POST',
        data: {'username': username},
        success: function(data) {
            if (data == 'taken' ) {
                $('.costumer_username_check').text("Tento uživatel je již zaregistrovaný v naší databázi.").show();
                $('.check-tag-username').css('visibility', 'hidden');
            } else if (username.length >= 6) { // check if the username is longer than 5 characters
                $('.check-tag-username').css('visibility', 'visible');
            }
        }
        });
    });


//////////////////////////////////////////////////////////////////////////////////////////



// -------------------phone number form ----------------------------------

$('#flag-selector').change(function() {
    var selectedOption = $(this).val();
    if (selectedOption == '+421') {
        $('.flag').attr('src', '/static/images/czech-flag.png');
    } else if (selectedOption == '+420') {
        $('.flag').attr('src', "/static/images/slovakia-flag.png");
    }
});



$('#registration_phone').on('input', function(){
    var phone_number = $(this).val();
    $('.check-tag-phone').css('visibility', 'hidden');
    if (phone_number.length === 9){
        $('.check-tag-phone').css('visibility', 'visible');
    }else{
        $('.check-tag-phone').css('visibility', 'hidden');
    }
});



$('#registration_phone').on('keydown', function(event) {
    // Allow only digits and the backspace key
    if ((event.keyCode < 48 || event.keyCode > 57) && event.keyCode != 8) {
        event.preventDefault();
    }
});


// ////////////////////////////////////////////////////////////////////////////



// ----------------------password number form --------------------------------------

var password_one;

$('.check-tag-password-one').css('visibility', 'hidden')
$('#Password1').on('input', function(){
    password_one = $(this).val();
    if (password_one.length < 8){
    $('.costumer_password_one_check').text("Heslo musí být dlouhé alespoň 8 znaků.").show();
    $('.check-tag-password-one').css('visibility', 'hidden');
    }else{
        $('.costumer_password_one_check').text("Heslo musí být dlouhé alespoň 8 znaků.").hide();
        $('.check-tag-password-one').css('visibility', 'visible');
    }
});


$('.check-tag-password-two').css('visibility', 'hidden');
$('#Password2').on('input', function(){
    var password_two = $(this).val();
    if (password_one === password_two){
        $('.check-tag-password-two').css('visibility', 'visible');
        $('.costumer_password_two_check').text("Hesla se musí shodovat.").hide();
    }else{
        $('.check-tag-password-two').css('visibility', 'hidden');
        $('.costumer_password_two_check').text("Hesla se musí shodovat.").show();
    }

});


