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

            x = Event(name=name, loc=loc, img=img)
            x.save()
            return render(request,'index.html')
