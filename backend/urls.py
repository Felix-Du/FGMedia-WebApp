"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import routers
from fgcomboapp import views
from django.conf import settings
from django.urls import re_path
from django.views.static import serve
from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register(r'combos', views.ComboView, 'combo')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    re_path(r'^api/game/$', views.GameView.game_list),
    re_path(r'^api/game/([0-9])$', views.GameView.game_detail),
    re_path(r'^api/combo/$', views.ComboView.combo_list),
    re_path(r'^api/combo/([0-9])$', views.ComboView.combo_detail),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
