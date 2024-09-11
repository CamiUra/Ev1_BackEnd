from django.shortcuts import render


def viewHome (request):
    return render(request, 'App/home.html')

def viewPage1 (request):
    return render(request, 'App/page1.html')

def viewPage2 (request):
    return render(request, 'App/page2.html')

def viewPage3 (request):
    return render(request, 'App/page3.html')

def viewPage4 (request):
    return render(request, 'App/page4.html')

def viewPage5 (request):
    return render(request, 'App/page5.html')

def viewPage6 (request):
    return render(request, 'App/page6.html')