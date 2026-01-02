from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BorrowingViewSet

app_name = "borrowings_service"

router = DefaultRouter()
router.register("borrowings", BorrowingViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
