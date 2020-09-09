from kivy.app import App
from kivy.lang import Builder


class Squaring(App):

    def build(self):
        self.title = "Squaring"

        self.root = Builder.load_file('squaring.kv')

    def calculate(self):
        number = float(self.root.ids.input_number.text)

        square = number * number

        self.root.ids.output_label.text = str(square)

        return self.root


if __name__ == '__main__':
    squaring = Squaring()
    squaring.run()
