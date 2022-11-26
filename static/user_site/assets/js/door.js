// var element = document.querySelector(".door");
// element.addEventListener("click", toggleDoor);

// function toggleDoor() {
//   element.classList.toggle("doorOpen");
// }
// var element2 = document.querySelector(".right");
// element2.addEventListener("click", toggleDoor1);

// function toggleDoor1() {
//   element2.classList.toggle("doorright");
// }

$(document).ready(function () {
  //   var hc = $("#leftdoor").hasClass("doorOpen");
  //   if (hc != true) {
  //     alert("has");
  //   }
  //   var rt = $("#leftdoor").attr("class", "doorOpen");
  //   var lt = $("#rightdoor").attr("class", "doorright");
  //   var rt = document.getElementById("leftdoor").getAttribute("class");
  //   var lt = document.getElementById("rightdoor").getAttribute("class");
  //   if (rt == "door doorOpen" && lt == "right doorright") {
  //     $("#maindoor").attr("class", "");
  //   }
});

$(".click").click(function () {
  $("#leftdoor").addClass("doorOpen");
  $("#rightdoor").addClass("doorright");
  $("#maindoor").css("overflow", "inherit");
  $("#lockbtn").hide();
});
