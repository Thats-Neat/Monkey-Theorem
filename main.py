# Monkey Theorem
# using simplified keyboard. A-Z

import random

class monkey():
    
    def __init__(self):
        self.letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        self.collection = ''
    
    def main(self):
        while True:
            self.addLetter()
            print(self.collection)
            
    def addLetter(self):
        self.collection += self.letters[random.randint(0, 25)]
        
    def wordIdentifier(self):
        pass
    


if __name__ == '__main__':
    main = monkey()
    main.main()