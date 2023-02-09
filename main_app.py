from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput
from seconds import Seconds
from kivy.event import EventDispatcher
from instructions import *
from sits import Sits
from runner import Runner
name=''
age=''
pq,p2,p3 = 0,0,0
def check_int(num):
    try:
        return int(num)
    except:
        return False



class InstrScr(Screen):
    def __init__(self, name='main'):
        super().__init__(name=name) # имя экрана должно передаваться конструктору класса Screen
        line1=BoxLayout(size_hint=(0.8,None),height='30sp')
        line2=BoxLayout(size_hint=(0.8,None),height='30sp')
        outer = BoxLayout(padding=8, spacing=8, orientation='vertical')
        instruction = Label(text=txt_instruction)
        nameLabel = Label(text="Введите имя:",halign='right')
        ageLabel = Label(text="Введите возраст",halign='right')
        self.inName = TextInput(multiline=False)
        self.inAge = TextInput(multiline=False)
        self.btn = Button(text="Продолжить", size_hint=(0.3 , 0.2), pos_hint={'center_x':0.5})
        self.btn.on_press=self.next
        line1.add_widget(nameLabel)
        line1.add_widget(self.inName)
        line2.add_widget(ageLabel)
        line2.add_widget(self.inAge)
        outer.add_widget(instruction)
        outer.add_widget(line1)
        outer.add_widget(line2)
        outer.add_widget(self.btn)
        self.add_widget(outer)
    def next(self):
        global name,age
        name=self.inName.text
        age = self.inAge.text
        print(name,age)

        self.manager.current = 'test1'


class Test1Scr(Screen):
    def __init__(self, name):
        super().__init__(name=name)
        self.next_screen = False
        layout=BoxLayout(orientation='vertical', spacing=8, padding=8)
        pulseLine = BoxLayout(size_hint=(0.8,None),height='30sp')
        line=BoxLayout(size_hint=(0.8,None),height='30sp')
        instuction = Label(text=txt_test1, size_hint=(0.8,0.4))
        

        lbl1=Label(text="Считайте пульс",halign='right')
        self.lbl1_sec=Seconds(15)
        self.lbl1_sec.bind(done=self.sec_finished)

        pulseLabel = Label(text="Введите пульс", halign='right')
        self.inPulse = TextInput(text = '0', multiline=False)
        self.inPulse.set_disabled(True)
        self.btn = Button(text='Начать', size_hint=(0.3,0.2),pos_hint={'center_x':0.5})
        self.btn.on_press = self.next
        pulseLine.add_widget(lbl1)
        pulseLine.add_widget(self.lbl1_sec)
        line.add_widget(pulseLabel)
        line.add_widget(self.inPulse)
        layout.add_widget(instuction)
        layout.add_widget(pulseLine)
        layout.add_widget(line)
        layout.add_widget(self.btn)
        self.add_widget(layout)
    def next(self):
        if not self.next_screen:
            self.btn.set_disabled(True)
            self.lbl1_sec.start()
        else:
            global p1
            p1 = check_int(self.inPulse.text)
            if p1 == False or p1<=0:
                p1=0
                self.inPulse.text = str(p1)
            else:
                self.manager.current = 'test2'
    
    def sec_finished(self, *args):
        print(args)
        self.next_screen = True
        self.inPulse.set_disabled(False)
        self.btn.set_disabled(False)
        self.btn.text = 'Продолжить'

class Test2Scr(Screen):
    def __init__(self, name):
        super().__init__(name=name)
        self.next_screen = False
        layout=BoxLayout(orientation='vertical', spacing=8, padding=8)
        instructions = Label(text = txt_sits, size_hint=(0.5,1))
        self.lbl_sits = Sits(30)
        self.run = Runner(size_hint=(0.4,1))
        self.run.bind(finished=self.run_finished)
        
        line = BoxLayout()
        vline = BoxLayout(orientation='vertical',size_hint=(0.3,1))
        vline.add_widget(self.lbl_sits)
        line.add_widget(instructions)
        line.add_widget(vline)
        line.add_widget(self.run)

        self.btn = Button(text='Начать', size_hint=(0.3,0.2), pos_hint = {'center_x':0.5})
        self.btn.on_press = self.next

        layout.add_widget(line)
        layout.add_widget(self.btn)
        self.add_widget(layout)

    def run_finished(self):
        self.btn.set_disabled(False)
        self.btn.text = 'Продолжить'
        self.next_screen = True


    def next(self):
        if not self.next_screen:
            self.btn.set_disabled(True)
            self.run.start()
            self.run.bind(value=self.lbl_sits.next)
        else:
            self.manager.current = 'test3'

