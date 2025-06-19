import sqlite3
from queries import QUERY_LIST, INSERT_DEMO

conn = sqlite3.connect('demo_data.sqlite3')
curs = conn.cursor()

data = [
    ('g', 3, 9),
    ('v', 5, 7),
    ('f', 8, 7)
]

table_name = 'demo'

def insert_data_sl(curs, conn, query):
    try:
        curs.executemany(query, data)
        conn.commit()
        return curs.rowcount
    except Exception as e:
        conn.rollback()
        raise Exception(f"Erroc executing insert statement: {e}")

def execute_query_sl(curs, conn, query):
    if query == INSERT_DEMO:
        return insert_data_sl(curs, conn, query)
    
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