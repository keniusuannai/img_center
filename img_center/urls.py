"""img_center URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from placehold import views as placehold_views
from backstage import views as backstage_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^(\d+)[/]?$', placehold_views.index),
    url(r'^(\d+)[x|X](\d+)[/]?$', placehold_views.index),
    url(r'^(\d+)[x|X](\d+)/([0-9a-fA-F]{6}|[0-9a-fA-F]{3})/([0-9a-fA-F]{6}|[0-9a-fA-F]{3})$', placehold_views.index),

    url(r'^backstage/', backstage_views.index),
]
