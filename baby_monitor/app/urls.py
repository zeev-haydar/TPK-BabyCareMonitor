from django.urls import path
from . import views

# API endpoints
urlapipatterns = [
    path('audio_prediction/', views.process_the_audio, name="audio_prediction"),
    path('song/', views.baby_song, name="baby_song"),
    path('hello/', views.hello_world, name="hello_world"),
    path('baby_status/', views.check_baby_status, name="baby_status"),
]

# Template endpoints
urltemplatepatterns = [
    path('video_stream/', views.video_stream_view, name='video_stream'),
]