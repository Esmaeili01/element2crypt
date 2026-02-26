from random import randint

class Element : 
    def __init__(self) : 

        self.ELEMENTS = (
            'h', 'he',
            'li', 'be',
            'b', 'c', 'n', 'o', 'f', 'ne',
            'na', 'mg',
            'al', 'si', 'p', 's', 'cl', 'ar',
            'k', 'ca',
            'sc', 'ti', 'v', 'cr', 'mn', 'fe', 'co', 'ni', 'cu', 'zn',
            'ga', 'ge', 'as', 'se', 'br', 'kr',
            'rb', 'sr',
            'y', 'zr', 'nb', 'mo', 'tc', 'ru', 'rh', 'pd', 'ag', 'cd',
            'in', 'sn', 'sb', 'te', 'i', 'xe',
            'cs', 'ba',
            'la', 'ce', 'pr', 'nd', 'pm', 'sm', 'eu', 'gd', 'tb', 'dy', 'ho', 'er', 'tm', 'yb',
            'lu', 'hf', 'ta', 'w', 're', 'os', 'ir', 'pt', 'au', 'hg',
            'tl', 'pb', 'bi', 'po', 'at', 'rn',
            'fr', 'ra',
            'ac', 'th', 'pa', 'u', 'np', 'pu', 'am', 'cm', 'bk', 'cf', 'es', 'fm', 'md', 'no',
            'lr', 'rf', 'db', 'sg', 'bh', 'hs', 'mt', 'ds', 'rg', 'cn',
            'nh', 'fl', 'mc', 'lv', 'ts', 'og',
            'j', 'q'
        )
        self.el_size = 120 
    
    
    def search(self , letter : str):
        choice = []
        choice_len = 0
        for i in range(self.el_size) : 
            if self.ELEMENTS[i][0] == letter : 
                choice.append(i+1)
                choice_len += 1

        print(choice)
        return choice[randint(0,choice_len-1)]

    
    def encrypt(self , text : str) : 
        text = text.lower()
        size = len(text)
        cipher = []
        for i in range(size):
            temp = self.search(text[i])
            cipher.append(temp)

        return cipher
    
    def decrypt(self , cipher : list):
        text = ""
        for i in cipher : 
            text += self.ELEMENTS[i-1][0]
        
        return text
    
t = "abcdefghijklmnopqrstuvwxyz"
x = Element()
c = x.encrypt(t)
print(c)
v = x.decrypt(c)
print(v)

