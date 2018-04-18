import kivy
kivy.require('1.10.0') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput

class LoginScreen(GridLayout):
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.cols = 2
        a=Label(text='User Name')
        self.add_widget(a)
        self.username = TextInput(multiline=False)
        self.add_widget(self.username)
        self.add_widget(Label(text='password'))
        self.password = TextInput(password=True, multiline=False)
        self.add_widget(self.password)
        print(self.password)
    def on_touch_down(self, touch):
        if touch.is_double_tap:
            print(touch,self.password.text)
            return False
class MyApp(App):

    def build(self):
        return LoginScreen()
    
    

if __name__ == '__main__':
    MyApp().run()
