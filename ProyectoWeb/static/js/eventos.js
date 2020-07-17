
document.addEventListener('DOMContentLoaded', () => {
    //Menu Navegador
    var elems = document.querySelectorAll('.sidenav');
    var instances = M.Sidenav.init(elems);

    //Carrucel
    var elems = document.querySelectorAll('.slider');
    var instances = M.Slider.init(elems,{
        indicators:false,
        interval:4000
    });
});

//Menu Fijo
$(document).ready(function(){
	var altura = $('nav').offset().top;
	
	$(window).on('scroll', function(){
		if ( $(window).scrollTop() > altura ){
			$('nav').addClass('menu-fixed');
		} else {
			$('nav').removeClass('menu-fixed');
		}
	});
 
});
