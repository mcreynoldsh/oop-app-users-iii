from users.User import User

class FreeUser(User):
    def post(self,str):
        instance_of_user = super()
        if self.count<=2:
            instance_of_user.post(str) 
        else:
            print("Reached your post limit")    
