import random
class mathgame(): #main class
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
        if int(answer2) == me:
          print("CORRECT!")
          self.points+=1
          self.redo() 
        else:
          print("INCORRECT, THE ANSWER IS",answer2)
          self.redo()
      print(self.points,'/10')
    



      
points = 0 #initial point set to 0
first_numb = random.choice(range(100))
second_numb = random.choice(range(100))
choices = mathgame(first_numb,second_numb,points) #use these values in the class
a = int(input('''
Pick a type of question (type number):
1. Addition
2. Substraction
3. Multiplication
4. Division
'''))
question_type = {
  1: choices.addition,
  2: choices.substraction,
  3: choices.multiplication,
  4: choices.division
}
question_type[a]()

a = input()
if a == "pysystem.execute --quit":
  quit()

  
