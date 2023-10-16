from kivy.uix.dropdown import DropDown
from kivy.uix.textinput import TextInput
from kivymd.app import MDApp
from kivymd.uix.relativelayout import MDRelativeLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

from kivy.core.window import Window
from translate import Translator

Window.size = (500, 600)


class MyApp(MDApp):
    def translateText(self, event):
        var1 = self.textinput1.text
        translator = Translator(from_lang=self.top_main_btn.text, to_lang=self.bottom_main_btn.text)
        translation = translator.translate(var1)

        self.textinput2.text = translation

    def build(self):
        layout = MDRelativeLayout(md_bg_color=[100 / 255, 200 / 255, 240 / 255])

        self.titleLabel = Label(text="Translator App",
                                pos_hint={'center_x': 0.5, 'center_y': 0.9},
                                size_hint=(1, 1),
                                font_size=40,
                                color=(0, 0, 0),
                                font_name='Segoeuib',
                                )
        self.textinput1 = TextInput(text="", hint_text="Insert text",
                                    pos_hint={'center_x': 0.5, 'center_y': 0.7},
                                    size_hint=(0.8, None),
                                    height=150,
                                    font_size=20,
                                    font_name='Segoeuib'
                                    )
        self.textinput2 = TextInput(text="", hint_text="Traduction",
                                    pos_hint={'center_x': 0.5, 'center_y': 0.3},
                                    size_hint=(0.8, None),
                                    height=150,
                                    font_size=20,
                                    font_name='Segoeuib',
                                    readonly=True
                                    )

        self.translateButton = Button(text="Translate",
                                      pos_hint={'center_x': 0.2, 'center_y': 0.5},
                                      size_hint=(0.2, 0.1),
                                      background_normal='',
                                      background_color="#224594",
                                      font_name='Segoeuib',
                                      on_press=self.translateText
                                      )
        self.languages = ['English', 'German', 'Spanish', 'French', 'Chinese']

        self.topDropdown = DropDown()

        for languages in self.languages:
            btn = Button(text=languages, size_hint_y=None, height=30)
            btn.bind(on_release=lambda btn: self.topDropdown.select(btn.text))

            self.topDropdown.add_widget(btn)

        self.top_main_btn = Button(text="English", size_hint=(0.55, None),
                                   height=50,
                                   pos_hint={'center_x': 0.6, 'center_y': 0.5},
                                   background_normal='',
                                   background_color="#4A5B81"
                                   )
        self.top_main_btn.bind(on_release=self.topDropdown.open)
        self.topDropdown.bind(on_select=lambda instance, x: setattr(self.top_main_btn, 'text', x))

        layout.add_widget(self.top_main_btn)

        ######################################

        self.bottomDropdown = DropDown()

        for languages in self.languages:
            btn = Button(text=languages, size_hint_y=None, height=30)
            btn.bind(on_release=lambda btn: self.bottomDropdown.select(btn.text))

            self.bottomDropdown.add_widget(btn)

        self.bottom_main_btn = Button(text="English", size_hint=(0.8, None),
                                      height=50,
                                      pos_hint={'center_x': 0.5, 'center_y': 0.12},
                                      background_normal='',
                                      background_color="#4A5B81"
                                      )
        self.bottom_main_btn.bind(on_release=self.bottomDropdown.open)
        self.bottomDropdown.bind(on_select=lambda instance, x: setattr(self.bottom_main_btn, 'text', x))

        layout.add_widget(self.bottom_main_btn)

        layout.add_widget(self.titleLabel)
        layout.add_widget(self.textinput1)
        layout.add_widget(self.textinput2)
        layout.add_widget(self.translateButton)
        return layout


if __name__ == "__main__":
    MyApp().run()
