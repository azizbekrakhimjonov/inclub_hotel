
from django.views.generic import ListView
from app.models import *
from django.shortcuts import render



def main(request):
    famous = Famous_Hotels.objects.all()
    return render(request, 'index.html', {'famouss': famous})



class InfoListView(ListView):
    model = Hotel
    template_name = 'rooms-single.html'
    context_object_name = 'rooms'

class MainListView(ListView):
    model = Hotel
    template_name = 'rooms.html'
    context_object_name = 'rooms'




def hotel_search(request):
    district = request.GET.get('district', '')
    rooms = Hotel.objects.filter(district__icontains=district)  # qidiruvni amalga oshirish
    return render(request, 'rooms.html', {'rooms': rooms})