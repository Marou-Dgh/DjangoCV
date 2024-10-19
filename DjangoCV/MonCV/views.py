from django.shortcuts import render

def MonCV_view(request):
    return render(request, 'MonCV/MonCV.html') # Pointing to my MonCV template