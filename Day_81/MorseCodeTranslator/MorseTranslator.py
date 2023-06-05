from morse_code import MORSE_CODE_DICT


class MorseTranslator:

    def __init__(self):
        self.quote = None

    def process_quote(self, func):
        try:
            return func()
        except ValueError:
            return "X"

    def encode(self):
        encoded = []
        for string in self.quote:
            try:
                encoded.append(MORSE_CODE_DICT[string])
            except KeyError:
                return f"I don't have '{string}' in my dictionary, try again."
        return ' '.join(encoded)

    def decode(self):
        decoded = []
        morse_keys = list(MORSE_CODE_DICT.keys())

        for letter in self.quote.split(" "):
            try:
                letter_index = list(MORSE_CODE_DICT.values()).index(letter)
                decoded.append(morse_keys[letter_index])
            except ValueError:
                return f"{letter} is not a valid morse code, try again."

        return ''.join(decoded)
