$(window).scroll(function(){
  if ($(this).scrollTop() > 100) {
    $('#scroll-up').fadeIn();
  } else {
    $('#scroll-up').fadeOut();
  }
});
$('#scroll-up').click(function(){
  $('html, body').animate({scrollTop : 0},800);
  return false;
});


document
  .getElementById("kayindi")
  .addEventListener("mouseover", function (event) {
    event.target.style.height = "100%";
    event.target.style.width = "100%";
  });

document
  .getElementById("kayindi")
  .addEventListener("mouseout", function (event) {
    event.target.style.height = "90%";
    event.target.style.width = "90%";
  });

document
  .getElementById("usturt")
  .addEventListener("mouseover", function (event) {
    event.target.style.height = "100%";
    event.target.style.width = "100%";
  });

document
  .getElementById("usturt")
  .addEventListener("mouseout", function (event) {
    event.target.style.height = "90%";
    event.target.style.width = "90%";
  });
document
  .getElementById("barchans")
  .addEventListener("mouseover", function (event) {
    event.target.style.height = "100%";
    event.target.style.width = "100%";
  });

document
  .getElementById("barchans")
  .addEventListener("mouseout", function (event) {
    event.target.style.height = "90%";
    event.target.style.width = "90%";
  });

var retype_password = document.querySelector("#form_retype_password"),
  once = function () {
    alert("Be sure that your password are the same");
    retype_password.removeEventListener("keypress", once);
  };
retype_password.addEventListener("keypress", once, false);

document.querySelector("#accept").addEventListener("click", function () {
  if ($("#btnSubmit").is(":disabled")) {
    $("#btnSubmit").removeAttr("disabled");
  } else {
    $("#btnSubmit").attr("disabled", "disabled");

  }
});

$(function () {
  
  $(window).scroll(function(){
    if ($(this).scrollTop() > 100) {
      $('#scroll-up').fadeIn();
    } else {
      $('#scroll-up').fadeOut();
    }
  });
  $('#scroll-up').click(function(){
    $('html, body').animate({scrollTop : 0},800);
    return false;
  });
  

  $("a[href='#top']").click(function () {
    $("html, body").animate({ scrollTop: 0 }, "slow");
    return false;
  });

  $("#email_error_message").hide();
  $("#password_error_message").hide();
  $("#retype_password_error_message").hide();

  var error_email = false;
  var error_password = false;
  var error_retype_password = false;

  $("#form_email").focusout(function () {
    check_email();
  });
  $("#form_password").focusout(function () {
    check_password();
  });
  $("#form_retype_password").focusout(function () {
    check_retype_password();
  });

  function check_email() {
    var pattern = /^([\w-\.]+@([\w-]+\.)+[\w-]{2,4})?$/;
    var email = $("#form_email").val();
    if (pattern.test(email) && email !== "") {
      $("#email_error_message").hide();
    } else {
      $("#email_error_message").html("Invalid Email");
      $("#email_error_message").show();
      $("#form_email").css("border", "2px solid #F90A0A");
      error_email = true;
    }
  }

  function check_password() {
    var password_length = $("#form_password").val().length;
    if (password_length < 8 || $("#form_password").val() === "") {
      $("#password_error_message").html(
        "You should enter at least 8 characters"
      );
      $("#password_error_message").show();
      $("#form_password").css("border", "2px solid  #F90A0A");
      error_password = true;
    } else {
      $("#password_error_message").hide();
    }
  }

  function check_retype_password() {
    var password = $("#form_password").val();
    var retype_password = $("#form_retype_password").val();
    if (password !== retype_password) {
      $("#retype_password_error_message").html("Password didn't matched");
      $("#retype_password_error_message").show();
      $("#form_retype_password").css("border", "2px solid #F90A0A");
      error_retype_password = true;
    } else {
      $("#retype_password_error_message").hide();
    }
  }

  $("#registration_form").submit(function () {
    error_email = false;
    error_password = false;
    error_retype_password = false;
    check_email();
    check_password();
    check_retype_password();

    if (
      error_email === false &&
      error_password === false &&
      error_retype_password === false
    ) {
      alert("Registration succesfull");
      return true;
    } else {
      alert("Please fill out the form correctly");
      return false;
    }
  });
});

function showHidePassword() {
  var x = document.getElementById("form_password");
  if (x.type === "password") {
    x.type = "text";
  } else {
    x.type = "password";
  }
}

$(document).ready(function () {
  var max_length = 600;
  $("textarea").keyup(function () {
    var len = max_length - $(this).val().length;
    $(".GFG").text(len);
  });
});



