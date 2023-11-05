import pygame

pygame.init()


white = (255, 255, 255)
purple = (255, 192, 203)
black = (0, 0, 0)


X = 400
Y = 400


display_surface = pygame.display.set_mode((X, Y))


pygame.display.set_caption('Professor Hangman!')


font = pygame.font.Font(None, 100)


text = font.render('THE END!!!!', True, purple, black)


textRect = text.get_rect()

textRect.center = (X // 2, Y // 2)
import random

def remove (astring):
  lists=[]
  with open (astring,"r") as file:
      for line in file :
          line=line.rstrip("\n")
          line=line.rstrip(", PhD")
          line=line.rstrip(", MS")
          a=lists.append(line)
      # print(lists)
  return lists  
names=remove("teachers.txt")

def word_selection(names): #chooses a random word
    select=random.choice(names)
    return select .upper() #changes it to uppercase
#name=word_selection(names)
#print(name)



    # word.append("_")

#print(word)
Remaining_Tries=6
print('Remaining Tries: ' +str(Remaining_Tries))
print('Note: Guess a space first')

def game():
  selectedword=word_selection(names)
  word= ["_"] * len(selectedword)
  #print(selectedword)
  print(word)
  lettersGuessed=[]
  #while loop for remanining tries and -1 after every wrong guess
  global Remaining_Tries
  while Remaining_Tries>0:
    print('Remaining Tries: ' +str(Remaining_Tries))
    Guess=input('Enter a letter: ').upper() #changes letter to uppercase
    print(Guess)
    if Guess not in selectedword:
       #if letter wrong
       Remaining_Tries=Remaining_Tries-1
    for index,letter in enumerate(selectedword):
      if Guess==letter:
        '''
        knowing where the correct letter is replace the "______" at the position where the correct letter is for example "____a"
        '''
        word[index]=Guess


    print(word)
  return selectedword

print(game())


while True:


    display_surface.fill(white)


    display_surface.blit(text, textRect)


    for event in pygame.event.get():

     
        if event.type == pygame.QUIT:

       
            pygame.quit()


            quit()

        pygame.display.update()

