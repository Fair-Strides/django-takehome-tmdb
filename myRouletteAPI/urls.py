from django.urls import path
from . import views

urlpatterns = [
    path('search/title=<title>', views.search, name='search'),
    path('details/movieId=<movieId>', views.details, name='details')
]