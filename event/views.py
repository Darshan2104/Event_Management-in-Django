from django.shortcuts import render, redirect, get_object_or_404
# from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .models import Eventlist

# from event.form import EventForm
# from django.views.generic.edit import FormView
# from  django.views.generic import ListView

# Create your views here.


def home(request):
    context = {
        'eventlist': Eventlist.objects.all().order_by('StartingDate')
    }
    return render(request, 'event/home.html', context)


@login_required
def event_view(request):
    if request.method == 'POST':
        postby = request.user
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

        obj = Eventlist(postby=postby, title=event_title, description=description, organizer=organizer, joiningfees=fee, pricemoney=price, members=numberofparticipants,
                        link=link, Eventtime=duration, venue=venue, StartingDate=starting_date, Endingdate=ending_date, Category=category, numberofseats=numberofseats)

        obj.save()
        return redirect('/')
    else:
        requser = request.user
        obj1 = Eventlist.objects.filter(postby=requser)
        # # print(obj1)
        return render(request, 'event/event_view.html', {'obj': obj1})


@login_required
def event_add(request):
    return render(request, 'event/event_add.html', {})


@login_required
def event_update(request, my_id):
    if request.method == 'POST':
        obj = Eventlist.objects.get(id=my_id)
        return render(request, 'event/event_update.html', {'obj': obj})


@login_required
def event_updated(request, my_id):
    if request.method == 'POST':
        Eventlist.objects.filter(pk=my_id).update(postby=request.user, title=request.POST['event_title'], Category=request.POST['Category'], description=request.POST['description'], organizer=request.POST['organizer'], joiningfees=request.POST['fee'], venue=request.POST[
            'venue'], StartingDate=request.POST['starting_date'], Endingdate=request.POST['ending_date'], Eventtime=request.POST['duration'], pricemoney=request.POST['price'], members=request.POST['numberofparticipants'], link=request.POST['link'], numberofseats=request.POST['numberofseats'])
        return redirect('/event_view')
    else:
        requser = request.user
        obj1 = Eventlist.objects.filter(postby=requser)
        return render(request, 'event/event_view.html', {'obj1': obj1})


@login_required
def event_delete(request, my_id):
    obj = get_object_or_404(Eventlist, id=my_id)
    obj.delete()
    return redirect('/event_view')


def about(request):
    return render(request, 'event/about.html', {'title': 'About'})


def event_details(request, my_id):
    obj = Eventlist.objects.get(id=my_id)
    return render(request, 'event/event_details.html', {'obj': obj})


def user_details(request, username):
    obj = User.objects.get(username=username)
    return render(request, 'event/userdetail.html', {'obj': obj})
