import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''


paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''


scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
list = [rock, paper, scissors] 
# kámen tupí nůžky, papír balí kámen, nužký stříhají papír
beats = {
    scissors: rock,
    rock: paper,
    paper: scissors
} 

# počítadlo score
user_score = 0
comp_score = 0
score = [user_score, comp_score]

while score[0] or score[1]  <= 3:
    # vybírá hráč
    user_number = int(input("Co si vyberete? Napište 0 pro kámen, 1 pro papír, 2 pro nůžky\n"))
    if user_number > 2: # když zadá spatné číslo vrátí ho to o krok zpátky
        user_number = int(input("Tomu nerozumím. Napište 0 pro kámen, 1 pro papír, 2 pro nůžky\n"))
    else: # když zadá jednu ze 3 možností pokračuje
        user_pick = list[user_number]
        print(f"Uživatel vybral:\n{user_pick}")

        # vybírá počítač
        comp_number = random.randint(0, len(list)-1)
        comp_pick = list[comp_number]
        print(f"počítač vybral:\n{comp_pick}")

        #podmínky pro určení vítěze
        if user_pick == comp_pick:
            print("remíza")
        elif user_pick == beats[comp_pick]:
            score[0] += 1
            print("Vyhrál jsi")
        else:
            score[1] += 1
            print("Prohrál jsi. Počítač vyhrál")

        print(score)
    