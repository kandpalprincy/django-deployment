from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'basic_app/index.html')
def relative(request):
    return render(request,'basic_app/relative.html')
def random(request):
    return render(request,'basic_app/random.html')
