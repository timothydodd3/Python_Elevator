#elevator.py
#Timothy Dodd
#05-09-2023

#This elevator should do the following once its done
# Go Up
# Go Down
# Get Called
# Travel a set amount of floors.

# Define everything here
current_floor = 1
floor = 1 
goUp = False

def elevatorCalled(current_floor, floor):
    
    while(floor != current_floor):
        if goUp == False:
            print("Currently on floor " + floor)
            floor = floor - 1
        else:
            print("Currently on floor " + floor)
            floor = floor + 1

