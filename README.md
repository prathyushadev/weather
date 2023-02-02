During this project we need to perform Data Modeling, Data Ingestion, Data Analysis and building Rest API
To get the data I have cloned data from https://github.com/corteva/code-challenge-template where there are multiple weather station files from different locations like Nebraska, Iowa, Illinois, Indiana, or Ohio. Multiple weather station files are not segregated to that particular location. So, I have randomly generated each weather station files to the location.

Intially I loaded the weather station files data to a database using dbsqlite. so, here the data is stored in key value pairs where we unique set of record with no redundancy and allocating each record with a particular weather station location. I got the stored all the data in databse with no duplicates.

I am performing data analysis for every year and for every weather station to calculate
Average maximum temperature
Average minimum temperature
Total accumulated precipitation

I have implemented REST API using Django framework for creating two end points
I have perfomred testing by running in my local host location 
/api/weather
To Laod data to database from a file or directory of files

/api/weather/stats
loading data to weather stats successfully 

#Steps to execute

##create venv and activate it

python -m venv proj_name
python -m venv proj_name --system-site-packages
proj_name\Scripts\activate.bat

##go to a particular project(weather) folder

cd weather

##execute the below commands

pip install -r requirements.txt

python manage.py runserver

######Loading data 

python manage.py load_weather --directory=<path of weatherstation files>

#####Calcuate weather stats

python manage.py agg_weather_report  # Weather report based upon data in database



