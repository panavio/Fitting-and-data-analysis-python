import random

score=0

#monty hall problem
for i in range(100000):
    l_choice=[0,1,2]
    l=[0,1,2]
    choice=random.randint(0,2)
    prize=random.randint(0,2)
    l_choice.remove(prize)
    if choice==prize:
        b=random.choice(l_choice)
    else:
        l_choice.remove(choice)
        b=l_choice[0]
    l.remove(b)
    l.remove(choice)
    if l[0]==prize:
        score+=1
    else:
        score+=0


print(score/1000)


import random

def monty_hall_simulation(num_trials):
    stay_win_count = 0
    switch_win_count = 0

    for _ in range(num_trials):
        # Doors setup
        doors = [0, 0, 1]  # 0 represents a goat, 1 represents the car
        random.shuffle(doors)

        # Contestant's initial choice
        contestant_choice = random.randrange(3)

        # Monty opens a door with a goat behind it
        remaining_closed_doors = [i for i in range(3) if i != contestant_choice and doors[i] == 0]
        door_opened_by_monty = random.choice(remaining_closed_doors)

        # Switch or stay strategy
        switch_choice = [i for i in range(3) if i != contestant_choice and i != door_opened_by_monty][0]

        # Check wins
        if doors[contestant_choice] == 1:
            stay_win_count += 1
        if doors[switch_choice] == 1:
            switch_win_count += 1

    stay_win_prob = stay_win_count / num_trials
    switch_win_prob = switch_win_count / num_trials

    print(f"Stay strategy win rate: {stay_win_prob * 100:.2f}%")
    print(f"Switch strategy win rate: {switch_win_prob * 100:.2f}%")

monty_hall_simulation(10000)  # You can adjust the number of trials as needed
