from django.urls import path, include
# import server
from .router import logs_router
from . import views

app_name = "server"

urlpatterns = [
    path('get-logs/', views.get_logs, name="get-logs"),
    path('', views.home, name="home"),
    path('home/', views.home, name="home"),
    # path('home/', views.get_logs, name="get-logs"),
    # path('home', include(logs_router.urls)),
]

