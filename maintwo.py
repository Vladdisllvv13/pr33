from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.config import Config
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.scatter import Scatter

Config.set('graphics', 'resizable', '0')
Config.set('graphics', 'width', '360')
Config.set('graphics', 'height', '800')


class myApp(App):
    def build(self):

        #s=Scatter() # тач двумя пальцами...Но зачем?
        fl=FloatLayout(size=(200, 200))
        #s.add_widget(fl)
        self.lb1 =Label(text ="",
                        pos=(20,700),
                        size_hint=(.93, .1))
        fl.add_widget(self.lb1)
        fl.add_widget(Button(
            text="",
            font_size=20,
            on_press=self.btn_pressPurple,
            background_color=[0.49, 0, 1, 1],  ##7d00ff фиолетовый
            background_normal='',
            size_hint=(.93, .1),
            pos=(13, 10)))
        fl.add_widget(Button(
            text="",
            font_size=20,
            on_press=self.btn_pressBlue,
            background_color=[0, 0, 1, 1],  ##0000ff синий
            background_normal='',
            size_hint=(.93, .1),
            pos=(13, 110)))
        
        fl.add_widget(Button(
            text="",
            font_size=20,
            on_press=self.btn_pressslowBlue,
            background_color=[0, 0.49, 1, 1],  #007dff голубой
            background_normal='',
            size_hint=(.93, .1),
            pos=(13, 210)))
        fl.add_widget(Button(
            text="",
            font_size=20,
            on_press=self.btn_pressGreen,
            background_color=[0, 1, 0, 1],  ##00ff00 зеленый
            background_normal='',
            size_hint=(.93, .1),
            pos=(13, 310)))
        fl.add_widget(Button(
            text="",
            font_size=20,
            on_press=self.btn_pressYellow,
            background_color=[1, 1, 0, 1],  ##ffff00 желтый
            background_normal='',
            size_hint=(.93, .1),
            pos=(13, 410)))
        fl.add_widget(Button(
            text="",
            font_size=20,
            on_press=self.btn_pressOrange,
            background_color=[1, 0.49, 0, 1],  ##ff7d00 оранжевый
            background_normal='',
            size_hint=(.93, .1),
            pos=(13, 510)))
        fl.add_widget(Button(
            text="",
            font_size=20,
            on_press=self.btn_pressRed,
            background_color=[1, 0, 0, 1],  ##ff0000 красный
            background_normal='',
            size_hint=(.93, .1),
            pos=(13, 610)))
        
        return fl

    
    def btn_pressPurple(self, instance):        
        instance.text='#ff00ff'        
        self.lb1.text = "Фиолетовый" 
    
    def btn_pressBlue(self, instance):        
        instance.text='#0000ff'        
        self.lb1.text = "Синий" 
    def btn_pressslowBlue(self, instance):        
        instance.text='#00ffff'      
        self.lb1.text = "Голубой" 
    def btn_pressGreen(self, instance):        
        instance.text='#00ff00'        
        self.lb1.text = "зеленый" 
    def btn_pressYellow(self, instance):        
        instance.text='#ffff00'        
        self.lb1.text = "Желтый" 
    def btn_pressOrange(self, instance):        
        instance.text='#ff5500'        
        self.lb1.text = "Оранжевый" 
    def btn_pressRed(self, instance):        
        instance.text='#ff0000'        
        self.lb1.text = "Красный" 
     
        
if __name__=="__main__":
    myApp().run()