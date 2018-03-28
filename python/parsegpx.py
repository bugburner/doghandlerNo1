path = "../Maps3D 2018-03-18 04-10pm.gpx"



import gpxpy
import gpxpy.gpx

# Parsing an existing file:
# -------------------------

gpx_file = open(path, 'r')

gpx = gpxpy.parse(gpx_file)

for track in gpx.tracks:
    for segment in track.segments:
        for point in segment.points:
            print 'Point at ({0},{1}) -> {2}'.format(point.latitude, point.longitude, point.elevation)

for waypoint in gpx.waypoints:
    print 'waypoint {0} -> ({1},{2})'.format(waypoint.name, waypoint.latitude, waypoint.longitude)
    
for route in gpx.routes:
    print 'Route:'
    for point in route.points:
        print 'Point at ({0},{1}) -> {2}'.format(point.latitude, point.longitude, point.elevation)

# There are many more utility methods and functions:
# You can manipulate/add/remove tracks, segments, points, waypoints and routes and
# get the GPX XML file from the resulting object:

print 'GPX:', gpx.to_xml()

# Creating a new file:
# --------------------

gpx = gpxpy.gpx.GPX()

# Create first track in our GPX:
gpx_track = gpxpy.gpx.GPXTrack()
gpx.tracks.append(gpx_track)

# Create first segment in our GPX track:
gpx_segment = gpxpy.gpx.GPXTrackSegment()
gpx_track.segments.append(gpx_segment)

# Create points:
gpx_segment.points.append(gpxpy.gpx.GPXTrackPoint(2.1234, 5.1234, elevation=1234))
gpx_segment.points.append(gpxpy.gpx.GPXTrackPoint(2.1235, 5.1235, elevation=1235))
gpx_segment.points.append(gpxpy.gpx.GPXTrackPoint(2.1236, 5.1236, elevation=1236))

# You can add routes and waypoints, too...

print 'Created GPX:', gpx.to_xml()
