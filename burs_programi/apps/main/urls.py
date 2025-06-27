from django.urls import path
from .views import home_view, scholarship_program_list, scholarship_program_detail, application_form_view, robots_txt

urlpatterns = [
    path('', home_view, name='home'),
    path('scholarships/', scholarship_program_list, name='scholarship_program_list'),
    path('scholarships/<slug:slug>/', scholarship_program_detail, name='scholarship_program_detail'),
    path('apply/', application_form_view, name='application_form'),
    path("robots.txt/", robots_txt, name="robots_txt"),

]

