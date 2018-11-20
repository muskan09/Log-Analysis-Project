#! usr/bin/env/python3

import psycopg2
DB_NAME="news"

#Assignment 1. What are the most popular three articles of all time?
FirstQuery="select title,my_views from ar_view limit 3"

#Assignment 2. Who are the most popular article authors of all time?
SecondQuery="select authors.name,sum(ar_view.my_views) as my_views from ar_view,authors where authors.id = ar_view.author group by authors.name order by my_views desc"

#Assignment 3. On which days did more than 1% of requests lead to errors?
ThirdQuery="select * from l_view where "error">1"

