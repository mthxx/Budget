from sidebar import Sidebar

class Expense():

    def __init__(self, data):
        # Define Sidebar Menu
        self.data = data
        self.view = Sidebar(self.data, "expense") 
