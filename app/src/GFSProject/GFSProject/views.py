from django.shortcuts import render
 
def index(request):
    return render(request, 'index.html', {})

def murmur(request):
    return render(request, 'murmur/list.html')

def diary(request):
    return render(request, 'diary/list.html')

    
def scraps(request):
    return render(request, 'scraps/list.html')