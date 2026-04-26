from kivy.uix.label import Label
from kivy.clock import Clock

class Sits(Label):

    def __init__(self, total, **kwargs):
        self.total = total
        self.current = 0
        my_text = "Squats: " + str(self.current) + " / " + str(self.total)
        super().__init__(text=my_text, **kwargs)

    def next(self, *args):
        if self.current < self.total:
            self.current += 1
            self.text = "Squats: " + str(self.current) + " / " + str(self.total)
