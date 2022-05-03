from django.urls import path

from housing_operations import views as housing_views



urlpatterns = [
     path('new_house',housing_views.post_new_house,name="new_house"),
     path('all_houses',housing_views.get_houses,name="houses"),
]
