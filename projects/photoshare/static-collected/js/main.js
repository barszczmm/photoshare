
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

//
var animateAppMessages = function() {
	var $messages = $('#app_messages ul').css({opacity: 0.8}),
		animation = function() {
			var height = $messages.height();
			$('li', $messages).animate({opacity: 0}, 1500);
			$messages.animate({width: 20, height: 20, opacity: 0.4}, 1500,
				function() {
					$messages.addClass('collapsed').click(
						function() {
							if ($messages.hasClass('collapsed')) {
								$('li', $messages).animate({opacity: 1}, 1500);
								$messages.removeClass('collapsed').animate({width: 980, height: height, opacity: 0.8}, 1500,
									function() {
										$messages.addClass('expanded');
									}
								);
							} else if ($messages.hasClass('expanded')) {
								$('li', $messages).animate({opacity: 0}, 1500);
								$messages.removeClass('expanded').animate({width: 20, height: 20, opacity: 0.4}, 1500,
									function() {
										$messages.addClass('collapsed');
									}
								);
							}
						}
					).hover(
						function() {
							if ($messages.hasClass('collapsed')) {
								$messages.css({opacity: 0.8});
							}
						},
						function() {
							if ($messages.hasClass('collapsed')) {
								$messages.css({opacity: 0.4});
							}
						}
					);
				}
			);
		};
	if ($messages.length) {
		setTimeout(animation, 2000);
	}
}

$(document).ready(function() {

	//animateAppMessages();

	// validate comment form
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

	// show usermenu info
	$('#user_menu .account').hover(
		function() {
			$('.info', this).css({height: 'auto'}).slideDown();
		},
		function() {
			$('.info', this).stop().slideUp();
		}
	);

	// usernamenu languages form
	$('#user_menu .language').not('.active').click(
		function() {
			var $clicked = $(this),
				$form = $clicked.parents('form');
			$('#language', $form).val($clicked.data('lang'));
			$form.submit();
		}
	);

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