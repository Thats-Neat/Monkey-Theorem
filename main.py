# Monkey Theorem
# using simplified keyboard. A-Z

import random
import time
from threading import Thread
import string


class monkey():
    
    def __init__(self):
        self.collection = ''


    def main(self):
        self.timer()
        
         
    def findString(self):
        string = input('STRING> ').replace(' ', '')
        z = 0
        
        start = time.time()
        while True:
            self.addLetter()
            
            
            if (z % 20000):
                if string in self.collection:
                    break
                
            z += 1
        
        print('Word Found')
        print(time.time()-start)
        input('')
            
    
    
    def addLetter(self):
        self.collection += random.choice(string.ascii_letters)
        
    
    def timer(self):
        start = time.time()
        
        while True:
            self.addLetter()
            print(len(self.collection))

            if len(self.collection) >= 100000:
                break
            
        
        print(time.time()-start)
    

if __name__ == '__main__':
    main = monkey()
    main.main()