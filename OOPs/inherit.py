class animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound.")
    
class dog(animal):
    def speak(self):
        print(f"{self.name} barks.")
class cat(animal):
    def speak(self):
        print(f"{self.name} meows.")
Dog= dog("Buddy")
Cat= cat("Whiskers")
Dog.speak()
Cat.speak()