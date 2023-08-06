from django.shortcuts import render

def customer_home_view(request):
    return render(request, '../templates/customer_home_page.html', {})

def customer_term_view(request):
    return render(request, '../templates/pages/terms_and_condition_page.html', {})

def customer_services_view(request):
    return render(request, '../templates/pages/services_page.html', {})

def customer_help_view(request):
    return render(request, '../templates/pages/help_page.html', {})

def customer_about_view(request):
    return render(request, '../templates/pages/about_page.html', {})

