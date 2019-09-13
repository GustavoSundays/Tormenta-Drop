from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.metrics import sp
from kivy.metrics import dp
from kivy.uix.label import Label
from index import drops

__version__ = "1.0"

class Mensagem(Label):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size_hint = (1, None)
        self.font_size = sp(20)
    
    def on_size(self, *args):
        self.text_size = (self.width - sp(10), None)

    def on_texture_size(self, *args):
        self.size = self.texture_size
        self.height += sp(20)

class Drops(BoxLayout):
    def __init__(self, drops, **kwargs):
        super().__init__(**kwargs)
        for drop in drops:
            self.ids.box.add_widget(Mensagem(text=drop))
                                                     
    def alteraConteudo(self):
        self.ids.box.clear_widgets()
        texto = self.ids.texto.text
        self.ids.box.add_widget(Mensagem(text=drops(texto)))
        self.ids.texto.text = ''

class Test(App):
    def build(self):
        return Drops([drops()])

Test().run()
