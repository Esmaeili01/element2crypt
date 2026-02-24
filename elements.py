from random import randint

class Periodic : 
    def __init__(self , text : str) : 

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
        self.text = text.lower()
        self.text_size = len(text)
    
    def search(self , pair : str):
        choices = [] 
        for i in range(self.el_size) : 
            if pair == self.ELEMENTS[i] : 
                choices.append(i+1)
                break
        
        first_letter = []
        second_letter = []
        for i in range(self.el_size) : 
            if pair[0] == self.ELEMENTS[i][0] : 
                first_letter.append(i+1)
            if len(pair) == 2 : 
                if pair[1] == self.ELEMENTS[i][0] : 
                    second_letter.append(i+1)

        if first_letter or second_letter : 
            for i in first_letter : 
                if len(pair) == 2 :  
                    for j in second_letter : 
                        choices.append((i,j))
                else : 
                    choices.append(i)

        return choices[randint(0 , len(choices)-1)]
    
    def encrypt(self) : 
        cipher = []
        for i in range(0,self.text_size , 2):
            temp = self.search(self.text[i:i+2])
            if type(temp) == int : 
                cipher.append(temp)
            else : 
                cipher += temp

        return cipher
    
t = "hel"
x = Periodic(t)
c = x.encrypt()

print(c)

