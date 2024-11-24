def code_nu(name):
    match name:
        case "manoj" | 'ron' | "kumar":
            print("ID IS : 123")
        case "kumar":
            print("ID IS : 1234")
        case "draco":
            print("ID IS : 12345")
        case _:
            print("Who?")
num = input("Enter a name: ").lower()
code_nu(num)




