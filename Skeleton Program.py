# Skeleton Program code for the AQA COMP1 Summer 2014 examination
# this code should be used in conjunction with the Preliminary Material
# written by the AQA Programmer Team
# developed in the Python 3.2 programming environment
# version 2 edited 06/03/2014
#04/04/14 Task one started
#04/04/14 Task one completed
#04/04/14 Task two started
#04/04/14 Task two completed
#xx/04/14 Task three started
#xx/04/14 Task three completed
#28/04/14 Task four started
#28/04/14 Task four completed
#29/04/14 Task five started
#02/04/14 Task five completed
#02/04/14 Task six started
#16/05/14 Task six completed
#16/05/14 Task seven started

import random
from datetime import date
import pdb

aceHigh = False
NO_OF_RECENT_SCORES = 3

class TCard():
  def __init__(self):
    self.Suit = 0
    self.Rank = 0

class TRecentScore():
  def __init__(self):
    self.Name = 'N/A'
    self.Score = 0
    self.Date = None

Deck = [None]
RecentScores = [None]
Choice = ''

def GetRank(RankNo):
  Rank = ''
  if RankNo == 1 or RankNo == 14:
    Rank = 'Ace'
  elif RankNo == 2:
    Rank = 'Two'
  elif RankNo == 3:
    Rank = 'Three'
  elif RankNo == 4:
    Rank = 'Four'
  elif RankNo == 5:
    Rank = 'Five'
  elif RankNo == 6:
    Rank = 'Six'
  elif RankNo == 7:
    Rank = 'Seven'
  elif RankNo == 8:
    Rank = 'Eight'
  elif RankNo == 9:
    Rank = 'Nine'
  elif RankNo == 10:
    Rank = 'Ten'
  elif RankNo == 11:
    Rank = 'Jack'
  elif RankNo == 12:
    Rank = 'Queen'
  elif RankNo == 13:
    Rank = 'King'
  return Rank

def GetSuit(SuitNo):
  Suit = ''
  if SuitNo == 1:
    Suit = 'Clubs'
  elif SuitNo == 2:
    Suit = 'Diamonds'
  elif SuitNo == 3:
    Suit = 'Hearts'
  elif SuitNo == 4:
    Suit = 'Spades'
  return Suit

def DisplayMenu():
  print()
  print('MAIN MENU')
  print()
  print('1. Play game (with shuffle)')
  print('2. Play game (without shuffle)')
  print('3. Display recent scores')
  print('4. Reset recent scores')
  print("5. Options")
  print()
  print('Select an option from the menu (or enter q to quit): ', end='')

#Task 2
def GetMenuChoice():
  Choice = input()
  if Choice.lower() not in ["1","2","3","4","5","q","quit"]:
    Choice = "f"
  print()
  return Choice[0].lower()

def LoadDeck(Deck):
  CurrentFile = open('deck.txt', 'r')
  Count = 1
  while True:
    LineFromFile = CurrentFile.readline()
    if not LineFromFile:
      CurrentFile.close()
      break
    Deck[Count].Suit = int(LineFromFile)
    LineFromFile = CurrentFile.readline()
    if aceHigh == True:
      Deck[Count].Rank = int(LineFromFile)
      if Deck[Count].Rank == 1:
        Deck[Count].Rank = 14
    else:
      Deck[Count].Rank = int(LineFromFile)
    Count = Count + 1
 
def ShuffleDeck(Deck):
  SwapSpace = TCard()
  NoOfSwaps = 1000
  for NoOfSwapsMadeSoFar in range(1, NoOfSwaps + 1):
    Position1 = random.randint(1, 52)
    Position2 = random.randint(1, 52)
    SwapSpace.Rank = Deck[Position1].Rank
    SwapSpace.Suit = Deck[Position1].Suit
    Deck[Position1].Rank = Deck[Position2].Rank
    Deck[Position1].Suit = Deck[Position2].Suit
    Deck[Position2].Rank = SwapSpace.Rank
    Deck[Position2].Suit = SwapSpace.Suit

