from django.shortcuts import get_object_or_404
from django.http import Http404
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User

from models import Photo
from forms import PhotoForm
from profiles.models import Profile


class PhotosListView(ListView):
    """
    List all photos or all user photos if username is specified.
    """
    context_object_name = 'photo_list'
    model = Photo

    def get_queryset(self):
        """
        If username is specified filter queryset using specified username.
        """
        username = self.kwargs.get('username', None)
        filters = {}
        if username:
            filters['user__username'] = username
        return super(PhotosListView, self).get_queryset().filter(**filters)

    def get_template_names(self):
        """
        Use different template if username is specified.
        """
        username = self.kwargs.get('username', None)
        if username:
            return ['photos/user_photos.html']

        return super(PhotosListView, self).get_template_names()

    def get_context_data(self, **kwargs):
        """
        Add user profile to context if username is specified.
        """
        username = self.kwargs.get('username', None)
        if username:
            user = get_object_or_404(User, username=username)
            try:
                profile = user.get_profile()
            except Profile.DoesNotExist:
                raise Http404
            context_data = super(PhotosListView, self).get_context_data(**kwargs)
            context_data['profile'] = profile
            return context_data

        return super(PhotosListView, self).get_context_data(**kwargs)


class PhotoDetailView(DetailView):
    """
    Show single photo.
    """
    context_object_name = 'photo'
    model = Photo
    pk_url_kwarg = 'photo_id'


class PhotoCreateView(CreateView):
    """
    Upload user photo.
    """
    context_object_name = 'photo'
    model = Photo
    form_class = PhotoForm

    def get_form(self, *args, **kwargs):
        """
        Set Photo's user from request.
        """
        form = super(PhotoCreateView, self).get_form(*args, **kwargs)
        form.instance = self.model(user=self.request.user)
        return form

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(PhotoCreateView, self).dispatch(*args, **kwargs)


class PhotoUpdateView(UpdateView):
    """
    Edit user photo.
    """
    context_object_name = 'photo'
    model = Photo
    form_class = PhotoForm
    pk_url_kwarg = 'photo_id'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(PhotoUpdateView, self).dispatch(*args, **kwargs)


class PhotoDeleteView(DeleteView):
    """
    Remove user photo.
    """
    context_object_name = 'photo'
    model = Photo
    pk_url_kwarg = 'photo_id'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(PhotoDeleteView, self).dispatch(*args, **kwargs)


