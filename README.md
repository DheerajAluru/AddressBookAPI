# AddressBookAPI
 
 This is an API based on FASTAPI and Sqlite3 (From SQLAlchemy) that takes addesses of locations and stores their corresponding coordinates(latitude,longitude positions) in the database.<br>
 
This API currently takes 2 inputs. (Username & Address) <br>

<h3> Steps to use this API: </h3> 
<h3>- Packages needed: </h3> 
(Having a virtual enviroment is preferable) <br>
 -FASTPI <br>
 -Pydantic <br>
 -Uvicorn <br>
 -geopy <br>
 Sqlalchemy <br>
 
You can Install these packages using pip Or install from requirements using below command <br>
 <a href="#">pip install -r requirements.txt</a> <br>
<h3> Files list</h3>
- <b>database.py : Creates an sqltie database using sqlalchemy <br>
- schema.py : Contains the description of tables, indexes (metadata) <br>
- models.py : Contains details about tables and their columns that should be created in the database <br>
(I have created empty directories "Templates, Data" for now so that they can be used if the API extends in the future) <br> <br>

Methods used and their purposes:<br>
- Create Details : This method takes username and address as inputs and creates an address list with coordinates from the address into the database. <br>
- Read Details : This method reads the database and returns results based on ID<br>
- Read Details List :Reads the entire database (Select *) <br>
- Update Details : Updates address along with coordinates for the respective address.<br>
- Delete Details : Deletes items from database based on ID<br>
- Read Coordinates : Takes coordinates as Input as returns its respective address from the database.<br>
- Read Coords : This method takes coordinates as Input as returns its respective address/ adresses in its range (default 1km) from the database.<br>

Used Geopy to convert coordinates from address and vice versa. Followed steps from  <a href="https://geopy.readthedocs.io/en/latest/#">Here</a> <br>



