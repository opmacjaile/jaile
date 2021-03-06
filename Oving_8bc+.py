# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 13:17:51 2021

@author: Jaile
"""



class Quiz:
    def __init__(self, questions, answer, alternatives):
        self.questions = questions
        self.alternatives = alternatives
        self.answer = answer
        
    def __str__(self):
        questions = f"{self.questions}\n\n"
        for alt in self.alternatives:
            questions += f"{all}\n"
        return questions
    
    
    def test_answer(self, user_answer):
        if str(user_answer) == str(self.answer[0][1]):
            return True
            
        else:        
            
            return False
            
           
            
    
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
        
        player_1 = input(f"{player1} answer: ")
        if quest_ions.test_answer(player_1):
            print("correct")
            player1_score += 1
            
        else:
            print("correct answer")
        
        print(f" you have {player1_score} correct of {len(objects)} ")
            
            
        player_2 = input(f"{player2} answer: ")
        if quest_ions.test_answer(player_2):
            print("correct")
            player2_score += 1
            
        else:
            print("wrong answer")
            
        print(f" you have {player2_score} correct of {len(objects)} \n")
            
        print(f"score board:\n {player1}: {player1_score} \n {player2}: {player2_score}")
        print("\n \n")
    
    












