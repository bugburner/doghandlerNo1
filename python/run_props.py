def get_av_speed(distance, time):
    #CALC AVERAGE SPEED OUT OF DISTANCE AND TIME
    #DISTANCE (FLOAT), #TIME (str(HH:MM:SS))
    av_speed = 0 
    
    time_split = time.split(':')
    mins = int(time_split[0])*60.0 + int(time_split[1])*1.0 + int(time_split[2])/60.0
    mins_per_km = mins / distance
    av_speed = round(1.0 / (mins_per_km /60.0),1)
    
    return av_speed
