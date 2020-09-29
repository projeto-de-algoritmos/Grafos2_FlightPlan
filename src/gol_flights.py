import pandas as pd
import math, json

def convert_csv_file_to_json_file(path):
  gol_flights = pd.read_csv(path).to_json('../gol_flights_json')

def to_radius(degree):
  return (math.pi / 180) * degree

def distance(_from, to):
  lat1 = to_radius(_from['latitude'])
  long1 = to_radius(_from['longitude'])
  lat2 = to_radius(to['latitude'])
  long2 = to_radius(to['longitude'])
  distance_lat = lat2 - lat1
  distance_long = long2 - long1
  
  distance = (math.sin(distance_lat / 2) ** 2) + math.cos(lat1) * math.cos(lat2) * (math.sin(distance_long / 2) ** 2)
  distance = 2 * math.asin(math.sqrt(distance))
  R = 6371 # earth's radius
  distance *= R
  return distance
