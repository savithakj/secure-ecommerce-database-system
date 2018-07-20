# README

The web application is built on Ruby on Rails with Postgres Server.




* Configuration
```bash
pip install requirements.txt
```
* Database creation

import a PostgreSQL database using the psql program

```bash
psql -U  ecommerce < dbexport.pgsql
```

* Database initialization

```bash

alembic upgrade head
```

 * Rail Server
 To install a dependencies using the gem dependency manager and to start Rails server
 ```bash
 
 bundle
 bundle exec rails s
 ```
Web application would be started by default in https://localhost:3000/

For testing purpose,

Customer test account username:testuser@rit.edu and password : test123

Administrator test account username:testadmin@rit.edu and password: testadmin