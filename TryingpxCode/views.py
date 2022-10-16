from django.shortcuts import render

# Create your views here.

def indexpxcode(request):
    return render(request, 'indexPX.html')