import time
streak = 0
def total_speed(total_dist, total_time):
    speed = total_dist / total_time
    return speed

def temp_speed(temp_dist, temp_time):
    speed = temp_dist / temp_time
    return speed

def add_distance(temp_dist, total_dist):
    total_dist[0] += temp_dist

def add_time(temp_time, total_time):
    total_time[0] += temp_time

if __name__ == '__main__':
    # string to get player name
    player_name = input("Please enter name: \n")
    print("The player's name is:", player_name)

    # double slideSpeed = 1
    time_elapsed = 0
    slide_counter = 0
    mile_age = 0
    mile_age_left = 0
    # int streak = 1
    slide_number = 0

    if slide_number <= 3:
        mile_age = 0
    elif slide_number <= 10:
        mile_age = 0.25
    elif slide_number <= 21:
        mile_age = 0.5

    # measure time
    input("Type 'start' to start the stopwatch...\n")
    start_time = time.time()  # record the starting time
    input("Type 'stop' to stop the stopwatch...\n")
    end_time = time.time()  # record the ending time
    elapsed_time = end_time - start_time  # calculate the elapsed time
    hours = int(elapsed_time / 3600)
    minutes = int((elapsed_time % 3600) / 60)
    seconds = int(elapsed_time % 60)
    print("Elapsed time:", hours, "hours", minutes, "minutes", seconds, "seconds")

    geo_miles = 3.8
    # temporary variables
    temp_dist = geo_miles
    total_dist = [0]
    add_distance(temp_dist, total_dist)
    total_time = [1]
    temp_time = elapsed_time / 3600

    print("Total distance walked/ran =", round(total_dist[0], 2))
    print("Average speed during run =", round(temp_speed(temp_dist, temp_time), 2), "mph")
    print("Total average speed =", round(total_speed(total_dist[0], total_time[0]), 2))
    if(seconds<=86399):
        dailyDist = temp_dist
        streakComparer = dailyDist
        if(dailyDist>=1):
            streak+=1
        elif(dailyDist<1 and seconds == 86399):
            streak = 0
