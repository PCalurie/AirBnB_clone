# 0x00. AirBnB clone - The console

![python](https://media.istockphoto.com/id/1045287634/photo/airbnb-amazon-ebay-news-and-other-apps-on-iphone-screen.jpg?s=612x612&w=0&k=20&c=f0e0WqGf9KZ12Cxg-Eg383aKuzbyamYsJWrkchWQ75w=)

This is part of a bigger pie of the [AirBnb](https://www.airbnb.com/) application that links travelers with airbnbs of their taste and choice.
This is the first part of the AirBnB clone project where we worked on the backend of the project whiles interfacing it with a console application with the help of the cmd module in python.

Data (python objects) generated are stored in a json file and can be accessed with the help of the json module in python
## Files created
- `3. BaseModel` - Dynamically initializes instances attributes with datetime methods
	or else
	- it assigns a unique id of the created instance and makes sure its in a string format
	- it assignes **creted_at** and **updated_at** with the current *datetime*
	- we create a new instance of the class and store it in memory
	- **__str__** prints the class name id and its dictionary attributes
	- **save(self)** saves the public attribute *update_time* with the current *datetime*
	- **to_dict** method makes sure we have a copy of the dictionary attributes first before we modify them
	- adds the name of the class key to a dictionary as a string
	- prints datetime in a string format and returns the new modified dictionary

- `4. Create BaseModel from dictionary` - completes `3. BaseModel`

- `5. Store first object` 
	- **all(self)**: returns all the dictionary objects stored in  __objects
	- **new(self, obj)**: returns the name and id of the of the objects created
	- **save(self)**: - opens a file with write permissions
		- creates a new dictionary *d* with *to_dict* method
		- *json.dump* function serializes the dictionary *d* and writes to a json file
	- **reload(self)** - opens the json file with read permissions
		- retrieves the class constructors
		- creates a new instance from the dict attributes
		- passes the new instance as new key words

- `models/__init__.py`
	- it imports *FileStorage* of the serialized data as objects
	- assignes storage variable to the instance created by FileStorage
	- reloads data from the file and stores it into the apps memory

- `console.py`
	- This is a command line intepreter file suitable for easier debugging and better understanding of how the programme works
	- create: Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id
	- show: Prints the string representation of an instance based on the class name and id.
	- destroy: Deletes an instance based on the class name and id
	- all: Prints all string representation of all instances based or not on the class name.
	- update: Updates an instance based on the class name and id by adding or updating attribute

![python](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2018/6/815046647d23428a14ca.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20230812%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230812T101323Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=7721839cc7d9bc131240e215f6df3891abcb5c37bbe55e60aa9d1df55d9841b3)
