from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect

# Create your views here.
from cards.forms import CreditForm


def home(request):
    return render(request, 'cards/homepage.html')

def get_info(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = CreditForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = CreditForm()

    return render(request, 'cards/forms.html', {'form': form})

def about_us(request):
    return render(request, 'cards/AboutUs.html')
