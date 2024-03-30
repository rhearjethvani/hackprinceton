class User:
    def __init__(self,username,is_admin,email,password) -> None:
        self.username=username
        self.email=email
        self.is_admin=is_admin
        self.password=password
        self.test_history=[] #json of {test, value}
        self.people=[] # #for only admins


        


