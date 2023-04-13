$( document ).ready(function() {

});

$('#demo1').toggle()

$('#btn1').click(function() {
  $('#demo2').hide();
  $('#demo3').hide();
  $('#demo1').toggle();
});

$('#btn2').click(function() {
  $('#demo1').hide();
  $('#demo3').hide();
  $('#demo2').toggle();
});

$('#btn3').click(function() {
  $('#demo1').hide();
  $('#demo2').hide();
  $('#demo3').toggle();
});