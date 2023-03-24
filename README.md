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
- <b>database.py</b> : Creates an sqltie database using sqlalchemy <br>
- <b>schema.py</b> : Contains the description of tables, indexes (metadata) <br>
- <b>models.py</b> : Contains details about tables and their columns that should be created in the database <br>
(I have created empty directories "Templates, Data" for now so that they can be used if the API extends in the future) <br> <br>
 <h3>Methods used and their purposes:</h3>
- <b>Create Details</b> : This method takes username and address as inputs and creates an address list with coordinates from the address into the database. <br>
- <b>Read Details </b>: This method reads the database and returns results based on ID<br>
- <b>Read Details List</b> :Reads the entire database (Select *) <br>
- <b>Update Details </b>: Updates address along with coordinates for the respective address.<br>
- <b>Delete Details </b>: Deletes items from database based on ID<br>
- <b>Read Coordinates </b>: Takes coordinates as Input as returns its respective address from the database.<br>
- <b>Read Coords </b>: This method takes coordinates as Input as returns its respective address/ adresses in its range (default 1km) from the database.<br>

<b>Storing the contents in the database as below </b><br>


<a href="https://drive.google.com/uc?export=view&id=<FILEID>"><img src="https://drive.google.com/uc?export=view&id=1RrH9emM4BmA95ENaJHF_VqY3IdeGHzbM" style="width: 650px; max-width: 100%; height: auto" title="Click to enlarge picture" /> <br>


Used Geopy to convert coordinates from address and vice versa. Followed steps from  <a href="https://geopy.readthedocs.io/en/latest/#">Here</a> <br>



