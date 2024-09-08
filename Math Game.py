import random
import os

class mathgame: #main class
    class arithmetics(): #arithmetic class
      def __init__(self, first_numb, second_numb, points): #instances for first and second number as well as the points
        self.first_numb = first_numb
        self.second_numb = second_numb
        self.points = points
      def redo(self): #Function called when you want to pick another 2 numbers
        self.first_numb = random.choice(range(100))
        self.second_numb = random.choice(range(100)) 
        
      def addition(self): #addition function
        for x in range(10):
          
          print(self.first_numb,'+',self.second_numb)
          answer = self.first_numb + self.second_numb
          me = int(input())
          os.system('clear')
          if answer == me:
            print("CORRECT!")
            self.points+=1
            self.redo()
           
          else:
            print("INCORRECT, THE ANSWER IS",answer)
            self.redo()
   
          
        print(self.points,'/10')
      def substraction(self):
        for x in range(10):
          print(self.first_numb,'-',self.second_numb)
          answer = self.first_numb - self.second_numb
          me = int(input())
          os.system('clear')
          if answer == me:
            print("CORRECT!")
            self.points+=1
            self.redo() 
          else:
            print("INCORRECT, THE ANSWER IS",answer)
            self.redo()
        print(self.points,'/10')
      def multiplication(self):
          for x in range(10):
            print(self.first_numb,'*',self.second_numb)
            answer = self.first_numb * self.second_numb
            me = int(input())
            os.system('clear')
            if answer == me:
              print("CORRECT!")
              self.points+=1
              self.redo() 
            else:
              print("INCORRECT, THE ANSWER IS",answer)
              self.redo()
          print(self.points,'/10')
    
      def division(self):
          for x in range(10):
            answer1 = self.first_numb * self.second_numb
            answer2 = answer1/self.second_numb
            print(answer1,'/',self.second_numb)
            me = int(input())
            os.system('clear')
            if int(answer2) == me:
              print("CORRECT!")
              self.points+=1
              self.redo() 
            else:
              print("INCORRECT, THE ANSWER IS",answer2)
              self.redo()

          
    class quadratics(): #arithmetic class
      def __init__(self, b, c, d, points): #instances for b,c and d, and the points
          self.b = b
          self.c = c
          self.d = d
          self.points = points
      def redo(self): #Function called when you want to other values
          self.b = random.choice(range(1,5))
          self.c = random.choice(range(1,5))
          self.d = random.choice(range(1,5))
      
      def quad(self):
          for x in range(10):
              print(self.b, 'x^2 +', (self.b*self.c)+(self.b*self.d), 'x+', (self.b*self.c*self.d))
              answer = str(-self.c) + ',' + str(-self.d)
              answer2 = str(-self.d) + ',' + str(-self.c)
              me = input()
              print("Clearing the screen...")  # Debug print
              os.system('clear')  # Clear the screen
              if answer == me or answer2 == me:
                  print("CORRECT!")
                  self.points += 1
                  self.redo()
              else:
                  print("INCORRECT, THE ANSWER IS", answer)
                  self.redo()
                
          print(self.points, '/10')           
                  
        

      

a = int(input('''
Pick a type of question (type number):
1. Arithmetic
2. Quadratics (Find the zeroes)
'''))

points = 0 #initial point set to 0
if a == 1:
    first_numb = random.choice(range(100)) #Pick a number between 0 and 99
    second_numb = random.choice(range(100)) #Pick a second number between 0 and 99
    choices = mathgame.arithmetics(first_numb,second_numb,points) #use these values in the class
    
    b = int(input('''
Pick a type of arithmetic question (type number):
1. Addition
2. Substraction
3. Multiplication
4. Division
''')) #Pick the type of arithmetic questions
    
    answers = {
        1: choices.addition,
        2: choices.substraction,
        3: choices.multiplication,
        4: choices.division
        } #Type of class chosen

    
    answers[b]() #function 
elif a==2: #if want the quadratic questions
    # bx^2 + cx + d
    b = random.choice(range(1,5))
    c = random.choice(range(1,5))
    d = random.choice(range(1,5))
    print("Seperate the zeroes with a comma")
    mathgame.quadratics(b,c,d,points).quad() #use these values in the class

    
    
    
    
    

  
