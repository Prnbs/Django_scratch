__author__ = 'prnbs'

from django.conf.urls import url
import auth_auth.views

urlpatterns = [
    url(r'^login/$', auth_auth.views.login_view),
    url(r'^logout/$', auth_auth.views.logout_view),

]
