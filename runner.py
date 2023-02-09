# напиши модуль для работы с анимацией
from kivy.properties import NumericProperty , BooleanProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.animation import Animation
from kivy.uix.button import Button

class Runner(BoxLayout):
    value = NumericProperty(0)
    finished = BooleanProperty(False)

    def __init__(self, total = 30 , steptime = 1.5,
                autoRepeat = True, bcolor = (0.73, 0.15, 0.96, 1),
                btextInprogress = 'Приседание', **kwargs):
        super().__init__(**kwargs)

        self.total = total
        self.autoRepeat = autoRepeat
        self.btextInprogress = btextInprogress
        self.animation = (Animation(pos_hint={'top':0.1}, duration = steptime/2) +
                          Animation(pos_hint={'top':1}, duration = steptime/2))
        self.animation.on_progress = self.next
        self.btn = Button(size_hint=(1,0.1), pos_hint={'top':1}, background_color = bcolor)
        self.add_widget(self.btn)

    def restart(self,total):
        self.total = total
        self.start()

    def start(self):
        self.value = 0
        self.finished = False
        self.btn.text = self.btextInprogress
        if self.autoRepeat:
            self.animation.repeat = True
        self.animation.start(self.btn)

    def next(self, widget, step):
        if step == 1.0:
            self.value +=1
            if self.value>= self.total:
                self.animation.repeat = False
                self.finished = True