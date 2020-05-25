"""pd110 URL Configuration

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
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
#from django.urls import path

from boletin import views
from .views import v_contacto
from .views import v_desayunos
from .views import v_comidas
from .views import v_cenas
#from boletin.views inicio

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^$', views.inicio, name='inicio'),
    url(r'^v_contacto/$', v_contacto, name='v_contacto'),
    url(r'^v_desayunos/$', v_desayunos, name='v_desayunos'),
    url(r'^v_comidas/$', v_comidas, name='v_comidas'),
    url(r'^v_cenas/$', v_cenas, name='v_cenas'),
    
    # path('admin/', admin.site.urls),
    # path('', views.inicio, name='inicio'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    #urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)