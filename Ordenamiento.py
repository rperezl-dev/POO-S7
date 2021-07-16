class Ordenar:
    def __init__(self,lista):
        self.lista=lista
    def borbuja(self):
        for i in range(len(self.lista)):
            for j in range(i+1,len(self.lista)):
                if self.lista[i]>self.lista[j]:
                    aux=self.lista[i]
                    self.lista[i]=self.lista[j]
                    self.lista[j]=aux
    def insertar(self,valor):
        self.borbuja()
        auxlista=[]
        enc=False
        for pos,ele in enumerate(self.lista):
            if ele > valor:
                auxlista.append(valor)
                enc=True
                break
        if enc: self.lista=self.lista[0:pos] + auxlista + self.lista[pos:]
        else:self.lista.append(valor)
        return self.lista

    def insertar2(self,valor):
        self.borbuja()
        auxlista=[]
        enc=False
        for pos,ele in enumerate(self.lista):
            if ele > valor:
                enc=True
                break
        if enc:
            for i in range(pos):
                auxlista.append(self.lista[i])
            auxlista.append(valor)
            for j in range(pos,len(self.lista)):
                auxlista.append(self.lista[j])
            self.lista=auxlista
        else:
            self.lista.append(valor)
        return self.lista

ord1=Ordenar([10,15,20,70,80])

print(ord1.insertar2(50))
#ord1.borbuja()
#print(ord1.lista)