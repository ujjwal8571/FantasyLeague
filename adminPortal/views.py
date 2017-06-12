from django.shortcuts import render

from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponse, render , HttpResponseRedirect
import sys
from .models import *




# Create your views here.

def admin_home(request):
    try:

        return render(request, 'adminPortal/admin_login_page.html',{})

    except BaseException as e:
        print(e + sys.exc_tb.tb_lineno)
        return HttpResponse("page not found")


def add_player_form(request):
    try:

        return render(request, 'adminPortal/addPlayerForm.html',{})

    except BaseException as e:
        print(e)
        return HttpResponse("page not found")



@csrf_exempt
def admin_login(request):
    try:
        if request.method == 'POST':


            posted_username = request.POST['username']
            posted_password = request.POST['password']

            user = authenticate(username=posted_username,password=posted_password)
            print(user)
            if user is None:

                return HttpResponse("You are not a registered user")

            admin_user = get_admin_by_user(user)

            if admin_user is None:
                return HttpResponse("BITCH, YOU ARE NOT THE ADMIN")



            login(request,user)
            # return HttpResponseRedirect('adminPortal/adminHome.html')
            return render(request, 'adminPortal/adminHome.html',{})
            # return HttpResponse("WELCOME BITCH, YOU BELONG HERE")

    except BaseException as e:
        print(e)
        return HttpResponse("Invalid Access")


def get_admin_by_user(user_arg):
    try:

        admin = ConsumerUser.objects.get(consumer_user = user_arg)
        print(admin)
        if admin is not None and admin.consumer_is_admin is True:
            return admin


        return None

    except Exception as e:
        print(e + sys.exc_tb.tb_lineno)
        return None



@login_required
def add_admin_request(request):

    try:
        if request.method == 'POST':

            posted_username = request.POST['username']
            posted_password = request.POST['password']

            user = User.objects.get(username = posted_username)

            if user is not None:
                consumer_user = ConsumerUser.objects.get(consumer_user = user)
                consumer_user.consumer_is_admin = True
                consumer_user.save()

                return HttpResponse(request,"Request Completed")

            new_user = User.objects.create_user(username=posted_username,email=None,password=posted_password)

            new_consumer_user = ConsumerUser(consumer_user = new_user)
            new_consumer_user.consumer_is_admin = True
            new_consumer_user.save()


    except Exception as e:
        print(e + sys.exc_tb.tb_lineno)
        return None

@login_required
@csrf_exempt
def add_player_request(request):
    try:
        if request.method == 'POST':
            player_first_name = request.POST['player_first_name']
            player_last_name = request.POST['player_last_name']
            player_age = request.POST['player_age']
            player_id = request.POST['player_id']
            player_country = request.POST['player_country']
            player_type =request.POST['player_type']
            player_price =request.POST['player_price']

            try:
                player_exists = Player.objects.get(player_id = player_id)
            except Player.DoesNotExist:
                player_exists = None

            if player_exists:
                return HttpResponse("BITCH PLAYER ALREADY EXISTS")

            new_player = add_new_player(player_first_name,player_last_name,player_age,player_id,player_country,player_type,player_price)
            print(new_player)
            if new_player:
                return HttpResponse("player added is %s %s" %(new_player.player_first_name,new_player.player_last_name))
                # return HttpResponse("player added")

    except Exception as e:
        print(e)
        return None


def add_new_player(player_first_name,player_last_name,player_age,player_id,player_country,player_type,player_price):
    try:
        new_player = Player()
        print("hello")
        new_player.player_first_name = player_first_name
        new_player.player_last_name = player_last_name
        new_player.player_id = player_id
        new_player.player_age = player_age
        new_player.player_price = player_price
        new_player.player_country = player_country
        new_player.player_type = player_type
        new_player.save()
        print(new_player)
        return new_player

    except Exception as e:
        print(e+ sys.exc_tb.tb_lineno)
        return None


@login_required
def update_player_request(request):
    try:
        if request.method == 'POST':
            player_first_name = request.POST['player_first_name']
            player_last_name = request.POST['player_last_name']
            player_age = request.POST['player_age']
            player_id = request.POST['player_id']
            player_country = request.POST['player_country']
            player_type =request.POST['player_type']
            player_price =request.POST['player_price']

            player_to_be_updated = find_player_by_id(posted_player_id)

            if player_to_be_updated is None:
                return HttpResponse(request,"THIS PLAYER ID DOES NOT EXIST",{})

            updated_player = update_player_details(player_to_be_updated,player_first_name,player_last_name,player_age,player_id,player_country,player_type,player_price)

            if updated_player:
                return HttpResponse(request,"PLAYER UPDATED",{})

            return HttpResponse(request,"ERROR 404",{})

    except Exception as e:
        print(e + sys.exc_tb.tb_lineno)
        return None

def update_player_details(player_to_be_updated,player_first_name,player_last_name,player_age,player_id,player_country,player_type,player_price):
    try:
        player_to_be_updated.player_first_name = player_first_name
        player_to_be_updated.player_last_name = player_last_name
        player_to_be_updated.player_age = player_age
        player_to_be_updated.player_id = player_id
        player_to_be_updated.player_type = player_type
        player_to_be_updated.player_country = player_country
        player_to_be_updated.player_price = player_price
        player_to_be_updated.save()

        return player_to_be_updated

    except Exception as e:
        print(e + sys.exc_tb.tb_lineno)
        return None





def find_player_by_id(player_id):
    try:
        player = Player.objects.get(player_id = player_id)

        return player

    except Exception as e:
        print(e + sys.exc_tb.tb_lineno)
        return None
