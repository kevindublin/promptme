from django.urls import path

from apps.core import views

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('about/', views.about, name='about'),
    path('form', views.form, name='form'),
    path('feedbackq/', views.feedbackq, name='feedbackq'),
    path('prompt/', views.prompt, name='prompt'),
    path('write/', views.write, name='write'),
    path('edit/', views.edit, name='edit'),
    path('membership', views.membership, name='membership'),
    path('update-draft/<draft_id>/', views.update_draft),
    path('delete-draft/<draft_id>/', views.delete_draft),
]
