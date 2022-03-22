# function goes here
def num_check(question):

    # checks that user has enter a number more than zero
    valid = False
    while not valid:

        error = "Please enter a number that is more than zero."

        try:

            # ask user to enter a number
            response = float(input(question))
            
            # checks number is more than zero
            if response > 0:
                return response

            # outputs error if input is invalid
            else:
                print(error)
                print()
        
        except ValueError:
            print(error)



# Main routine goes here
width = num_check("Width: ")
height = numcheck("Height: ")
print()
print("Width", width)
print("Height", height)
print()