from random import randint

class Periodic : 
    def __init__(self) : 

        self.ELEMENTS = (
                'H', 'He', 
                'Li', 'Be', 
                'B', 'C', 'N', 'O', 'F', 'Ne', 
                'Na', 'Mg', 
                'Al', 'Si', 'P', 'S', 'Cl', 'Ar', 
                'K', 'Ca', 
                'SC', 'Ti', 'V', 'Cr', 'Mn', 'Fe', 'Co', 'Ni', 'Cu', 'Zn', 
                'Ga', 'Ge', 'As', 'Se', 'Br', 'Kr', 
                'Rb', 'Sr', 
                'Y', 'Zr', 'Nb', 'Mo', 'Tc', 'Ru', 'Rh', 'Pd', 'Ag', 'Cd', 
                'In', 'Sn', 'Sb', 'Te', 'I', 'Xe', 
                'Cs', 'Ba', 
                'La', 'Ce', 'Pr', 'Nd', 'Pm', 'Sm', 'Eu', 'Gd', 'Tb', 'Dy', 'Ho', 'Er', 'Tm', 'Yb', 
                'Lu', 'Hf', 'Ta', 'W', 'Re', 'Os', 'Ir', 'Pt', 'Au', 'Hg', 
                'Tl', 'Pb', 'Bi', 'Po', 'At', 'Rn', 
                'Fr', 'Ra', 
                'Ac', 'Th', 'Pa', 'U', 'Np', 'Pu', 'Am', 'Cm', 'Bk', 'Cf', 'Es', 'Fm', 'Md', 'No', 
                'Lr', 'Rf', 'Db', 'Sg', 'Bh', 'Hs', 'Mt', 'Ds', 'Rg', 'Cn', 
                'Nh', 'Fl', 'Mc', 'Lv', 'Ts', 'Og', 
                'J', 'Q'
            )
        self.el_size = 120 
    
    def search(self , pair : str):
        choices = [] 
        for i in range(self.el_size) : 
            if pair == self.ELEMENTS[i] : 
                choices.append(i)
                break
        first_letter = []
        second_letter = []
        for i in range(self.el_size) : 
            if pair[0] == self.ELEMENTS[i][0] : 
                first_letter.append(i)
            if pair[1] == self.ELEMENTS[i][0] : 
                second_letter.append(i)

        if first_letter and second_letter : 
            for i in first_letter : 
                for j in second_letter : 
                    choices.append(i,j)
        
        return choices[randint(0 , len(choices)-1)]
    
    def encrypt(self , text : str) : 

        pass
