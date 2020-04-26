from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import Card
from django.shortcuts import redirect
from cards.forms import CreditForm
from .object import ChosenCards
import operator
# Create your views here.


def home(request):
    return render(request, 'cards/homepage.html')


def get_display_cards(request):
    return render(request, 'cards/display_cards.html')


def get_info(request):
    # if this is a POST request we need to process the form data
    print("IN THE FORM")  # testing if we're in the method
    if request.method == 'POST':
        print("FORM IS VALID---")  # testing whether  form can be submitted
        # create a form instance and populate it with data from the request:
        form = CreditForm(request.POST)
        if form.is_valid():
            # extract the data from the form.cleaned_data
            groceries = form.cleaned_data['groceries']
            dining_out = form.cleaned_data['dining']
            gas = form.cleaned_data['gas']
            travel = form.cleaned_data['travels']
            everything_else = form.cleaned_data['etc']

            credit_score = form.cleaned_data['credit_score']
            annual = form.cleaned_data['annual']
            banks = form.cleaned_data['banks']
            if banks == ['all']:
                banks = ['chase', 'citi', 'amex', 'capital one', 'bank of america', 'wells fargo']
            # test, retrieving additional info
            print(credit_score)
            print(annual)
            print(banks)

            list_of_cards = get_best_cards(groceries, dining_out, gas, travel, everything_else)
            best_cards=[]

            for card in list_of_cards:
                card_obj = get_cards(card)
                best_cards.append(card_obj)

            context = {}
            context['best_cards'] = best_cards
            return render(request, 'cards/forms.html', context)
    # if a GET (or any other method) we'll create a blank form
    else:
        form = CreditForm()
    return render(request, 'cards/forms.html', {'form': form})


def get_cards(card_param):
    assert card_param is not None

    card = Card.objects.get(cardName=card_param)
    return card


# The method will likely be split
def get_best_cards(grocery_input, dining_out_input, gas_input, travel_input, everything_else_input):
    # checking params are non negative values and are not empty
    for parameter in locals().values():
        assert parameter >= 0 and parameter is not None

    cards_by_value = ChosenCards()
    card_set = Card.objects.all()

    for card in card_set:
        card_value = float(calculate_card_value(card, grocery_input, dining_out_input, gas_input, travel_input,
                                          everything_else_input))
        print("%s value: %d" %(card.cardName, card_value))
        cards_by_value.chosen_cards[card.cardName] = card_value

    print('Before sorting:')
    print(cards_by_value.chosen_cards)

    sorted_cards = sort_cards_by_value(cards_by_value.chosen_cards)

    print('After sorting:')
    print(sorted_cards)

    return list(sorted_cards.keys())


def calculate_card_value(card, grocery_input, dining_out_input, gas_input, travel_input, everything_else_input):
    for parameter in list(locals().values())[1:]:
        assert parameter >= 0 and parameter is not None

    card_grocer_multiplier = card.groceryMultiplier
    card_restaurant_multiplier = card.restMultiplier
    card_gas_multiplier = card.gasMultiplier
    card_travel_multiplier = card.travelMultiplier
    card_everything_else_multiplier = card.elseMultiplier
    card_reward_value = card.rewardValue
    card_annual_fee = card.annualFee

    card_value = float((((grocery_input * card_grocer_multiplier) + (dining_out_input * card_restaurant_multiplier)
                   + (gas_input * card_gas_multiplier) + (travel_input * card_travel_multiplier)
                   + (everything_else_input * card_everything_else_multiplier)) * card_reward_value) - card_annual_fee)

    return card_value


def sort_cards_by_value(cards):
    assert cards is not None

    return dict(sorted(cards.items(), key=operator.itemgetter(1), reverse=True))


def about_us(request):
    return render(request, 'cards/AboutUs.html')
