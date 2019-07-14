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

})
