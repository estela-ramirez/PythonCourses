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
elevation
elevation
[33.685697, -117.825982, 34.054394, -118.243941]
http://open.mapquestapi.com/elevation/v1/profile?key=CsF74gbUMlrJ3VcVtA5gpVpqgbicSGLI&shapeFormat=raw&latLngCollection=33.685697,-117.825982,34.054394,-118.243941
Traceback (most recent call last):
  File "/Users/EstelaRamirez/Desktop/P3 User_Interface.py", line 200, in <module>
    main()
  File "/Users/EstelaRamirez/Desktop/P3 User_Interface.py", line 197, in main
    _run_user_interface()
  File "/Users/EstelaRamirez/Desktop/P3 User_Interface.py", line 191, in _run_user_interface
    get_info_according_to_output_choice(json_data, outputs, num_of_locations)
  File "/Users/EstelaRamirez/Desktop/P3 User_Interface.py", line 157, in get_info_according_to_output_choice
    elev_json_data = URL.get_elev_json_data(elev_url) # not getting it right, maybe the url
  File "/Users/EstelaRamirez/Desktop/URL.py", line 92, in get_elev_json_data
    if _elev_error_message(elev_json_data):
  File "/Users/EstelaRamirez/Desktop/URL.py", line 81, in _elev_error_message
    if message[0] == 'Error':
IndexError: string index out of range
>>> 
========= RESTART: /Users/EstelaRamirez/Desktop/P3 User_Interface.py =========
Traceback (most recent call last):
  File "/Users/EstelaRamirez/Desktop/P3 User_Interface.py", line 12, in <module>
    import URL
  File "/Users/EstelaRamirez/Desktop/URL.py", line 81
    if message.startswith('Error')
                                 ^
SyntaxError: invalid syntax
>>> 
========= RESTART: /Users/EstelaRamirez/Desktop/P3 User_Interface.py =========
2
Irvine, CA
Los Angeles, CA
http://open.mapquestapi.com/directions/v2/route?key=CsF74gbUMlrJ3VcVtA5gpVpqgbicSGLI&from=Irvine%2C+CA&to=Los+Angeles%2C+CA
2
elevation
elevation
[33.685697, -117.825982, 34.054394, -118.243941]
http://open.mapquestapi.com/elevation/v1/profile?key=CsF74gbUMlrJ3VcVtA5gpVpqgbicSGLI&shapeFormat=raw&latLngCollection=33.685697,-117.825982,34.054394,-118.243941

ELEVATIONS
0
21
1
96
[33.685697, -117.825982, 34.054394, -118.243941]
http://open.mapquestapi.com/elevation/v1/profile?key=CsF74gbUMlrJ3VcVtA5gpVpqgbicSGLI&shapeFormat=raw&latLngCollection=33.685697,-117.825982,34.054394,-118.243941

ELEVATIONS
0
21
1
96

Directions Courtesy of MapQuest; Map Data Copyright OpenStreetMap Contributors.
>>> 
========= RESTART: /Users/EstelaRamirez/Desktop/P3 User_Interface.py =========
2
Irvine, CA
Los Angeles, CA
http://open.mapquestapi.com/directions/v2/route?key=CsF74gbUMlrJ3VcVtA5gpVpqgbicSGLI&from=Irvine%2C+CA&to=Los+Angeles%2C+CA
3
latlong
elevation
elevation

LATLONGS
33.69N -117.83E
34.05N -118.24E
[33.685697, -117.825982, 34.054394, -118.243941]
http://open.mapquestapi.com/elevation/v1/profile?key=CsF74gbUMlrJ3VcVtA5gpVpqgbicSGLI&shapeFormat=raw&latLngCollection=33.685697,-117.825982,34.054394,-118.243941

ELEVATIONS
21
96
[33.685697, -117.825982, 34.054394, -118.243941]
http://open.mapquestapi.com/elevation/v1/profile?key=CsF74gbUMlrJ3VcVtA5gpVpqgbicSGLI&shapeFormat=raw&latLngCollection=33.685697,-117.825982,34.054394,-118.243941

ELEVATIONS
21
96

Directions Courtesy of MapQuest; Map Data Copyright OpenStreetMap Contributors.
>>> 
