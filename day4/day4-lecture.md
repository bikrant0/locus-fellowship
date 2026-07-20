# What a database actually give you.


# PRimary key
Unique key identifier

# Foreign Key


# SQL - main four commands
## INSERT **- adds a row.**
- INSERT INTO projects (title, owner_id)
- VALUES ('Weather App', 1);

## SELECT **- reads rows.**
- SELECT * FROM projects
- WHERE owner_id = 1;

## UPDATE **- change a row**
- UPDATE projects SET status = 'shipped'
- WHERE id = 3;

## DELETE **- remove a row**
- DELETE FROM projects
- WHERE id = 3;


SqLite 
▸ Data is structured & related
▸ Strong consistency & integrity
▸ Powerful queries with JOINs
▸ Postgres, MySQL, SQLite

PostgreSQL
▸ Data is fluid or unstructured
▸ Scales horizontally with ease
▸ Fast for simple lookups
▸ MongoDB, Redis, Firebase

Runs


ORM
Saving data to the 