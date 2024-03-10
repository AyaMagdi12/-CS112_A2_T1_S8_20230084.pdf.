# A welcome massage to two players and their understanding of the game
print("------- welcome in this game -------") 
print(" A) this game played by two players")
print(" B) the winner is the first to reach 100 points")
print(" C) the number is between (1:10)")


# Take the names of the two players 
player1_name = str(input(" Enter the name of the first player "))
player2_name = str(input(" Enter the name of the second player "))
print (" welcome " +player1_name+ " and " +player2_name+ " to this game")


def the_game():
    sum = 0
    correct_number = 100-sum 
    while True :
        try:
            # Player 1's turn
            player1_input = int(input(player1_name+": Enter a number from 1 to 10: "))
            while player1_input < 1 or player1_input > 10:
                print("Invalid input . please enter a number from 1 to 10.")
                player1_input = int(input(player1_name + ": Enter a number from 1 to 10:"))
            sum+=player1_input
            print("sum =", sum)
            while  sum >=100:
                if sum == 100:
                    print(player1_name +" is the winner ")
                    print ("END GAME")
                    exit()
                if sum > 100:
                    sum -= player1_input 
                    while True:
                        player1_input = int(input(player1_name + " you have score bigger than 100 points "+player1_name + " please enter the correct number"))
                        if player1_input == correct_number:
                            print(player1_name+" is the winner")
                            print ("END GAME")
                            exit()
                        elif player1_input < correct_number:
                             sum += player1_input
                             print("sum = ",sum)
                             break
                        else:
                            continue     

            # Player 2's turn
            player2_input = int(input(player2_name+" :Enter a number from 1 to 10: "))
            while player2_input < 1 or player2_input > 10  :
                print ("Invalid input . please enter a number from 1 to 10")
                player2_input = int(input(player2_name + ": Enter a number from 1 to 10:"))
            sum+=player2_input
            print ("sum =", sum)
            while sum>=100:
                if sum == 100:
                    print (player2_name +" is the winner")
                    print ("END GAME ")
                    exit()
                if sum > 100:
                    sum-= player2_input   
                    while True:
                        player2_input = int(input(player2_name + " you have score bigger than 100 points "+player2_name + " please enter the correct number"))    
                    if player2_input == correct_number:
                        print(player2_name+" is the winner")
                        print ("END GAME")
                        exit()
                    elif player2_input < correct_number:
                         sum += player2_input
                         print("sum = ",sum)
                         break
                    else:
                        continue     

        except ValueError:
            print(" please enter a valid number ")
            continue                    
    
the_game()          