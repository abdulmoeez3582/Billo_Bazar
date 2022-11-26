$("#ShoppingCart").click(function () {
  $("#isOpen").toggleClass("is-open");
});

$("#ShoppingCartMob").click(function () {
  $("#isOpenMob").toggleClass("is-open");
});

$("#billingAddressChange").click(function () {
  $("#billingaddress").slideToggle();
});
$("#shippingAddressForm").hide();
$("#shippingAddressChange").click(function () {
  $("#shippingAddressForm").slideToggle();
});

$("#cod").click(function () {
  $("#codDes").slideDown();
  $("#banktransferDetails").slideUp();
  $("#creditcardDetails").slideUp();
});

$("#banktransfer").click(function () {
  $("#banktransferDetails").slideDown();
  $("#creditcardDetails").slideUp();
  $("#codDes").slideUp();
});

$("#creditcard").click(function () {
  $("#creditcardDetails").slideDown();
  $("#banktransferDetails").slideUp();
  $("#codDes").slideUp();
});

function Selected(div) {

  $(div).addClass("selected");
  $(div).siblings().removeClass("selected");

}