from django.urls import path

from .views import ClassRoomListView, ClassRoomDetailView, ClassRoomCreateView, ClassRoomUpdateView, ClassRoomDetailView, ClassRoomDeleteView

urlpatterns = [
  path('list/', ClassRoomListView.as_view(), name='classroom-list'),
  path('<int:pk>/', ClassRoomDetailView.as_view(), name='classroom-detail'),
  path('create/', ClassRoomCreateView.as_view(), name='classroom-create'),
  path('<int:pk>/update/', ClassRoomUpdateView.as_view(), name='classroom-update'),
  path('<int:pk>/delete/', ClassRoomDeleteView.as_view(), name='classroom-delete'),
]
