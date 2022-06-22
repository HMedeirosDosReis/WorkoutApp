class user:
    def __init__(self, adminName,userName, password, fname, lname, workoutA, workoutB, 
               objective, workoutC= None, workoutD=None, workoutE=None, workoutDone=False,
                exerciseDone=False):
        self.userName = userName
        self.password = password
        self.fname = fname
        self.lname = lname
        self.workoutA = workoutA
        self.workoutB = workoutB
        self.workoutC = workoutC
        self.workoutD = workoutD
        self.workoutE = workoutE
        self.objective = objective
        self.workoutDone = workoutDone
        self.exerciseDone = exerciseDone
        self.adminName = adminName

    def UserName(self):
        return self.userName
    def Password(self):
        return self.password
    def FName(self):
        return self.fname
    def LName(self):
        return self.lname
    def WorkoutA(self):
        return self.workoutA
    def WorkoutB(self):
        return self.workoutB
    def WorkoutC(self):
        return self.workoutC
    def WorkoutD(self):
        return self.workoutD
    def WorkoutD(self):
        return self.workoutD
    def Objective(self):
        return self.objective
    def WorkoutDone(self):
        return self.workoutDone
    def ExerciseDone(self):
        return self.exerciseDone
    def AdminName(self):
        return self.adminName
    
    def sp_print(self):
        print("Name: "+self.fname+" "+self.lname+"\n")
        print("Trainer: "+self.adminName)

