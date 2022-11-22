from entities.user import User
from entities.invoice import Invoice


class InvoiceService:
    def __init__(self, id):
        self.id = id

    def create_invoice(Invoice):
        pass

    def read_invoice(Invoice):
        pass
    
    def update_invoice(Invoice, status):
        pass
    
    def delete_invoice(Invoice):
        pass


    def login(self, username, password):

        """ user = self._user_repository.find_by_username(username)

        if not user or user.password != password:
            raise InvalidCredentialsError("Invalid username or password")

        self._user = user

        return user """
    
    






invoice_service = InvoiceService