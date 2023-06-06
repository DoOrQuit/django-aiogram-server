# django-aiogram-server

Backend server to test an aiogram bot.

Requires to create  Google Developer Profile to get a service_mail.json file, which has to be inserted when GoogleCalendar instance creates in "home_view".

On the server itself not much fuatures implemented:
1) User and UserProfile models;
2) User objection creating utilizing API routing;
3) Login and Registration pages. First I was planning to make a functionality for user (to search for service) and admin (to manage incoming requests for a service). But finally decided to keep the home page available only for admin as a hub to monitor scheduled services to take care of. For this reason home_page is available only for superusers while login and registration for everyone just to demonstrate some skills.
4) On the home_page I've made a list of closest task to carry out. Task are groupped by date and sorted by time. Information on task plate such as date adn time retrieved from Googe Calendar API. Customer name ad description just a placeholders.
