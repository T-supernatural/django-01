from django.urls import path
from .views import home_view, details_home, update_view

urlpatterns = [
    path('', home_view, name='home'),
    path('book/<int:book_id>/', details_home, name='details_page'),
    path('update/<int:book_id>/', update_view, name='update_page')
]