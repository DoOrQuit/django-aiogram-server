from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, redirect
from django.urls import reverse

from core.services import GoogleCalendar

# Create your views here.


def home_page_view(request):
    calendar = GoogleCalendar("34d26d5fc687a92669649f6988b8ce852006f604a82e154ef055c991bbb24e49@group.calendar.google.com")  # TODO Insert Your CalendarId here
    # Returns events for next 2 days (might be adjusted)
    closest_events = calendar.events_list_simplified()[:3]
    return render(request, "core/home_base.html", context={"closest_events": closest_events})


def redirect_view(request):
    return redirect(reverse('core:home'), permanent=True)
