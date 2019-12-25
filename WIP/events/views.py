from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.utils import timezone
from .models import Event
from .forms import addEvent

def index(request):
	events = Event.objects.all()
	dayEvents = events.filter(eventType="Day Event")
	exams = events.filter(eventType="Exam")
	deadlines = events.filter(eventType="Deadline")
	return render(request, 'events/home.html', {'dayEvents': dayEvents, 'exams': exams, 'deadlines': deadlines})

def listOfEvents(request):
	events = Event.objects.all()
	return render(request, 'events/events.html', {'events': events})

def addNewEvent(request):
    if request.method == "POST":
        form = addEvent(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.dateCreated = timezone.now()
            event.save()
            return redirect(index)
    else:
        form = addEvent()
    return render(request, 'events/add.html', {'form': form})

def viewEvent(request, eventname):
	events = Event.objects.all()
	event = events.get(eventName=eventname)
	return render(request, 'events/viewEvent.html', {'event': event})

def settings(request):
	return render(request, 'events/settings.html')

def calendar(request):
	return render(request, 'events/calendar.html')

def deleteEvent(request, eventname):
	Event.objects.get(eventName=eventname).delete()
	events = Event.objects.all()
	return redirect(listOfEvents)