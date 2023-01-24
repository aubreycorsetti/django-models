from django.urls import path
from .views import SnackListView, HomePageView, SnackDetailView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('snack/', SnackListView.as_view(), name='snack_list'),
    path('snack/<int:pk>/', SnackDetailView.as_view(), name='snack_detail'),

]
