
import gpxpy
import gpxpy.gpx
import gpxpy.geo
import os

# Parsing an existing file:
# -------------------------

def mean(l):
    if len(l)>0:
        av_l = sum(l) / float(len(l))
    else:
        av_l = sum(l)
    return av_l

def get_plot(indz, elev, speed,av_speed):
    import time
    ts = time.time()
    gnuplot_file = "/tmp/gnuplot_header.plt"
    gnuplot_output = "/tmp/gnuplot_output_%s.svg"%ts
    gnuplot_input = "/tmp/gnuplot_data_%s"%ts
    gnuplot_header = """
set terminal svg enhanced dashed;
set output;
set xlabel 'x [km]';
set ylabel 'Hoehe [m]';
set y2label 'Geschwindigkeit [km/h]';
set ytics axis;
set y2tics;


set style line 1 lc rgb '#0060ad' lw 2 lt -1 pt 4 pi -1;
set style line 2 lc rgb '#60ad00' lw 2 lt -1 pt 4 pi -1;
set style line 3 lc rgb '#ad0000' lw 2 pt 4 pi -1 ;

"""
    gnuplot_header = gnuplot_header + "\nset xrange [0:%s];"%max(indz)
    gnuplot_header = gnuplot_header + "\nset output '%s';"%gnuplot_output
    gnuplot_header = gnuplot_header + "\nplot '%s' using 1:2 with lines ls 1 title 'Hoehe', '' using 1:3 axes x1y2 with lines ls 2 title 'Speed', %s ls 3 axes x1y2 title '';"%(gnuplot_input, av_speed)
    
    f = open(gnuplot_file, "w+")
    f.write(gnuplot_header)
    f.write("\n")
    f.close()
    
    f = open (gnuplot_input, "w+")
    for i in range (0,len(indz)):
        f.write( "%s %s %s\n"%(indz[i], elev[i], speed[i] ))
    f.close()

    os.system('gnuplot %s'%gnuplot_file)
    
    svg = str()
    f = open (gnuplot_output,"r")
    for row in f:
        svg = svg + row
    f.close()
    os.remove(gnuplot_file)
    os.remove(gnuplot_output)
    os.remove(gnuplot_input)
    return svg

def get_map_3d(x,y,z,e):
    import time
    ts = time.time()
    gnuplot_file = "/tmp/gnuplot_header.plt"
    gnuplot_output = "/tmp/gnuplot_output_%s.svg"%ts
    gnuplot_input = "/tmp/gnuplot_data_%s"%ts
    gnuplot_header = """
set terminal svg enhanced dashed;
set output;
set xlabel '';
set ylabel '';
unset ytics;
unset xtics;
set zlabel 'Hoehe';
set style line 1 lc rgb '#0060ad' lw 2 lt -1 pt 4 pi -1;
set style line 2 lc rgb '#60ad00' lw 2 lt -1 pt 4 pi -1;
set style line 3 lc rgb '#ad0000' lw 2 pt 4 pi -1 ;

"""
    gnuplot_header = gnuplot_header + "\nset output '%s';"%gnuplot_output
    gnuplot_header = gnuplot_header + "\nsplot '%s' using 1:2:3:4 with lines palette title'';"%(gnuplot_input)
    
    f = open(gnuplot_file, "w+")
    f.write(gnuplot_header)
    f.write("\n")
    f.close()

    f = open (gnuplot_input, "w+")
    for i in range (0,len(x)):
        f.write( "%s %s %s %s\n"%(0-x[i], y[i], z[i], e[i] ))
    f.close()
    os.system('gnuplot %s'%gnuplot_file)
    
    svg = str()
    f = open (gnuplot_output,"r")
    for row in f:
        svg = svg + row
    f.close()
    os.remove(gnuplot_file)
    os.remove(gnuplot_output)
    os.remove(gnuplot_input)
    return svg

