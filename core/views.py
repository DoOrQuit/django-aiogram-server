from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, redirect
from django.urls import reverse

from core.services import GoogleCalendar

# Create your views here.


@user_passes_test(lambda user: user.is_superuser)
def home_page_view(request):
    calendar = GoogleCalendar()  # TODO Insert Your CalendarId here
    # Returns events for next 2 days (might be adjusted)
    closest_events = calendar.events_list_simplified()[:3]
    return render(request, "core/home_base.html", context={"closest_events": closest_events})


def redirect_view(request):
    return redirect(reverse('core:home'), permanent=True)
