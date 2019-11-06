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
    path('update-draft/<draft_id>/', views.update_draft),
    path('delete-draft/<draft_id>/', views.delete_draft),
    path('send-to-queue/<draft_id>/', views.send_to_queue),
    path('remove-from-queue/<draft_id>/', views.remove_from_queue),
    path('next-in-queue/', views.next_in_q, name='next_in_q'),
]