def get_map_2d(x,y,z):
    import time
    ts = time.time()
    gnuplot_file = "/tmp/gnuplot_header.plt"
    gnuplot_output = "/tmp/gnuplot_output_%s.svg"%ts
    gnuplot_input = "/tmp/gnuplot_data_%s"%ts
    gnuplot_header = """
set terminal svg enhanced dashed;
set output;
set xlabel '';
set ylabel '';

unset ytics;
unset xtics;

set style line 1 lc rgb '#0060ad' lw 2 lt -1 pt 4 pi -1;
set style line 2 lc rgb '#60ad00' lw 2 lt -1 pt 4 pi -1;
set style line 3 lc rgb '#ad0000' lw 2 pt 4 pi -1 ;

"""
    gnuplot_header = gnuplot_header + "\nset output '%s';"%gnuplot_output
    gnuplot_header = gnuplot_header + "\nplot '%s' using 1:2:3 with lines palette title'';"%(gnuplot_input)
    
    f = open(gnuplot_file, "w+")
    f.write(gnuplot_header)
    f.write("\n")
    f.close()

    f = open (gnuplot_input, "w+")
    for i in range (0,len(x)):
        f.write( "%s %s %s\n"%(0-x[i], y[i], z[i]))
    f.close()
    os.system('gnuplot %s'%gnuplot_file)
    
    svg = str()
    f = open (gnuplot_output,"r")
    for row in f:
        svg = svg + row
    f.close()
    os.remove(gnuplot_file)
    os.remove(gnuplot_output)
    os.remove(gnuplot_input)
    return svg

    
    
def parse_gpx(path):
    gpx_file = open(path, 'r')

    gpx = gpxpy.parse(gpx_file)
    
    distance = 0.0
    old_lat = 0.0
    old_lon = 0.0
    old_elev = 0.0
    elev = list()
    indz = list()
    speed = list()
    lat = list()
    lon = list()
    speed.append(0.0)
    for track in gpx.tracks:
        for segment in track.segments:
            for point in segment.points:
                if not old_lat == 0:
                    distance = distance + gpxpy.geo.distance(old_lat, old_lon, old_elev, point.latitude, point. longitude, point.elevation )
                    speed.append(point.speed_between(old_point)*3.6) 
                old_lat = point.latitude
                old_lon = point.longitude
                lat.append(point.latitude)
                lon.append(point.longitude)
                old_elev = point.elevation
                old_point = point
                indz.append(distance/1e3)
                elev.append(point.elevation)

            s_min_km = (segment.get_duration() / 60.0) / (segment.length_3d() / 1000)
            av_speed = 1.0 / s_min_km * 60.0
        
    max_speed = max(speed)
    for i in range(1,len(speed)-1):
        if abs(speed[i] - speed [i-1]) > max_speed*0.1 and abs(speed[i] - speed [i+1]) > max_speed*0.1:
            speed[i] = abs(speed[i-1]-speed[i+1]) + min([speed[i-1], speed[i+1]])
        
    svg = get_plot(indz,elev,speed,av_speed)
    map3d = get_map_3d(lat,lon, elev, speed)
    map2d = get_map_2d(lat,lon, speed)
    return distance, svg, map3d, map2d

def get_det_speed(path):
    gpx_file = open(path, 'r')

    gpx = gpxpy.parse(gpx_file)

    speed_up_l = list()
    speed_down_l = list()
    speed_eq_l = list()
    pitch_l = list()
    speed_l = list()
    old_elev = 0.0
    distance = 0.0
    av_speed = 0.0

    for track in gpx.tracks:
        for segment in track.segments:
            for point in segment.points:
                if not old_elev == 0:
                    if abs((point.elevation - old_point.elevation) / gpxpy.geo.distance(old_point.latitude, old_point.longitude, old_point.elevation, point.latitude, point.longitude, point.elevation)) < 0.07:
                        speed_eq_l.append(point.speed_between(old_point)*3.6)
                    else:
                        if point.elevation - old_point.elevation < 0:
                            speed_down_l.append(point.speed_between(old_point)*3.6)
                        else:
                            speed_up_l.append(point.speed_between(old_point)*3.6)
                    pitch_l.append ((point.elevation - old_point.elevation) / gpxpy.geo.distance(old_point.latitude, old_point.longitude, old_point.elevation, point.latitude, point.longitude, point.elevation))
                    speed_l.append(point.speed_between(old_point)*3.6)
                old_elev = point.elevation
                old_point = point
            distance = segment.length_3d()/1000.0
            s_min_km = (segment.get_duration() / 60.0) / (segment.length_3d() / 1000)
            av_speed = 1.0 / s_min_km * 60.0

    speed_up = mean (speed_up_l)
    speed_down = mean (speed_down_l)
    speed_eq = mean (speed_eq_l)
    #return 0.0,0.0,0.0
    return speed_up, speed_down, speed_eq, av_speed, distance, speed_l, pitch_l
                
