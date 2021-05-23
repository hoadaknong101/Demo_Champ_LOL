from django.urls import path
from .views import HomeView, get_Cosplay,  get_General, get_General_With_Name, post_Cosplay
urlpatterns = [
    path('', HomeView),
    path('home/', HomeView),
    path('general/', get_General),
    path('general/<str:general_name>', get_General_With_Name),
    path('cosplay/', get_Cosplay),
    path('addcosplay/', post_Cosplay),
]
