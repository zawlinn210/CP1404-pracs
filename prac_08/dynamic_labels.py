from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


NEW_COLOUR = (1, 0, 0, 1)


class DynamicLabelsApp(App):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name_to_phone = {"Bob Brown": "0414144411", "Cat Cyan": "0441411211", "Oren Ochre": "0432123456"}

    def build(self):
        """Build the Kivy GUI."""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_labels()
        return self.root

    def create_labels(self):
        """Create label from dictionary."""
        for name in self.name_to_phone:
            temp_label = Label(text=name)
            temp_label.color = NEW_COLOUR
            self.root.ids.main_box.add_widget(temp_label)


DynamicLabelsApp().run()