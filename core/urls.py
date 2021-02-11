from django.urls import path

from . import views

urlpatterns = [
  path('', views.IndexView.as_view(), name='home'),
  path('site-config', views.siteconfig_view, name='configs'),

]
