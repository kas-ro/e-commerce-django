from django.urls import path

from shop import views

app_name = 'shop'
urlpatterns = [
    path(route='', view=views.home_view, name='home'),
]