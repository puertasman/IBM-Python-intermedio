print("### recursividad ###")

def recursiva(numero):
    if numero == 1:
        print(numero, end = " ")
    else:
        recursiva(numero-1)
        print(numero, end = " ")

if __name__ == "__main__":
    recursiva(20)