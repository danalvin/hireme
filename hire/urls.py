from django.urls import path, include
from .views import *

app_name = 'hire'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('events', EventListView.as_view(), name= 'events'),
    path('events/<int:id>' , EventDetailsView.as_view(), name = 'event-details'),
    path('event/create', EventCreateView.as_view(), name = 'create-event'),
]
