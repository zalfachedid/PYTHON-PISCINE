#!/usr/bin/env python
# coding: utf-8

# # function.py

# # 1

# In[ ]:


#Créer une fonction qui demande à l'utilisateur son nom et prénom et affiche un message dans la console.


<<<<<<< HEAD
# In[83]:
=======
# In[67]:
>>>>>>> 0397b487072e94c03044f40090a5ae95da1ec94a


def prenom():
    x=input("quel est votre nom ")
    y=input("quel est votre prénom ")
<<<<<<< HEAD
    print("Bonjour {} {}".format(y,x))
=======
    if (not str(x)or not str(y)):
        print("they should be strings")
        prenom()
    else:
        print("Bonjour {} {}".format(y,x))


# In[68]:


prenom()
>>>>>>> 0397b487072e94c03044f40090a5ae95da1ec94a


# # 2

# In[5]:


#Créer une fonction qui demande à l'utilisateur son age et affiche l'année ou il aura 100 ans.


<<<<<<< HEAD
# In[109]:


def age():
    a=int(input("quel age avez vous? "))
    if (not int(a)):
        print("age can no be a strings")
        age()
    elif (a<0):
        print("age needs to be >0")
        age()
    elif (a.real != a) :
        print("age need to be real")
        age()
    elif (1<a>1000) :
        print("age needs to be <1000 and >1")
        age()
    else:
        y=100-a+2022
        print("En {}, vous aurez 100 ans".format(y))
=======
# In[13]:


def age():
    x=int(input("quel age avez vous? "))
    y=100-x+2022
    print("En {}, vous aurez 100 ans".format(y))


# In[14]:


age()
>>>>>>> 0397b487072e94c03044f40090a5ae95da1ec94a


# # 3

# In[ ]:


#Écrire un programme qui, à partir de la saisie d'un rayon et d'une hauteur, calcule le volume d'un cône droit.


<<<<<<< HEAD
# In[90]:
=======
# In[19]:
>>>>>>> 0397b487072e94c03044f40090a5ae95da1ec94a


import math as mt


<<<<<<< HEAD
# In[107]:
=======
# In[30]:
>>>>>>> 0397b487072e94c03044f40090a5ae95da1ec94a


def volume():
    x=float(input("rayon "))
    y=float(input("hauteur "))
<<<<<<< HEAD
    if (not int(x) or not int(y)):
        print("rayon and hauteur can no be a strings")
        volume()
    elif (x<0 or y<0):
        print("rayon and hauteur needs to be >0")
        volume()
    elif (x.real != x or y.real != y) :
        print("rayon and hauteur need to be real")
        volume()
    elif (1<x>1000 or 1<y>1000) :
        print("rayon and hauteur needs to be <1000 and >1")
        volume()
    else:
        z=1/3*mt.pi*x*x*y
        print("le volume d'un cône droit de rayon {} et de hauteur {} est {}".format(x,y,z))
=======
    z=1/3*mt.pi*x*x*y
    print("le volume d'un cône droit de rayon {} et de hauteur {} est {}".format(x,y,z))


# In[31]:


volume()
>>>>>>> 0397b487072e94c03044f40090a5ae95da1ec94a


# # 4

# In[ ]:


#Ecrire un programme qui demande à l'utilisateur un nombre et détermine si ce nombre est pair ou impar avec un message d'affichage.


<<<<<<< HEAD
# In[ ]:


def paritée():
    a=int(input("nombre "))
    if (not int(a)):
        print("it can no be a strings")
        paritée()
    elif (a<0):
        print("it needs to be >0")
        paritée()
    elif (a.real != a) :
        print("it need to be real")
        paritée()
    elif (1<a>1000) :
        print("it needs to be <1000 and >1")
        paritée()
    else:
        if a%2==0:
            print ("{} est pair".format(a))
        else:
            print("{} est impair".format(a))
=======
# In[34]:


def paritée():
    x=int(input("nombre "))
    if x%2==0:
        print ("{} est pair".format(x))
    else:
        print("{} est impair".format(x))


# In[36]:



paritée()
>>>>>>> 0397b487072e94c03044f40090a5ae95da1ec94a


# # 5

# In[ ]:


# Ecrire une fonction qui calcul la suite de fibonnaci pour un rang donnée.


<<<<<<< HEAD
# In[111]:
=======
# In[7]:
>>>>>>> 0397b487072e94c03044f40090a5ae95da1ec94a


