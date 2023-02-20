from django.urls import re_path
from PhoneApp import views

urlpatterns = [
    re_path(r'^initiate-call$', views.CallAPI),
    re_path(r'^call-report$', views.CallAPI)
]