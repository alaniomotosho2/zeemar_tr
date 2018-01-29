from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request,'app/index.html')


def about_us(request):
	return render(request,'app/about.html')

def profile(request):
	return render(request,'app/profile.html')
