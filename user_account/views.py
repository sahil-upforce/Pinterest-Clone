import datetime

from django.contrib.auth import get_user_model, logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView, PasswordResetDoneView, PasswordResetView, \
    PasswordResetConfirmView, PasswordResetCompleteView
from django.db.models import Q
from django.shortcuts import redirect, render
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode
from django.views import generic
from django.views.decorators.cache import never_cache

from user_account.forms import UserRegisterForm, UserUpdateForm, UserDetailUpdateForm, UserPasswordResetForm
from user_account.models import UserProfile
from user_account.tokens import account_activation_token

User = get_user_model()


class HomePage(generic.TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(HomePage, self).get_context_data(**kwargs)
        context['pins_objs'] = self.get_queryset()
        return context

    def get_queryset(self):
        data = []
        if self.request.user:
            data = []
        else:
            # data = Pin.objects.all()
            pass
        return data


class TodayPinsView(generic.TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(TodayPinsView, self).get_context_data(**kwargs)
        today = datetime.date.today()
        # context['pins_objs'] = Pin.objects.filter(created_at__date=today)
        return context


class UserRegisterView(generic.CreateView):
    form_class = UserRegisterForm
    model = User
    template_name = 'user_account/registration.html'
    success_url = reverse_lazy("home")

    def get_form(self, form_class=None):
        form = super(UserRegisterView, self).get_form(form_class=form_class)
        form.request = self.request
        return form


class UserEmailVerification(generic.View):
    def get(self, request, uid, token):
        try:
            uid = force_str(urlsafe_base64_decode(uid))
            user = User.objects.get(pk=uid)
        except(TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None
        if user is not None and account_activation_token.check_token(user, token):
            user.is_active = True
            user.save()
            login(request, user)
            return redirect(to='home')
        else:
            return render(request=request, template_name='', context={})


class UserPasswordResetView(PasswordResetView):
    template_name = 'user_account/password_reset.html'
    email_template_name = 'emails/password_reset_email.html'
    success_url = reverse_lazy('users:password_reset_done')
    form_class = UserPasswordResetForm

    def get_form(self, form_class=None):
        form = super(UserPasswordResetView, self).get_form(form_class=form_class)
        form.request = self.request
        return form


class UserPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'user_account/password_reset_done.html'


class UserPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'user_account/password_reset_confirm.html'
    success_url = reverse_lazy('users:password_reset_complete')


class UserPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'user_account/password_reset_complete.html'


@method_decorator(decorator=(login_required, never_cache), name='dispatch')
class UserUpdateView(generic.UpdateView):
    model = User
    form_class = UserUpdateForm
    profile_form = UserDetailUpdateForm
    change_password_form = PasswordChangeForm
    template_name = 'user_account/edit_user.html'
    slug_url_kwarg = 'username'
    slug_field = 'username'
    context_object_name = 'user_obj'

    def get_context_data(self, **kwargs):
        context = super(UserUpdateView, self).get_context_data(**kwargs)
        context['change_password_form'] = self.change_password_form
        try:
            context['profile_form'] = self.profile_form(instance=self.request.user.user_profile)
        except Exception as e:
            context['profile_form'] = self.profile_form()
        return context

    def post(self, request, *args, **kwargs):
        user_profile_obj, created = UserProfile.objects.get_or_create(user=request.user)
        profile_form = self.profile_form(self.request.POST, instance=user_profile_obj)
        if profile_form.is_valid():
            profile_form.save()
        return super(UserUpdateView, self).post(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('users:edit_user', kwargs={'username': self.request.user.username})


@method_decorator(decorator=(login_required, never_cache), name='dispatch')
class UserPasswordChangeView(PasswordChangeView):
    template_name = 'user_account/change_password.html'

    def get_form(self, form_class=None):
        form = super().get_form()
        form.fields.get('old_password').widget.attrs["class"] = 'form-control'
        form.fields.get('new_password1').widget.attrs["class"] = 'form-control'
        form.fields.get('new_password2').widget.attrs["class"] = 'form-control'
        return form

    def get_success_url(self):
        return reverse('users:user_profile', kwargs={'id': self.request.user.id})


@method_decorator(decorator=(login_required, never_cache), name='dispatch')
class UserProfileView(generic.DetailView):
    model = User
    template_name = 'user_account/profile.html'
    slug_url_kwarg = 'id'
    slug_field = 'id'
    context_object_name = 'user_obj'


@method_decorator(decorator=(login_required, never_cache), name='dispatch')
class UserDeleteView(generic.View):
    template_name = 'user_account/delete_user.html'

    def get(self, request, username):
        return render(request=request, template_name=self.template_name)

    def post(self, request, username):
        user = request.user
        user.is_active = False
        user.save()
        logout(request)
        return redirect('login')


@method_decorator(decorator=(login_required, never_cache), name='dispatch')
class UserSearchView(generic.View):
    def get(self, request):
        search_params = self.search_filters()
        data = list(User.objects.filter(search_params).exclude(id=request.user.id))
        context = {'data': data}
        return render(request=request, template_name='user_account/user_search_page.html', context=context)

    def search_filters(self):
        search_param = self.request.GET.get('search_input')
        if not search_param:
            search_param = ','
        search_query = Q(username__icontains=search_param) | Q(email__icontains=search_param)
        return search_query


@method_decorator(decorator=(login_required, never_cache), name='dispatch')
class FollowUnfollowUser(generic.View):
    def get(self, request, user_id):
        follow_obj = request.user.following.filter(id=user_id)
        if follow_obj.exists():
            request.user.following.remove(user_id)
        else:
            request.user.following.add(user_id)
        return redirect('users:user_profile', user_id)


@method_decorator(decorator=(login_required, never_cache), name='dispatch')
class GetFollowingsList(generic.ListView):
    model = User
    template_name = 'user_account/followers_following_list.html'
    context_object_name = 'users'

    def get_queryset(self):
        username = self.kwargs.get('username')
        input_field = self.kwargs.get('input_field')
        if username:
            queryset = User.objects.filter(username=username)
            if queryset:
                if input_field == 'followings':
                    return queryset.first().following.all()
                elif input_field == 'followers':
                    return queryset.first().followers.all()
            else:
                return []
        return []
