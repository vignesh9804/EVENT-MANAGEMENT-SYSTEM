from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import Event
from .forms import EventForm,SignUpForm
def home(request):
    # template=loader.get_template('event.html')
    return render(request,'event.html')
def login(request):
    return render(request,'event2.html')
def addevent(request):
    return render(request,'event3.html')

def event_list(request):
    events = Event.objects.all()
    return render(request, 'event_list.html', {'events': events})

def add_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('event_list')
    else:
        form = EventForm()

    return render(request, 'add_event.html', {'form': form})

def delete_event(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    deleted_sno = event.s_no  # Store the S.No before deletion
    event.delete()

    # Update the S.No for events with higher S.No values
    events_after_deletion = Event.objects.filter(s_no__gt=deleted_sno)
    for event in events_after_deletion:
        event.s_no -= 1
        event.save()

    return redirect('event_list')

def number_del(request):
    # template=loader.get_template('event.html')
    return render(request,'number_delete.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()  # This line saves the user data to the database
            return redirect('signup_success')  # Create a success page or redirect to another page
    else:
        form = SignUpForm()

    return render(request, 'signup.html', {'form': form})