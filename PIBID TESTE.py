#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install matplotlib


# In[2]:


import random
import math
import matplotlib
import matplotlib.pyplot


# In[5]:


print('Vale ressaltar que isso é somente um jogo. Não é possivel controlar a evolução de acordo com o seu desejo. Tudo ocorre de forma aleatória, aonde pode ou não ser benéfico. A evolução nada mais é que uma mudança.')
x = random.randint(1, 101)
print(x)


# In[6]:


if 1<=x<=50:
    especie = "Mariposa"
    print(f"Parabéns, você é responsável pela espécie de {especie}. Seu principal dever é sobreviver juntamente de sua espécie, aos acasos da evolução.")
    jogo_inicio=input('Para darmos início a nossa aventura, digite 1. Caso deseje finalizar o jogo, digite 2.')
    if int(jogo_inicio)==1:
        print('Então daremos início a nossa incrível jornada.')
        qnt=10000
        print(f'A população atual de {especie} é de {qnt}') 
        print(f'Após a chegada do ser humano, a espécie de {especie} pode ver seu habitat ser destruido. Existem dois indivíduos que nasceram com características diferentes. Um possui uma coloração mais escura, o que o pode fazer se adequar melhor ao ambiente e sobreviver aos predadores. O outro é um indivíduo desenvolveu uma asa com maior tamanho, o que aumentou sua velocidade. Qual desses indivíduos você escolheria para passar suas características a diante? PS: O outro será descartado.')
        escolha1=int(input('Digite aqui 1 para o primeiro indivíduo e 2 para o segundo indivíduo.')) 
        if escolha1==1:
            print(f'A população de {especie} desenvolveu uma coloração mais escura, o que proporcionou um aumento de 10% da população.')
            qnt1=qnt+(qnt/10)
            print(f'A população atual é de {qnt1}')
            y=random.randint(1, 101)
            if 1<=y<=60:       
                print(f'A humanidade poluiu o meio ambiente, e isso destruiu o habitat da espécie {especie}. A quantidade de {especie} diminuiu em 70%.')
                qnt2=(qnt1/100)*30
                print(qnt2)
                qnts=['Quantidade inicial', 'Quantidade 1', 'Quantidade 2']
                valores=[qnt, qnt1, qnt2]
                matplotlib.pyplot.plot(qnts, valores)
                matplotlib.pyplot.show()
            if 60<y<=100:
                print(f'A humanidade poluiu o meio ambiente, porém a espécie de {especie} foi capaz de desenvolver um filtro para resistir a poluição. Espécie +20%.')
                qnt2=(qnt1/100)*120
                print(qnt2)
                qnts=['Quantidade inicial', 'Quantidade 1', 'Quantidade 2']
                valores=[qnt, qnt1, qnt2]
                matplotlib.pyplot.plot(qnts, valores)
                matplotlib.pyplot.show()
        if escolha1==2:
            print(f'A espécie de {especie} foi capaz de desenvolver uma habilidade para voar mais rapido.')
            a=random.randint(1, 101)
            if 1<=a<=30:
                print(f'Os predadores da espécie de {especie} desenvolveram a habilidade de se locomover mais rápido. A espécie de {especie} foi predada e teve uma baixa de 20% da população.')
                qnt1=(qnt/100)*80
                print(qnt1)
                print(f'A espécie de {especie} desenvolveu ao acaso uma habilidade de resistência a altas temperaturas.')
                print(f'Devido a nova habilidade de resistencia a altas temperaturas, a espécie foi capaz de se locomover até regiões tropicais, porém sofreu uma perda de 25% de sua população no trajeto.')
                qnt2=(qnt1/100)*75
                valores=[qnt, qnt1, qnt2]
                matplotlib.pyplot.plot(qnts, valores)
                matplotlib.pyplot.show()
            if 30<a<=100:
                print(f'A espécie de {especie} foi capaz de fugir de seus predadores, e com isso sua população aumentou em 150%.')
                qnt1=(qnt/100)*150
                print(qnt1)
                print(f'Devido a seu aumento, o ser humano considerou a espécie de {especie} como uma praga, e lançou venenos para acabar com a população. -89% da população')
                qnt2=(qnt1/100)*11
                valores=[qnt, qnt1, qnt2]
                matplotlib.pyplot.plot(qnts, valores)
                matplotlib.pyplot.show()
    if jogo_inicio==2:
        print('Fim')

if 50<x<=100:
    print('era so um teste kkkkkkkk')


# In[ ]:




