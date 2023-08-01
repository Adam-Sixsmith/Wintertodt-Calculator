import math

def XpLeft():
    global total_xp_left
    
    current_xp = int(input("What is your current XP? "))
    
    # Having to use this as the target XP due to not knowing the proper way to work out the XP based
    # on what level they want yet without having a bunch of code with each level and it's xp required
    target_xp = int(input("What is the target XP you're looking to get? (You can get this from Runelites Cacluator)"))
    
    total_xp_left = target_xp - current_xp
    
    xp_left_to_get = f"You have {target_xp - current_xp} xp left to get to your level"
    
    print(xp_left_to_get)
    
def games_to_go():
    global rounded_number_of_games, total_xp_left
    
    average_xp_per_game = 25000
    
    total_games = total_xp_left / average_xp_per_game
    
    rounded_number_of_games = math.ceil(total_games)
    
    print(f"You have roughly {rounded_number_of_games} games left until your level")
    
def time_until_level():
    global rounded_number_of_games
    
    average_game_time_seconds = 5 * 60 + 20
    total_time_seconds = rounded_number_of_games * average_game_time_seconds
    
    hours = total_time_seconds // 3600
    minutes = (total_time_seconds % 3600) // 60
    seconds = total_time_seconds % 60
    
    print(f"It will take approximately {hours} hours, {minutes} minutes, and {seconds} seconds to reach your level based on the average game being 5 minutes and 20 seconds.")
    
def main():
    XpLeft()
    games_to_go()
    time_until_level()
    
main()