from django.urls import path
from . import views

app_name = 'api'

urlpatterns = [
    path('list/', views.ListView.as_view(), name='list'),
    path('detail/<int:pk>', views.DetailView.as_view(), name='detail'),
]
