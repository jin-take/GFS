from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .forms import EventForm
from .models import Event, Category, Tag

def EventsList(request):
    if 'POST' in request.method:
        if 'category' in request.POST and request.POST['category']:
            events = Event.objects.filter(category__name=request.POST['category']).values('id', 'title', 'date')  # ...1
        else:
            events = Event.objects.values('id', 'title', 'date')
    else:
        events = Event.objects.values('id', 'title', 'date')
    categories = Category.objects.values('name')  # ...2

    return render(request, 'scraps/list.html', {'categories': categories, 'events': events})  # ...3


def PostEvent(request):
    if request.method == 'POST':
        form = EventForm(request.POST)  # ...1
        if form.is_valid():  # ...2
            form.save()
            return render(request, 'scraps/post.html', {'form': form})  # ...3

    return render(request, 'scraps/post.html', {'form': EventForm()})

def EventDetail(request, id):
    return render(request, 'scraps/detail.html', {'event': Event.objects.get(id=id)})
