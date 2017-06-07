#!/usr/bin/env python3
# -*- coding: utf8 -*-

from geocodeQuery import GeocodeQuery



gq = GeocodeQuery("zh-tw", "tw")
addr = "台北市新湖二路280號"
gq.get_geocode(addr)
print("Latitude : "+str(gq.get_lat()))
print("Longitude : "+str(gq.get_lng()))