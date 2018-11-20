#! usr/bin/env/python3

import psycopg2
DB_NAME = "news"

# Assignment 1. What are the most popular three articles of all time?
FirstQuery = 'select title,my_views from ar_view limit 3'

# Assignment 2. Who are the most popular article authors of all time?
SecondQuery = """select authors.name,sum(ar_view.my_views) as my_views
               from ar_view,authors where authors.id = ar_view.author group
               by authors.name order by my_views desc"""

# Assignment 3. On which days did more than 1% of requests lead to errors?
ThirdQuery = 'select * from l_view where "error">1'

# Heading for printing,store the output of queries
FirstQuery_Output = dict()
FirstQuery_Output["heading"] = 'Top 3 articles are :- \n'

SecondQuery_Output = dict()
SecondQuery_Output["heading"] = 'Most popular authors are :- \n'

ThirdQuery_Output = dict()
ThirdQuery_Output["heading"] = """The days on which more than 1% of
                                  requests lead to errors :- \n"""


# Runs the query against the news db and fetches the results
def dbquery_output(query):
    db = psycopg2.connect(database=DB_NAME)
    m = db.cursor()
    m.execute(query)
    outputs = m.fetchall()
    db.close()
    return outputs

# Stores the result returned by running the queries against the news db
FirstQuery_Output["outputs"] = dbquery_output(FirstQuery)
SecondQuery_Output["outputs"] = dbquery_output(SecondQuery)
ThirdQuery_Output["outputs"] = dbquery_output(ThirdQuery)


# Prints the output to the query
# "What are the most popular three articles of all time?"
def print_article_query_results(query_output):
    print (query_output["heading"])
    for data in query_output["outputs"]:
        print ('\t\t\tArticle "' + str(data[0]) +
               '" has ' + str(data[1]) + ' views.')


# Prints the output to the query
# "Who are the most popular article authors of all time?"
def print_author_query_results(query_output):
    print (query_output["heading"])
    for data in query_output["outputs"]:
        print ('\t\t\tAuthor "' + str(data[0]) +
               '" has ' + str(data[1]) + ' views.')


# Prints the output to the query
# "On which days did more than 1% of requests lead to errors?"
def print_error_query_results(query_output):
    print (query_output["heading"])
    for data in query_output["outputs"]:
        print ('\t\t\tThe day ' + str(data[0]) +
               ' had ' + str(data[1]) + '% errors.')


# Prints the final output after all the operations
print_article_query_results(FirstQuery_Output)
print_author_query_results(SecondQuery_Output)
print_error_query_results(ThirdQuery_Output)
