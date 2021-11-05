# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 14:53:57 2021

@author: Jaile
"""





with open("sporsmaalsfil.txt", "r", encoding="UTF8") as csvfile:      
    
    
    
    count = 0
    
    questions = []

    answers = []
    
    alternatives = []


    
    for linje in csvfile:
        
            
        elementer = linje.split(":")
        questions.append(elementer[0])
        answers.append(elementer[1])
        alternatives.append(elementer[2])
    
        
        count += 1
        
        
        
print(linje)
        
        
        
        
        
        
        
        
        