
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from app1.views import StudentModelViewSet
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()

router.register('student', StudentModelViewSet, basename='student')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('auth/', include('auth_app.urls')),
    path('token/', obtain_auth_token)

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

