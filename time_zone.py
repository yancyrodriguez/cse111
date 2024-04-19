#This time zone project was created after reviewing ideas.
#I considered if someone wants to travel and wanted to know the time zone continents

import datetime #datetime Python module
import pytz

def get_time_zone(time_zone_file): #function def get_time_zone
    try:
        with open(time_zone_file, 'r') as file:
            zones = file.readlines()
        
        for zone_name in zones:
            zone_name = zone_name.strip()
            try:
                zone = pytz.timezone(zone_name)
                current_time = datetime.datetime.now(zone)
                print(f"The current time zone in {zone_name} is {current_time.strftime('%Y-%m-%d %H:%M:%S')}")
            except pytz.UnknownTimeZoneError:
                print(f"Error: The time zone '{zone_name}' is not recognized.")
    except FileNotFoundError:
        print(f"Error: The file '{time_zone_file}' is not found.")
    except Exception as e:
        print(f"Error has occured: {e}")

get_time_zone("time_zone.txt")