def fibonacci(x):
    l=[0,1,1]
<<<<<<< HEAD
    if (not int(x)):
        print("x can no be a strings")
        x=int(input("x="))
        fibonacci(x)
    elif (x<0):
        print("x needs to be >0")
        x=int(input("x="))
        fibonacci(x)
    elif (x.real != x) :
        print("x need to be real")
        x=int(input("x="))
        fibonacci(x)
    elif (1<x>1000) :
        print("x needs to be <1000 and >1")
        x=int(input("x="))
        fibonacci(x)
    else:
        if x<= 3:
            l=l[0:x+1]
        else:
            for i in range(x-3):
                u=l[-1]+l[-2]
                l.append(u)
    return l


=======
    if x<= 3:
        l=l[0:x+1]
    else:
        for i in range(x-3):
            u=l[-1]+l[-2]
            l.append(u)
    return l


# In[8]:


print(fibonacci(10))


>>>>>>> 0397b487072e94c03044f40090a5ae95da1ec94a
# # 6

# In[ ]:


#Ecrire une fonction qui détermine tous les ppcm et pgcd d'un nombre donnée


<<<<<<< HEAD
# In[ ]:
=======
# In[14]:
>>>>>>> 0397b487072e94c03044f40090a5ae95da1ec94a


def ppcm_pgcd(x,y):
    l=[]
    t=[]
    v=[]
    s=1
<<<<<<< HEAD
    if (not int(x) or not int(y)):
        print("x et y can no be a strings")
        x=int(input("x="))
        y=int(input("x="))
        ppcm_pgcd(x,y)
    elif (x<0 or y<0):
        print("x et y needs to be >0")
        x=int(input("x="))
        y=int(input("x="))
        ppcm_pgcd(x,y)
    elif (x.real != x or y.real != y) :
        print("x et y need to be real")
        x=int(input("x="))
        y=int(input("x="))
        ppcm_pgcd(x,y)
    elif (1<x>1000 or 1<y>1000) :
        print("x et y needs to be <1000 and >1")
        x=int(input("x="))
        y=int(input("x="))
        ppcm_pgcd(x,y)
    else:
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


=======
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


>>>>>>> 0397b487072e94c03044f40090a5ae95da1ec94a
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


<<<<<<< HEAD
=======
# In[20]:


r=[1,3,6,29]


# In[21]:


print(commun(l,r))


>>>>>>> 0397b487072e94c03044f40090a5ae95da1ec94a
# # 8

# In[ ]:


#Ecrire une fonction qui determine si une chaine de caractère est un palyndrome


<<<<<<< HEAD
=======
# In[24]:


t='ksjhdfh'
u=[i for i in t]
print(u)


# In[32]:


v= [u[i]for i in range(-1,-len(u)-1,-1)]
print(v)


>>>>>>> 0397b487072e94c03044f40090a5ae95da1ec94a
# In[34]:


def polyndrome(x):
    u=[i for i in x]
    v= [u[i]for i in range(-1,-len(u)-1,-1)]
    if u==v:
        print("{} est un polyndrome".format(x))
    else:
        print("{} n'est pas un polyndrome".format(x))


<<<<<<< HEAD
=======
# In[36]:


polyndrome("haha")


>>>>>>> 0397b487072e94c03044f40090a5ae95da1ec94a
# # 9

# In[ ]:


#Ecrire une fonction qui enelve tout les doublons d'une liste


<<<<<<< HEAD
# In[75]:
=======
# In[ ]:


def remove(l,x):
    for i in range(0,len(l)):
        if 


# In[73]:
>>>>>>> 0397b487072e94c03044f40090a5ae95da1ec94a


def doublon(x):
    for i in range(0,len(x)):
        if x[i] in x:
            x.remove(x[i])
            doublon(x)
        else:
            continue
    return x


<<<<<<< HEAD
=======
# In[74]:


print(doublon([1,2,4,6]))


>>>>>>> 0397b487072e94c03044f40090a5ae95da1ec94a
# # 10

# In[ ]:


#Ecrire une fonction qui valide si une adresse IP est valide.


# In[ ]:





<<<<<<< HEAD
# # 11

# In[77]:


#Ecrire un programme qui transcrit un nombre en paramètre en binaire en gardant les 0 devant
=======
# In[ ]:





# In[ ]:





# In[ ]:



>>>>>>> 0397b487072e94c03044f40090a5ae95da1ec94a


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




