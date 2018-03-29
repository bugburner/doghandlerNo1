
import gpxpy
import gpxpy.gpx
import gpxpy.geo
import os

# Parsing an existing file:
# -------------------------

def get_plot(indz, elev):
    import time
    ts = time.time()
    gnuplot_file = "/tmp/gnuplot_header.plt"
    gnuplot_output = "/tmp/gnuplot_output_%s.svg"%ts
    gnuplot_input = "/tmp/gnuplot_data_%s"%ts
    gnuplot_header = """
set terminal svg;
"""
    gnuplot_header = gnuplot_header + "\nset output '%s';"%gnuplot_output
    gnuplot_header = gnuplot_header + "\nplot '%s' using 1:2 with linespoints;"%gnuplot_input
    
    f = open(gnuplot_file, "w+")
    f.write(gnuplot_header)
    f.write("\n")
    f.close()
    
    f = open (gnuplot_input, "w+")
    for i in range (0,len(indz)):
        f.write( "%s %s\n"%(indz[i], elev[i]) )
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
    
    for track in gpx.tracks:
        for segment in track.segments:
            for point in segment.points:
                if not old_lat == 0:
                    distance = distance + gpxpy.geo.distance(old_lat, old_lon, old_elev, point.latitude, point. longitude, point.elevation ) 
                old_lat = point.latitude
                old_lon = point.longitude
                old_elev = point.elevation
                indz.append(distance)
                elev.append(point.elevation)
                speed.append("")
    svg = get_plot(indz,elev)
    return distance, svg

# There are many more utility methods and functions:
# You can manipulate/add/remove tracks, segments, points, waypoints and routes and
# get the GPX XML file from the resulting object:
