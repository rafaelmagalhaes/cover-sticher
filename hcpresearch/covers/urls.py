from django.urls import path

from . import views

app_name = "covers"

urlpatterns = [
    path('', views.index, name='cover-index'),
    path('process_images', views.CoversViews.as_view())
]
