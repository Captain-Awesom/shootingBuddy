# Start Date 2022.05.25
# Hours accumulated.  6
# Make a normal distribution generator. Done 2022.05.26
# Generated an Array of normally distributed random numbers. Done 2022.05.26
# Analyze a round of shooting, 30 arrows to get the statistical variables to feed into distribution. Done 2022.06.05
# Read file IO for data collection. Done 2022.06.05
# Reorganize code to proper order of operations. Done 2022.06.05
# Make outputs of numbers to mimic shooting buddy. Done 2022.06.05

# NEXT
# clean up the state machine
# add proper state exits for match play
# start making some of these calls into functions, especially for state machine




import random                                                   # IMPORT REQUIRED LIBRARIES
import statistics
from scipy.stats import norm
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

#old plot

# Creating the distribution
#data = np.arange(1, 10, 0.01)
#pdf = norm.pdf(data, loc=5.3, scale=1)

# Visualizing the distribution
#sb.set_style('whitegrid')
#sb.lineplot(x=data, y=pdf,
# color='black')
#plt.xlabel('Heights')
#plt.ylabel('Probability Density')
#plt.show()

#random_number = random.randint(1, 10)
#print(random_number)


# IO READING TO OUPUT TO AN ARRAY
df = pd.read_excel('SamData.xls', sheet_name='Indoor')          # DATAFRAME FROM .XLS FILE
exdata = [0] * df.size                                          # EMPTY ARRAY TO PLACE DATA

for i in range(0, df.shape[0], 1):                              # CYCLING THROUGH DATAFRAME AND PLACING INTO ARRAY
    exdata[3 * i] = df.at[i, 'A']                                # COLUMN A CYCLE
    exdata[(3 * i) + 1] = df.at[i, 'B']
    exdata[(3 * i) + 2] = df.at[i, 'C']

exDataMean = statistics.mean(exdata)
exDataStddev = statistics.stdev(exdata)
print("Mean ", exDataMean)
print("Std_dev ", exDataStddev)


scoreRound = np.random.normal(exDataMean, exDataStddev, size=(10, 3))       # ROUND OF 30 ARROWS CREATED

calcs = scoreRound.copy()
calcs = calcs.ravel()


#
#mu, sigma = 5, 1.5 # mean and standard deviation
#s = np.random.normal(mu, sigma, 1000)
#count, bins, ignored = plt.hist(scoreRound, 10, density=True)      #count is data, bins is number of columns
#plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) *np.exp( - (bins - mu)**2 / (2 * sigma**2) ),linewidth=2, color='r')
#plt.show()
#


size = len(calcs)
# ROUNDING SECTION FOR ARRAY ALSO CLEANS <0 AND >10
for i in range(0, len(calcs), 1):
    calcs[i] = np.round(calcs[i])                           # ROUNDING ACTION
    if calcs[i] > 10:                                       # SETS VALUES OVER 10 TO 10
        calcs[i] = 10
    if calcs[i] < 0:                                        # SETS VALUES UNDER 0 TO 0
        calcs[i] = 0


calcs = calcs.ravel()
test = scoreRound.ravel()

print("Mean diff ", statistics.mean(calcs) - statistics.mean(test))
print("Std_dev diff ", statistics.stdev(calcs) - statistics.stdev(test))

gameOn = 1
state = 1
opponentName = ''
yourScores = []
roundScores = [] * 3
dataScores = [] * 3
dataScoresIncrement = 0
opponentTotal = 0
yourTotal = 0
# state = 1 is into
# state = 2 is shooting
#
#

while gameOn > 0:
    while state == 1:
        print('Hello and welcome to shootingBuddy!')
        print('Please name your opponent.')
        opponentName = input()
        print('You will be shooting against', opponentName)
        state = 2
    while state == 2:
        print('Please input your first arrow scores.')
        roundScores.append(int(input()))
        print('Please input your second arrow scores.')
        roundScores.append(int(input()))
        print('Please input your third arrow scores.')
        roundScores.append(int(input()))
        dataScores = [10, 10, 10]
        if sum(roundScores) < sum(dataScores):
            opponentTotal = opponentTotal + 2
            print('Round over. Your score is', yourTotal, opponentName, 'score is', opponentTotal)
            roundScores = [] * 3
        if sum(roundScores) > sum(dataScores):
            yourTotal = yourTotal + 2
            print('Round over. Your score is', yourTotal, opponentName, 'score is', opponentTotal)
            roundScores = [] * 3
        if sum(roundScores) == sum(dataScores):
            opponentTotal = opponentTotal + 1
            yourTotal = yourTotal + 1
            print('Round over. Your score is', yourTotal, opponentName, 'score is', opponentTotal)
            roundScores = [] * 3
        if yourTotal > 5:
            print('You win!')
        if opponentTotal > 5:
            print(opponentName, ' wins!')
            gameOn = 0
            state = 0
        if (yourTotal == 6) & (opponentTotal == 6):
            print('It''s a tie!!!!!')