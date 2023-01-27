from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout

# Create your views here.
def signup_view(request):
    if request.method == 'POST':#when you send a post request by clicking
        form = UserCreationForm(request.POST)#will also show erros
        if form.is_valid():
            user = form.save()
            login(request,user)
            #log user in
            return redirect('articles:list')
    else:
        form = UserCreationForm()#its a get request so just loads you into the pag
    return render(request, "accounts/signup.html",{'form':form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            #log the user in
            user = form.get_user()#get the user from the auth form
            login(request,user)
            return redirect('articles:list')
    else:
        form = AuthenticationForm()
    return render(request, "accounts/login.html", {'form':form })

def logout_view(request):
    if request.method=='POST':
        logout(request)
        return redirect('articles:list')