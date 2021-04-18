from django.views.generic import ListView, DetailView
from django.http import Http404
from django.shortcuts import render
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