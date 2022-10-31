from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'ticket', views.TicketViewset)
router.register(r'event', views.EventViewset)
router.register(r'eventCategory', views.EventCategoryViewset)

urlpatterns = [
    path('', include(router.urls))
]