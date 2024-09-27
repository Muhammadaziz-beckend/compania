from django.urls import path
from .views import *

urlpatterns = [
    path("order/", order, name="order"),
    path("order/main/<int:id>/", order_main, name="main"),
    path("order/update/<int:id>/", update, name="update"),
    path("", index, name="home"),
]
