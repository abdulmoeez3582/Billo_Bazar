$(document).ready(function () {
  var val = 0;

  $("#checkEmail").change(function () {
    var chk = $("#checkEmail").is(":checked");
    if (chk == true) {
      $("#checkEmail").attr("value", "changeEmailYes");
      val += 1;
      validate();
    } else {
      $("#checkEmail").attr("value", "changeEmailNo");
      val -= 1;
      validate();
    }
    var isChangeEmail = document
      .getElementById("checkEmail")
      .getAttribute("value");
    if (isChangeEmail == "changeEmailYes") {
      document.getElementById("OnlyEmail").style.display = "initial";
      document.getElementById("EmailAndPassword").style.display = "none";
      validate();
    } else {
      document.getElementById("OnlyEmail").style.display = "none";
      validate();
    }
  });
  $("#checkPwd").change(function () {
    var chk = $("#checkPwd").is(":checked");
    if (chk == true) {
      $("#checkPwd").attr("value", "changePasswordYes");
      val += 1;
      validate();
    } else {
      $("#checkPwd").attr("value", "changePasswordNo");
      val -= 1;
      validate();
    }
    var isChangePwd = document.getElementById("checkPwd").getAttribute("value");
    if (isChangePwd == "changePasswordYes") {
      document.getElementById("OnlyPassword").style.display = "initial";
      document.getElementById("EmailAndPassword").style.display = "none";
      validate();
    } else {
      document.getElementById("OnlyPassword").style.display = "none";
      validate();
    }
  });

  $("#demosample").click(function () {
    alert(val);
  });
  function validate() {
    if (val == 1) {
      var isChangePwd = document
        .getElementById("checkPwd")
        .getAttribute("value");
      var isChangeEmail = document
        .getElementById("checkEmail")
        .getAttribute("value");
      if (isChangePwd == "changePasswordYes") {
        document.getElementById("OnlyPassword").style.display = "initial";
        document.getElementById("EmailAndPassword").style.display = "none";
      } else if (isChangeEmail == "changeEmailYes") {
        document.getElementById("OnlyEmail").style.display = "initial";
        document.getElementById("EmailAndPassword").style.display = "none";
      } else {
        document.getElementById("OnlyPassword").style.display = "none";
        document.getElementById("OnlyEmail").style.display = "none";
      }
    }
    if (val == 2) {
      document.getElementById("OnlyEmail").style.display = "none";
      document.getElementById("OnlyPassword").style.display = "none";
      document.getElementById("EmailAndPassword").style.display = "initial";
    } else {
      document.getElementById("EmailAndPassword").style.display = "none";
    }
  }

  $("#menuToggle").click(function () {
    $("#UserMenu").slideToggle("slow", function () {
      if ($("#UserMenu").is(":hidden")) {
        $("#menuToggle").attr("class", "fas fa-plus");
      } else {
        $("#menuToggle").attr("class", "fas fa-minus");
      }
    });
  });
});
