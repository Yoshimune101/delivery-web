from django.urls import include, path
from . import views
from .views import index
from django.contrib.auth import views as auth_views

app_name = 'delivery_web_app'

urlpatterns = [
    path('', index, name='index'),

    #path('URLを記載/', views.SignUpSuccessView.as_view(), name='名前を記載'),

]