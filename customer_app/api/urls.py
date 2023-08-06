from django.urls import path
from customer_app.api.views import *

app_name = 'customer'

urlpatterns = [
    path('', customer_home_view, name='customerHomeView'),
    path('term_and_conitions/', customer_term_view, name='customerTermAndConView'),
    path('services/', customer_services_view, name='customerServicesView'),
    path('help/', customer_help_view, name='customerHelpView'),
    path('about/', customer_about_view, name='customerAboutView'),
]
