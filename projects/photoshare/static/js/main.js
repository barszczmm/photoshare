
// validate comment form
var validateCommentForm = function() {
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
};

// sumbit button opacity animation
var animateSubmitButton = function() {
	// animate submit button opacity
	$('input[type="submit"]').hover(
		function() {
			$(this).fadeTo(200, 0.5);
		},
		function() {
			$(this).fadeTo(200, 1);
		}
	);
};

// animate form error messages
var animateErrors = function() {
	$('.errorlist').each(
		function() {
			var $error_list = $(this),
				form_width = $error_list.parents('form:first').width();

			if ($('textarea', $(this).next()).length) {
				$error_list.animate({width: 320}, 500);
			} else {
				$error_list.animate({width: form_width - $error_list.next().find('input').outerWidth() - 50}, 1000);
			}
		}
	);
};

// all forms related functions
var formsFunctions = function() {
	animateErrors();
	animateSubmitButton();
	validateCommentForm();
};


// animate application messages
var appMessageAnimation = function() {
	$('#app_messages li:visible:first').animate({marginTop: -25, opacity: 0}, 2000,
		function() {
			$(this).hide();
			setTimeout(appMessageAnimation, 3000);
		}
	);
};
var animateAppMessages = function() {
	setTimeout(appMessageAnimation, 3000);
};

// show usermenu info
var usermenuInfo = function() {
	var timeout,
		$account = $('#user_menu .account');
	$account.hover(
		function() {
			var show = function() {
					$('.info', $account).css({height: 'auto'}).slideDown(300);
				};
			timeout = setTimeout(show, 300);
		},
		function() {
			clearTimeout(timeout);
			$('.info', $account).stop().delay(200).slideUp(100);
		}
	);
};

// usermenu languages form
var languagesForm = function() {
	$('#user_menu .language').not('.active').click(
		function() {
			var $clicked = $(this),
				$form = $clicked.parents('form');
			$('#language', $form).val($clicked.data('lang'));
			$form.submit();
		}
	);
}

// all top bar functions
var topBarFunctions = function() {
	animateAppMessages();
	usermenuInfo();
	languagesForm();
}


// some links require login so show login form for not logged in users
var loginRequiredLinks = function() {
	$('body.notlogged a.loginrequired').click(
		function() {
			alert('login required');
			return false;
		}
	);
}

$(document).ready(function() {

	topBarFunctions();

	loginRequiredLinks();

	formsFunctions();

	// ratings
	$('#add_rating .score, #rating_list .score').wrapInner('<span class="fg" />').append('<span class="bg" />');
	$('#add_rating .score .bg, #rating_list .score .bg').css({opacity: function() { return $(this).parent().data('score')/5; }});


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
							// if there is no no-hash class it means tabs are with hashes so we need to change tab
							$('.tab-content:eq('+$clicked.index()+')', $tabs).addClass('active').siblings().removeClass('active');
						} else {
							return;
							// there is no-hash class so tab urls are normal urls (not hashes)
							// so we need to check if we need to load something using AJAX or not
							if ($tabs.hasClass('ajax')) {
								// there is ajax class so we need to load data using AJAX requests
								$clicked.addClass('loading');
								// TODO: add some overlay with loader
								$('.tab-content.active', $tabs).addClass('loading');
								
								$.ajax({
									url: $('a', $clicked).attr('href') + 'ajax/',
									error: function(jqXHR, textStatus, errorThrown) {
										$clicked.removeClass('loading');
										// TODO: add message in appMessages
										console.log(textStatus + ' / ' + errorThrown);
									},
									success: function(data, textStatus, jqXHR) {
										var $data = $(data);
										$('head title').html($data.filter('#title').html());
										$('#subtitle').html($data.filter('#subtitle').html());
										$('.tab-content.active', $tabs).removeClass('loading').html($data.filter('#tab_content').html());
										$clicked.removeClass('loading');
										// TODO: use history.js's pushState to change url
									}
								});
								return false;
							}
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