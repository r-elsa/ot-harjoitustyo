
import uuid

class User:
    def __init__(id, self, email, username, password, isRegistered, isAdmin):
        id = uuid.uuid1().hex
        self.email = email
        self.username=username
        self.password = password
        self.isRegistered = isRegistered
        self.isAdmin = isAdmin
    
   
