# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 13:54:27 2023

@author: HP
"""


d={1:'Onion',2:'Lettuce',3:'Tomato',4:'Olives',5:'Peppers'}
per_cost=5

while True:
    
    print("Chose three Toppings \n1.Onion \n2.Lettuce \n3.Tomato \n4.Olives \n5.Peppers \n")
    toping=input("Input only three different value from 1 to 5 \nUse space as seperator: ")
    try:
        a,b,c=toping.split(" ")
        a,b,c=int(a),int(b),int(c)
        if a!=b and a!=c and b!=c:
            if a>=1 or a<=5 and b>=1 or b<=5 and c>=1 or c<=5 :
                break
    except:
        print("\n\nInvalid Input\n\n")
    
        

how_many=int(input("Input number of Sandwiches you want:"))
total_cost =5*how_many
# print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))
print(f'\\n\n\nTopings you selected:\t{d[a], d[b], d[c]}\nQuantity:\t{how_many}\nTotal Cost:\t{total_cost}')