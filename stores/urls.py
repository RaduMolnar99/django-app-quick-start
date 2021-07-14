from django.urls import include, path
from rest_framework import routers

from stores import views


router = routers.DefaultRouter(trailing_slash=False)
router.register(r"stores", views.SearchView)

urlpatterns = [
    path("", include(router.urls)),
]