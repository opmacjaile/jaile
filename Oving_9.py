# -*- coding: utf-8 -*-
"""
Created on Fri Nov  5 09:03:27 2021

@author: Jaile
"""



class Quiz:
    def __init__(self, questions, answer, alternatives):
        self.questions = questions
        self.alternatives = alternatives
        self.answer = answer
        
    def __str__(self):
        questions = f"{self.questions}\n\n"
        for alt in range(len(self.alternatives)):
            questions += f"{alt}.{self.alternatives[alt]}\n"
        return "\n" + questions
    
    
    def test_answer(self, player1_answer, player2_answer):
        if str(self.answer [0][1]) == str(player1_answer):
            print(f"{player1} result: corret")
            
        else:        
            print(f"{player1} result: wrong")
            
        if str(self.answer [0][1]) == str(player2_answer):
             print(f"{player2} result: corret")
             print("\n")
             
        else:
            print(f"{player2} result: wrong")
            print("\n")
            
        print("correct asnwer is: " + self.answer[0][1])
        return (str(self.answer [0][1]) == str(player1_answer), str(self.answer [0][1]) == str(player2_answer))
           
            
    
def read_file():
    
    with open("sporsmaalsfil.txt", "r", encoding="UTF8") as csvfile: 
    
        objects = list()
        
        for linje in csvfile:
        
            ele = linje.split(":")
            questions = ele[0]
            answer = ele[1].split(":")
            alternatives = ele[2].strip("[] \n").split(", ")
            
            objects.append(Quiz(questions, answer, alternatives))
            
        return objects
            
            
            
        
                
if __name__ == "__main__":
    player_1 = input("your name: ")
    player1 = player_1
    player_2 = input("your name: ")
    player2 = player_2
    player1_score = 0
    player2_score = 0 
    objects = read_file()
    
    
    for quest_ions in objects:
        print(str(quest_ions))
        
        player1_answer = int(input(f"{player1} answer: "))
        
        player2_answer = int(input(f"{player2} answer: "))
        
        print("\n")

        plyr1, plyr2 = quest_ions.test_answer(player1_answer, player2_answer)   

        if plyr1:
            player1_score += 1
            
        
        
            
        if plyr2:
            player2_score += 1
            

            
        print("\n")
        
        print(f"{player1} you have {player1_score} correct of {len(objects)} ")
        print(f"{player2} you have {player2_score} correct of {len(objects)} \n")
        
        print(f"score board:\n {player1}: {player1_score} \n {player2}: {player2_score}")
        
        print("\n")
        