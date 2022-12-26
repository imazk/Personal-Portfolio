from django.urls import path
from . import views

urlpatterns = [
    path('',views.home_page,name="main_home" ),
    path('login/', views.loginpage, name="login"),
    path('resume/', views.resume, name="resume"),
    path('download/', views.download_pdf, name="download")

]