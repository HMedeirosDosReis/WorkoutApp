#! /usr/bin/env python3

from user import * 
def choices():
    print("Welcome to Workout App!")

    typeOfUser = input("Are you an instructor or a member? "+"\n")
    instructorList = ["add workout","remove workout","check progress","alter workout","add member","assign workout"]
    
   #memberList = ["Workout A","Workout B", "", ]
    if typeOfUser=="member":
        accessWorkouts = input("Would you like to access your workouts? (yes/no)"+"\n")
    
        if accessWorkouts == "yes":
            print("Done!!")
            ## workout class
    
        else:
            print("...")
    
    elif typeOfUser == "instructor": 
        print("Here is a list of available options to be accessed: "+", ".join(instructorList)+
                ".")
        option =input( "Which option would you like to acces?"+"\n")
        
        if option==instructorList[0]:
           print("...")
        elif option==instructorList[1]:
           print("...")
        elif option==instructorList[2]:
           print("...")
        elif option==instructorList[3]:
           print("...")
        elif option==instructorList[4]:
           print("...")
        elif option==instructorList[5]:
           print("...")

def main():
    testUser = user("Prof1", "HM", "1011","henr", "med", "workA", "workB", "gain")
#    testUser.sp_print()


if __name__ == "__main__":
    main()
    choices()
