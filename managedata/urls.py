from django.urls import path

from . import views

urlpatterns = [
    path('', views.ComplaintsListView.as_view(), name='complaints-list'),
    path('search', views.SearchResultsView.as_view(), name='search_results'),
    path('<int:pk>', views.ComplaintsDetailView.as_view(), name='complaints-detail'),
    path('addcomplaint',views.ComplaintCreate.as_view(), name='add-complaint'),
    path('<int:pk>/update',views.ComplaintUpdate.as_view(), name = 'update-complaint'),
    
]