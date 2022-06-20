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

    def UserName(myUser):
        return myUser.userName

    

