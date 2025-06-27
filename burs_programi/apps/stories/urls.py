from django.urls import path
from .views import testimonial_view, story_detail

urlpatterns = [
    path('', testimonial_view, name='testimonials'),
    path('basari-hikayesi/<slug:slug>/', story_detail, name='story_detail'),

]
