"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from blog_app import views as blog_app_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', blog_app_views.home, name='home'),
    url(r'^single_post/(?P<slug>[\w-]+)/$', blog_app_views.single_post, name='single_post')

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# url(r'^blog/', 'myapp.views.blog', name='blog'),
# url(r'^blog/(?P<slug>[\w-]+)/$', 'myapp.views.blog_detail', name='blog_detail'),
#
# url(r'^blog/$', 'myapp.views.blog', name='blog'),
# url(r'^blog/(?P<slug>[\w-]+)/$', 'myapp.views.blog_detail', name='blog_detail'),