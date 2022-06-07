from django.urls import path
from . import views

urlpatterns = [
    path("home",views.home,name="home"),
    path('delete/<int:event_id>', views.delete_event, name='delete'),
]


