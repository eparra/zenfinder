#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
from math import cos, sin, asin, sqrt, pi
import requests

global ZENS

ZENS = {
  "Amsterdam": {
    "IP": "185.46.212.32",
    "latitude": 52.370216,
    "longitude": 4.895168,  
    "zone": ['zscalerbeta']
  }, 
  "Atlanta-II": {
    "IP": "104.129.204.32",
    "latitude": 33.748995,
    "longitude": -84.387982,      
    "zone": ['zscalerbeta']
  },   
  "Brussels": {
    "IP": "165.225.88.32",
    "latitude": 50.850346,
    "longitude": 4.351721,  
    "zone": ['zscalerbeta']
  }, 
  "Capetown ": {
    "IP": "196.23.154.86",
    "latitude": -33.924869,
    "longitude": 18.424055,      
    "zone": ['zscalerbeta']
  },     
  "Chennai": {
    "IP": "165.225.104.32",
    "latitude": 13.082680,
    "longitude": 80.270718,     
    "zone": ['zscalerbeta']
  },    
  "Chicago": {
    "IP": "104.129.196.32",
    "latitude": 41.878114,
    "longitude": -87.629798,     
    "zone": ['zscalerbeta']
  },   
  "Copenhagen": {
    "IP": "165.225.64.32",
    "latitude": 55.676097,
    "longitude": 12.568337,  
    "zone": ['zscalerbeta']
  }, 
  "Dallas-I": {
    "IP": "165.225.34.32",
    "latitude": 32.776664,
    "longitude": -96.796988,      
    "zone": ['zscalerbeta']
  }, 
  "Denver": {
    "IP": "104.129.200.32",
    "latitude": 39.739236,
    "longitude": -104.990251,        
    "zone": ['zscalerbeta']
  }, 
  "Frankfurt-IV": {
    "IP": "165.225.72.32",
    "latitude": 50.110922,
    "longitude": 8.682127,  
    "zone": ['zscalerbeta']
  }, 
  "Hong Kong": {
    "IP": "202.130.161.199",
    "latitude": 22.396428,
    "longitude": 114.109497,  
    "zone": ['zscalerbeta']
  },   
  "Hong Kong-II": {
    "IP": "165.225.96.32",
    "latitude": 22.396428,
    "longitude": 114.109497,  
    "zone": ['zscalerbeta']
  },     
  "Johannesburg": {
    "IP": "196.23.147.214",
    "latitude": -26.204103,
    "longitude": 28.047305,  
    "zone": ['zscalerbeta']
  },
  "Kuala Lumpur": {
    "IP": "49.236.207.190",
    "latitude": 3.139003,
    "longitude": 101.686855,  
    "zone": ['zscalerbeta']
  },
  "Lagos": {
    "IP": "197.156.241.242",
    "latitude": 6.524379,
    "longitude": 3.379206,     
    "zone": ['zscalerbeta']
  },
  "London-III": {
    "IP": "165.225.80.32",
    "latitude": 51.507351,
    "longitude": -0.127758,  
    "zone": ['zscalerbeta']
  },       
  "Los Angeles": {
    "IP": "104.129.198.32",
    "latitude": 34.052234,
    "longitude": -118.243685,      
    "zone": ['zscalerbeta']
  }, 
  "Madrid": {
    "IP": "89.167.129.32",
    "latitude": 40.416775,
    "longitude": -3.703790,  
    "zone": ['zscalerbeta']
  },
  "Melbourne": {
    "IP": "8165.225.98.32",
    "latitude": -37.813628,
    "longitude": 144.963058,  
    "zone": ['zscalerbeta']
  },
  "Miami-II": {
    "IP": "165.225.32.32",
    "latitude": 25.761680,
    "longitude": -80.191790,     
    "zone": ['zscalerbeta']
  },  
  "Milan-II": {
    "IP": "165.225.86.32", 
    "latitude": 45.464204,
    "longitude": 9.189982,  
    "zone": ['zscalerbeta']
  }, 
  "Moscow-III": {
    "IP": "165.225.66.32",
    "latitude": 55.755826,
    "longitude": 37.617300,  
    "zone": ['zscalerbeta']
  }, 
  "Mumbai-II": {
    "IP": "165.225.106.32",
    "latitude": 19.075984,
    "longitude": 72.877656,  
    "zone": ['zscalerbeta']
  },
  "New York": {
    "IP": "209.51.184.2",
    "latitude": 40.712784,
    "longitude": -74.005941,      
    "zone": ['zscalerbeta']
  },  
  "New York-II": {
    "IP": "199.168.151.129",
    "latitude": 40.712784,
    "longitude": -74.005941,      
    "zone": ['zscalerbeta']
  },  
  "New York-III": {
    "IP": "165.225.38.36",
    "latitude": 40.712784,
    "longitude": -74.005941,      
    "zone": ['zscalerbeta']
  },  
  "Oslo-II": {
    "IP": "89.191.7.25", 
    "latitude": 59.913869,
    "longitude": 10.752245,  
    "zone": ['zscalerbeta']
  }, 
  "Paris-II": {
    "IP": "165.225.76.32",
    "latitude": 48.856614,
    "longitude": 2.352222,  
    "zone": ['zscalerbeta']
  }, 
  "San Francisco-IV": {
    "IP": "104.129.192.32",
    "latitude": 37.774929,
    "longitude": -122.419416,      
    "zone": ['zscalerbeta']
  },   
  "Sao Paulo": {
    "IP": "64.215.22.32",
    "latitude": -23.550520,
    "longitude": -46.633309,      
    "zone": ['zscalerbeta']
  },   
  "Seattle": {
    "IP": "165.225.50.8",
    "latitude": 47.606209,
    "longitude": -122.332071,       
    "zone": ['zscalerbeta']
  },    
  "Shanghai": {
    "IP": "58.220.95.8",
    "latitude": 31.230390,
    "longitude": 121.473702,       
    "zone": ['zscalerbeta']
  },    
  "Singapore": {
    "IP": "542.99.164.32",
    "latitude": 1.352083,
    "longitude": 103.819836,       
    "zone": ['zscalerbeta']
  },  
  "Stockholm": {
    "IP": "165.225.68.32",
    "latitude": 59.329323,
    "longitude": 18.068581,  
    "zone": ['zscalerbeta']
  },       
  "Sydney": {
    "IP": "175.45.116.32",
    "latitude": -33.868820,
    "longitude": 151.209296,  
    "zone": ['zscalerbeta']
  },  
  "Taipei": {
    "IP": "165.225.102.32",
    "latitude": 25.032969,
    "longitude": 121.565418,  
    "zone": ['zscalerbeta']
  },  
  "Tel Aviv": {
    "IP": "94.188.248.71",
    "latitude": 32.085300,
    "longitude": 34.781768,  
    "zone": ['zscalerbeta']
  },
  "Tianjin": {
    "IP": "139.220.195.32",
    "latitude": 39.343357,
    "longitude": 117.361648,  
    "zone": ['zscalerbeta']
  },
  "Tianjin-II": {
    "IP": "221.122.91.32",
    "latitude": 39.343357,
    "longitude": 117.361648,  
    "zone": ['zscalerbeta']
  },
  "Tokyo-II": {
    "IP": "165.225.100.32",
    "latitude": 35.689487,
    "longitude": 139.691706,  
    "zone": ['zscalerbeta']
  },
  "Toronto-II": {
    "IP": "165.225.36.32",
    "latitude": 43.653226,
    "longitude": -79.383184,      
    "zone": ['zscalerbeta']
  },      
  "Warsaw": {
    "IP": "165.225.84.32",
    "latitude": 52.229676,
    "longitude": 21.012229,  
    "zone": ['zscalerbeta']
  },
  "Washington DC": {
    "IP": "104.129.194.32",
    "latitude": 38.907192,
    "longitude": -77.036871,      
    "zone": ['zscalerbeta']
  },    
  "Zurich": {
    "IP": "185.46.214.32",
    "latitude": 47.376887,
    "longitude": 8.541694,  
    "zone": ['zscalerbeta']
  }          
}

