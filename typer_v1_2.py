from sqlalchemy import null
import keyboard

def hbd(text):
    if text == "hbd":
        print("Happy Birthday to you!")
    else:
        print("Have a good day")


def print_newline(times):
    for i in range(times):
        print('\n')

def main_block():
    print("     typer v1.2    ")
    server_name = input("     server name? ")
    rangeIs = input("how long is your discussion? ")

    if rangeIs.isnumeric():
        number1 = int(rangeIs)
        for i in range(number1):
            print_newline(1)
            inputZ = " [message " + "#" + server_name + "]"
            write = input(inputZ)
            print("you:" + write)
            hbd(write)
    else:
        print('Sorry Wrong Input')

if __name__ == "__main__":
    main_block()
    