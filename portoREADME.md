We have provided an accurate dataset describing a complete year (from 01/07/2013 to 30/06/2014) of the trajectories for all the 442 taxis running in the city of Porto, in Portugal (i.e. one CSV file named "portugalTaxi.csv"). These taxis operate through a taxi dispatch central, using mobile data terminals installed in the vehicles. We categorize each ride into three categories:

A) taxi central based, B) stand-based or C) non-taxi central based. For the first, we provide an anonymized id, when such information is available from the telephone call. The last two categories refer to services that were demanded directly to the taxi drivers on a B) taxi stand or on a C) random street.

Each data sample corresponds to one completed trip. It contains a total of 
9 (nine) features, described as follows:

1. TRIP_ID: (`String`) It contains an unique identifier for each trip;
2. CALL_TYPE: (`char`) It identifies the way used to demand this service. It may contain one of three possible values:
    - "A" if this trip was dispatched from the central;
    - "B" if this trip was demanded directly to a taxi driver on a specific stand;
    - "C" otherwise (i.e. a trip demanded on a random street).
3. ORIGIN_CALL: (`integer`) It contains an unique identifier for each phone number which was used to demand, at least, one service. It identifies the trip’s customer if CALL_TYPE="A". Otherwise, it assumes a NULL value;
4. ORIGIN_STAND: (`integer`) It contains an unique identifier for the taxi stand. It identifies the starting point of the trip if CALL_TYPE="B". Otherwise, it assumes a NULL value;
5. TAXI_ID: (`integer`) It contains an unique identifier for the taxi driver that performed each trip;
6. TIMESTAMP: (`integer`) Unix Timestamp (in seconds). It identifies the trip’s start; 
7. DAYTYPE: (`char`) It identifies the daytype of the trip’s start. It assumes one of three possible values:
    - "B" if this trip started on a holiday or any other special day (i.e. extending holidays, floating holidays, etc.);
    - "C" if the trip started on a day before a type-B day;
    - "A" otherwise (i.e. a normal day, workday or weekend).
8. MISSING_DATA: (`Boolean`) It is "FALSE" when the GPS data stream is complete and "TRUE" whenever one (or more) locations are missing
9. POLYLINE: (`String`): It contains a list of GPS coordinates (i.e. WGS84 format) mapped as a string. The beginning and the end of the string are identified with brackets (i.e. [ and ], respectively). Each pair of coordinates is also identified by the same brackets as [LONGITUDE, LATITUDE]. This list contains one pair of coordinates for each 15 seconds of trip. The last list item corresponds to the trip’s destination while the first one represents its start;
