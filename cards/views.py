from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import Card
from django.shortcuts import redirect
# Create your views here.
from cards.forms import CreditForm


def home(request):
    return render(request, 'cards/homepage.html')


def get_display_cards(request):
    return render(request, 'cards/display_cards.html')


def get_info(request):
    # if this is a POST request we need to process the form data
    print("IN THE FORM") # testing if we're in the method
    if request.method == 'POST':
        print("FORM IS VALID---") # testing whether  form can be submitted
        # create a form instance and populate it with data from the request:
        form = CreditForm(request.POST)
        if form.is_valid():
            # extract the data from the form.cleaned_data
            groceries = form.cleaned_data['groceries']
            gas = form.cleaned_data['gas']
            travels = form.cleaned_data['travels']
            clothes = form.cleaned_data['clothes']
            everything_else = form.cleaned_data['etc']

            # find_cards(groceries, gas, travels, clothes, everything_else)

            return redirect("/display_cards")
    # if a GET (or any other method) we'll create a blank form
    else:
        form = CreditForm()

    return render(request, 'cards/forms.html', {'form': form})


def about_us(request):
    return render(request, 'cards/AboutUs.html')
