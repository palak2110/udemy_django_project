from django.shortcuts import render

# Create your views here.
def wordimage(request):
	words = word.objects
	return render(request,'home.html',{'words':words})