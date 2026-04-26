"""theanimeradio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from pages import views as page_views

urlpatterns = [
    path("",include("pages.urls")),
    path("usersreg/", include("usersreg.urls")),
    path("reccomendation/", include("reccomendationengine.urls")),
    path("recommendation/", include("reccomendationengine.urls")),
    path("polling/", include("polling.urls")),
    path("sitemap.xml", page_views.sitemap, name="sitemap"),
    path("robots.txt", page_views.robots_txt, name="robots_txt"),
    path('admin/', admin.site.urls),
]

urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
