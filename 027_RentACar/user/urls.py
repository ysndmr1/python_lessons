from django.urls import path, include

# afeter'/user/' isteklerinden sonra
urlpatterns = [path("auth/", include("dj_rest_auth.urls"))]


# ---------------------
# Router
# ---------------------
from rest_framework.routers import DefaultRouter
from .views import UserView

router = DefaultRouter()
router.register("", UserView)
urlpatterns += router.urls
