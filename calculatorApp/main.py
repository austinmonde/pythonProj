from kivy.app import App #imports the App class from kivy.app module
from kivy.uix.boxlayout import BoxLayout #imports the BoxLayout class from the kivy.uix.boxlayout module
from kivy.uix.button import Button #imports the Button class from the kivy.uix.button module
from kivy.uix.textinput import TextInput # imports the TextInput class from the kivy.uix.textinput module

'''defining a class named MainApp that inherits from 
the App class in the Kivy library.'''
class MainApp(App):
    def build(self): #construct the UI of your application
        self.icon = "images/calculator_icon.png"
        self.operators = ["/", "*", "+", "-"]
        self.was_last_operator = None
        self.last_button = None
        
        main_layout = BoxLayout(orientation = 'vertical')
        self.solution = TextInput(background_color = "black", foreground_color = "white")

        main_layout.add_widget(self.solution)
        buttons = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "+"],
            [".", "0", "C", "-"],
        ]

        for row in buttons:
            h_layout = BoxLayout()
            for label in row:
                button = Button(
                    text = label, font_size=30, background_color = "grey",
                    pos_hint={"center_x":0.5, "center_y":0.5}
                )
                button.bind(on_press=self.on_button_press)
                h_layout.add_widget(button)
            main_layout.add_widget(h_layout)

        equals_button = Button(
            text = "=", font_size=30, background_color = "grey",
                    pos_hint={"center_x":0.5, "center_y":0.5}
        )
        equals_button.bind(on_press=self.on_solution)
        main_layout.add_widget(equals_button)

        return main_layout


if __name__ == "__main__":
    app = MainApp()
    app.run()