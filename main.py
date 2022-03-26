# Monkey Theorem
# using simplified keyboard. A-Z

import random
import time
from threading import Thread

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
        self.findString()
        
        
    def findDict(self):
        z = 0
        while True:
            self.addLetter()
            if (z % 20000):
                self.wordIdentifier()
            z += 1
            
    def findString(self):
        string = input('STRING> ').replace(' ', '')
        z = 0
        
        while True:
            self.addLetter()
            
            
            if (z % 20000):
                if string in self.collection:
                    break
                
            z += 1
        
        print('Word Found')
            
    def addLetter(self):
        self.collection += self.letters[random.randint(0, 25)]
        
    def wordIdentifier(self):
        for i in range(0, len(self.words)):
            if self.words[i] in self.collection and self.words[i] not in self.found:
                print(f'WORD FOUND - {self.words[i]}')
                self.found.append(self.words[i])
                
    def timer(self):
        start = time.time()
        
        while True:
            print(len(self.collection))
            if len(self.collection) >= 1000000:
                break
            
        
        print(time.time()-start)
    

if __name__ == '__main__':
    main = monkey()
    main.main()