initSlider();
function initSlider() {
  $(".owl-carousel-home").owlCarousel({
    items: 1,
    loop: true,
    autoplay: false,
    dots: false,
    nav: true,
    autoplayTimeout: 3000,
    autoplayHoverPause: true,
    onInitialized: startProgressBar,
    onTranslate: resetProgressBar,
    onTranslated: startProgressBar,
  });
}
$(".play").on("click", function () {
  owl.trigger("play.owl.autoplay", [1000]);
});
$(".stop").on("click", function () {
  owl.trigger("stop.owl.autoplay");
});

$(".owl-custom-testimonial").owlCarousel({
  items: 1,
  loop: true,
  autoplay: false,
  dots: false,
  nav: true,
  autoplayTimeout: 3000,
  autoplayHoverPause: true,
});
$(".play").on("click", function () {
  owl.trigger("play.owl.autoplay", [1000]);
});
$(".stop").on("click", function () {
  owl.trigger("stop.owl.autoplay");
});
function startProgressBar() {
  // apply keyframe animation
  $(".slide-progress").css({
    width: "100%",
    transition: "width 5000ms",
  });
}

function resetProgressBar() {
  $(".slide-progress").css({
    width: 0,
    transition: "width 0s",
  });
}

$(document).scroll(function () {
  "use strict";

  var y = $(this).scrollTop();
  if (y > 300) {
    $(".floatbutton").fadeIn();
  } else {
    $(".floatbutton").fadeOut();
  }
});

$(".clickbutton").click(function () {
  $(".floatbutton").toggleClass("active");
});

$(".floating_strip .rotatekaro a").on("click", function (e) {
  $(".floating_form").toggleClass("open");
});
// $("#startProject").click(function () {
//   var getID = document.getElementById("startProject");
//   if ($(getID).hasClass("show")) {
//     $(".top-header").css("zIndex", "1");
//   } else {
//     alert("not has");
//   }
// });
