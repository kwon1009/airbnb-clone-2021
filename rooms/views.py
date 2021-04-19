from django.views.generic import ListView, DetailView
from django.shortcuts import render
from django_countries import countries
from . import models


# Class Based View
class HomeView(ListView):

    """ Home View Definition """

    model = models.Room
    paginate_by = 10
    ordering = "created"
    context_object_name = "rooms"


# Function Based View - room detail
"""
def room_detail(request, pk):
    try:
        room = models.Room.objects.get(pk=pk)
        return render(
            request,
            "rooms/detail.html",
            {
                "room": room,
            },
        )
    except models.Room.DoesNotExist:
        raise Http404()
"""

# Class Based View - room detail
class RoomDetail(DetailView):

    """ Room Detail Definition """

    model = models.Room


def search(request):
    city = request.GET.get("city", "Anywhere")
    city = str.capitalize(city)
    room_types = models.RoomType.objects.all()
    print(countries)
    return render(
        request,
        "rooms/search.html",
        {
            "city": city,
            "countries": countries,
            "room_types": room_types,
        },
    )
