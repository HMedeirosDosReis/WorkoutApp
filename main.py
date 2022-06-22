#! /usr/bin/env python3

from user import * 
def choices():
    print("Welcome to Workout App!")

    typeOfUser = input("Are you an instructor or a member? "+"\n")

    #memberList = ["Workout A","Workout B", "", ]
    if typeOfUser=="member":
        accessWorkouts = input("Would you like to access your workouts? (yes/no)"+"\n")
    
        if accessWorkouts == "yes":
            print("Done!!")
            ## workout class
    
        else:
            print("...")



def main():
    testUser = user("Prof1", "HM", "1011","henr", "med", "workA", "workB", "gain")
#    testUser.sp_print()


if __name__ == "__main__":
    main()
    choices()
