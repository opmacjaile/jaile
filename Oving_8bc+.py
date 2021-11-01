# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 13:17:51 2021

@author: Jaile
"""



class Quiz:
    def __init__(self, questions, alternatives, answer):
        self.questions = questions
        self.alternatives = alternatives
        self.answer = answer
        
    def __str__(self):
        question_structure = f"spørsmålet er: {self.questions} \n 1.{self.alternatives[0]} \n 2.{self.alternatives[1]} \n 3.{self.alternatives[2]} "
        return question_structure
    
    
    def test_answer(self, user_answer):
        if self.answer == user_answer:
            
            
            print("correct answer")
            
        else:
            print("wrong answer")
                
if __name__ == "__main__":

    questions = "how fast is the speed of light?"
    alternatives = ["300 000km/s", "300 000m/s", "3 000 000m/s"]
    answer = 1

    quiz = Quiz(questions, alternatives, answer)
    print(quiz)
    user_answer = int(input("what is the correct answer hole number:"))
    quiz.test_answer(user_answer)
    
    
    
    questions = "What is the capital of Australia?"
    alternatives = ["Sydney", "Canberra", "Melbourne"]
    answer = 2
    
    quiz = Quiz(questions, alternatives, answer)
    print(quiz)
    user_answer = int(input("what is the correct answer hole number:"))
    quiz.test_answer(user_answer)
    
    
    
    questions = "what is the average weight of a blue whale?"
    alternatives = ["140 tons", "30 tons", "75 tons"]
    answer = 1
    
    quiz = Quiz(questions, alternatives, answer)
    print(quiz)
    user_answer = int(input("what is the correct answer hole number:"))
    quiz.test_answer(user_answer)


