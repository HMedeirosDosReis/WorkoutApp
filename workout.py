class workout:
    def __init__(self, ID, listOfExercises):
        self.ID = ID
        self.listOfExercises = listOfExercises

    def ListOfExercises(self):
        return self.listOfExercises
    def ID(self):
        return self.ID

    def sp_print(self):
        print("ID: "+ID+"\n")
        for i in range(0,len(self.listOfExercises)):
            print(self.ListOfExercises[i])
