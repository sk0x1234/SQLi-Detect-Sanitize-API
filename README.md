# SQLi-Detect-Sanitize-API
SQL injection  Detection  FLASK application API ENDPOINT



I used basic SQL injection detection methods like Commenting characters list of [ ' ; ' , '{' , '--'  ] , and also using '  '' OR  to extensions to detect the data validity.  we can extend the detection methods to other patterns by adding the characters to the list of characters.



## RUN

` python app.py ` 

runs on port 4000;     takes input form, and sends POST data to the end point '/v1/sanitized/input/'  and gets json object in returns; 
