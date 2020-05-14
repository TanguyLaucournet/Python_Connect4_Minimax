# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 14:32:39 2020

@author: PC
"""
import copy
import random 
def Actions(s):
    actions=[] #contient les actions possibles (les colonnes dans lesquelles on peut encore jouer)
    for j in range(12): #on parcourt l'ensemble des colonnes
        if(s[0][j]==' '): #si la case en haut de la colonne est vide, celà signifie que l'on peut encore placer au moins un jeton dans la colonne
            actions.append(j) #on ajoute la colonne aux actions possibles
    return actions

def Resultat(s,a,joueur):
    nouvelEtat= copy.deepcopy(s) #deepcopy est utilisé afin de ne pas modifier s
    row=5 #derniere ligne du tableau
    while(row>=0): #en fonction de la colonne choisi, on remonte cette dernière jusqu'à trouver la première case vide et y placer le jeton
        if(nouvelEtat[row][a]==' '):  
            nouvelEtat[row][a]=joueur
            row=-1
        else:
            row=row - 1
    return nouvelEtat

def Terminal_Test(s):
        
    for i in range(5,-1,-1):#permet de vérifier si un des deux joueurs a aligné 4 jetons sur une ligne
        temp=''
        count=0
        for j in range(12):                
            if(s[i][j]==temp):
                count+=1
                if(count==4): 
                    return True
            elif(s[i][j]!=temp):
                if(s[i][j]=='X' or s[i][j]=='O'):
                    temp=s[i][j]
                    count=1
                else:
                    temp=''
                    count=0
    
    for j in range(12): #permet de vérifier si un des deux joueurs a aligné 4 jetons sur une colonne
        if(count==4):
            return True
        temp=''  
        count=0
        for i in range(5,-1,-1):           
            if(s[i][j]==temp):
                count+=1
                if(count==4):
                    return True
            elif(s[i][j]!=temp):
                if(s[i][j]=='X' or s[i][j]=='O'):
                    temp=s[i][j]
                    count=1
                else:
                    temp=''
                    count=0
                    
    for k in range(2,-9,-1): #permet de vérifier si un des deux joueurs a aligné 4 jetons sur une diagonale "descendante" 
        temp=''
        count=0
        for j in range(12):
            for i in range(5,-1,-1):
                if(i-j==k):
                    if(s[i][j]==temp):
                        count+=1
                        if(count==4):
                            return True
                    elif(s[i][j]!=temp):
                        if(s[i][j]=='X' or s[i][j]=='O'):
                            temp=s[i][j]
                            count=1
                        else:
                            temp=''
                            count=0
    
    for k in range(3,14): #permet de vérifier si un des deux joueurs a aligné 4 jetons sur une diagonale "montante" 
        temp=''
        count=0
        for j in range(12): 
            for i in range(5,-1,-1):
                if(i+j==k):
                    if(s[i][j]==temp):
                        count+=1
                        if(count==4):
                            return True
                    elif(s[i][j]!=temp):
                        if(s[i][j]=='X' or s[i][j]=='O'):
                            temp=s[i][j]
                            count=1
                        else:
                            temp=''
                            count=0
                    
    for row in s:
        if(' ' in row): #on vérifie s'il reste des espaces vides 
            return False 
    
    return True #le tableau est complet 
def Heuristic(s):
    
    jetons=0
    for i in range(5,-1,-1):
        for j in range(12):
            if(s[i][j]=='O' or s[i][j]=='X'):
                jetons+=1
    
    for i in range(5,-1,-1):#detrmine quel joueur à aligner 4 jetons sur une ligne (on considère que X est notre joueur et O l'adversaire)
        temp=''
        count=0
        for j in range(12):                
            if(s[i][j]==temp):
                count+=1
                if(count==4):
                    if(temp=='X'):
                        return 1000*(42-jetons)
                    else:
                        return -1000*(42-jetons)
            elif(s[i][j]!=temp):
                if(s[i][j]=='X' or s[i][j]=='O'):
                    temp=s[i][j]
                    count=1
                else:
                    temp=''
                    count=0
    
    for j in range(12): #alignement sur une colonne 
        temp=''  
        count=0
        for i in range(5,-1,-1):           
            if(s[i][j]==temp):
                count+=1
                if(count==4):
                    if(temp=='X'):
                        return 1000*(42-jetons)
                    else:
                        return -1000*(42-jetons)
            elif(s[i][j]!=temp):
                if(s[i][j]=='X' or s[i][j]=='O'):
                    temp=s[i][j]
                    count=1
                else:
                    temp=''
                    count=0
                    
    for k in range(2,-9,-1): #alignement 4 jetons sur une diagonale "descendante" 
        temp=''
        count=0
        for j in range(12):
            for i in range(5,-1,-1):
                if(i-j==k):
                    if(s[i][j]==temp):
                        count+=1
                        if(count==4):
                            if(temp=='X'):
                                return 1000*(42-jetons)
                            else:
                                return-1000*(42-jetons)
                    elif(s[i][j]!=temp):
                        if(s[i][j]=='X' or s[i][j]=='O'):
                            temp=s[i][j]
                            count=1
                        else:
                            temp=''
                            count=0
    
    for k in range(3,14): #alignement 4 jetons sur une diagonale "montante" 
        temp=''
        count=0
        for j in range(12): 
            for i in range(5,-1,-1):
                if(i+j==k):
                    if(s[i][j]==temp):
                        count+=1
                        if(count==4):
                            if(temp=='X'):
                                return 1000*(42-jetons)
                            else:
                                return-1000*(42-jetons)
                    elif(s[i][j]!=temp):
                        if(s[i][j]=='X' or s[i][j]=='O'):
                            temp=s[i][j]
                            count=1
                        else:
                            temp=''
                            count=0
    
    poids=0                
    for i in range(5,-1,-1):
        for j in range(12):
            joueur=s[i][j]
            if(joueur=='X'):
                if(i==5):
                    if(j==0):
                        for k in range(i - 1, i + 1):
                            for l in range(j, j+2):
                                if(k!=i and l!=j):
                                    if(s[k][l]==joueur):
                                        poids+=2
                                    elif(s[k][l]==' '):
                                        poids+=1
                                    else:
                                        poids-=1;
                    elif(j==11):
                        for k in range(i - 1, i + 1):
                            for l in range(j-1, j+1):
                                if(k!=i and l!=j):
                                    if(s[k][l]==joueur):
                                        poids+=2
                                    elif(s[k][l]==' '):
                                        poids+=1
                                    else:
                                        poids-=1;
                    else:
                        for k in range(i - 1, i + 1):
                            for l in range(j-1, j+2):
                                if(k!=i and l!=j):
                                    if(s[k][l]==joueur):
                                        poids+=2
                                    elif(s[k][l]==' '):
                                        poids+=1
                                    else:
                                        poids-=1;
                                            
                elif(i==0):
                    if(j==0):
                        for k in range(i, i + 2):
                            for l in range(j, j+2):
                                if(k!=i and l!=j):
                                    if(s[k][l]==joueur):
                                        poids+=2
                                    elif(s[k][l]==' '):
                                        poids+=1
                                    else:
                                        poids-=1;
                    elif(j==11):
                        for k in range(i, i + 2):
                            for l in range(j-1, j+1):
                                if(k!=i and l!=j):
                                    if(s[k][l]==joueur):
                                        poids+=2
                                    elif(s[k][l]==' '):
                                        poids+=1
                                    else:
                                        poids-=1;
                    else:
                        for k in range(i, i + 2):
                            for l in range(j-1, j+2):
                                if(k!=i and l!=j):
                                    if(s[k][l]==joueur):
                                        poids+=2
                                    elif(s[k][l]==' '):
                                        poids+=1
                                    else:
                                        poids-=1;   
                    
                else:
                    if(j==0):
                        for k in range(i-1, i + 2):
                            for l in range(j, j+2):
                                if(k!=i and l!=j):
                                    if(s[k][l]==joueur):
                                        poids+=2
                                    elif(s[k][l]==' '):
                                        poids+=1
                                    else:
                                        poids-=1;
                    elif(j==11):
                        for k in range(i-1, i + 2):
                            for l in range(j-1, j+1):
                                if(k!=i and l!=j):
                                    if(s[k][l]==joueur):
                                        poids+=2
                                    elif(s[k][l]==' '):
                                        poids+=1
                                    else:
                                        poids-=1;
                    else:
                        for k in range(i-1, i + 2):
                            for l in range(j-1, j+2):
                                if(k!=i and l!=j):
                                    if(s[k][l]==joueur):
                                        poids+=2
                                    elif(s[k][l]==' '):
                                        poids+=1
                                    else:
                                        poids-=1;
    

            elif(joueur=='O'):
                if(i==5):
                    if(j==0):
                        for k in range(i - 1, i + 1):
                            for l in range(j, j+2):
                                if(k!=i and l!=j):
                                    if(s[k][l]==joueur):
                                        poids-=2
                                    elif(s[k][l]==' '):
                                        poids-=1
                                    else:
                                        poids+=1;
                    elif(j==11):
                        for k in range(i - 1, i + 1):
                            for l in range(j-1, j+1):
                                if(k!=i and l!=j):
                                    if(s[k][l]==joueur):
                                        poids-=2
                                    elif(s[k][l]==' '):
                                        poids-=1
                                    else:
                                        poids+=1;
                    else:
                        for k in range(i - 1, i + 1):
                            for l in range(j-1, j+2):
                                if(k!=i and l!=j):
                                    if(s[k][l]==joueur):
                                        poids-=2
                                    elif(s[k][l]==' '):
                                        poids-=1
                                    else:
                                        poids+=1;
                                            
                elif(i==0):
                    if(j==0):
                        for k in range(i, i + 2):
                            for l in range(j, j+2):
                                if(k!=i and l!=j):
                                    if(s[k][l]==joueur):
                                        poids-=2
                                    elif(s[k][l]==' '):
                                        poids-=1
                                    else:
                                        poids+=1;
                    elif(j==11):
                        for k in range(i, i + 2):
                            for l in range(j-1, j+1):
                                if(k!=i and l!=j):
                                    if(s[k][l]==joueur):
                                        poids-=2
                                    elif(s[k][l]==' '):
                                        poids-=1
                                    else:
                                        poids+=1;
                    else:
                        for k in range(i, i + 2):
                            for l in range(j-1, j+2):
                                if(k!=i and l!=j):
                                    if(s[k][l]==joueur):
                                        poids-=2
                                    elif(s[k][l]==' '):
                                        poids-=1
                                    else:
                                        poids+=1;   
                    
                else:
                    if(j==0):
                        for k in range(i-1, i + 2):
                            for l in range(j, j+2):
                                if(k!=i and l!=j):
                                    if(s[k][l]==joueur):
                                        poids-=2
                                    elif(s[k][l]==' '):
                                        poids-=1
                                    else:
                                        poids+=1;
                    elif(j==11):
                        for k in range(i-1, i + 2):
                            for l in range(j-1, j+1):
                                if(k!=i and l!=j):
                                    if(s[k][l]==joueur):
                                        poids-=2
                                    elif(s[k][l]==' '):
                                        poids-=1
                                    else:
                                        poids+=1;
                    else:
                        for k in range(i-1, i + 2):
                            for l in range(j-1, j+2):
                                if(k!=i and l!=j):
                                    if(s[k][l]==joueur):
                                        poids-=2
                                    elif(s[k][l]==' '):
                                        poids-=1
                                    else:
                                        poids+=1;
    
    return poids


def Utility(s):
        
    for i in range(5,-1,-1):#detrmine quel joueur à aligner 4 jetons sur une ligne (on considère que X est notre joueur et O l'adversaire)
        temp=''
        count=0
        for j in range(12):                
            if(s[i][j]==temp):
                count+=1
                if(count==4):
                    if(temp=='X'):
                        return 1
                    else:
                        return-1
            elif(s[i][j]!=temp):
                if(s[i][j]=='X' or s[i][j]=='O'):
                    temp=s[i][j]
                    count=1
                else:
                    temp=''
                    count=0
    
    for j in range(12): #alignement sur une colonne 
        if(count==4):
            return 1
        temp=''  
        count=0
        for i in range(5,-1,-1):           
            if(s[i][j]==temp):
                count+=1
                if(count==4):
                    if(temp=='X'):
                        return 1
                    else:
                        return-1
            elif(s[i][j]!=temp):
                if(s[i][j]=='X' or s[i][j]=='O'):
                    temp=s[i][j]
                    count=1
                else:
                    temp=''
                    count=0
                    
    for k in range(2,-9,-1): #alignement 4 jetons sur une diagonale "descendante" 
        temp=''
        count=0
        for j in range(12):
            for i in range(5,-1,-1):
                if(i-j==k):
                    if(s[i][j]==temp):
                        count+=1
                        if(count==4):
                            if(temp=='X'):
                                return 1
                            else:
                                return-1
                    elif(s[i][j]!=temp):
                        if(s[i][j]=='X' or s[i][j]=='O'):
                            temp=s[i][j]
                            count=1
                        else:
                            temp=''
                            count=0
    
    for k in range(3,14): #alignement 4 jetons sur une diagonale "montante" 
        temp=''
        count=0
        for j in range(12): 
            for i in range(5,-1,-1):
                if(i+j==k):
                    if(s[i][j]==temp):
                        count+=1
                        if(count==4):
                            if(temp=='X'):
                                return 1
                            else:
                                return-1
                    elif(s[i][j]!=temp):
                        if(s[i][j]=='X' or s[i][j]=='O'):
                            temp=s[i][j]
                            count=1
                        else:
                            temp=''
                            count=0
                    
    return 0 #égalité

   
#-----------------------------------------------------------------------------#
    
def afficher_colonnes(nb_colonne=12):
    
    print(' ',end=' ')
    for j in range(1,nb_colonne+1):
        print(j,end=' ')
    print()
        
def afficher_grille(p4):
    i = int() ; j = int() # index pour parcourir les cases de la grille
 #1.afficher le titre
    print() # sauter une ligne
    print(" ",'Grille de jeu') # ajout de 2 espaces pour centrer le titre sur la grille
 #2.afficher le bord supérieur
    afficher_colonnes()
 #3.afficher la grille avec les bords gauche et droit
    for i in range(1,len(p4)+1) : # on affiche d’abord la ligne supérieure
 #3.1.afficher le numéro de ligne à gauche
        print(i,end=" ")
 #3.2.afficher la ligne i
        for j in range(1,len(p4[0])+1) :
            print(p4[i-1][j-1],end="|")
        print()
        
        
def joue(p4):
    
    y = int(input("Sur quelle colonne souhaitez vous jouer? "))-1 
    while( y not in [0,1,2,3,4,5,6,7,8,9,10,11]): # permet de vérifier que la données récupérée est bien un int entre 0 et 11
       print("Mauvaise entrée, veuillez recommencer: ")
       y = int(input("Sur quelle colonne souhaitez vous jouer? "))-1
    
    actions=Actions(p4)
    colonne_complete= True
    if (y in actions):
        colonne_complete=False
    while colonne_complete: # demande au joueur de rejouer si il selectionne une colonne complète
        print("Colonne complète, veuillez recommencer: ")
        y = int(input("Sur quelle colonne souhaitez vous jouer? "))-1
        if (y in actions):
            colonne_complete=False
                
    return y
#-----------------------------------------------------------------------------#         

    
    

#-----------------------------------------------------------------------------#


def AlphaDecision(s,depth):
     
    action=Actions(s)[0]
    vMax=-1000
    for i in Actions(s) :
        
        if  Utility(Resultat(s,i,'X'))==1:# l'IA regarde directement si elle peut gagner la partie grace a un coup
            print("L'IA joue sur la colonne "+str(i+1))
            return i
    for i in Actions(s) :
        if  Utility(Resultat(s,i,'O'))==-1:# l'IA regarde si elle peut empecher l'adversaire de gagner
            print("L'IA joue sur la colonne "+str(i+1))
            return i
    for i in Actions(s) :
        temp= Resultat(s,i,'X')       
        #print('première action IA= '+str(i))
        v=Min_Value(temp,i,depth,0,-100,100)
        if(v>vMax):
            vMax=v
            
            action=i
        #print('Valeur max trouvée: '+str(vMax))
    if action==Actions(s)[0]: # Si le choix du alpha beta ne donne rien et renvoi la première case disponible ont choisi de jouer au hasard entre les colonnes 2 et 10
        action=50
        badaction=True # permet de vérifier que notre choix random ne permet pas a l'adversaire de gagner
        while action not in Actions(s) and  badaction:
            print('random choice')
            action= random.randint(2, 10)  
            test = Resultat(s,action,'X')
            if Utility(Resultat(test,action,'O'))!= -1:
                badaction=False
    print("L'IA joue sur la colonne "+str(action+1))
        
    return action

def Max_Value(s,j,depth,k,alpha,beta):
    if(Terminal_Test(s) or k==depth):
        #print(Heuristic(s,'O'))
        return Heuristic(s)
    
    maxv=float('-inf')
    
    for i in Actions(s):
        
        maxv=max(maxv,Min_Value(Resultat(s,i,'X'),i,depth,k,alpha,beta))
        if(maxv>=beta):
            return maxv
        alpha=max(alpha,maxv)
    return maxv

def Min_Value(s,j,depth,k,alpha,beta):
    if(Terminal_Test(s) or k==depth):
        #print(Heuristic(s,'X'))
        return Heuristic(s)
    minv=float('inf')
    k+=1
    for i in Actions(s):
        
        minv=min(minv,Max_Value(Resultat(s,i,'O'),i,depth,k,alpha,beta))
        if(minv<=alpha):
            return minv
        beta=min(beta,minv)
    return minv
#----------------------------------------------------------------------------#
    



def demarre () : #b fonction effectuant la structure globale d'une partie
      p4 = [[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
            [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
            [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
            [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
            [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
            [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']]  
      mode = input("Voulez-vous jouer au mode JvsJ ou IAvsJ  ? Taper 1  ou 2 : ")
      while mode not in ['1','2']: # evite les erreurs de saisie
          print("Entrée invalide: ")
          mode = input("Voulez-vous jouer au mode JvsJ, ou IAvsJ? Taper 1 ou 2 : ")
      if mode=='1': # JVJ
          afficher_grille(p4) 
          x=0
          while not Terminal_Test(p4):
              print("Tour du joueur "+str(x+1)+":")
              a=int(joue(p4))
              if x==0:
                  p4=Resultat(p4,a,'X')
              else:
                  p4=Resultat(p4,a,'O')
              afficher_grille(p4)
              x=x^1
          if Utility(p4)==0:
              print("Egalité")
          elif Utility(p4)==-1:
              print("Victoire du joueur 2")
          else:
              print("Victoire du joueur 1")
      if mode =='2': # JvIA
           x = int(input("Qui commence ? 0 pour l'IA, 1 pour le joueur"))
           while x not in [0,1]:
               x = int(input("Qui commence ? 0 pour l'IA, 1 pour le joueur"))
           
           afficher_grille(p4)
           token=0
           while not Terminal_Test(p4) and token<=42:
               print("Nombre de jetons joués :" +str(token))
               token+=1
               if x==0:
                   print("Tour de l'IA: ")
                   if token <=3: # l'IA joues ses deux premiers coups aléatoirement entre les colonnes 3 et 7
                       y= random.randint(3, 8)
                       print("L'IA joue sur la colonne "+str(y+1))
                       p4= Resultat(p4,y,'X')
                   else:
                       
                       p4= Resultat(p4,AlphaDecision(p4,2),'X')
                       
                   
                   
                   afficher_grille(p4)
               else:
                   print("Tour du joueur: ")
                   
                   a = joue(p4)
                   p4=Resultat(p4,a,'O')
                   afficher_grille(p4)
               x=x^1
           
           if Utility(p4)==-1:
               print("Victoire du joueur ")
           elif Utility(p4)==1:
               print("Victoire de l'IA")
               afficher_grille(p4)
           elif Utility(p4)==0 or token == 42:
               print("Egalité")
demarre()