class ChosenCards(object):
    def __init__(self, **kwargs):
        pass

    # keys will be populated with the credit card
    keys = {'card_name', 'calculated_value'}
    chosen_cards = dict.fromkeys(keys)