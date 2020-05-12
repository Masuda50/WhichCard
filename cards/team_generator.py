members = {
    "Yorli Chazari": "https://cdn4.iconfinder.com/data/icons/emoji-18/61/25-512.png",
    "Julia Berdecia": "https://cdn4.iconfinder.com/data/icons/emoji-18/61/1-512.png",
    "Aqsa Malik": "https://cdn4.iconfinder.com/data/icons/emoji-18/61/5-512.png",
    "Natalia Harrow": "https://cdn4.iconfinder.com/data/icons/emoji-18/61/3-512.png",
    "Quetourah Dalencourt": "https://cdn0.iconfinder.com/data/icons/reactions/64/Icon_Reactions-09-512.png",
    "Nicholas Comer": "https://cdn4.iconfinder.com/data/icons/emoji-18/61/13-512.png",
    "Masuda Farehia": "https://cdn4.iconfinder.com/data/icons/emoji-66/64/09-smirking-512.png",
    "Prof. Haydar": "https://cdn4.iconfinder.com/data/icons/emoji-18/61/19-512.png"
}


class Frame:
    def __init__(self, name, address):
        self.name = name
        self.address = address


def get_frames():
    return __create_members()


def __create_members():
    return [Frame(key, value) for (key, value) in members.items()]
