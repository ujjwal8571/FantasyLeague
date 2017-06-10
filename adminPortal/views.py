from django.shortcuts import render

from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import HttpResponse, render , HttpResponseRedirect
import sys
from .models import *




# Create your views here.

def admin_home(request):
    try:

        return render(request, 'adminPortal/admin_login_page.html',{})

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

            if user is None:

                return HttpResponse("You are not a registered user")

            admin_user = get_admin_by_user(user)

            if admin_user is None:
                return HttpResponse("BITCH, YOU ARE NOT THE ADMIN")



            login(request,user)
            # return HttpResponseRedirect(reverse('#TODO'))
            return HttpResponse("WELCOME BITCH, YOU BELONG HERE")

    except BaseException as e:
        # print(e + sys.exc_traceback.tb_lineno)
        return HttpResponse("Invalid Access")


def get_admin_by_user(user_arg):
    try:

        admin = ConsumerUser.objects.get(consumer_user = user_arg)
        print(admin)
        if admin is not None and admin.consumer_is_admin is True:
            return admin


        return None

    except Exception as e:
        # print(e + sys.exc_traceback.tb_lineno)
        return None
