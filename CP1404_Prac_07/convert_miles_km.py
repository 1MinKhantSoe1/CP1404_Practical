from kivy.app import App
from kivy.lang import Builder
from kivy.app import StringProperty


class Convert_Miles_KM(App):
    message = StringProperty()

    def build(self):

        self.title = "Convert Miles to Kilometres"

        self.root = Builder.load_file('convert_miles_km.kv')

    def calculate(self):
        number = float(self.root.ids.input_number.text)

        square = number / 0.62137

        self.root.ids.output_label.text = str("{:.3f}".format(square))

        self.message = self.root.ids.output_label.text

    def handle_increment(self):
        number = int(self.root.ids.input_number.text)
        increase = number + 1
        self.root.ids.input_number.text = str(increase)

    def handle_decrement(self):
        number = int(self.root.ids.input_number.text)
        increase = number - 1
        self.root.ids.input_number.text = str(increase)

        return self.root


if __name__ == '__main__':
    convert_miles_km = Convert_Miles_KM()
    convert_miles_km.run()
