from django.urls import path
from snippets import views
from django.urls import path, include

urlpatterns = [
    path('snippets/', views.snippet_list),
    path('snippets/<int:pk>/', views.snippet_detail),
    path('', include('snippets.urls')),
]