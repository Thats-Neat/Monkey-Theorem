# Monkey Theorem
# using simplified keyboard. A-Z

import random
import time
from threading import Thread
import string
import threading


class monkey():
    
    def __init__(self):
        self.collection = ''


    def main(self):
        self.findString()
        
         
    def findString(self):
        string = input('STRING> ').replace(' ', '')
        z = 0
        
        start = time.time()
        
        for i in range(1):
            thread = threading.Thread(target=self.addLetter)
            thread.start()
        
        while True:
             
            if (z % 20000):
                if string in self.collection:
                    break
                
            z += 1
        
        print('Word Found')
        print(time.time()-start)
        input('')
            
    
    
    def addLetter(self):
        while True:
            self.collection = "".join([random.choice(string.ascii_letters), self.collection])
        

        
    
    def timer(self):
        start = time.time()
        
        for i in range(1):
            thread = threading.Thread(target=self.addLetter)
            thread.start()
            
        
        
        
        while True:
            #print(len(self.collection))

            if len(self.collection) >= 100000:
                break
            
        
        print(time.time()-start)
        input('')
    

if __name__ == '__main__':
    main = monkey()
    main.main()