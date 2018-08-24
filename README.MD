# README

The web application is built on Ruby on Rails with Postgres Server.

* Files and Location
requirements.txt --> data migration/requirements.txt
dbexport.pgsql --> data_dump/dbexport.pgsql


For Ubuntu Users,

Steps for installing Ruby on Rails.

Step 1: sudo apt-get update
Step 2 sudo apt-get install curl
Step 3a:curl -L https://get.rvm.io | bash -s stable --ruby

Step 3 b: source ~/.rvm/scripts/rvm
Step 4: rvm get stable --autolibs=enable
Step 5: rvm install ruby
Step 6: rvm --default use ruby-2.5.1
Step 7: gem install bundler 
Step 8: gem install rails

Steps for installing Database

Step 1:sudo apt-get update
Step 2:sudo apt-get install postgresql

Steps for installing Python

Step 1:sudo apt-get update
Step 2:sudo apt-get install python3.6

For Setting up with the project envirnment,

Step 1: pip install requirements.txt
Step 2: psql ecommerce < dbexport.pgsql

Set the directory ecommerce,start the rails Server

Step 1: bundle
Step 2: bundle exec rails s

Open https://localhost:3000/ in any browser.
Web application would be started by default in https://localhost:3000/





For Mac Users,

MacOS comes with a "system Ruby" pre-installed. MacOS High Sierra includes Ruby 2.0.0p645 which is not the newest version.You should update to Ruby 2.5.0 by using RVM, the Ruby Version Manager.

Please install Homebrew

/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

Steps for installing Ruby on Rails.

Step 1: brew install gpg
After GPG is installed (or if it is already installed), install the security key for RVM:
Step 2 command curl -sSL https://rvm.io/mpapis.asc | gpg --import -
If you skip the gpg steps you may not be able to install RVM.

Step 3a:curl -L https://get.rvm.io | bash -s stable

STep 3b: source ~/.rvm/scripts/rvm
Step 4: rvm get stable --autolibs=enable
Step 5: rvm install ruby-2.5.0
Step 6: rvm --default use ruby-2.5.1
Step 7: gem install bundler 
Step 8: gem install rails

Steps for installing Database

Step 1:Download Postgres.app from https://postgresapp.com/ and follow steps for installing

Steps for installing Python

Step 1:brew install python

For Setting up with the project envirnment,

Step 1: pip install requirements.txt
Step 2: psql ecommerce < dbexport.pgsql

Set the directory ecommerce,start the rails Server

Step 1: bundle
Step 2: bundle exec rails s

Open https://localhost:3000/ in any browser.




For Windows Users,

Steps for installing Ruby on Rails.

Step 1:Open "Bash on Ubuntu on Windows"
Step 2:sudo apt-get update
STep 3:sudo apt-get install git-core curl zlib1g-dev build-essential libssl-dev libreadline-dev libyaml-dev libsqlite3-dev sqlite3 libxml2-dev libxslt1-dev libcurl4-openssl-dev software-properties-common libffi-dev
Step 4:sudo apt-get install libgdbm-dev libncurses5-dev automake libtool bison libffi-dev
Step 5:gpg --keyserver hkp://keys.gnupg.net --recv-keys 409B6B1796C275462A1703113804BB82D39DC0E3 7D2BAF1CF37B13E2069D6956105BD0E739499BDB
Step 6: curl -sSL https://get.rvm.io | bash -s stable
Step 7:source ~/.rvm/scripts/rvm
Step 8:rvm install 2.5.1
Step 9:rvm use 2.5.1 --default
Step 10:ruby -v
Step 11: gem install bundler

Step 8: gem install rails

Steps for installing Database

Step 1:Download Postgres.app from https://www.postgresql.org/download/windows/ and follow steps for installing

Steps for installing Python

Step 1:brew install python

For Setting up with the project envirnment,

Step 1: pip install requirements.txt
Step 2: psql ecommerce < dbexport.pgsql

Set the directory ecommerce,start the rails Server

Step 1: bundle
Step 2: bundle exec rails s

Open https://localhost:3000/ in any browser.



For testing purpose,

Customer test account username:testuser@rit.edu and password : test123

Administrator test account username:testadmin@rit.edu and password: testadmin