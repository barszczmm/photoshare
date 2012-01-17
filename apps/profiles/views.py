from django.shortcuts import render_to_response, get_object_or_404
from django.http import Http404
from django.template import RequestContext
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