def DisplayCard(ThisCard):
  print()
  print('Card is the', GetRank(ThisCard.Rank), 'of', GetSuit(ThisCard.Suit))
  print()

def GetCard(ThisCard, Deck, NoOfCardsTurnedOver):
  ThisCard.Rank = Deck[1].Rank
  ThisCard.Suit = Deck[1].Suit
  for Count in range(1, 52 - NoOfCardsTurnedOver):
    Deck[Count].Rank = Deck[Count + 1].Rank
    Deck[Count].Suit = Deck[Count + 1].Suit
  Deck[52 - NoOfCardsTurnedOver].Suit = 0
  Deck[52 - NoOfCardsTurnedOver].Rank = 0

def IsNextCardHigher(LastCard, NextCard):
  Higher = False
  if NextCard.Rank > LastCard.Rank:
    Higher = True
  return Higher

#Task 3
def GetPlayerName():
  valid = False
  print()
  while not valid:
    PlayerName = input('Please enter your name: ')
    if len(PlayerName) >= 1:
      valid = True
    else:
      print("You must enter something for your name!")
  print()
  return PlayerName

#Task 1
def GetChoiceFromUser():
  Choice = input('Do you think the next card will be higher than the last card (enter y or n)? ')
  if Choice.lower() not in ["y","yes","n","no"]:
    Choice = "f"
  return Choice[0].lower()

def DisplayEndOfGameMessage(Score):
  print()
  print('GAME OVER!')
  print('Your score was', Score)
  if Score == 51:
    print('WOW! You completed a perfect game.')
  print()

def DisplayCorrectGuessMessage(Score):
  print()
  print('Well done! You guessed correctly.')
  print('Your score is now ', Score, '.', sep='')
  print()

def ResetRecentScores(RecentScores):
  for Count in range(1, NO_OF_RECENT_SCORES + 1):
    RecentScores[Count].Name = ''
    RecentScores[Count].Score = 0

def BubbleSortScores(RecentScores):
  done = False
  step = NO_OF_RECENT_SCORES + 2
  while not done:
    step -= 1
    for i in range(1, step):
      if RecentScores[i].Score < RecentScores[i+1].Score:
        temp = RecentScores[i]
        temp1 = RecentScores[i+1]
        RecentScores[i] = temp1
        RecentScores[i+1] = temp
        
#Task4 #Task5
def DisplayRecentScores(RecentScores):
  nameSpace = 4
  scoreSpace = 5
  dateSpace = 8
  print()
  print('Recent Scores: ')
  print()
  for Count in range(1, NO_OF_RECENT_SCORES + 1):
    if len(RecentScores[Count].Name) > nameSpace:
      nameSpace = len(RecentScores[Count].Name)
    if len(str(RecentScores[Count].Score)) > scoreSpace:
      scoreSpace = len(str(RecentScores[Count].Score))
  print("{0:<{1}} {2:<{3}} {4:<{5}}".format("Name",nameSpace,"Score",scoreSpace,"Date",dateSpace))
  for Count in range(1, NO_OF_RECENT_SCORES + 1):
    if RecentScores[Count].Date != None:
      scoreTime = RecentScores[Count].Date.strftime("%y/%m/%d")
    else:
      scoreTime = "N/A"
    print("{0:<{1}} {2:<{3}} {4:<{5}}".format(RecentScores[Count].Name,nameSpace,RecentScores[Count].Score,scoreSpace,scoreTime,dateSpace))
  print()
  print('Press the Enter key to return to the main menu')
  input()
  print()

