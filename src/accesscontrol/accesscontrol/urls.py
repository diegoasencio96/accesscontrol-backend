"""accesscontrol URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.utils.html import format_html
from apps.configurations.models import General

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.users.urls')),
    path('', include('apps.locks.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

try:
    general = General.objects.all().first()
    site_name = general.site_name
    logo_url = "/media/" + str(general.site_image)
    name = format_html("<img src={url} height={h} width={w}><br><h5>" + site_name + "</h5>", url=logo_url, w=general.with_image, h=general.height_image)
    admin.site.site_header = name if site_name else 'Administración del Sistema'
except:
    pass

admin.site.index_template = 'admin/index.html' # Test new index admin
