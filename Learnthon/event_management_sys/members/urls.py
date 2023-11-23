from django.urls import path
from .views import home,login,addevent,event_list,add_event,delete_event,number_del,signup
urlpatterns=[
    path('',home,name='members'),
    path('login',login),
    path('addevent',addevent),
    path('events/', event_list, name='event_list'),
    path('add_event/', add_event, name='add_event'),
    path('delete_event/<int:event_id>/',delete_event, name='delete_event'),
    # path('number_del/', delete_event_by_sno, name='delete_event_by_sno'),
    path('delete_number/',number_del),
    path('signup/', signup, name='signup'),


]