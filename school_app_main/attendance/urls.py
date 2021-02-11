from django.urls import path

from .views import AttendanceListView, AttendanceDetailView, AttendanceCreateView, AttendanceUpdateView, AttendanceDetailView, AttendanceDeleteView

urlpatterns = [
  path('list/', AttendanceListView.as_view(), name='attendance-list'),
  path('<int:pk>/', AttendanceDetailView.as_view(), name='attendance-detail'),
  path('create/', AttendanceCreateView.as_view(), name='attendance-create'),
  path('<int:pk>/update/', AttendanceUpdateView.as_view(), name='attendance-update'),
  path('<int:pk>/delete/', AttendanceDeleteView.as_view(), name='attendance-delete'),
]
