#!/usr/bin/env python

from os import path, getcwd
from collections import defaultdict
config = defaultdict(defaultdict)

config["importer"] = "osm2pgsql" # either 'imposm' or 'osm2pgsql'

# The name given to the style. This is the name it will have in the TileMill
# project list, and a sanitized version will be used as the directory name
# in which the project is stored
# config["name"] = "San Diego [Bright]"
config["name"] = "Baltimore [Bright]"

# The absolute path to your MapBox projects directory. You should 
# not need to change this unless you have configured TileMill specially
config["path"] = path.expanduser("~/Documents/MapBox/project")

# PostGIS connection setup
# Leave empty for Mapnik defaults. The only required parameter is dbname.
config["postgis"]["host"]     = ""
config["postgis"]["port"]     = ""
config["postgis"]["dbname"]   = "baltimore"
config["postgis"]["user"]     = ""
config["postgis"]["password"] = ""

# Increase performance if you are only rendering a particular area by
# specifying a bounding box to restrict queries. Format is "XMIN,YMIN,XMAX,YMAX"
# in the same units as the database (probably spherical mercator meters). The
# whole world is "-20037508.34 -20037508.34 20037508.34 20037508.34".
# Leave blank to let Mapnik estimate.

# World
# config["postgis"]["extent"] = "-20037508.34,-20037508.34,20037508.34,20037508.34"
# San Diego
# config['bounds'] = "-117.4773385039 32.5719017933 -116.3670803398 33.2681644656"
# config["postgis"]["extent"] = "-117.4773385039 32.5719017933 -116.3670803398 33.2681644656"
config['minzoom'] = 0
config['maxzoom'] = 16
# config['bounds'] = [-117.4773385039, 32.5719017933, -116.3670803398, 33.2681644656]
# config['center'] = [-116.92220942185, 32.920033129450005]
# config["postgis"]["extent"] = "-20037508.34,-20037508.34,20037508.34,20037508.34"

# baltimore
config['bounds'] = [-76.71192455920391, 39.18833888607322, -76.52859020861797, 39.37356590965929]
config['center'] = [-76.61613751086406, 39.289118496474586]
config["postgis"]["extent"] = "-20037508.34,-20037508.34,20037508.34,20037508.34"

# 39.37356590965929, -76.71192455920391
# 39.18833888607322, -76.52859020861797
# 39.289118496474586, -76.61613751086406

# Land shapefiles required for the style. If you have already downloaded
# these or wish to use different versions, specify their paths here.
# OSM land shapefiles from MapBox are indexed for Mapnik and have blatant 
# errors corrected (eg triangles along the 180 E/W line). They can be download
# from:
# - http://tilemill-data.s3.amazonaws.com/osm/coastline-good.zip
# - http://tilemill-data.s3.amazonaws.com/osm/shoreline_300.zip
# But, they are updated infrequently. The latest versions can be downloaded from osm.org:
# - http://tile.openstreetmap.org/processed_p.tar.bz2
# - http://tile.openstreetmap.org/shoreline_300.tar.bz2
shapefiledir = path.expanduser('~/Downloads/shapefiles/')
config["processed_p"] = path.join(shapefiledir,"coastline-good.zip")
config["shoreline_300"] = path.join(shapefiledir,"shoreline_300.zip")
# http://mapbox-geodata.s3.amazonaws.com/natural-earth-1.3.0/physical/10m-land.zip
config["land"] = path.join(shapefiledir,"10m-land.zip")
