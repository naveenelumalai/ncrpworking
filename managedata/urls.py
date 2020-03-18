from django.urls import path

from . import views

urlpatterns = [
    path('complaints/', views.ComplaintsListView.as_view(), name='complaints'),
    path('complaints/<int:pk>', views.ComplaintsDetailView.as_view(), name='complaints-detail'),

]