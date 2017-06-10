from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$',views.admin_home,name='admin_home'),
    url(r'^admin_login_request/',views.admin_login,name='admin_login'),
]
