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

The database management system implemented to govern the data is PostgreSQL, which is a popular open-source Object Relational database system that extends the Structured Query Language or SQL.

### **Benefits**

PostreSQL has been chosen due to its many benefits at the expected dataset and user base size. Being a Relational DBMS, PostreSQL offers great scalability to a small to medium-sized database, due to the tendency to house the entire database on a single server. Performance is also excellent for reading & writing data at the expected database size, with good speed for retrieval by implementing join tables and allowing indexing.

PostreSQL has many more features to add on top of the standard SQL, and has a simple syntax to utilise CRUD commands throughout the database. This simplicity makes database management very efficient and accurate.

It is also completely open-source and free, and allows users to create their own data types as well as make custom functions to fit their needs. PostgreSQL also supports Geographical objects, which allows developers to cater it for location based services.

The very nature of Relational DBMS create a much easier framework to include greater security measures, due to the relational nature of data within a data set, which by convention creates strong data integrity.
PostreSQL also implements write ahead logging, which ensures data integrity by writing information to secure storage before permanent changes are effected in the database.

### **Drawbacks**

Being open-source has its negatives due to the fact that PostreSQL has no warranty or liability afforded to its users concerning potential issues or errors with the DBMS.

In general not many open-source applications support PostreSQL, which can limit its usage. PostreSQL is also slower than some other DBMS such as MySQL, due to its focus on compatability.

Relational Databases suffer performance issues with larger sets of data due to the inclination to vertically scale, with the entire database generally existing on a singular server, and the ability to increase dataset sizes consists of scaling vertically by adding more CPU, RAM and GPU to a system.

Non relational DBMS such as MongoDB, Cassandra and Firebase using noSQL tend to have better larger dataset scalability and performance by horizontally scaling and implementing mulitple servers to the database pool, which share data throughout the network.

## ORM

Object Relational Mapping is the process where objects are implemented to connect a programming language to database systems, where object-oriented programming concepts can be applied to SQL databases. There are many different ORM packages specific to particular object oriented languages, such as SQL Alchemy's use with Pythons web framework Flask or Hibernate ORM with Java.

### **Key Benefits**

ORM's work by generating objects to connect with the tables in the database virtually, allowing developers to modify, update, retrive, delete and create data within these tables.

The use of ORM's saves developers time and effort, and by extension reducing overall production cost by allowing them to connect, access and modify a given Database, utilising their preferred development language, without the need to even spend time learning SQL. This prevents developers having to write sometimes very long queries or implementations in the native DBMS language.

ORM's also make an application independant of the given DBMS used in the backend, allowing generic queries to be made in the utilised programming language, and if migrating to another database, these queries can easily be modified and reused in another DBMS.

ORM's add the benefit of data abstraction which gives a very clear separation of concerns, with the data being housed in a server and managed and accessed using the ORM in a web application.

ORM's are an extension of many programming languages and therefore its very easy to learn the nuances of a particular ORM tool if the language is already known, such as the ability to implement effective testing protocols, and conforming to good code design principles among the many developers that many be working on a project which would otherwise be difficult to achieve utilising the native DBMS SQL.

## Endpoints

## ERD

## Third Party Services

## Models & Relationships

## Database Relations

## Project Management

## Resources

## Tech-Stack

## Author

Matthew Hawkins
