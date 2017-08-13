#!/usr/bin/env python3
# -*- coding: utf8 -*-

from geocodeQuery import GeocodeQuery



gq = GeocodeQuery("zh-tw", "tw")
addr = "高雄市那瑪夏區"
gq.get_geocode(addr)
print("Latitude : "+str(gq.get_lat()))
print("Longitude : "+str(gq.get_lng()))