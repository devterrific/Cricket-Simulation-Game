import random,time

##DEV TERRIFIC FUN SMALL PROJECTS
team = ["afg", "india", "pak", "aus"]

def choose_team():
    print(f"You have these teams to choose from: {', '.join(team)}")
    while True:
        your_team = input("Please choose a team: ").lower()
        if your_team in team:
            print(f"You chose {your_team}")
            break
        else:
            print("Please choose between afg, india, pak, aus and look out for spelling.")
    
    while True:
        opps = input("Please choose the opponent team: ").lower()
        if opps in team and opps != your_team:
            print(f"You chose {opps} as the opponent")
            break
        elif opps == your_team:
            print("You cannot choose your own team as the opponent. Try again.")
        else:
            print("Please choose between afg, india, pak, aus and look out for spelling.")

    return your_team, opps


def chooseovers():
    while True:
        try:
            overs = int(input("please choose a over between 1 and 50 "))
        except ValueError:
            print("error : please choose a number between 1 and 50 ")
            continue
        if overs <= 50:
            return overs
        else:
            print("you choosed a wrong number try again ")


def randomruns():
    a = random.randint(0,6)
    return a

#bat or ball
def batorball():
    while True:

        true_answer = ["bat","ball"]

        answer = input("please enter whether you want to ball or bat " )
        if answer in true_answer:
            print(f"your choose {answer}")
            break
        else:
            print("choose between bat or ball")

    return answer

#start the game //logic

def game_logic(your_team, opps_team, chosen_overs, bat_or_ball):
    innings = 1
    while innings <= 2:
        # Determine the batting and bowling teams based on user's choice and the innings number
        if (bat_or_ball == 'bat' and innings == 1) or (bat_or_ball == 'ball' and innings == 2):
            batting_team, bowling_team = your_team, opps_team
        else:
            batting_team, bowling_team = opps_team, your_team
        
        print(f"Innings {innings}: {batting_team} batting against {bowling_team}")

        runscounter = 0
        overs_counter = 0
        out_players = 0

        while overs_counter < chosen_overs and out_players < 10:
            a = randomruns()
            time.sleep(0.5)
            if a == 0:
                time.sleep(0.5)
                out_players += 1
                time.sleep(0.5)
                overs_counter += 1/6
                time.sleep(0.5)
                print(f"{batting_team} has a score of {runscounter} and have {10 - out_players} players remaining")
            else:
                time.sleep(0.5)
                runscounter += a
                time.sleep(0.5)
                overs_counter += 1/6
                time.sleep(0.5)
                print(f"{batting_team} has a score of {runscounter} and have {10 - out_players} players remaining")

        innings += 1  

def __main__():
    your_team, opps_team = choose_team()
    bat_or_ball = batorball()
    chosen_overs = chooseovers()
    print(f"You are playing as {your_team} agianst {opps_team}")
    print(f"your choosed {chosen_overs} overs ")
    print(f"and you are choose to {bat_or_ball}")    

    game_logic(your_team, opps_team, chosen_overs, bat_or_ball)


    
if __name__ == "__main__":
    __main__()

