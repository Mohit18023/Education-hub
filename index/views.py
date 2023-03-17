from django.shortcuts import render

# Create your views here.
def indexaction(request):
    return render(request,'index_page.html')