from django.shortcuts import render
from .models import Event
# Create your views here.
def index(request):

    events = Event.objects.all()

    return render(request, "index.html", {'events': events})

def createpost(request):
        if request.method == 'POST':
            name = request.POST['name']
            loc = request.POST['loc']
            img = request.POST['img']
            date = request.POST['date']
            time = request.POST['time']

            x = Event(name=name, loc=loc, img=img, date=date, time=time)
            x.save()
            return render(request,'index.html')
