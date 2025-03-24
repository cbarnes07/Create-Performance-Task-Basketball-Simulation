import pandas as pd
pd.set_option('display.max_columns', None)
pd.set_option('display.max_colwidth', 0)

print('NBA All Star Game (Redo)')
print ('Pick a Team and Start Drafting')
teams = ['Team Lebron', 'Team Durant']

for a, b in enumerate(teams, 1):
  print ('{} {}'.format(a, b))

number1 = int(input('Number:'))



# Read in Dataframe
mydata = pd.read_csv('allstar.csv')

newplayers = []
cpuplayers = []

numstartplayers = mydata['FULL NAME'].to_list()

#Contains following players: Joel Embiid, Giannis Antetokounmpo, Stephen Curry,DeMar DeRozan, Ja Morant, Jayson Tatum, Trae Young, Andrew Wiggins, Nikola Jokic.

import random
import time
time.sleep(1)

if number1 == 1:
  print('\nPick a Player')
  newplayers.append(numstartplayers[4])
  del numstartplayers[4]
  for a, b in enumerate(numstartplayers, 1):
    print ('{} {}'.format(a, b))
  for startplayer in numstartplayers:    
    number2 = int(input('Player:'))
    number3 = number2 - 1
    team = numstartplayers[number3]
    newplayers.append(team)
    del numstartplayers[number3]
    import time
    time.sleep(1)
    rchoice = random.choice(numstartplayers)
    print(f'\nTeam Durant picks',             
rchoice + '.')
    cpuplayers.append(rchoice)
    numstartplayers.remove(rchoice)
    time.sleep(1)
    print('\nPick a Player')
    for a, b in enumerate(numstartplayers, 1):
      print ('{} {}'.format(a, b))
    
  remaining = numstartplayers
  number6 = int(input('Player:'))
  number7 = number6 - 1
  team3 = numstartplayers[number7]
  newplayers.append(team3)
  del numstartplayers[number7]
  schoice = random.choice(numstartplayers)
  take = schoice
  cpuplayers.append(take)
  numstartplayers.remove(take)
  time.sleep(1)
  print(f'\nTeam Durant picks', schoice + '.')
  time.sleep(1)
  tchoice = random.choice(numstartplayers)
  remove3 = tchoice
  numstartplayers.remove(remove3)
  print(f'Team Durant picks', tchoice + '.')
  time.sleep(1)
  cpuplayers.append(remove3)
  print('\nTeam Lebron:')

if number1 == 2:
  cpuplayers.append(numstartplayers[4])
  del numstartplayers[4]
  l2choice = random.choice(numstartplayers)
  print(f'\nTeam Lebron picks',             
l2choice + '.')
  cpuplayers.append(l2choice)
  time.sleep(1)
  remove = l2choice
  numstartplayers.remove(remove)
  print('\nPick a Player')
  for a, b in enumerate(numstartplayers, 1):
    print ('{} {}'.format(a, b))
  for startplayer in numstartplayers:    
    number4 = int(input('Player:'))
    number5 = number4 - 1
    newplayers.append(numstartplayers[number5])
    team = numstartplayers[number5]
    del numstartplayers[number5]
    import time
    time.sleep(1)
    l3choice = random.choice(numstartplayers)
    print(f'\nTeam Lebron picks',             
l3choice + '.')
    cpuplayers.append(l3choice)
    numstartplayers.remove(l3choice)
    time.sleep(1)
    print('\nPick a Player')
    time.sleep(1)
    for a, b in enumerate(numstartplayers, 1):
      print ('{} {}'.format(a, b))
  time.sleep(1)
  l4choice = random.choice(numstartplayers)
  print('\nYou (Team Durant) get', l4choice,  'and...')
  newplayers.append(l4choice)
  numstartplayers.remove(l4choice)
  time.sleep(2)
  l5choice = random.choice(numstartplayers)
  print('You (Team Durant) get', l5choice + '.')
  numstartplayers.remove(l5choice)
  newplayers.append(l5choice)
  time.sleep(1)
  print('\nTeam Durant:')

mydata = pd.read_csv('allstar.csv')

newplayers = pd.DataFrame(newplayers, columns=['FULL NAME']) #Turn list into dataframe
newplayerstats = newplayers.merge(mydata)
print(newplayerstats.to_string())
print('\nOpposing Team:')
cpuplayers = pd.DataFrame(cpuplayers, columns=['FULL NAME']) #Turn list into dataframe
cpuplayerstats = cpuplayers.merge(mydata)
print(cpuplayerstats.to_string())

time.sleep(1)
print('')

def final_score(team): 
  freethrow = random.randint(10,15)
  twopoint = random.randint(70,90)
  threepoint = random.randint(60,80)
  ftamount = round(freethrow/5 * team['FT%'])
  twopamount = round(twopoint/5 * team['2P%'])*2
  threepamount = round(threepoint/5 * team['3P%'])*3
  team['score'] = ftamount+twopamount+threepamount
  for player,score in zip(team['FULL NAME'],team['score']):
    time.sleep(0.7)
    print(player, 'scored', score,'points.')
  print('\nFinal Score:', int(team['score'].sum()))
  time.sleep
  if int(team['score'].sum()) <= 175:
    print('That\'s a normal All-Star Game score.')
  else:
    print('That\'s a high All-Star Game score.')
    
time.sleep(0.7)
print('\nYour Team\'s Stats and Score')  
print('--------------------------------------')
final_score(newplayerstats)
print('\nThe Opposing Team\'s Stats and Score')
print('--------------------------------------')
final_score(cpuplayerstats)

if newplayerstats['score'].sum() > cpuplayerstats['score'].sum():
  print('\nCongrats, you have won the All-Star Game!')
elif newplayerstats['score'].sum() == cpuplayerstats['score'].sum():
  print('\nYou Tied.')
else:
  print('\nYou lost, better luck next year.')


