
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from core.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('shop.urls')),
    path('signup/', signup, name="signup"),
    path('signin/', signin, name="signin"),
    path('profile/', profile, name="profile"),
    path('logout/', sign_out, name="logout"),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
