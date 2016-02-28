from django.shortcuts import render
from django.contrib import auth
from django.http import HttpResponseRedirect
from auth_auth.forms import LoginForm

# Create your views here.



def login_view(request):
    username = request.POST.get('email', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)
    if user is not None and user.is_active:
        auth.login(request, user)

        return HttpResponseRedirect("/links/getmyurl/")
    else:
        # show error page
        form = LoginForm()
        return render(request, 'login.html', {'form': form})


def logout_view(request):
    auth.logout(request)
    # redirect to a success page
    return HttpResponseRedirect("/auth_auth/loggedout/")