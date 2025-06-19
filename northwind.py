import sqlite3
from northwind_queries import QUERY_LIST

conn = sqlite3.connect('northwind.sqlite3')
curs = conn.cursor()

def execute_query_sl(curs, conn, query):
    curs.execute(query)
    conn.commit()
    return curs.fetchall()

def execute_queries(curs, conn, queries):
    answers_dict = {}
    for index, query in enumerate(queries):
        answers_dict[index] = execute_query_sl(curs, conn, query)
    return answers_dict

if __name__ == '__main__':
    answers_dict = execute_queries(curs, conn, QUERY_LIST)
    for index, value in enumerate(answers_dict.values()):
        print(f'{index}: {value}')