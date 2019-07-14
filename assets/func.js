$(document).ready(function(){
  $('.bars, .item').click(function(){
    $('.bar1').toggleClass('bar1_ac')
    $('.bar2').toggleClass('bar2_ac')
    $('.bar3').toggleClass('bar3_ac')
    $('.profile').toggleClass('menu_ac')
  })

// $('.searchbar2').focus(function(){
//   var y = $(this).val();
//   $(window).keydown(function(r){
//     if (r == 35) {
//
//     }
//   })
// })

$('.b2').click(function(){
    var x = $('.searchbar').val();
      if( x.length === 0){
      $('.whyno').addClass('show1');
    }
    $('.searchbar2').val(x);
})
$('.it2').click(function(){

  var css = 'html {-webkit-filter: invert(100%);' + '-moz-filter: invert(100%);' + '-o-filter: invert(100%);' + '-ms-filter: invert(100%); }';
  var head = document.getElementsByTagName('head')[0];
  var style = document.createElement('style');
  if (!window.counter) {
      window.counter = 1;
    } else {
      window.counter++;
      if (window.counter % 2 == 0) {
          var css = 'html {-webkit-filter: invert(0%);}'
        }
      }
      style.type = 'text/css';
      if (style.styleSheet) {
        style.styleSheet.cssText = css;
      } else {
        style.appendChild(document.createTextNode(css));
      }
      head.appendChild(style);
    })

})
