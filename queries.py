'''Queries for demo table'''

# drop table before creation
DROP_DEMO = '''
    DROP TABLE IF EXISTS demo;
'''

# create demo table
CREATE_DEMO = '''
    CREATE TABLE IF NOT EXISTS demo (
        s CHAR(1),
        x INT,
        y INT
    );
'''

# insert into demo table
INSERT_DEMO = """
    INSERT INTO demo (s, x, y)
    VALUES (?, ?, ?)
"""

# verify the demo table was created
CHECK_DEMO = '''
    SELECT name FROM sqlite_master WHERE type='table' AND name='demo';
'''

ROW_COUNT = '''
    SELECT COUNT(*)
    FROM demo;
'''

XY_AT_LEAST_5 = '''
    SELECT COUNT(*)
    FROM demo
    WHERE x >= 5 AND y >= 5;
'''

UNIQUE_Y = '''
    SELECT COUNT(DISTINCT y)
    FROM demo;
'''

QUERY_LIST = [
    DROP_DEMO,
    CREATE_DEMO,
    INSERT_DEMO,
    CHECK_DEMO,
    ROW_COUNT,
    XY_AT_LEAST_5,
    UNIQUE_Y
]