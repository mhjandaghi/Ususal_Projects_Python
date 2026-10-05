# imports and global vars
from abc import ABC, abstractmethod
import string
import random

# create password gen abstract class
class PasswordGeneratorAbstract(ABC):
    
    @abstractmethod
    def generate_password(self, length=8):
        pass



# create numeric password generator
class NumericPasswordGenerator(PasswordGeneratorAbstract):
    letters = string.digits
    
    def generate_password(self, length=8):
        return "".join(str(random.choice(self.letters))for _ in range(length))
        # result = ""
        # for _ in range(length):
        #     result += str(random.choice(self.letters))
            
        # return result

# create letters password generator
class LettersPasswordGenerator(PasswordGeneratorAbstract):
    letters = string.ascii_letters
    
    def generate_password(self, length=8):
        return "".join(str(random.choice(self.letters))for _ in range(length))

# create mixed password generator
class MixedPasswordGenerator(PasswordGeneratorAbstract):
    letters = string.ascii_letters + string.digits
    
    def generate_password(self, length=8):
        return "".join(str(random.choice(self.letters))for _ in range(length))


# run the app
generator = MixedPasswordGenerator()
print(generator.generate_password(12))