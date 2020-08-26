import sqlite3
from _config import DATABASE_PATH

with sqlite3.connect(DATABASE_PATH) as connection:
    c = connection.cursor()

    c.execute("""create table tasks (task_id integer primary key autoincrement, name text not null, due_date text not null, priority integer  not null,
    status integer not null)""")

    c.execute('insert into tasks (name, due_date, priority, status) values ("Finish this tutorial", "26/08/2020", 10, 1)')
    c.execute('insert into tasks (name, due_date, priority, status) values ("Finish this course", "26/08/2020", 10, 1)')
