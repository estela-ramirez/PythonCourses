Python 3.6.0 (v3.6.0:41df79263a11, Dec 22 2016, 17:23:13) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> 
========= RESTART: /Users/EstelaRamirez/Desktop/P3 User_Interface.py =========
2
Irvine, CA
Los Angeles, CA
http://open.mapquestapi.com/directions/v2/route?key=CsF74gbUMlrJ3VcVtA5gpVpqgbicSGLI&from=Irvine%2C+CA&to=Los+Angeles%2C+CA
2
latlong
latlong

LATLONGS
Traceback (most recent call last):
  File "/Users/EstelaRamirez/Desktop/P3 User_Interface.py", line 160, in <module>
    main()
  File "/Users/EstelaRamirez/Desktop/P3 User_Interface.py", line 157, in main
    _run_user_interface()
  File "/Users/EstelaRamirez/Desktop/P3 User_Interface.py", line 151, in _run_user_interface
    get_info_according_to_output_choice(json_data, outputs, num_of_locations)
  File "/Users/EstelaRamirez/Desktop/P3 User_Interface.py", line 119, in get_info_according_to_output_choice
    Get_LatLng_Info(json_data, num_of_locations)
  File "/Users/EstelaRamirez/Desktop/P3 User_Interface.py", line 80, in Get_LatLng_Info
    latlng.add_direction_to_lat(lat, lng)
  File "/Users/EstelaRamirez/Desktop/Classes.py", line 35, in add_direction_to_lat
    if self._negative in self._lat:
TypeError: argument of type 'float' is not iterable
>>> 
========= RESTART: /Users/EstelaRamirez/Desktop/P3 User_Interface.py =========
2
Irvine, CA
Los Angeles, CA
http://open.mapquestapi.com/directions/v2/route?key=CsF74gbUMlrJ3VcVtA5gpVpqgbicSGLI&from=Irvine%2C+CA&to=Los+Angeles%2C+CA
2
latlong
latlong

LATLONGS
Traceback (most recent call last):
  File "/Users/EstelaRamirez/Desktop/P3 User_Interface.py", line 160, in <module>
    main()
  File "/Users/EstelaRamirez/Desktop/P3 User_Interface.py", line 157, in main
    _run_user_interface()
  File "/Users/EstelaRamirez/Desktop/P3 User_Interface.py", line 151, in _run_user_interface
    get_info_according_to_output_choice(json_data, outputs, num_of_locations)
  File "/Users/EstelaRamirez/Desktop/P3 User_Interface.py", line 119, in get_info_according_to_output_choice
    Get_LatLng_Info(json_data, num_of_locations)
  File "/Users/EstelaRamirez/Desktop/P3 User_Interface.py", line 80, in Get_LatLng_Info
    latlng.add_direction_to_lat(lat, lng)
  File "/Users/EstelaRamirez/Desktop/Classes.py", line 38, in add_direction_to_lat
    self._lat = str(self._lat) + N
NameError: name 'N' is not defined
>>> 
========= RESTART: /Users/EstelaRamirez/Desktop/P3 User_Interface.py =========
2
Irivne, CA
Los Angeles, CA
http://open.mapquestapi.com/directions/v2/route?key=CsF74gbUMlrJ3VcVtA5gpVpqgbicSGLI&from=Irivne%2C+CA&to=Los+Angeles%2C+CA
2
latlong
latlong

LATLONGS
39.78N -100.45E
34.05N -118.24E

LATLONGS
39.78N -100.45E
34.05N -118.24E

Directions Courtesy of MapQuest; Map Data Copyright OpenStreetMap Contributors.
>>> 
========= RESTART: /Users/EstelaRamirez/Desktop/P3 User_Interface.py =========
2
Irvine, CA
Los Angeles, CA
http://open.mapquestapi.com/directions/v2/route?key=CsF74gbUMlrJ3VcVtA5gpVpqgbicSGLI&from=Irvine%2C+CA&to=Los+Angeles%2C+CA
2
latlong
latlong

LATLONGS
33.685697 -117.825982
34.054394 -118.243941

LATLONGS
33.685697 -117.825982
34.054394 -118.243941

Directions Courtesy of MapQuest; Map Data Copyright OpenStreetMap Contributors.
>>> 
========= RESTART: /Users/EstelaRamirez/Desktop/P3 User_Interface.py =========
2
Irvine, CA
Los Angeles, CA
http://open.mapquestapi.com/directions/v2/route?key=CsF74gbUMlrJ3VcVtA5gpVpqgbicSGLI&from=Irvine%2C+CA&to=Los+Angeles%2C+CA
2
latlong
latlong

LATLONGS
33.69 -117.83
34.05 -118.24

LATLONGS
33.69 -117.83
34.05 -118.24

Directions Courtesy of MapQuest; Map Data Copyright OpenStreetMap Contributors.
>>> 
========= RESTART: /Users/EstelaRamirez/Desktop/P3 User_Interface.py =========
2
Irvine, CA
Los Angeles, CA
http://open.mapquestapi.com/directions/v2/route?key=CsF74gbUMlrJ3VcVtA5gpVpqgbicSGLI&from=Irvine%2C+CA&to=Los+Angeles%2C+CA
2
latlong
latlong

LATLONGS
-117.83
-117.83E
33.69N -117.83E
-118.24
-118.24E
34.05N -118.24E

LATLONGS
-117.83
-117.83E
33.69N -117.83E
-118.24
-118.24E
34.05N -118.24E

Directions Courtesy of MapQuest; Map Data Copyright OpenStreetMap Contributors.
>>> 
========= RESTART: /Users/EstelaRamirez/Desktop/P3 User_Interface.py =========
2
Irvine, CA
Los Angeles, CA
http://open.mapquestapi.com/directions/v2/route?key=CsF74gbUMlrJ3VcVtA5gpVpqgbicSGLI&from=Irvine%2C+CA&to=Los+Angeles%2C+CA
2
latlong
latlong

LATLONGS
33.69N -117.83E
34.05N -118.24E

LATLONGS
33.69N -117.83E
34.05N -118.24E

Directions Courtesy of MapQuest; Map Data Copyright OpenStreetMap Contributors.
>>> 
