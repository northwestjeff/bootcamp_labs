from django.conf.urls import include, url
from django.contrib import admin
from polls import views

urlpatterns = [
    # ex: /polls/
    url(r'^$', views.home, name='index'),
    # ex: /polls/5/
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /polls/5/results/
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]

# CANNOT GET THE PAGE TO RENDER FOR POLLS.URL.PY FROM THE DJANGO TUTORIAL