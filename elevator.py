#elevator.py
#Timothy Dodd
#05-09-2023

# Change the values in these variables to whatever is needed.
num_floors = 4

# These variables are used by the function.
current_floor = 1   #Start at ground level.
floor = 1 
goUp = False



def elevatorCalled(current_floor: int, floor: int):

    if(floor > current_floor):
        goUp = True
    else:
        goUp = False

    while(floor != current_floor):
        if goUp == False:
            print(f"Currently on floor {current_floor}")
            current_floor = current_floor - 1
        else:
            print(f"Currently on floor {current_floor}")
            current_floor = current_floor + 1

    if (floor == current_floor):
        print(f"Reached floor {floor}!")

    return current_floor

#main Area
#Print this value when called. 
print(f"Please note: This elevator can only travel {num_floors} floors")

while(floor <= num_floors and floor >= 1):
    floor = int(input("Enter a floor number to call the elevator (Or enter 0 to leave): "))
    
    #Get a valid floor number.
    while floor > num_floors or floor < 0:
        print ("That floor value is not valid")
        floor = int(input("Enter a floor number to call the elevator (Or enter 0 to leave): "))
    # Check if the value 0 is specified. Exit the program if so.
    if floor == 0:
        print ("Goodbye!")
        break

    #Get the elevator to go to the current floor
    current_floor = elevatorCalled(current_floor, floor)
    floor = int(input("Ding! Hop in and Enter your desired floor number: "))
    while(floor >= num_floors and floor <= 1):
        print("This elevator cannot go to that floor, please try again.")
        floor = int(input("Enter in a new floor value: "))

    current_floor = elevatorCalled(current_floor, floor)