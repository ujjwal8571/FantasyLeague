from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$',views.admin_home,name='admin_home'),
    url(r'^adminLoginRequest/',views.admin_login,name='admin_login'),
    url(r'^addAdmin/',views.add_admin_request,name='add_admin'),
    url(r'^addPlayer/',views.add_player_request,name='add_player'),
    url('^updatePlayer/',views.update_player_request,name='update_player'),
    url('^addPlayerForm/',views.add_player_form,name='add_player_form')

]
