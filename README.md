# Bouldering API

[GitHub Repository](https://github.com/M-Hawk/API-Web-Server)
## About

Many Australian rock climbers and specifically boulderers are eager to record what they have achieved in their climbing career, or hobby by logging ascents of particular problems and historic routes.

This is done to not only measure their success over time, but also demonstrate their skillset. It also acts as a way to communicate certain nuances of a particular climb and its perceived grading or difficulty to other members of the climbing community.

Many climbing routes are located in undiscovered areas and are completely unknown until someone decides to observe whether there is an achieveable route to the top of the rockface or boulder, in which a climber may either ascend it themselves or document it as a route to be climbed. Historically the first ascensionist gets to name the route.

The issue is, there isn't many ways for boulderers in Australia to log their ascents of problems, a term which is synonymous with route or climb, discuss and find exact locations of the routes and the rock type, grade the level of difficulty, talk about particular nuances to achieve the climb and provide information on area ethics, hazards and changes to the area.

## Aim

The aim of this application is solve the aforementioned issues by providing a means for boulderers to log their ascents, including grading the difficulty, methods of achieving it through descriptions, send type, and discussing changes that may be present.

This solution is implemented through the use of an API Web Application that utilises a database to store information of known routes that have been documented, store users information and their ascents, as well as giving users the ability to access known routes and find them in specific areas.

Users information is protected through the use of authentication methods, such as the implementation of user logins utilising a slow hash password encryption service.

The database is protected and managed by members of the climbing community with administration rights using authorisation to access and modify data through the use of tokens.

## Database

The database management system implemented to govern the data is PostgreSQL, which is a popular open-source Object Relational database system that extends the Structured Query Language or SQL (Editor, 2019).

### **Benefits**

PostreSQL has been chosen due to its many benefits at the expected dataset and user base size. Being a Relational DBMS, PostreSQL offers great scalability to a small to medium-sized database, due to the tendency to house the entire database on a single server. Performance is also excellent for reading & writing data at the expected database size, with good speed for retrieval by implementing join tables and allowing indexing (Editor, 2019).

PostreSQL has many more features to add on top of the standard SQL, and has a simple syntax to utilise CRUD commands throughout the database. This simplicity makes database management very efficient and accurate.

It is also completely open-source and free, and allows users to create their own data types as well as make custom functions to fit their needs. PostgreSQL also supports Geographical objects, which allows developers to cater it for location based services.

The very nature of Relational DBMS create a much easier framework to include greater security measures, due to the relational nature of data within a data set, which by convention creates strong data integrity.
PostreSQL also implements write ahead logging, which ensures data integrity by writing information to secure storage before permanent changes are effected in the database.

### **Drawbacks**

Being open-source has its negatives due to the fact that PostreSQL has no warranty or liability afforded to its users concerning potential issues or errors with the DBMS.

In general not many open-source applications support PostreSQL, which can limit its usage. PostreSQL is also slower than some other DBMS such as MySQL, due to its focus on compatability.

Relational Databases suffer performance issues with larger sets of data due to the inclination to vertically scale, with the entire database generally existing on a singular server, and the ability to increase dataset sizes consists of scaling vertically by adding more CPU, RAM and GPU to a system (Editor, 2019).

Non relational DBMS such as MongoDB, Cassandra and Firebase using noSQL tend to have better larger dataset scalability and performance by horizontally scaling and implementing mulitple servers to the database pool, which share data throughout the network (Editor, 2019).

## ORM

In research from Pedamkar … (2022) Object Relational Mapping is the process where objects are implemented to connect a programming language to database systems, where object-oriented programming concepts can be applied to SQL databases. There are many different ORM packages specific to particular object oriented languages, such as SQL Alchemy's use with Pythons web framework Flask or Hibernate ORM with Java.

### **Key Benefits**

In research from LearnNowOnline … (2012) ORM's work by generating objects to connect with the tables in the database virtually, allowing developers to modify, update, retrive, delete and create data within these tables.

The use of ORM's saves developers time and effort, and by extension reducing overall production cost by allowing them to connect, access and modify a given Database, utilising their preferred development language, often in a more simplistic manner, without the need to even spend time learning SQL. This prevents developers having to write sometimes very long queries or implementations in the native DBMS language.

ORM's also make an application independant of the given DBMS used in the backend, allowing generic queries to be made in the utilised programming language, and if migrating to another database, these queries can easily be modified and reused in another DBMS do to the irrespective nature of these queries Pedamkar … (2022).

ORM's add the benefit of data abstraction which gives a very clear separation of concerns, with the data being housed in a server and managed and accessed using the ORM in a web application.

ORM's are an extension of many programming languages and therefore its very easy to learn the nuances of a particular ORM tool if the language is already known, such as the ability to implement effective testing protocols, and conforming to good code design principles among the many developers that many be working on a project which would otherwise be difficult to achieve utilising the native DBMS SQL.

### **Functionalities**

According to (Session Basics — SQLAlchemy 1.4 Documentation, n.d.)Sessions are a construct of ORM's that establish a connection to a database and allow conversations to occur such as queries between the ORM and the database. A session acts as an interaction in time that holds objects that have been loaded or associated in the sessions lifespan. It initially begins in a stateless manner, where then queries or other changes are effected and then exist in a session to be established as a transaction on a connection with an engine for the duration of the session, until they are either required to commit these changes or abandon the changes for the current transaction.

Sessions track these changes as a single virtual transaction at a time, via use of an object that uses the underlying engine to make real connection transactions within the database (Transactions and Connection Management — SQLAlchemy 1.4 Documentation, n.d.).

ORM's add another layer of protection against SQL injection by reducing explicit SQL queries and giving the ability to add query parameterization, which is a way to create SQL statements in a dynamic manner. By creating a basic query that has placeholders and adding the client side query parameters to the placeholders can help prevent malicious users from corrupting the database (What Is SQL Injection | SQLI Attack Example & Prevention Methods | Imperva, 2021).

## Endpoints

[Endpoints Document for Bouldering API](/docs/endpoints.md)

## ERD

![Entity Relationship Diagram](/docs/T2A2%20ERD%20-%20Database%20ER%20diagram%20(crow's%20foot).png)

## Third Party Services

These third party services were utilised in the production of this API

### Flask

Flask is a micro WSGI web app framework in Python. It allows architecture to be implemented without much boiler plate code, aswell as providing a decent amount of resources for development.

### SQL Alchemy

SQL Alchemy is a Python toolkit and Object Relational Mapper (ORM) that allows developers to utilise and access SQL Databases, using a connection capability called psycopg2.

### Flask-SQLAlchemy

This Service allows Flask to be utilised using the ORM SQL Alchemy library for effective SQL management.

### Marshmallow

Marshmallow is an ORM Python framework-agnostic library for converting complex datatypes, such as objects, to and from native Python datatypes.
It has a extensive library for utilising Schemas and model relations aswell as providing excellent JSON displays.

### Flask-Marshmallow

It is a minor integration layer for Flask to add marshmallow features to Flask.

### Marshmallow-SQLAlchemy

Integrates Marshmallow and SQLAlchemy, allows SQLAlchemy to utilise Marshmallow's d,serialisation libraries.

### JWT

JSON Web Tokens are an industry standard authentication token service for Web Applications, that allows the secure transmission of data between entities over the internet. It uses a secret key algorithm to serialize and deserialize the token information.

### BCrypt

BCrypt is a password hashing function that protects against malicious attacks. And uses a SHA-256-based hash algorithm to encode passwords.

## Models & Relationships

The models used replicate data from the given ERD and uses python data types through SQL Alchemy to achieve an accurate representation of the expected data in SQL.

Each primary key provided in every entities model is an automatic serialised sequence when the creation of an object entity occurs. Every model that has a foreign key associated must reference the primary key of its expected corresponding model.

Inclusions in entities model attributes:

1. *nullable=False* if a model contains nullable equal false property, that attribute must be given when creating that model object
2. *unique=True* if a model contains unique equals true, any other model of the same object type must have a different given entry, which also must be unique
3. *primary_key=True* The attribute that contains this is the primary key that other models reference with their foreign keys
4. *db.ForeignKey("object.primary_key")* If an attribute contains this its foreign key relates to another models primary key
5. *back_populates = "object"* the object that a relation is bound to
6. *cascade="all, delete"* provided in the relationship keyword, if this is set, the objects that related to the instance of the object defined in back_populates will all be deleted. This prevents data corruption.

Marshmallow Schemas utilise the given data from the models to interact with the user requests, validate incoming data and provides the ability to create effective responses to be formatted and given back to the user.

The fields variable represents all the information from the given model to be validated and represented as the JSON request and reponse. The ordered keyword determines that the fields will be displayed in the listed order.

### **Climbers**

The Climbers model has a relationship with the Ascents model, many ascents can reference a climber and if a climber object is deleted so too will its related Ascents. It also has the Boolean Admin which gives certain rights to perform particular operations within the database.

**Model**

1. *climber_id* = db.Column(db.Integer, primary_key=True)
2. *admin* = db.Column(db.Boolean(), default=False)
3. *user_name* = db.Column(db.String(100), nullable=False, unique=True)
4. *password* = db.Column(db.String, nullable=False)
5. *first_name* = db.Column(db.String(50), nullable=False)
6. *last_name* = db.Column(db.String(80), nullable=False)
7. *email_address* = db.Column(db.String, nullable=False, unique=True)
8. *created* = db.Column(db.Date)
9. *ascents* = db.relationship("Ascent", back_populates = "climber", cascade="all, delete")

**Schema**

When a climber schema is presented as a JSON response, it includes the Schema of the Ascents model that is related to it via its foreign key and displays that information. It notably also excludes climber to prevent a nested climber schema of the same climber from being displayed.

1. *ascents* = fields.List(fields.Nested("AscentSchema", exclude=["climber"]))
2. *fields* = ("climber_id", "admin", "user_name", "password", "first_name", "last_name", "email_address", "ascents")

### **Ascents**

The Ascent model is related to climbers and problems through its foreign keys.

**Model**

1. *ascent_id* = db.Column(db.Integer, primary_key=True)
2. *tick_type* = db.Column(db.String, nullable=False, default=VALID_TICK_TYPES[0])
3. *comments* = db.Column(db.Text)
4. *created* = db.Column(db.Date)
5. *climber_id* = db.Column(db.Integer, db.ForeignKey("climbers.climber_id"), nullable=False)
6. *problem_id* = db.Column(db.Integer, db.ForeignKey("problems.problem_id"), nullable=False)
7. *problem* = db.relationship("Problem", back_populates="ascents")
8. *climber* = db.relationship("Climber", back_populates="ascents")

**Schema**

When an Ascents schema is presented as a JSON response, it includes the Schemas of the Climbers and Problems models that are related to it via its foreign keys and displays that information.

1. *problem* = fields.Nested("ProblemSchema", only=["problem_id", "problem_name", "v_grade"])
2. *climber* = fields.Nested("ClimberSchema", only=["climber_id", "user_name"])
3. *fields* = ("ascent_id", "climber", "problem", "tick_type", "comments", "created")

### **Problems**

The Problem model is related to ascents through ascents foreign key, and sectors its own foreign key.  A problem model can have many ascents and a sector can have many problems.

It also contains hybrid_properties that interpolate strings onto the given data type for JSON requests and responses.

**Model**

1. *problem_id* = db.Column(db.Integer, primary_key=True)
2. *problem_name* = db.Column(db.String(50), nullable=False)
3. *grade* = db.Column(db.Integer)
4. *surface_type* = db.Column(db.String(50))
5. *description* = db.Column(db.Text)
6. *access* = db.Column(db.Text)
7. *height_metres* = db.Column(db.Integer)
8. *comments* = db.Column(db.Text)
9. *created* = db.Column(db.Date)
10. *sector_id* = db.Column(db.Integer, db.ForeignKey("sectors.sector_id"), nullable=False)
11. *sector* = db.relationship("Sector", back_populates="problems")
12. *ascents* = db.relationship("Ascent", back_populates="problem", cascade="all, delete")

@hybrid_property
def v_grade (self):
    return f"V{self.grade}"

@hybrid_property
def height (self):
    return f"{self.height_metres} Metres"

**Schema**

When an Problem schema is presented as a JSON response, it includes the Schemas of the Ascents linked to its model and that ascents climber which is nested.

1. *ascents* = fields.List(fields.Nested("AscentSchema", exclude=["ascent_id", "problem"]))
2. *fields* = ("problem_id", "problem_name", "v_grade", "surface_type", "description", "access", "height", "comments", "sector_id", "ascents")

### **Sectors**

The Sector model is related to problems through its foreign key. A sector model can belong to an area and a sector can have many problems.

It contains hybrid_properties that interpolate strings onto the given data type for giving accurate latitude and longitude information for Australian Users in the JSON requests and responses.

**Model**

1. *sector_id* = db.Column(db.Integer, primary_key=True)
2. *sector_name* = db.Column(db.String(50), nullable=False)
3. *description* = db.Column(db.Text)
4. *access* = db.Column(db.Text)
5. *latitude* = db.Column(db.Float(precision=6))
6. *longitude* = db.Column(db.Float(precision=6))
7. *created* = db.Column(db.Date)
8. *area_id* = db.Column(db.Integer, db.ForeignKey("areas.area_id"), nullable=False)
9. *area* = db.relationship("Area", back_populates="sectors")
10. *problems* = db.relationship("Problem", back_populates="sector", cascade="all, delete")

@hybrid_property
def latitude_south (self):
    return f"{self.latitude} South"

@hybrid_property
def longitude_east (self):
    return f"{self.longitude} East"

**Schema**

When an Sector schema is presented as a JSON response, it includes the Schemas of the Problems linked to its model and excludes the ascents of those problems in the problems model.

1. *problems* = fields.List(fields.Nested("ProblemSchema", exclude=["ascents"]))
2. *fields* = ("sector_id", "sector_name", "description", "access", 
        "latitude_south", "longitude_east", "area_id", "problems")

### **Areas**

The Areas model is related to the sectors model through its foreign key. An area model can belong to a state and a area can have many sectors.

It contains the same hybrid_properties as sectors for latitude and longitude that interpolate strings onto the given data type for JSON requests and responses.

**Model**

1. *area_id* = db.Column(db.Integer, primary_key=True)
2. *area_name* = db.Column(db.String(50), nullable=False)
3. *description* = db.Column(db.Text)
4. *ethics* = db.Column(db.Text)
5. *access* = db.Column(db.Text)
6. *latitude* = db.Column(db.Float(precision=6))
7. *longitude* = db.Column(db.Float(precision=6))
8. *created* = db.Column(db.Date)
9. *state_id* = db.Column(db.Integer, db.ForeignKey("states.state_id"), nullable=False)
10. *state* = db.relationship("State", back_populates="areas")
11. *sectors* = db.relationship("Sector", back_populates="area", cascade="all, delete")

@hybrid_property
def latitude_south (self):
    return f"{self.latitude} South"

@hybrid_property
def longitude_east (self):
    return f"{self.longitude} East"

**Schema**

When an Area schema is presented as a JSON response, it includes the Schemas of the Sectors linked to its model and excludes the problems of those sectors in the problems model.

1. *sectors* = fields.List(fields.Nested("SectorSchema", exclude=["problems"])))
2. *fields* = ("area_id", "area_name", "description", "ethics", "access", "latitude_south", "longitude_east", "state_id", "sectors")

### **States**

The States model is related to the areas model through its foreign key. An state model can have many areas and is the parent of all other entities in the model relationship. Excluding the climber users.

**Model**

1. *state_id* = db.Column(db.Integer, primary_key=True)
2. *state_name* = db.Column(db.String(50), nullable=False)
3. *state_acronym* = db.Column(db.String(10), nullable=False)
4. *created* = db.Column(db.Date)
5. *areas* = db.relationship("Area", back_populates="state", cascade="all, delete")

**Schema**

When an State schema is presented as a JSON response, it includes the Schemas of the Areas linked to its model and excludes the problems of those areas in the problems model.

1. *areas* = fields.List(fields.Nested("AreaSchema", exclude=["state_id", "sectors"]))
2. *fields* = ("state_id", "state_name", "state_acronym", "areas")

## Database Relations

To ensure an accurate representation of the database to be implemented programmatically, an Entity relationship diagram was produced representing relationships between entities. The following information was considered when constructing the relationship diagram.

### **Entities**

**Climbers**

In order for application users to be able to log their ascents of particular climbs, they would need to be able to store these ascents in relationship to their personal account. Therefore a user table was required named "Climbers", which holds pertinent information relating to an individual account. An individual climber account has a relationship with the entity "Ascents" a climber can have zero or many "Ascents", depending on how many ascents they have logged.

Attributes of a climber include:

1. *climber_id*, the primary key for a climber
2. *admin*, which determines what rights a climber have granted within the db and if they are an administrator or not
3. *user_name*, holds a given climbers username
4. *password*, holds a climbers password to ensure accurate authentication
5. *first_name*, the first name of the climber
6. *last_name*, the last name of the climber
7. *email_address*, the climbers email address for contact
8. *created*, timestamp of when the account was created

**Ascents**

The Ascents entity represents the table containing information relating to a climbers experience of a particular problem and is required for a user to log their ascents. This entity relates to the Climbers entity and the Problems entity, and represents a join table between the two. An ascent can have one and only one climber, as in order for it to exist an individual climber must log it to be so, and an Ascent can have one and only one problem, as an individual ascent relates to an individual problem.

Attributes of an ascent entity include:  

1. *ascent_id*, the primary key which identifies a particular ascent by id  
2. *climber_id*, the foreign key which maps to the primary key in the climbers entity in order to determine the climber who logged this ascent
3. *problem_id*, the foreign key which maps an ascent to a particular problem
4. *tick_type*, represents how an ascent was climbed, i.e was it climbed first go ?, second go or did they receive help or are they currently projecting the problem
5. *comments*, allows a climber to describe particular points of note about a climb, their perception of the grade of difficulty and potential hazards or changes
6. *created*, timestamp of when the ascent was created

**Problems**

The Problems entity contains all the attributes relating to a particular "problem" or sometimes called a route, and is required to hold all the information about the problems that climbers ascend. Problems are related to the ascents entity for climbers to log their ascents, and the sectors entity which contains a group of problems. A problem can have zero of multiple ascents, that is zero or many people could climb this problem, and a problem belongs to one and only one bouldering sector.

Attributes of a problem include:

1. *problem_id*, a primary key that identifies a specific problem
2. *sector_id*, a foreign key , that relates a problem to a particular sector in the sector entity using its sector_id.
3. *problem_name* holds the name of the particular problem
4. *grade* represents the difficulty of the climb in the typical bouldering V scale
5. *surface_type*, represents a particular type of rock or surface being climbed such as granite, limestone, sandstone etc
6. *description*, provides information to climbers about the history and technical aspects of the climb
7. *access*, displays how a climber can find a particular problem, is there a path, is it overgrown, how far is it from an areas entry location
8. *height_metres*, the height of a particular problem in metres, rounded up if between two integers for safety
9. *comments*, information on methods, hazards and changes that may have occured to a particular problem
10. *created*, timestamp of when the problem was created

**Sectors**

The Sectors entity represents a collection of problems located within a greater geographical area of many boulders, as a group of boulders may be spread far about over a reasonable distance, a sector is briefly a general collection of a group of boulders, that have problems on them. This entity is required to store information that is pertinent to a group of problems that may change over time within its sector. The sectors entity is related to the problems entity and the areas entity. A sector can have one or many problems within it, as if there was zero it would not be listed, and a sector can only be a part of one and only one area as its location cannot change.

Attributes of an sector include:

1. *sector_id*, which is the primary key that identifies a particular area of boulders
2. *area_id*, a foreign key that relates to the area entity through its primary key area_id, as sectors are located within areas
3. *sector_name*, an attribute that holds the name of a particular bouldering sector
4. *description*, general information of a particular area, including its history and topography
5. *access*, this attribute provides information to find this group of boulders within a climbing area
6. *latitute*, provides up to a six decimal latitudinal geographic reference, suffixed by South for Australia
7. *longitude*, provides up to a six decimal longitudinal geographic reference, suffixed by East for Australia
8. *created*, timestamp of when the area was created

**Areas**

The Areas entity represents a collection of sectors located in a particular area of the country, and is required to store information that is pertinent to a group of sectors and their problems. The areas entity is related to the sectors entity and the states entity. An area can have one or many sectors within in, as if there was zero it would not be listed, and an area belongs to one and only one state as its location does not change.

Attributes of an area include:

1. *area_id*, which is the primary key that identifies a particular area of boulders
2. *state_id*, a foreign key that relates to the states entity through its primary key state_id, as areas are located within states
3. *area_name*, an attribute that holds the name of a particular bouldering area
4. *description*, general information of a particular area, including its history and topography
5. *ethics*, ethics that pertain to a particular climbing area such as expectations for noise, littering, no go areas and spiritual locations
6. *access*, this attribute provides information to find and park in a specific climbing area, or a general mustering point
7. *latitute*, provides up to a six decimal latitudinal geographic reference, suffixed by South for Australia
8. *longitude*, provides up to a six decimal longitudinal geographic reference, suffixed by East for Australia
9. *created*, timestamp of when the area was created

**States**

The State entity lists all the states and territories of Australia, separating states allows areas to reference a states id, in the unlikely chance a state or territory changes name or is modified. A state can have zero or many bouldering areas within it.

Attributes of a state include:

1. *state_id*, the primary key that identifies a particular state or territory in Australian
2. *state_name*, the name assosciated with a particular state_id
3. *state_acronym*, the acroynm of a state_name
4. *created*, timestamp of when the area was created

## Project Management

During the project planning stage it was determined that production would be broken down into phases to achieve better management of the tasks required utilising an agile software development life cycle methodology. These phases are listed below:

### **Analysis Phase**

**Idea**

The Aim of this project is to provide better access for Australian Rock Climbers, and in particular those who participate in the style of Bouldering to be able to have access to a tracking system, that logs their climbing and achievements as well as giving them the ability to access a database of information relating to the routes or problems, by seeking information on locations, difficulty and other pertinent information relevant to a particular route.

The database is aimed to be mananged by members of the climbing community who have administration rights to ensure quality data integrity and resolve and issues that may arise.

**Requirements**

Prior to design, a list of requirements have been determined that will achieve the aforementioed goal.

1. A Project management software is to be implemented to ensure good management of tasks and required outcomes. In order to achieve good time management an Agile methodology is to be utilised.

2. Creation of an ERD to indentify database requirements and expected relationships between entities: Users, Ascents, Routes/Problems and Areas.

3. A Database management system is required to manage all the expected data for the users. The total user base at this stage is not expected to rise above a single server requirement. The users will interact in a relational manner with other entities of the database, therefore a Relational DBMS should be utilised.

4. The programming language utilised should have the required addons and frameworks to achieve the desired outcome, be simplistic in syntax and easy to understand to ensure good code design. The potential of administrators managing the database in the climbing community is subject to change, therefore new developers may be required to be trained, which gives higher consideration to a simplistic approach.

5. The expected user base is to interact with the product in a web application through a browser, therefore a web application framework is required to achieve this.

6. To accurately manage incoming and outgoing requests to the database and ensure data integrity is effectively managed and responses are sent in an expected manner, an Application Programming Interface (API) should be utilised.

7. In order to protect user information and give the correct access to administrators, user authentication and authorisation is required.

8. Incoming user requests are to be validated to prevent unexpected behaviour and potential malicious attacks against the database and its contents.

9. At this stage there is no requirement for a front end framework, as this will be implemented at a later stage.

### **Design Phase**

1. In order to track stages of development, it is determined that the agile methodology of Kanban is used, breaking tasks down into smaller stages to be implemented in sprints to ensure effective time management. This will be tracked using Trello and tasks will be separated into cards with specific expectations and time requirements. Github is to be utilised to protect progress throughout the implementation process.

2. Construction of an ERD utilising LucidChart for simplistic UI and efficient and clear relational notation.

3. The RDBMS utilised is PostgreSQL due to its extensive extensions of the SQL language and simple commands to achieve CRUD operations. PostgreSQL is also excellent for a small to medium user base with high query performance at the expected user level.

4. Python has been chosed as the development language due to its simplicty and extensive extensions including efficient and flexible web frameworks of a project at this size.

5. Utilising its native language of Python the web framework decided to manage the backend is Flask. Flask is a robust extensible web framework with support to manage databases in a secure manner. With add ons such as Marshmallow and the ORM SQL Alchemy allows efficient and secure querying of the database with the ability to create paramaterized CRUD operations tohelp prevent malicous attacks.

6. The restful design architecture methodology in an API is to be used to ensure accurate and congruent data to the front end utilising a JSON format. The MVC architecture will also be implemented to create a separation of concerns within the development process and adding a simplistic file structure allows debugging and maintenance to be achieved by a relatively small number of developers.

7. To ensure authentication and authorisation for users and administrators, JWT tokens are to be implemented in the design process.

8. During the later stages of development user validation wil be vetted using Flask/Marshmallows inbuilt packages, ensuring only expected input is received to the database.

9. Currently no Front End Framework has been identified and is to be considered once a working implementation of the API is achieved.

### **Implementation Phase**

1. Create Project Management Software Trello board for task tracking throughout the implementation phase.
2. Create ERD to determine database structure and implementation
3. Create file structure adhering to MVC architecture protocols
4. Initialise Github repository and conduct regular commits throughout implementation
5. Install all required Software, Programs and add ons including Flask, Marshmallow, SQLAlchemy, PostreSQL
6. Create virtual environment & utilities, requirements.txt, gitignore, pycache, env, and sample files.
7. Construction of a simple Flask application to ensure expected behaviour
8. Develop SQL Alchemy models from developed ERD
9. Creation of Controllers and Blueprints
10. Marshmallow Schema creation
11. Creation of Routes and Endpoints including all CRUD operations
12. Authentication and Authorisation
13. CLI command creation for testing phase

### **Testing Phase**

1. Test CLI commands to ensure database is represented as expected
2. Test all expected output is in JSON format
3. Test authorisation and authentication
4. Test all CRUD commands
5. Test all user input is valid

### **Deployment**

Deployment is to be postponed until a suitable Front End Framework is identified post API development and testing.

### **Maintenance Phase**

Maintenance will be conducted at regular intervals by administrators utilising the steps expressed in the testing phase. Furthermore, administrators will regularly check for potential misuse and malicious interference of the database. As well as keeping track of user numbers to determine scalability requirements.

[Project Management Software Link](https://trello.com/b/r5QgFhTp/t2a2-web-api)

Add photos of trello board here

![Early Stage Trello Board](/docs/Early%20Stage%20Trello%20Board.png)
![Middle Stage Trello Board](/docs/Trello%20Board%20Three.png)
![Completed Trello Board](/docs/Trello%20Board%20Complete.png)

## Setup Requirements

* Fork or Clone Repository
* Ensure environment variables are set correctly
* Install & Activate virtual machine
* Install Dependencies in requirements.txt
* use command flask run in src/ folder
* Hosted on http://127.0.0.1:8080
* Test data is located under controllers/cli_commands.py
* flask db drop && flask db create && flask db seed
* test endpoints using  https://www.postman.com/

## Author

Matthew Hawkins

## References

[Editor. (2019, October 15). Comparing Database Management Systems: MySQL, PostgreSQL, MSSQL Server, MongoDB, Elasticsearch and others. AltexSoft.](https://www.altexsoft.com/blog/business/comparing-database-management-systems-mysql-postgresql-mssql-server-mongodb-elasticsearch-and-others/)

[Pedamkar, P. (2022, June 21). What is ORM? EDUCBA.](https://www.educba.com/what-is-orm/)

[LearnNowOnline. (2012, August 28). Proven eLearning for Individuals to Enterprise.](https://www.learnnowonline.com/blogs/2012/08/28/4-benefits-of-object-relational-mapping-orm)

[Session Basics — SQLAlchemy 1.4 Documentation. (n.d.). Retrieved November 5, 2022, from](https://docs.sqlalchemy.org/en/14/orm/session_basics.html)

[Transactions and Connection Management — SQLAlchemy 1.4 Documentation. (n.d.). Retrieved November 4, 2022, from](https://docs.sqlalchemy.org/en/14/orm/session_transaction.html)

[What is SQL Injection | SQLI Attack Example & Prevention Methods | Imperva. (2021, March 11). Learning Center.](https://www.imperva.com/learn/application-security/sql-injection-sqli/)

https://www.thecrag.com/en/climbing/australia/black-range-bouldering