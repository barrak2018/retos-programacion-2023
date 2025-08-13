leet_dict = {
    'a': '4',
    'b': 'I3',
    'c': '[',
    'd': ')',
    'e': '3',
    'f': '|=',
    'g': '&',
    'h': '#',
    'i': '1',
    'j': ',_|',
    'k': '>|',
    'l': '1',
    'm': '/\\/\\',
    'n': '/\\/',
    'o': '0',
    'p': '|*',
    'q': '(_,)',
    'r': 'I2',
    's': '5',
    't': '7',
    'u': '(_)',
    'v': '\\/',
    'w': '\\/\\/',
    'x': '><',
    'y': 'j',
    'z': '2',
    '1': 'l',
    '2': 'R',
    '3': 'E',
    '4': 'A',
    '5': 'S',
    '6': 'B',
    '7': 'T',
    '8': 'B',
    '9': 'g',
    '0': 'o',
    ' ': ' ' 
}
def alphabet_to_leet(text: str, dictionary = leet_dict):
    model = str.maketrans(dictionary)
    message = text.lower()
    return message.translate(model)

print(alphabet_to_leet("Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever "))