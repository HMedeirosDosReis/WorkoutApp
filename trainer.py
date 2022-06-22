class trainer:
    def __init__(self, adminName, password, fname, lname, listOfUsers):
        self.password = password
        self.fname = fname
        self.lname = lname
        self.adminName = adminName
        self.listOfUsers = listOfUsers

    def Password(self):
        return self.password
    def FName(self):
        return self.fname
    def LName(self):
        return self.lname
    def AdminName(self):
        return self.adminName
    def ListOfUsers(self):
        return self.listOfUsers
    
    def sp_print(self):
        print("Trainer: "+self.fname+" "+self.lname+"\n")
        print("Coaching: "+self.listOfUsers)
