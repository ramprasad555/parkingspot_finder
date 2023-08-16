"""
Code to find the parking spot
"""
from Graph import Heap


array_of_parking_spots = [["AL1-23", "AR1-21","AL2-27","AR2-25","AL3-37","AR3-35","AL4-45","AR4-43","AL5-49","AR5-47"],
                          ["BL1-7","BR1-3","BL2-13","BR2-9","BL3-19","BR3-17","BL4-33","BR4-31", "BL5-41","BR5-39"],
                          ["CL1-1","CR1-2","CL2-5", "CR2-6","CL3-11","CR3-12","CL4-15","CR4-16","CL5-29","CR5-30"],
                          ["DL1-4", "DR1-8","DL2-10","DR2-14","DL3-18","DR3-20","DL4-32","DR4-34","DL5-40","DR5-42"],
                          ["EL1-22","ER1-24","EL2-26","ER2-28","EL3-36","ER3-38","EL4-44","ER4-46","EL5-48","ER5-50"]
]

'''
1. Create a parking area using min heap -- done
2. when requests for a parking spot - 
2a. Pop a min_distance spot from min heap and restructure the heap
2b. update the parking spot as occupied in the occupancy dictionary
3. when user leaves the parking spot - 
3a. update the occupancy dictionary
3b. add the parking spot back to the heap.
4. add miscellaneous functionalities like - number of spots left.
'''

def main():
    global Parking_Area
    global Parking_occupancy 
    global numberofspots
    Parking_Area = Heap()
    
    Parking_occupancy = {}
    # print(type(Parking_Area))
    for i in array_of_parking_spots:
        for j in i:
            Parking_Area.add_spot(j)
            Parking_occupancy[j] = False

def update_parking_spot(spot):
    if(not Parking_occupancy[spot]):
        Parking_occupancy[spot] = True
    else:
        get_parking_spot()

def get_parking_spot():
    if Parking_Area.length > 0:
        spot = Parking_Area.pop_min()
        if(not Parking_occupancy[spot]):
            return spot
        else:
            get_parking_spot()
    else:
        return "Parking Area is Full, PLease select another Parking Area"

def entering_parking():
    inp = input("do you want the nearest spot? Yes : No")
    if(inp == "Yes"):
        spot = get_parking_spot()
        print("The nearest spot is " + spot)
        print(spot)
        inp2 = input("Are you parking here ? Yes : No")
        if (inp2 == "Yes"):
            update_parking_spot(spot)
        else:
            Parking_Area.add_spot(spot)
    else:
        print("thank you for your time")
    
def exiting_parking(inp1):
   
    if Parking_occupancy[inp1]:
        Parking_occupancy[inp1] = False
        Parking_Area.add_spot(inp1)
        print("thankyou parking spot is vacant")
    else:
        print("Spot not found or already vacant")



if __name__ == "__main__":
    main()
    print("spot_finder is running")
    entering_parking()
    # inp1 = input('enter the name of the spot you are leaving')
    # exiting_parking(inp1)
    # print(Parking_Area.length)

    
   


