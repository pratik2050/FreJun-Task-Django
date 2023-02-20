from django.urls import re_path
from PhoneApp import views

urlpatterns = [
    re_path(r'^initiate-call$', views.postApi),
    re_path(r'^call-report/([0-9999999999]+)$', views.getAPI)
]