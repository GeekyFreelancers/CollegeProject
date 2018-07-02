from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request,'Feedback/Login.html')

def register(request):
    return render(request,'Feedback/Register.html')

