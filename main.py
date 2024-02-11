import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class childApp(GridLayout):
    def __init__(self, **kwargs):
        super(childApp, self).__init__(**kwargs)
        self.cols = 2
        self.add_widget(Label(text='Resident Name'))
        self.r_name = TextInput()
        self.add_widget(self.r_name)

        self.add_widget(Label(text='Flat Number'))
        self.r_number = TextInput()
        self.add_widget(self.r_number)

        self.press = Button(text="Login")
        self.press.bind(on_release=self.login)  # Fix the method name here
        self.add_widget(self.press)

    def login(self, instance):  # Use lowercase "login" here
        print("Name of resident:", self.r_name.text)
        print("Flat number of resident:", self.r_number.text)
        print()

class parentApp(App):
    def build(self):
        return childApp()

if __name__ == "__main__":
    parentApp().run()
