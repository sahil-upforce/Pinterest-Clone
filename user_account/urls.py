from django.urls import path

from user_account.views import (
    UserProfileView, UserSearchView, UserUpdateView, UserDeleteView, FollowUnfollowUser, UserPasswordChangeView,
    UserEmailVerification, UserPasswordResetView, UserPasswordResetConfirmView
)

app_name = 'users'

urlpatterns = [
    path('email-verification/<uid>/<token>', UserEmailVerification.as_view(), name='user_email_verification'),
    path('search', UserSearchView.as_view(), name='user_search'),
    path('delete-account/<str:username>', UserDeleteView.as_view(), name='delete_account'),
    path('profile/<int:id>', UserProfileView.as_view(), name='user_profile'),
    path('edit-profile/<str:username>', UserUpdateView.as_view(), name='edit_user'),
    path('follow-unfollow/<int:user_id>', FollowUnfollowUser.as_view(), name='follow_unfollow'),
    path('change-password', UserPasswordChangeView.as_view(), name='change_password'),

    path('password-reset', UserPasswordResetView.as_view(), name='password_reset'),
    path('reset/<uidb64>/<token>', UserPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
]
