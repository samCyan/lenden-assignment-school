from django.urls import path

from .views import StaffAnalyticsListView, StaffAnalyticsDetailView

urlpatterns = [
  path('list/', StaffAnalyticsListView.as_view(), name='staff-analytics-list'),
  # path('<int:pk>/', StaffAnalyticsDetailView.as_view(), name='staff-analytics-detail')
]