class Test3Scr(Screen):
    def __init__(self, name):
        super().__init__(name=name) # имя экрана должно передаваться конструктору класса Screen
        self.next_screen = False
        self.stage = 0
        self.lbl_sec = Seconds(15)
        self.lbl_sec.bind(done=self.sec_finished)
        self.lbl = Label(text='Считайте пульс:',halign='right')

        line1=BoxLayout(size_hint=(0.8,None),height='30sp')
        line2=BoxLayout(size_hint=(0.8,None),height='30sp')
        outer = BoxLayout(padding=8, spacing=8, orientation='vertical')
        pulseLine = BoxLayout(spacing = 8, padding = 8)
        instruction = Label(text=txt_test2)
        pulse2Label = Label(text="Результат:",halign='right')
        pulse3Label = Label(text="Результат после отдыха:",halign='right')
        self.inPulse2 = TextInput(multiline=False)
        self.inPulse3 = TextInput(multiline=False)
        self.inPulse2.set_disabled(True)
        self.inPulse3.set_disabled(True)
        self.btn = Button(text="Начать", size_hint=(0.3 , 0.4), pos_hint={'center_x':0.5})
        self.btn.on_press=self.next
        line1.add_widget(pulse2Label)
        line1.add_widget(self.inPulse2)
        line2.add_widget(pulse3Label)
        line2.add_widget(self.inPulse3)
        outer.add_widget(instruction)
        pulseLine.add_widget(self.lbl)
        pulseLine.add_widget(self.lbl_sec)
        outer.add_widget(pulseLine)
        outer.add_widget(line1)
        outer.add_widget(line2)
        outer.add_widget(self.btn)
        self.add_widget(outer)

    def sec_finished(self, *args):
        if self.lbl_sec.done:
            if self.stage == 0:
                self.stage = 1
                self.lbl.text = 'Отдыхайте'
                self.lbl_sec.restart(30)
                self.inPulse2.set_disabled(False)
            elif self.stage == 1:
                self.stage = 2
                self.lbl.text = 'Считайте Пульс'
                self.lbl_sec.restart(15)
            elif self.stage == 2:
                self.inPulse3.set_disabled(False)
                self.btn.set_disabled(False)
                self.btn.text = 'Завершить'
                self.next_screen = True


    def next(self):
        if not self.next_screen:
            self.btn.set_disabled(True)
            self.lbl_sec.start()
        else:
            global p2,p3
            p2 = check_int(self.inPulse2.text)
            p3 = check_int(self.inPulse3.text)
            if p2 == False or p2<=0:
                p2 = 0
                self.inPulse2.text=str(p2)
            elif p3 == False or p3<=0:
                p3 = 0
                self.inPulse3.text = str(p3)
            else:
                self.manager.current = 'result'

class ResultScr(Screen):
    def __init__(self, name):
        super().__init__(name=name) # имя экрана должно передаваться конструктору класса Screen
        layout = BoxLayout(padding=8, spacing=8, orientation='vertical')

class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(InstrScr())
        sm.add_widget(Test1Scr(name ='test1'))
        sm.add_widget(Test2Scr(name ='test2'))
        sm.add_widget(Test3Scr(name ='test3'))
        sm.add_widget(ResultScr(name ='result'))
        # будет показан FirstScr, потому что он добавлен первым. Это можно поменять вот так:
        # sm.current = 'second'
        sm.current='main'
        return sm

app = MyApp()
app.run()