from django.shortcuts import render

def customer_home_view(request):
    return render(request, '../templates/customer_home_page.html', {})