# напиши модуль для подсчета количества приседаний
from kivy.uix.label import Label
from kivy.clock import Clock

class Sits(Label):
    
    def __init__(self, total, **kwargs):
        self.current = 0
        self.total = total
        my_text = 'Осталось приседаний:'+str(self.total-self.current)
        super().__init__(text=my_text, **kwargs)

    def next(self, *args):
        self.current += 1
        remaining = max(0,self.total - self.current)
        my_text = 'Осталось приседаний:'+str(remaining)
        self.text = my_text