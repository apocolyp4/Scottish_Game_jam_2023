class Button:
    def __init__(self):
        self.state = False
        self.last_state = False
        self.pressed = False
        self.released = False

    def update(self, state):
        self.state = state > 0

        if self.state == True and self.last_state == False:
            self.pressed = True
        else:
            self.pressed = False

        if self.state == False and self.last_state == True:
            self.released = True
        else:
            self.released = False         

        self.last_state  = state > 0