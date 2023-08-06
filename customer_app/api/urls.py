from django.urls import path
from customer_app.api.views import customer_home_view

app_name = 'customer'

urlpatterns = [
    path('', customer_home_view, name='customerHomeView'),
]
