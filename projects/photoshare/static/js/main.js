
// animate error messages
var animateErrors = function() {
	$('.errorlist').each(
		function() {
			if ($('textarea', $(this).next()).length) {
				$(this).animate({width: 320}, 500);
			} else {
				$(this).animate({width: 700}, 1000);
			}
		}
	);
}

animateErrors();

$(document).ready(function() {

	//
	$('#post_comment input[type="submit"]').click(
		function() {
			var $comment = $(this).parents('form:first').find('p textarea');
			if ($comment.val() == '') {
				$comment.parent().prev('.errorlist').remove();
				$comment.parent().before('<ul class="errorlist"><li>'+field_required_error+'</li></ul>');
				animateErrors();
				return false;
			}
		}
	);

	// animate submit button opacity
	$('input[type="submit"]').hover(
		function() {
			$(this).fadeTo(200, 0.5);
		},
		function() {
			$(this).fadeTo(200, 1);
		}
	);

	// show usermenu submenu
	$('#user_menu .authenticated .account').hover(
		function() {
			$('ul', this).slideDown();
		},
		function() {
			$('ul', this).slideUp();
		}
	).find('ul').css('opacity', 0.9);

	// tabs
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