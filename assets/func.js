$(document).ready(function(){
  // $(window).load(function(){
  //   setInterval(function(){
  //     $('.loader').addClass('hide')
  //     $('.searchbar, .search_box').addClass('show')
  //   }, 3000)
  // })
  $(window).keydown(function(event){
    var k = event.which;
    var f = $('.searchbar').val();
    var fb = 'github';
    var gb = 'Github';
    console.log(k);
    if(k == 13){
      var x = $('.searchbar').val();
        if( x.length === 0){
        $('.whyno').addClass('show1');

      }else{
        var r1 = Math.random();
        $('.timer').text('Showing all results in ' + r1);

        $('body, html').animate({scrollTop: $('.main').offset().top}, 500)
        if (f == fb || f == gb) {
          $('.r1').addClass('width40')
          $('.r2').addClass('width40')
          $('.wp1').hide()
          $('.infobox').addClass('info_ac')
        }
      }
      $('.searchbar2').val(x)
    }
    //  if (k == 38) {
    //   $('body, html').animate({scrollTop: $('.land').offset().top}, 500)
    //
    // }
  })
  $('.logo').click(function(){
    $('body, html').animate({scrollTop: $('.land').offset().top}, 500)
  })
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

$('.b2').click(function(event){
    var x = $('.searchbar').val();
      if( x.length === 0){
      $('.whyno').addClass('show1');

    }else{
      var f = $('.searchbar').val();
      var fb = 'github';
      var gb = 'Github';
      var r1 = Math.random();
      $('.timer').text('Showing all results in ' + r1);
      $('body, html').animate({scrollTop: $('.main').offset().top}, 500)
      if (f == fb || f == gb) {
        $('.r1').addClass('width40')
        $('.r2').addClass('width40')
        $('.wp1').hide()
        $('.infobox').addClass('info_ac')
      }

    }
    $('.searchbar2').val(x)
})
$('.it2').click(function(){
  $('.result').toggleClass('b-light')
  $('.result_box').toggleClass('f-light')
})
$('.page2').hide();
$('.page1').click(function(){
  $('.results').addClass('result_ac')
  $('.page2').show();
  $(this).hide()
})
$('.page2').click(function(){
  $('.results').removeClass('result_ac')
  $('.page1').show();
  $(this).hide()
})
$('.result, .infobox').hover(function(){
  $(this).toggleClass('up')
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
