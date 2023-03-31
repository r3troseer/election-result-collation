## Election Result Collation System

This is a Django-based web application that helps collate election results from polling units across various local governments in Delta State.


**Features**:

- View the result of any individual polling unit.
- View the summed total result of all polling units under any particular local government.
- Store results for all parties for a new polling unit.


**Installation**

1. Clone the repository to your local machine:
```
git clone https://github.com/username/election-result-collation.git
```

2. Install the required Python packages:
```
pip install -r requirements.txt
```

3. Migrate the database:
```
python manage.py migrate
```

4. Run the development server:
```
python manage.py runserver
```

5. Open your web browser and go to http://localhost:8000/ to view the application.


>**Usage**

>>To view the result of any individual polling unit, go to http://localhost:8000/polling-unit-result/?q=`<polling_unit_uniqueid>` where `<polling_unit_uniqueid>` is the unique ID of the polling unit.

>>To view the summed total result of all polling units under any particular local government, go to http://localhost:8000/lga-results/ and select the desired local government from the dropdown list.

>>To store results for all parties for a new polling unit, go to http://localhost:8000/new-polling-unit-result/ and fill out the form.


>**Contributing**

>>Contributions are welcome! If you find any issues or have suggestions for improvement, please create a GitHub issue or submit a pull request.