from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from adverts.views import (AdvertDetailsView,
                           AdvertCreateView,
                           AdvertUpdateView,
                           AdvertDeleteView,
                           AdvertActivateView,
                           UserAdvertView,
                           load_models,
                           load_years,
                           )

app_name = "adverts"

urlpatterns = [
    path("<int:pk>/", AdvertDetailsView.as_view(), name="advert"),
    path("create/", AdvertCreateView.as_view(), name="advert_create"),
    path("create/load_models/", load_models, name="load_models"),
    path("create/load_years/", load_years, name="load_years"),
    path("<int:pk>/update/", AdvertUpdateView.as_view(), name="update-advert"),
    path("<int:pk>/confirm-delete/", AdvertDeleteView.as_view(), name="confirm-delete-advert"),
    path("<int:pk>/confirm-activate/", AdvertActivateView.as_view(), name="confirm-activate-advert"),
    path("user-adverts/", UserAdvertView.as_view(), name="user-adverts"),


]


