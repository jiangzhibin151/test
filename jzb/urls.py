from django.conf.urls import url
from . import view

urlpatterns = [
    url(r'^$', view.userInfor),
    url(r'^userinfo/$', view.userInfor),
    url(r'^select/(\d+)/$', view.select, name='select'),
]