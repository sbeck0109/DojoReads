from django.urls import path
from . import views

urlpatterns = [
    path('', views.loginReg),
    path('process_reg', views.process_reg),
    path('process_login', views.process_login),
]
