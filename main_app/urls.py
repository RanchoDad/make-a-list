from django.urls import path, include
from . import views


urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('playlists/', views.playlists_index, name='index'),
  path('playlists/<int:playlist_id>/', views.playlists_detail, name='detail'),
  path('playlists/create/', views.PlaylistCreate.as_view(), name='playlists_create'),
  path('playlists/<int:pk>/update/', views.PlaylistUpdate.as_view(), name='playlists_update'),
  path('playlists/<int:pk>/delete/', views.PlaylistDelete.as_view(), name='playlists_delete'),
  path('playlists/<int:playlist_id>/add_review/', views.add_review, name='add_review'),
#   path('playlists/<int:playlist_id>/add_photo/', views.add_photo, name='add_photo'),
  path('playlists/<int:playlist_id>/assoc_song/<int:song_id>/', views.assoc_song, name='assoc_song'),
  path('playlists/<int:playlist_id>/unassoc_song/<int:song_id>/', views.unassoc_song, name='unassoc_song'),
  path('songs/', views.SongList.as_view(), name='songs_index'),
  path('songs/<int:pk>/', views.SongDetail.as_view(), name='songs_detail'),
  path('songs/create/', views.SongCreate.as_view(), name='songs_create'),
  path('songs/<int:pk>/update/', views.SongUpdate.as_view(), name='songs_update'),
  path('songs/<int:pk>/delete/', views.SongDelete.as_view(), name='songs_delete'),
  path('accounts/signup/', views.signup, name='signup'),
  path('search/', views.search_view, name='search'),
]