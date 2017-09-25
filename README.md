# zenfinder

Zscaler ZEN Finder

## OVERVIEW

_ZEN Finder_ will locate the two closest Zscaler Enforcement Nodes (ZENs) by latitude and longitude.  This is accomplished by calculating the distance between two points on a spherical plane to calculate the distance between two points on Earth.  

The repo is under active development.  If you take a clone, you are getting the latest, and perhaps not entirely stable code.  This repository is not affiliated with Zscaler, Inc.

## INTENDED USERS

Fill in later

## INSTALLATION

### Installing Dependancies using PIP

TBD

### USAGE

Example:

    z = ZenFinder(ZENS, "zscalerbeta")

    # Example using getIpGeo method and passing IP address (full response)
    z.getIpGeo("208.65.255.0")
    z.getzens()

    # Example using getIpGeo method and passing IP address (partial response)
    z.getIpGeo("89.174.23.239")
    z.getzens()

    # Example using setGeo method and passing lattitude and longitude
    z.setGeo(25.761680, -80.191790)
    z.getzens()
    
Example Output:

    eparra@eparra-zscaler:~$ python zenfinder.py
    
    getIpGeo: Boca Raton, United States
    getIpGeo: 26.4095 latitude and -80.0942 longitude set
    getzens : 1st ZEN: 165.225.32.32, 2nd ZEN: 104.129.204.32
    
    getIpGeo: (No city in response), Poland
    getIpGeo: 52.2394 latitude and 21.0362 longitude set
    getzens : 1st ZEN: 165.225.84.32, 2nd ZEN: 165.225.64.32

    setGeo  : 25.76168 latitude and -80.19179 longitude set
    getzens : 1st ZEN: 165.225.32.32, 2nd ZEN: 104.129.204.32

## SUPPORT

This repository is not affiliated with Zscaler, Inc.  Please open issues here.

## TO DO

* Parse "region_name" from freegeoip.net
* Group all ZENs within a given geography to a parent reference
* Use programatic interface for ZEN data acquisition. 

## CONTRIBUTORS

TBD

*Contributors:*

[Eddie Parra](https://github.com/eparra)

## LICENSE

MIT
