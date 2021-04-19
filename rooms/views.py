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
    country = request.GET.get("country", "KR")
    room_type = int(request.GET.get("room_type", 0))
    price = int(request.GET.get("price", 0))
    guests = int(request.GET.get("guests", 0))
    bedrooms = int(request.GET.get("bedrooms", 0))
    beds = int(request.GET.get("beds", 0))
    baths = int(request.GET.get("baths", 0))
    s_amenities = request.GET.get("amenities")
    s_facilities = request.GET.get("facilities")

    form = {
        "city": city,
        "s_country": country,  # selected country
        "s_room_type": room_type,  # selected room type
        "price": price,
        "guests": guests,
        "bedrooms": bedrooms,
        "beds": beds,
        "baths": baths,
    }

    room_types = models.RoomType.objects.all()
    amenities = models.Amenity.objects.all()
    facilities = models.Facility.objects.all()

    choices = {
        "countries": countries,
        "room_types": room_types,
        "amenities": amenities,
        "facilities": facilities,
    }

    return render(
        request,
        "rooms/search.html",
        {**form, **choices},
    )
