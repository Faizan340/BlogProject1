import os
from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.detail import DetailView
from django.views import View
from django.urls import reverse_lazy
from mypep.forms import SignUpForm
from mypep.models import ProfileModel


class UserLogin(LoginView):
    """
    LoginView which by default provides us with a form
    """
    template_name = 'mypep/login.html'
    fields = "__all__"
    redirect_authenticated_user = True
    success_url = reverse_lazy('mypep:base')


class SignUpView(CreateView):
    """
    Created SignupView which has SignUpForm for user registraion
    """
    form_class = SignUpForm
    success_url = reverse_lazy('mypep:base')
    template_name = 'mypep/signup.html'

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(SignUpView, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('mypep:base')
        return super(SignUpView, self).get(*args, **kwargs)


class MyView(View):
    """
    Home page view
    """

    def get(self, request):
        """
        Function to render home page
        """
        return render(request, 'mypep/hello.html')


# class ProfileUpdate(UpdateView):
#     model = ProfileModel
#     template_name = 'mypep/profilemodel_update.html'
#     fields = '__all__'
#     pk_url_kwarg = 'pk'
#     success_url = reverse_lazy('mypep:detail')

#     def form_valid(self, form):
#         # Get the user's current profile picture
#         old_picture = self.request.user.user_image

#         # Delete the old profile picture
#         if old_picture:
#             os.remove(os.path.join(settings.MEDIA_ROOT, str(old_picture)))

#         # Update the user's profile picture
#         self.request.user.user_image = form.cleaned_data['user_image']
#         self.request.user.save()

#         return super().form_valid(form)



class ProfileUpdate(UpdateView):
    model = ProfileModel
    fields = '__all__'
    template_name = 'mypep/profilemodel_update.html'
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('mypep:detail')

    def form_valid(self, form):
        print(self.request.user.profilemodel.user_location)
        print('3333333333333333333')
        
        # Get the user's current profile picture
        old_picture = self.request.user.profilemodel.user_image

        # Assign the new profile picture from the form
        self.request.user.user_image = form.cleaned_data['user_image']

        # Delete the old profile picture if it exists
        if old_picture:
            old_picture_path = os.path.join(settings.MEDIA_ROOT, str(old_picture))
            # if os.path.exists(old_picture_path):
            os.remove(old_picture_path)

        return super().form_valid(form)


class ProfileDetail(DetailView):
    model = 'ProfileModel'
    fields = '__all__'


class MyDetailView(View):
    """
    Home page view
    """

    def get(self, request):
        """
        Function to render home page
        """
        return render(request, 'mypep/profilemodel_detail.html')









