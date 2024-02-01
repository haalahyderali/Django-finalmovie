from . import views
from django.urls import path
app_name='finalmovieapp'
from .views import MovieCreateView,MovieListView,CommentCreateView

urlpatterns = [
    # path('',views.home,name='home'),
    path('',views.allMoviesCat,name='allMoviesCat'),

    path('cbvadd/', MovieCreateView.as_view(), name='task-create'),
    path('cbvcomment/<int:pk>/', CommentCreateView.as_view(), name='add_comment'),
    path('movies/', MovieListView.as_view(),name='movies'),
    path('cbvupdate/<int:pk>/', views.MovieUpdateView.as_view(), name='cbvupdate'),
    path('cbvdelete/<int:pk>/', views.MovieDeleteView.as_view(), name='cbvdelete'),

    path('<slug:c_slug>/' ,views.allMoviesCat,name='movie_by_category'),
    path('<slug:c_slug>/<slug:movie_slug>/', views.movieDetail, name='moviesCatDetail'),




    ]