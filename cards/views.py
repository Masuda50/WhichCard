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
            find_cards(groceries, gas, travels, clothes, everything_else)

            redirect("cards/display_cards.html")
    # if a GET (or any other method) we'll create a blank form
    else:
        form = CreditForm()

    return render(request, 'cards/forms.html', {'form': form})


# The method will likely be split
def find_cards(groceries, gas, travels, clothes, everything_else):
    #TODO
    # compute the value for all cards from the database
    # add every value to the dictionary of type ChosenCards (found in object.py)
    # sort the dictionary by card values - custom comparator
    # take up to the first 5 cards from the list find them in thh database
    # (cards can be queried from the database using their names)
    # when cards found in the database display their:
    #     name, bank, annual fee, rewards type, credit score
    print(" Got the form data ")
    print("groceries", groceries)
    print("gas", gas)
    print("travels", travels)
    print("clothes", clothes)
    print("everything else", everything_else)
    print("\n")