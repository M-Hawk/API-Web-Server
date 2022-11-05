# Bouldering API

## About

Many Rock Climbers are eager to record what they have achieved in their climbing career or hobby by logging ascents of particular problems and historic routes.

This is done to not only measure their success over time, but also demonstrate their skillset. It also acts as a way to communicate certain nuances of a particular climb and its perceived grading or difficulty to other members of the climbing community.

Many climbing routes are located in undiscovered areas and are completely unknown until someone decides to observe whether there is an achieveable route to the top of the rockface or boulder, in which a climber may either ascend it themselves or document it as a route to be climbed. Historically the first ascensionist gets to name the route.

The problem is, there isn't many ways for climbers to log their ascents of routes, discuss and find exact locations of the routes and the rock type, grade the level of difficulty, talk about particular nuances to achieve the climb and provide information on area ethics, hazards and changes to the area.

## Aim

The aim of this application is solve the aforementioned issues by providing a means for climbers to log their ascents, including grading the difficulty, methods of achieving it through descriptions, send type, and discussing changes that may be present.

This solution is implemented through the use of an API Web Application that utilises a database to store information of known routes that have been documented, store users information and their ascents, as well as giving users the ability to access known routes and add their own found routes to the database.

Users information is protected through the use of authentication and authorisation methods, such as the implementation of user logins, and authorisation to access and modify data through the use of tokens.

The database is protected and managed by members of the climbing community with administration rights.

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

## ERD

## Third Party Services

## Models & Relationships

## Database Relations

## Project Management

During the project planning stage it was determined that production would be broken down into phases to achieve better management of the tasks required utilising an agile software development life cycle methodology. These phases are listed below:

### **Analysis Phase**

**Idea**

The Aim of this project is to provide better access for Rock Climbers, and in particular those who participate in the style of Bouldering to be able to have access to a tracking system, that logs their climbing and achievements as well as giving them the ability to access a database of information relating to the routes or problems, by seeking information on locations, difficulty and other pertinent information relevant to a particular route, and giving them the ability to add additional routes to the database for the benefit of all.

The database is aimed to be mananged by members of the climbing community who have administration rights to ensure quality data integrity and resolve and issues that may arise.

**Requirements**

Prior to design, a list of requirements have been determined that will achieve the aforementioed goal.

1. A Project management software is to be implemented to ensure good management of tasks and required outcomes. In order to achieve good time management an Agile methodology is to be utilised.

2. Creation of an ERD to indentify database requirements and expected relationships between entities: Users, Ascents, Routes/Problems and Locations.

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

![Early Stage Trello Board](/docs/Early Stage Trello Board.png)

## Resources

## Tech-Stack

## Author

Matthew Hawkins

## References

[Editor. (2019, October 15). Comparing Database Management Systems: MySQL, PostgreSQL, MSSQL Server, MongoDB, Elasticsearch and others. AltexSoft.](https://www.altexsoft.com/blog/business/comparing-database-management-systems-mysql-postgresql-mssql-server-mongodb-elasticsearch-and-others/)

[Pedamkar, P. (2022, June 21). What is ORM? EDUCBA.](https://www.educba.com/what-is-orm/)

[LearnNowOnline. (2012, August 28). Proven eLearning for Individuals to Enterprise.](https://www.learnnowonline.com/blogs/2012/08/28/4-benefits-of-object-relational-mapping-orm)

[Session Basics — SQLAlchemy 1.4 Documentation. (n.d.). Retrieved November 5, 2022, from](https://docs.sqlalchemy.org/en/14/orm/session_basics.html)

[Transactions and Connection Management — SQLAlchemy 1.4 Documentation. (n.d.). Retrieved November 4, 2022, from](https://docs.sqlalchemy.org/en/14/orm/session_transaction.html)

[What is SQL Injection | SQLI Attack Example & Prevention Methods | Imperva. (2021, March 11). Learning Center.](https://www.imperva.com/learn/application-security/sql-injection-sqli/)
