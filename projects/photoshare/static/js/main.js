$('.errorlist').each(
	function() {
		if ($('textarea', $(this).next()).length) {
			$(this).animate({width: 320}, 500);
		} else {
			$(this).animate({width: 700}, 1000);
		}
	}
);


$(document).ready(function() {

	//
	$('input[type="submit"]').hover(
		function() {
			$(this).fadeTo(200, 0.5);
		},
		function() {
			$(this).fadeTo(200, 1);
		}
	);


	$('#user_menu .authenticated .account').hover(
		function() {
			$('ul', this).slideDown();
		},
		function() {
			$('ul', this).slideUp();
		}
	).find('ul').css('opacity', 0.9);

	
	$('.tabs').each(
		function() {
			var $tabs = $(this);
			$('.tab-title', $tabs).click(
				function() {
					var $clicked = $(this);
					if (!$clicked.hasClass('active')) {
						$clicked.addClass('active').siblings().removeClass('active');
						if (!$tabs.hasClass('no-hash')) {
							$('.tab-content:eq('+$clicked.index()+')', $tabs).addClass('active').siblings().removeClass('active');
						}
					} else {
						return false;
					}
				}
			);
		}
	);
	if (window.location.hash != '') {
		$('.tabs .tab-title a[href='+window.location.hash+']').parent().click();
	}

});