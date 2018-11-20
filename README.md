# Log Analysis Project

## Project Description

>The goal is to create a reporting tool that prints out reports (in plain text) based on the data in the database. This reporting tool is a Python program using the psycopg2 module to connect to the database.
>In this project, we'll work with data that could have come from a real-world web application, with fields representing information that a web server would record, such as HTTP status codes and URL paths. The web server and the reporting tool both connect to the same database, allowing information to flow from the web server into the report.

### Prerequisite knowledge:

  * [Python3](https://www.python.org/)
  * [PostgreSQL](https://www.postgresql.org/)
  
### Additional Tools used:

  * [Vagrant](https://www.vagrantup.com/)
  * [VirtualBox](https://www.virtualbox.org/)
  * [Git commands](https://in.udacity.com/course/how-to-use-git-and-github--ud775-india)
  * [PEP 8](https://www.python.org/dev/peps/pep-0008/)
  
### Setup for the project

  1. Install VirtualBox
  2. Setup the Vagrant
  2. Clone [fullstack-nanodegree-vm](https://github.com/udacity/fullstack-nanodegree-vm) repository.
  3. Download the [data](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) from here.
  4. After unzipping you'll find a newsdata.sql file inside.
  5. Copy the content of this repository, by cloning it from
  [this link](https://github.com/muskan09/Log-Analysis-Project)
  6. Copy newdata.sql
  
## Tasks of this project

 **What are the most popular three articles of all time?** 

>Which articles have been accessed the most? Present this information as a sorted list with the most popular article at the top.

**Who are the most popular article authors of all time?**
 
>That is, when you sum up all of the articles each author has written, which authors get the most page views? Present this as a sorted list with the most popular author at the top.

**On which days did more than 1% of requests lead to errors?** 
 
>The log table includes a column status that indicates the HTTP status code that the news site sent to the user's browser.     
  
## To run the project

#### Step 1: Launch the vm, this step helps us share files in vagrant directory

  1. Go to the downloaded FSND-Virtual-Machine folder, install the vagrant inside the vagrant folder then run the following command:
  
  ```
    $ vagrant up
  ```
  2. To connect to the vagrant use the following command:
  
  ```
    $ vagrant ssh 
  ```
  3. Change directory to /vagrant using the command:
  
  ```
    $ cd /vagrant 
  ```  
  4. To exit the vagrant:
  
  ```
   $ exit   
  ```
 
#### Step 2: Database Setup

  1. To load the database in our vagarant
  
  ```
    psql -d news -f newsdata.sql
  ```
  
The database includes three tables:

  * The authors table includes information about the authors of articles.
  * The articles table includes the articles themselves.
  * The log table includes one entry for each time a user has accessed the site.
  
  2. Run `psql -d news` to connect to the database.
  
  3. Explore the tables using the `\dt` and `\d table` commands and `select` statements. 
  
 #### Step 3: Views used

  1. ar_view (for more information, visit the screenshot folder on this repository) [repo link](https://github.com/muskan09/Log-Analysis-Project) 
  
  ```
    create view ar_view as select title,author,count(*) as my_views from log,articles where 
    log.path like concat('%',articles.slug) group by articles.title,articles.author 
    order by my_views desc;  
  ```
  
  2.  l_view (for more information, visit the screenshot folder on this repository) [repo link](https://github.com/muskan09/Log-Analysis-Project) 
  
  ```
    create view l_view as select date(time),round(100.0*sum(case log.status when '200 OK' 
    then 0 else 1 end)/count(log.status),2) as "error" from log group by date(time) 
    order by "error" desc;
  ```

#### Step 4: Run the python code after suitable queries

  ```
    $ python LogAnalysis.py 
  ```

## Expected Output of the python code
	Top 3 articles are :- 

			Article "Candidate is jerk, alleges rival" has 338647 views.
			Article "Bears love berries, alleges bear" has 253801 views.
			Article "Bad things gone, say good people" has 170098 views.
	Most popular authors are :- 

			Author "Ursula La Multa" has 507594 views.
			Author "Rudolf von Treppenwitz" has 423457 views.
			Author "Anonymous Contributor" has 170098 views.
			Author "Markoff Chaney" has 84557 views.
	The days on which more than 1% of requests lead to errors :- 

			The day 2016-07-17 had 2.26% errors.
