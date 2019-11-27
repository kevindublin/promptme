from django.urls import path

from apps.accounts import views

urlpatterns = [
    path('login/', views.log_in, name='login'),
    path('signup/', views.sign_up, name='signup'),
    path('logout/', views.logout_view, name='logout'),
    path('edit-profile/', views.edit_profile, name='edit_profile'),
    path('users/', views.view_all_users, name='view_all_users'),
    path('users/<username>/', views.view_profile, name='view_profile'),
    path('membership/', views.membership, name='membership'),
    path('update-prompt/<prompt_id>/', views.update_prompt),
    path('write-userprompt/<prompt_id>/', views.write_userprompt),
    path('delete-prompt/<prompt_id>/', views.delete_prompt, name='delete_prompt'),
    path('public-toggle/<prompt_id>/', views.public_toggle, name='public_toggle'),
    path('upvote-prompt/<prompt_id>/', views.upvote_prompt),
    path('downvote-prompt/<prompt_id>/', views.downvote_prompt),
]
