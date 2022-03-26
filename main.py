# Monkey Theorem
# using simplified keyboard. A-Z

# To Add
# find sentence with spaces
# find words in common list
# find given string

import random

class monkey():
    
    def __init__(self):
        self.letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] # maybe add ' '
        self.collection = ''
        self.words = []
        self.found = []
        
        with open('words.txt', 'r') as f:
            self.words = f.readlines()
            
        for i in range(0, len(self.words)):
            self.words[i] = self.words[i].strip('\n')

        
        
    def main(self):
        z = 0
        while True:
            self.addLetter()
            if (z % 20000):
                self.wordIdentifier()
            z += 1
        
            
    def addLetter(self):
        self.collection += self.letters[random.randint(0, 25)]
        
    def wordIdentifier(self):
        for i in range(0, len(self.words)):
            if self.words[i] in self.collection and self.words[i] not in self.found:
                print(f'WORD FOUND - {self.words[i]}')
                self.found.append(self.words[i])
    

if __name__ == '__main__':
    main = monkey()
    main.main()