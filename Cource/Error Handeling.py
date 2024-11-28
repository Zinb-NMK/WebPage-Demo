def main():
        x = get_int()
        print(f"x is{x}")


 def get_int():
     while True:
         try:
             n = int(input("Enter an integer: "))
         except ValueError:
                print("n is not an integer.")
         else:
            break
        return x

main()