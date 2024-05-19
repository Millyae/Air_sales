from django.http import HttpResponseNotFound, JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from .forms import EmailForm, NameForm, DateOfBirthForm, PhoneForm, PassportForm
from .models import Favorites, Tickets, PurchasedTickets

@require_http_methods(["POST"])
def validate_email(request):
    form = EmailForm(request.POST)
    if form.is_valid():
        return render(request, 'success.html')
    return render(request, 'email_form.html', {'form': form})

@require_http_methods(["POST"])
def validate_name(request):
    form = NameForm(request.POST)
    if form.is_valid():
        return render(request, 'success.html')
    return render(request, 'name_form.html', {'form': form})

@require_http_methods(["POST"])
def validate_date_of_birth(request):
    form = DateOfBirthForm(request.POST)
    if form.is_valid():
        return render(request, 'success.html')
    return render(request, 'date_of_birth_form.html', {'form': form})

@require_http_methods(["POST"])
def validate_phone_number(request):
    form = PhoneForm(request.POST)
    if form.is_valid():
        return render(request, 'success.html')
    return render(request, 'phone_form.html', {'form': form})

@require_http_methods(["POST"])
def validate_passport(request):
    form = PassportForm(request.POST)
    if form.is_valid():
        return render(request, 'success.html')
    return render(request, 'passport_form.html', {'form': form})

@require_http_methods(["GET"])
def get_favorite_tickets(request, user_id):
    try:
        favorites = Favorites.objects.get(user__id=user_id)
        return render(request, 'favorite_tickets.html', {'favorites': favorites})
    except Favorites.DoesNotExist:
        return HttpResponseNotFound('Favorites not found for this user')

@require_http_methods(["GET"])
def get_tickets(request):
    tickets = Tickets.objects.all()
    ticket_data = [{
        'id': ticket.id,
        'price': str(ticket.price),
        'departure_location': ticket.departure_location,
        'arrival_location': ticket.arrival_location,
        'flight': ticket.flight,
        'airplane': ticket.airplane,
        'sent_in_plane': ticket.sent_in_plane,
        'number_of_passengers': ticket.number_of_passengers
    } for ticket in tickets]
    return JsonResponse({'tickets': ticket_data})

@require_http_methods(["GET"])
def get_purchased_tickets(request, user_id):
    purchased_tickets = PurchasedTickets.objects.filter(user__id=user_id)
    tickets_data = list(purchased_tickets.values())
    return JsonResponse({'purchased_tickets': tickets_data})