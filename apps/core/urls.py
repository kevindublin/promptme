from django.urls import path

from apps.core import views

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('feedback-dashboard/<draft_id>/', views.feedback_dashboard),
    path('about/', views.about, name='about'),
    path('privacy/', views.privacy, name='privacy'),
    path('feedbackq/', views.feedbackq, name='feedbackq'),
    path('prompt/', views.prompt, name='prompt'),
    path('write/', views.write, name='write'),
    path('edit/', views.edit, name='edit'),
    path('update-draft/<draft_id>/', views.update_draft),
    path('delete-draft/<draft_id>/', views.delete_draft),
    path('send-to-queue/<draft_id>/', views.send_to_queue),
    path('remove-from-queue/<draft_id>/', views.remove_from_queue),
    path('queue-next/', views.queue_next, name="queue_next"),
    path('delete-feedback/<int:feedback_id>/<int:draft_id>',
         views.delete_feedback, name="delete-feedback"),
    path('contact/', views.contact, name='contact'),

]
