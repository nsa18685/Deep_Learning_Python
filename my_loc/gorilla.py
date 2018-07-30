# coding: utf-8

# In[ ]:

class Go():
    def __init__(self):
        self.banna = 0
        
    def eat(self, num):
        self.banna = num
        
    def walk(self, num):
        for i in range(num):
            if self.banna > 0:
                print('뚜벅뚜벅')
                self.banna -= 1
            elif self.banna == 0:
                print('바나나가 없으면 걸어갈 수 없습니다.')
                break;
                
    def shout(self, num):
        for i in range(num):
            if self.banna > 0:
                print('우아 ~~~~')
                self.banna -= 1
            elif self.banna == 0:
                print('바나나가 없으면 소리를 지를 수 없습니다.')
                break;
    
    def print(self):
        print('banna {} 개 남았습니다. '.format(self.banna))
