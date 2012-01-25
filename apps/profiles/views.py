from urlparse import urlsplit

from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response, get_object_or_404
from django.http import Http404, HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from models import Profile


def profile_comments(request, username):
    """
    List comments for user profile.
    """
    user = get_object_or_404(User, username=username)
    try:
        profile = user.get_profile()
    except Profile.DoesNotExist:
        raise Http404

    return render_to_response('profiles/profile_comments.html',
                              {'profile': profile},
                              context_instance=RequestContext(request))


@login_required
def become_profile_fan(request, username):
    """
    Current user becomes a fan of specified user.
    """
    user = get_object_or_404(User, username=username)
    fanned_profile = None
    try:
        fanned_profile = user.get_profile()
    except Profile.DoesNotExist:
        raise Http404

    user_profile = request.user.get_profile()

    user_profile.fan_of.add(fanned_profile)

    # try to go back to previous page
    referer = request.META.get('HTTP_REFERER', None)
    if referer:
        try:
            redirect_to = urlsplit(referer, 'http', False)[2]
        except IndexError:
            redirect_to = reverse('userena_profile_detail', {'username': username})
    # if that fails try to go to user profile page
    else:
        redirect_to = reverse('userena_profile_detail', {'username': username})

    return HttpResponseRedirect(redirect_to)


@login_required
def stop_being_profile_fan(request, username):
    """
    Current user stops being a fan of specified user.
    """
    user = get_object_or_404(User, username=username)
    fanned_profile = None
    try:
        fanned_profile = user.get_profile()
    except Profile.DoesNotExist:
        raise Http404

    user_profile = request.user.get_profile()

    user_profile.fan_of.remove(fanned_profile)

    # try to go back to previous page
    referer = request.META.get('HTTP_REFERER', None)
    if referer:
        try:
            redirect_to = urlsplit(referer, 'http', False)[2]
        except IndexError:
            redirect_to = reverse('userena_profile_detail', {'username': username})
    # if that fails try yto go to user page
    else:
        redirect_to = reverse('userena_profile_detail', {'username': username})

    return HttpResponseRedirect(redirect_to)

