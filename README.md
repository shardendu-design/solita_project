# solita_project

## Helsinki City Bike App(Dev Academy Pre-assignment)

The application is about importing data from given links and storing them in a database. After importing there should be some action done before storing in a database and displaying it in a web based application.

## Technology Used

### Pragramming Language

#### Python

### Framework

#### Flask,Pandas

### Database

#### PostgreSQL

I have used a condo environment to develop a City Bike application instead of virtualenv. The Conda environment is much smoother than virtualenv and supports most of the dependency itself. To be able to run the project there are some required dependencies that should be installed in env and in the system.

#### 1. Install PostgreSQL on Mac( I am using version 10)
#### 2. Install SQLAlchemy
#### 3. Install psycopg2 inside the env
#### 4. Install Flask-bootstrap
#### 5. Flask and rest of the dependency 

#### Data source

https://dev.hsl.fi/citybikes/od-trips-2021/2021-05.csv

https://dev.hsl.fi/citybikes/od-trips-2021/2021-06.csv

https://dev.hsl.fi/citybikes/od-trips-2021/2021-07.csv

#### Data Import

Donloaded data from above links in csv and store it in a local machine. Since there are three different csv files we need to merge them in one csv file.

![merged data](images/data_merged.png)

Validating data before importing merged csv files. There are few steps for validation of any kind of data before use for a specific purpose.

#### Check data type

![check data](images/check_data_type.png)

#### Check for misssing values

![missing values](images/check_missing_values.png)


#### Check duplicate rows and drop them


![duplicate rows](images/chek_duplicate_rows.png)

#### Don't import journeys that lasted for less than ten seconds

![import less the ten seconds](images/import_less_then_ten.png)

#### Don't import journeys that covered distances shorter than 10 meters

![import shorter the ten meters](images/shorter_then_ten_meters.png)

Now the data has been validated so lets save it as a csv file in the local machine.

![save data csv](images/filtered_data.png)