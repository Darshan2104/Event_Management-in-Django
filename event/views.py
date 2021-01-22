from django.shortcuts import render, redirect, get_object_or_404
# from django.http import HttpResponse
from .models import Eventlist
# from event.form import EventForm
# from django.views.generic.edit import FormView

# from  django.views.generic import ListView

# Create your views here.


def home(request):
    context = {
        'eventlist': Eventlist.objects.all()
    }
    return render(request, 'event/home.html', context)


def event_view(request):
    if request.method == 'POST':
        event_title = request.POST['event_title']
        category = request.POST['Category']
        description = request.POST['description']
        organizer = request.POST['organizer']
        venue = request.POST['venue']
        starting_date = request.POST['starting_date']
        ending_date = request.POST['ending_date']
        duration = request.POST['duration']
        fee = request.POST['fee']
        price = request.POST['price']
        numberofparticipants = request.POST['numberofparticipants']
        link = request.POST['link']
        numberofseats = request.POST['numberofseats']

        obj = Eventlist(title=event_title, description=description, organizer=organizer, joiningfees=fee, pricemoney=price, members=numberofparticipants,
                        link=link, Eventtime=duration, venue=venue, StartingDate=starting_date, Endingdate=ending_date, Category=category, numberofseats=numberofseats)
        obj.save()
        return redirect('/')
    else:
        return render(request, 'event/event_view.html', {})


# class EventView(FormView):
#     template_name = 'event_view.html'
#     form_class = EventForm
#     success_url = '/thanks/'

#     def form_valid(self, form):
#         # This method is called when valid form data has been POSTed.
#         # It should return an HttpResponse.
#         # form.send_email()
#         return super().form_valid(form)

def event_add(request):
    return render(request, 'event/event_add.html', {})


def get_id(request):
    return render(request, 'event/getid.html', {})


def event_update(request):
    if request.method == 'POST':
        eventid = request.POST['eventid']
        obj = Eventlist.objects.get(id=eventid)
        Eventlist.objects.get(id=eventid).delete()
        return render(request, 'event/event_update.html', {'obj': obj})


def event_delete(request):
    eventid = request.POST['eventid']
    obj = get_object_or_404(Eventlist, id=eventid)
    obj.delete()
    return redirect('/')


def about(request):
    return render(request, 'event/about.html', {'title': 'About'})


def event_details(request, my_id):
    obj = Eventlist.objects.get(id=my_id)
    return render(request, 'event/event_details.html', {'obj': obj})
