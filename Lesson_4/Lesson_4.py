# self => this

class Human:
    def talk(self, sentence):
        print(f"Human is talking: {sentence}")

    def walk(self):
        print("Human is walking")


human = Human()
human.talk("Merhaba")  # python otomatık olarak self den sonrakı degıskene atar
human.walk()
