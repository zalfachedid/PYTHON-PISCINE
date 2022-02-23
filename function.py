#!/usr/bin/env python
# coding: utf-8

# # function.py

# # 1

# In[ ]:


#Créer une fonction qui demande à l'utilisateur son nom et prénom et affiche un message dans la console.


# In[67]:


def prenom():
    x=input("quel est votre nom ")
    y=input("quel est votre prénom ")
    if (not str(x)or not str(y)):
        print("they should be strings")
        prenom()
    else:
        print("Bonjour {} {}".format(y,x))


# In[68]:


prenom()


# # 2

# In[5]:


#Créer une fonction qui demande à l'utilisateur son age et affiche l'année ou il aura 100 ans.


# In[13]:


def age():
    x=int(input("quel age avez vous? "))
    y=100-x+2022
    print("En {}, vous aurez 100 ans".format(y))


# In[14]:


age()


# # 3

# In[ ]:


#Écrire un programme qui, à partir de la saisie d'un rayon et d'une hauteur, calcule le volume d'un cône droit.


# In[19]:


import math as mt


# In[30]:


def volume():
    x=float(input("rayon "))
    y=float(input("hauteur "))
    z=1/3*mt.pi*x*x*y
    print("le volume d'un cône droit de rayon {} et de hauteur {} est {}".format(x,y,z))


# In[31]:


volume()


# # 4

# In[ ]:


#Ecrire un programme qui demande à l'utilisateur un nombre et détermine si ce nombre est pair ou impar avec un message d'affichage.


# In[34]:


def paritée():
    x=int(input("nombre "))
    if x%2==0:
        print ("{} est pair".format(x))
    else:
        print("{} est impair".format(x))


# In[36]:



paritée()


# # 5

# In[ ]:


# Ecrire une fonction qui calcul la suite de fibonnaci pour un rang donnée.


# In[7]:


def fibonacci(x):
    l=[0,1,1]
    if x<= 3:
        l=l[0:x+1]
    else:
        for i in range(x-3):
            u=l[-1]+l[-2]
            l.append(u)
    return l


# In[8]:


print(fibonacci(10))


# # 6

# In[ ]:


#Ecrire une fonction qui détermine tous les ppcm et pgcd d'un nombre donnée


# In[14]:


def ppcm_pgcd(x,y):
    l=[]
    t=[]
    v=[]
    s=1
    for i in range(1,x):
        if x%i==0:
            l.append(i)
        else:
            continue
    for i in range(1,y):
        if y%i==0:
            t.append(i)
        else:
            continue
    for i in range(0,len(l)):
        if l[i] in t:
            v.append(l[i])
        else:
            continue
    m=max(v)
    while (s*x)%y != 0:
        s=s+1
    r=s*x
    print("PPCM: {}, PGCD: {}".format(r,m))


# In[17]:


l=[1,4,6,10,9]


# In[6]:


print(4 in l)


# In[49]:


len(l)


# In[53]:


max(l)


# In[15]:


ppcm_pgcd(10,12)


# # 7

# In[ ]:


#Ecrire une fonction qui prend deux liste en paramètres et renvoie tous les elements communs au deux listes


# In[16]:


def commun(l,v):
    t=[]
    for i in range(0,len(l)):
        if l[i] in v:
            t.append(l[i])
        else :
            continue   
    return t


# In[20]:


r=[1,3,6,29]


# In[21]:


print(commun(l,r))


# # 8

# In[ ]:


#Ecrire une fonction qui determine si une chaine de caractère est un palyndrome


# In[24]:


t='ksjhdfh'
u=[i for i in t]
print(u)


# In[32]:


v= [u[i]for i in range(-1,-len(u)-1,-1)]
print(v)


# In[34]:


def polyndrome(x):
    u=[i for i in x]
    v= [u[i]for i in range(-1,-len(u)-1,-1)]
    if u==v:
        print("{} est un polyndrome".format(x))
    else:
        print("{} n'est pas un polyndrome".format(x))


# In[36]:


polyndrome("haha")


# # 9

# In[ ]:


#Ecrire une fonction qui enelve tout les doublons d'une liste


# In[ ]:


def remove(l,x):
    for i in range(0,len(l)):
        if 


# In[73]:


def doublon(x):
    for i in range(0,len(x)):
        if x[i] in x:
            x.remove(x[i])
            doublon(x)
        else:
            continue
    return x


# In[74]:


print(doublon([1,2,4,6]))


# # 10

# In[ ]:


#Ecrire une fonction qui valide si une adresse IP est valide.


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




