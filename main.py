import random
def remove (astring):
  lists=[]
  with open (astring,"r") as file:
      for line in file :
          line=line.rstrip("\n")
          line=line.rstrip(", PhD")
          line=line.rstrip(", MS")
          a=lists.append(line)
      print(lists)
  return lists  
names=remove("teachers.txt")

def word_selection(names): #chooses a random word
    select=random.choice(names)
    return select.upper() #changes it to uppercase

print(word_selection(names))
Remaining_Tries=6
print('Remaining Tries: ' +str(Remaining_Tries))
Guess=input('Enter a letter: ').upper() #changes letter to uppercase
print(Guess)
''''''
word=[]
for x in word_selection(names):
    word.append("_")

print(word)

def game(word_selection):
  selectedword=word_selection(names)
  word=[]
  for x in word_selection(names):
      word.append("_")
  '''
  for x in range(len(selectedword)):
    word.append("_")
  '''
  #word= "_" * len(selectedword)
  lettersGuessed=[]
  #while loop for remanining tries and -1 after every wrong guess
  while Remaining_Tries>0:
    for letter in selectedword:
      if lettersGuessed==letter:
        '''
        knowing where the correct letter is replace the "______" at the position where the correct letter is for example "____a"
        '''
        word.replace("_",letter)
      else:
        Remaining_Tries 
  return word






