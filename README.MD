# README


This is a web application which showcases role based authentication of data. The application is written in Ruby ( on Rails ) and uses PostgreSql

* Files and Location
requirements.txt --> data migration/requirements.txt
dbexport.pgsql --> data_dump/dbexport.pgsql


For Ubuntu Users,

## Steps for installing Ruby on Rails.
### Installing Ruby on Ubuntu
- sudo apt-get update && apt-get install curl
- curl -L https://get.rvm.io | bash -s stable --ruby # installs ruby version manager
  - source ~/.rvm/scripts/rvm
- rvm get stable --autolibs=enable
- rvm install ruby-2.5

Once the installation of Ruby is done:
- rvm --default use ruby-2.5
- gem install bundler --no-ri --no-rdoc 
- gem install rails --no-ri --no-rdoc

### Installing Ruby on a Mac machine. 

MacOS comes with a "system Ruby" pre-installed. MacOS High Sierra includes Ruby 2.0.0p645 which is not the newest version. We should update to Ruby 2.5.0 by using RVM, the Ruby Version Manager.

Let start off my installing Homebrew, if not already installed. 

- `/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)`

#### Steps for installing Ruby on Rails.

- brew install gpg

After GPG is installed (or if it is already installed), install the security key for RVM:

- curl -sSL https://rvm.io/mpapis.asc | gpg --import -

NOTE: If you skip the gpg steps you may not be able to install RVM.

- curl -L https://get.rvm.io | bash -s stable
  - source ~/.rvm/scripts/rvm
- rvm get stable --autolibs=enable
- rvm install ruby-2.5.0
- rvm --default use ruby-2.5.1
- gem install bundler --no-ri 
- gem install rails  --no-rdoc


## Steps for installing Database

To install on a debian based on:
- sudo apt-get update && apt-get install postgresql

I recommend using the excellent [Postgres app for Mac](https://postgresapp.com/).

## Steps for installing Python

sudo apt-get update && apt-get install python3.6

## For Setting up with the project envirnment,

- pip install requirements.txt
- psql ecommerce < dbexport.pgsql

### Why do I have the app in Ruby and db import script in python?

I started off this small project on Python, but then I wanted to try and learn Ruby on Rails. I never got around to rewriting the said script into Ruby


### Starting the application.

Within the application directory, run:
- bundle
- bundle exec rails s

### Lets checkout the app :)

Open https://localhost:3000/ in any browser.
For testing purpose,

Customer test account: `username:testuser@rit.edu` and `password : test123`
Administrator test account: `username:testadmin@rit.edu` and `password: testadmin`
