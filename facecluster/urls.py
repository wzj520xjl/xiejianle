from django.conf.urls import url

from facecluster import views

urlpatterns = [
    url(r'index/',views.index,name='index'),
]