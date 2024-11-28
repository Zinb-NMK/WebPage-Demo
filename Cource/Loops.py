def main():
    print_square(4)

def print_square(size):

    #for each r ow in square
    for i in range(size):

        #for each brick in row
        for j in  range(size):

            #print brick
            print("#", end="")
        print()

main()
