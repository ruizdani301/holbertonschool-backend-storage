# NoSQL

### Resources
Read or watch:

- NoSQL Databases Explained
- What is NoSQL ?
- Building Your First Application: An Introduction to MongoDB
- MongoDB Tutorial 2 : Insert, Update, Remove, Query
  Aggregation
- Introduction to MongoDB and Python
- mongo Shell Methods
- The mongo Shell

## MongoDB Command File
- All your files will be interpreted/compiled on Ubuntu 18.04 LTS using MongoDB (version 4.2)
- All your files should end with a new line
- The first line of all your files should be a comment: // my comment
- A README.md file, at the root of the folder of the project, is mandatory
- The length of your files will be tested using wc


#### Potential issue if documents creation doesn’t work or this error: Data directory /data/db not found., terminating (source and source)

$ sudo mkdir -p /data/db
Or if /etc/init.d/mongod is missing, please find here an example of the file:

- Click to expand/hide file contents
- Use “container-on-demand” to run MongoDB
- Ask for container Ubuntu 18.04 - MongoDB
- Connect via SSH
  Or via the WebTerminal
- In the container, you should start MongoDB before playing with it: