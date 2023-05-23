from .views import UserCreateView, UserView
from rest_framework.routers import DefaultRouter
from django.urls import path, include

# '/user/':
urlpatterns = [
    path('auth/', include('dj_rest_auth.urls'))
]

# ---------- Router ----------
router = DefaultRouter()
router.register('create', UserCreateView)  # permissions.AllowAny
router.register('', UserView)  # permissions.IsAdminUser
urlpatterns += router.urls
