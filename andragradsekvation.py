import math

class Andragradsekvation:
    
    def __init__(self, p, q):
        self.p=int(p)
        self.q=int(q)
    
    def diskriminant(self):
        return ((self.p)/2)**2-q
    
    def lösningar(self):
        lista =list()

        if self.diskriminant()<0:
            lista = []
            return lista
        
        elif self.diskriminant() >=0:
            x1 = (-self.p/2) + (math.sqrt((self.p/2)** 2 - self.q))
            x2 = (-self.p/2) - (math.sqrt((self.p/2)** 2 - self.q))
            
            ex1= round(x1,2)
            ex2= round(x2,2)
            
            if ex2==ex1:
               
               lista=[ex1]
            else:
                
                
                lista=[ex1,ex2]
        return lista
        
    
    def __str__(self):
        str = (f'x^2 + {self.p}x + {self.q} = 0')
        return str



str = input('Ange heltalen p och q i en andragradsekvation (x\u00b2 + px + q = 0): ')
lista = str.split()

for index in range(0, len(lista)):
    lista[index] = int(lista[index])

p = lista[0]
q = lista[1]

ekvation = Andragradsekvation(p,q)
lösningar = ekvation.lösningar()
print(ekvation)

if len(lösningar) == 0:
    print('Ekvationen har inga reella lösningar')
elif len(lösningar) == 1:
    print(f'Ekvationen har en lösning: {lösningar[0]}')
else:
    print(f'Ekvationen har två lösningar: {lösningar[0]} och {lösningar[1]}')