class ZenFinder(object):

    def __init__(self, zens, zone = "zscalerbeta"):

        self.zens = zens
        self.zone = zone
        self.earth_rad = 6371   # earth radius in kilometers   


    def _deg_to_rad(self, deg):
        return deg * (pi / 180)


    def _haversine(self, rad):
        return sin(rad/2) ** 2


    def _haversine_distance(self, coordinates_1, coordinates_2):
        """
        Calculates the distance between two points on spherical plane
        used here to calc the distance between two points on earth

        args:
            - coordinates_1: first point latitude and longitude 
            - coordinates_2: seconed point latitude and longitude
        returns: distance between those points in kilometers
        """
        lat_1 = self._deg_to_rad(coordinates_1['latitude'])
        lon_1 = self._deg_to_rad(coordinates_1['longitude'])
        lat_2 = self._deg_to_rad(coordinates_2['latitude'])
        lon_2 = self._deg_to_rad(coordinates_2['longitude'])

        dlat = lat_2 - lat_1
        dlon = lon_2 - lon_1

        cangle = self._haversine(dlat) + cos(lat_1) * cos(lat_2) * self._haversine(dlon)
        distance = 2 * self.earth_rad * asin(sqrt(cangle))
        return distance


    def getzens(self):
        """
        Get the nearest two cities in a certain zone to a given longitude
        and latitude point
        Instance args:
            - self.latitude: set by getGeo() or getIpGeo()
            - self.longitude: set by getGeo() or getIpGeo()
        """
        zens = self.zens
        coordinates = {
            'latitude': self.latitude,
            'longitude': self.longitude,
        }
        zone_cities_dist = {
            city_name: self._haversine_distance(coordinates, city_data)
            for city_name, city_data in zens.items()
            if self.zone in city_data['zone']
        }
        ordered = sorted(zone_cities_dist.items(), key=lambda x: x[1])
        first_nearest_zen = ordered[0][0]
        seconed_nearest_zen = ordered[1][0]

        print "getzens : 1st ZEN: {}, 2nd ZEN: {}".format(
            zens[first_nearest_zen]['IP'],
            zens[seconed_nearest_zen]['IP']
        )
        return [
            {first_nearest_zen: zens[first_nearest_zen]['IP']},
            {seconed_nearest_zen: zens[seconed_nearest_zen]['IP']}
        ]


    def getIpGeo(self, ipaddr):
        """
        Perform a geo IP lookup with freegeoip.net
        args:
            - ipaddr: IP address to geo IP lookup
        """
        url = "http://freegeoip.net/json/{}".format(ipaddr)    
        response = requests.get(url)
        if response.text:
            response_json = json.loads(response.text)
            self.latitude = response_json['latitude']
            self.longitude = response_json['longitude']
            if not response_json['city'] or not response_json['country_name']:
                if not response_json['city']:
                    response_json['city'] = "(No city in resposne)"
                if not response_json['country_name']:
                    response_json['country_name'] = "(No country in resposne)"
            print "getIpGeo: {}, {}".format(response_json['city'], response_json['country_name'])
            print "getIpGeo: {} latitude and {} longitude set".format(self.latitude, self.longitude)
            return [
                {'latitude': self.latitude},
                {'longitude': self.longitude}            
            ]
        else:
            return None


    def setGeo(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude       
        print "setGeo  : {} latitude and {} longitude set".format(self.latitude, self.longitude)


def main():

    z = ZenFinder(ZENS, "zscalerbeta")

    # Example using getIpGeo method and passing IP address
    z.getIpGeo("89.174.23.239")
    z.getzens()

    # Example using setGeo method and passing lattitude and longitude
    z.setGeo(25.761680, -80.191790)
    z.getzens()
  

if __name__ == '__main__':
    main()