#Task 4
def UpdateRecentScores(RecentScores, Score):
  valid = False
  while not valid:
    appeScore = input("Do you wish to add your score to the high score table (y or n): ")
    if appeScore.lower()[0] in ["y","n"]:
      valid = True
    else:
      print("Choice not valid.")
  if appeScore == "y":
    PlayerName = GetPlayerName()
    FoundSpace = False
    Count = 1
    while (not FoundSpace) and (Count <= NO_OF_RECENT_SCORES+1):
      if RecentScores[Count].Name == 'N/A':
        FoundSpace = True
      else:
        Count = Count + 1
    if not FoundSpace:
      for Count in range(1, NO_OF_RECENT_SCORES+1):
        RecentScores[Count].Name = RecentScores[Count + 1].Name
        RecentScores[Count].Score = RecentScores[Count + 1].Score
      Count = NO_OF_RECENT_SCORES
    RecentScores[Count].Name = PlayerName
    RecentScores[Count].Score = Score
    RecentScores[Count].Date = date.today()
#+--------------------------------------------------------------------------+
#Task 6
def DisplayOptions():
  print()
  print()
  print("OPTION MENU")
  print()
  print("1. Set Ace to be HIGH or LOW")
  print()

def GetOptionChoice():
  valid = False
  while not valid:
    OptionChoice = input('Select an option from the menu (or enter q to quit): ')
    if OptionChoice[0].lower() not in ["1","q"]:
      print("Choice not valid!")
    else:
      valid = True
  return OptionChoice[0].lower()

def SetOptions(OptionChoice):
  if OptionChoice == "1":
    SetAceHighOrLow()
  if OptionChoice == "q":
    DisplayMenu()
    Choice = GetMenuChoice()

def SetAceHighOrLow():
  global aceHigh
  valid = False
  while not valid:
    highOrLow = input("Do you want the Ace to be (h)igh or (l)ow (or enter q to quit): ")
    if highOrLow[0].lower() not in ["h","l","q"]:
      print("Choice not valid!")
    else:
      valid = True
  if highOrLow[0].lower() == "q":
    DisplayMenu()
    Choice = GetMenuChoice()
  elif highOrLow[0].lower() == "h":
    aceHigh = True
  elif highOrLow[0].lower() == "l":
    aceHigh = False
#+--------------------------------------------------------------------------+  

def PlayGame(Deck, RecentScores):
  LastCard = TCard()
  NextCard = TCard()
  GameOver = False
  GetCard(LastCard, Deck, 0)
  DisplayCard(LastCard)
  NoOfCardsTurnedOver = 1
  while (NoOfCardsTurnedOver < 52) and (not GameOver):
    GetCard(NextCard, Deck, NoOfCardsTurnedOver)
    Choice = ''
    while (Choice != 'y') and (Choice != 'n'):
      Choice = GetChoiceFromUser()
    DisplayCard(NextCard)
    NoOfCardsTurnedOver = NoOfCardsTurnedOver + 1
    Higher = IsNextCardHigher(LastCard, NextCard)
    if (Higher and Choice == 'y') or (not Higher and Choice == 'n'):
      DisplayCorrectGuessMessage(NoOfCardsTurnedOver - 1)
      LastCard.Rank = NextCard.Rank
      LastCard.Suit = NextCard.Suit
    else:
      GameOver = True
  if GameOver:
    DisplayEndOfGameMessage(NoOfCardsTurnedOver - 2)
    UpdateRecentScores(RecentScores, NoOfCardsTurnedOver - 2)
  else:
    DisplayEndOfGameMessage(51)
    UpdateRecentScores(RecentScores, 51)

if __name__ == '__main__':
  for Count in range(1, 53):
    Deck.append(TCard())
  for Count in range(1, NO_OF_RECENT_SCORES + 1):
    RecentScores.append(TRecentScore())
  Choice = ''
  while Choice != 'q':
    DisplayMenu()
    Choice = GetMenuChoice()
    if Choice == '1':
      LoadDeck(Deck)
      ShuffleDeck(Deck)
      PlayGame(Deck, RecentScores)
    elif Choice == '2':
      LoadDeck(Deck)
      PlayGame(Deck, RecentScores)
    elif Choice == '3':
      DisplayRecentScores(RecentScores)
    elif Choice == '4':
      ResetRecentScores(RecentScores)
    elif Choice == "5":
      DisplayOptions()
      OptionChoice = GetOptionChoice()
      SetOptions(OptionChoice)
