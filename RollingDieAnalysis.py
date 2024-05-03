import random
# rolling a die 6 times and reporting the outcomes
outcome = []
ones = 0
twos = 0
three = 0
four = 0
five = 0
six = 0

print("Experiment to analyse the theoretical and practical outcomes of rolling a die 6 Times")
print("Outcomes:")

for i in range(6):
    dice = random.randint(1, 6)
    outcome.append(dice)
    if dice == 1:
        ones += 1
    elif dice == 2:
        twos += 1
    elif dice == 3:
        three += 1
    elif dice == 4:
        four += 1
    elif dice == 5:
        five += 1
    elif dice == 6:
        six += 1


print(outcome)
print("1s: ",ones)
print("2s: ",twos)
print("3s: ",three)
print("4s: ",four)
print("5s: ",five)
print("6s: ",six)

prob = 1/6
prob1 = ones/6
prob2 = twos/6
prob3 = three/6
prob4 = four/6
prob5 = five/6
prob6 = six/6

print("Theoretical probability of ONE:  ",prob,"actual probability",prob1)
print("Theoretical probability of TWO:  ",prob,"actual probability",prob2)
print("Theoretical probability of THREE:",prob,"actual probability",prob3)
print("Theoretical probability of FOUR: ",prob,"actual probability",prob4)
print("Theoretical probability of FIVE: ",prob,"actual probability",prob5)
print("Theoretical probability of SIX:  ",prob,"actual probability",prob6)

prob_d1 = abs(prob - prob1)
prob_d2 = abs(prob - prob2)
prob_d3 = abs(prob - prob3)
prob_d4 = abs(prob - prob4)
prob_d5 = abs(prob - prob5)
prob_d6 = abs(prob - prob6)
print()
print("Probability difference for one:  ",prob_d1)
print("Probability difference for two:  ",prob_d2)
print("Probability difference for three:",prob_d3)
print("Probability difference for four: ",prob_d4)
print("Probability difference for five: ",prob_d5)
print("Probability difference for six:  ",prob_d6)

print()
avg_prob = (prob_d1+prob_d2+prob_d3+prob_d4+prob_d5+prob_d6)
print("Average Probability difference:",avg_prob)