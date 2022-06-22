class workout:
    def __init__(self, name, desc, reps, sets): 
        self.name = name
        self.desc = desc
        self.reps = reps
        self.sets = sets

    def Name(self):
        return self.name
    def Desc(self):
        return self.desc
    def Reps(self):
        return self.reps
    def Sets(self):
        return self.sets

    def sp_print(self):
        print("Exercise: "+self.name+"\n")
        print("Description" :+self.desc+"\n")
        print(self.sets+"x"self.reps)

