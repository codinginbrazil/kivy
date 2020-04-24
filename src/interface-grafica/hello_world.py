# [Apresentação do kivy](https://kivy.org/doc/stable/guide/basic.html#quickstart)

# preparação de ambiente
## Ubuntu -> sudo apt install pip
## Fedora -> sudo dnf install pip
## pip install kivy


from kivy.app import App
from kivy.uix.button import Button

class TestApp(App):
    def build(self):
        return Button(text='Hello World')

TestApp().run()