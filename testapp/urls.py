"""testapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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

# from django.contrib import admin
# from django.urls import path
#
# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]

from django.conf.urls import url

from . import view

urlpatterns = [
    url(r'^select$', view.ajax_mainpage),
    url(r'^terminal_svr$', view.terminal_svr, name='terminal_svr'),
    # url(r'^ajax_try$', view.ajax_try),
    url(r'^ajax_dict/$', view.ajax_dict, name='ajax-dict'),
    url(r'^ajax_readurl/$', view.ajax_readurl, name='ajax_readurl'),
    url(r'getdata/$',view.getdata),
]
