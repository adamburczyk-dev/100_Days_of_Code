from MorseTranslator import MorseTranslator

program_running = True
translator = MorseTranslator()

print("Welcome to Morse Translator!")
while program_running:
    method = input("Do you want to encode or decode? \n").lower()
    if method == 'encode':
        translator.quote = input("Write quote to encode: ").upper()
        print(translator.encode())

    elif method == 'decode':
        translator.quote = input("Write a quote like this: -..- -.-- --..\n")
        print(translator.decode())
    else:
        print("It is not a valid method, try again.")

    decision = input("Do you want to try again? Y/N\n").upper()

    if decision == "N":
        print("Okay! Bye!")
        program_running = False
