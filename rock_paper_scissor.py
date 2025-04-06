''' Rock Paper Scissors '''
import random 
print("Welcome to Rock Paper Scissors!")

while True:
    player_sel = input("Enter, Rock 'r', Paper 'p', or Scissors 's': ").lower()

    sel_list = ['r', 'p', 's']
    cpu_sel = random.choice(sel_list)

    if player_sel == cpu_sel:
        print("Tie!")
        print("You selected: ", player_sel, "and computer selected: ", cpu_sel)
    elif (player_sel == 's' and cpu_sel == 'p') or (player_sel == 'p' and cpu_sel == 'r') or (player_sel == 'r' and cpu_sel == 's'):
        print("You won!")
        print("You selected: ", player_sel, "and computer selected: ", cpu_sel)
    elif (player_sel == 's' and cpu_sel == 'r') or (player_sel == 'p' and cpu_sel == 's') or (player_sel == 'r' and cpu_sel == 'p'):
        print("You Lost!")
        print("You selected: ",player_sel, "and computer selected: ",cpu_sel)
    play_again = input("Play again? (y/n): ")
    if play_again.lower() != 'y':
        print("Exiting...")
        break