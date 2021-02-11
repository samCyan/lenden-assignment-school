from django.urls import path

from .views import SubjectListView, SubjectDetailView, SubjectCreateView, SubjectUpdateView, SubjectDetailView, SubjectDeleteView

urlpatterns = [
  path('list/', SubjectListView.as_view(), name='subject-list'),
  path('<int:pk>/', SubjectDetailView.as_view(), name='subject-detail'),
  path('create/', SubjectCreateView.as_view(), name='subject-create'),
  path('<int:pk>/update/', SubjectUpdateView.as_view(), name='subject-update'),
  path('<int:pk>/delete/', SubjectDeleteView.as_view(), name='subject-delete'),
]
