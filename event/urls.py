from django.urls import path
from . import views
from users import views as views1

urlpatterns = [
    path('', views.home, name='event-home'),
    path('event_view/', views.event_view, name='event-view'),
    path('about/', views.about, name='event-about'),
    path('register/', views1.register, name='users-register'),
    path('event_view/add/', views.event_add, name='event_add'),
    path('event_view/getid/', views.get_id, name='get_id'),
    path('event_view/getid/update', views.event_update, name='event_update'),
    path('event_view/getid/delete', views.event_delete, name='event_delete'),
    path('event_details/<int:my_id>', views.event_details, name='event_details')
]
