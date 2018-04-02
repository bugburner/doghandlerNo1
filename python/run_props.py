def get_av_speed(distance, time):
    #CALC AVERAGE SPEED OUT OF DISTANCE AND TIME
    #DISTANCE (FLOAT), #TIME (str(HH:MM:SS))
    av_speed = 0 
    
    time_split = time.split(':')
    mins = int(time_split[0])*60.0 + int(time_split[1])*1.0 + int(time_split[2])/60.0
    mins_per_km = mins / distance
    av_speed = round(1.0 / (mins_per_km /60.0),1)
    
    return av_speed

def get_2d_plot (x,y,title,xdim,ydim):
    import time
    import os
    if len(x)  == 0:
        return ""

    ts = time.time()
    gnuplot_file = "/tmp/gnuplot_header.plt"
    gnuplot_output = "/tmp/gnuplot_output_%s.svg"%ts
    gnuplot_input = "/tmp/gnuplot_data_%s"%ts
    gnuplot_header = """
set terminal svg enhanced dashed;
set output;"""
    gnuplot_header = gnuplot_header + "set xlabel 'x [%s]';"%xdim
    gnuplot_header = gnuplot_header + "set ylabel 'y [%s]';"%ydim

    gnuplot_header = gnuplot_header +"""



set style line 1 lc rgb '#0060ad' lw 2 lt -1 pt 4 pi -1;
set style line 2 lc rgb '#60ad00' lw 2 lt -1 pt 4 pi -1;
set style line 3 lc rgb '#ad0000' lw 2 pt 4 pi -1 ;

"""
    gnuplot_header = gnuplot_header + "\nset xrange [%s:%s];"%(min(x),max(x))
    gnuplot_header = gnuplot_header + "\nset output '%s';"%gnuplot_output
    gnuplot_header = gnuplot_header + "\nplot '%s' using 1:2 with linespoints ls 1 title '%s';"%(gnuplot_input, title)
    
    f = open(gnuplot_file, "w+")
    f.write(gnuplot_header)
    f.write("\n")
    f.close()
    
    f = open (gnuplot_input, "w+")
    for i in range (0,len(x)):
        f.write( "%s %s\n"%(x[i], y[i]))
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

