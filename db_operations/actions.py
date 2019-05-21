import os
import pymysql as pymysql
from urlparse import urlparse
from datetime import datetime

ENV = os.environ.get("ENV" , "LOCAL") # get the environment.
DB_URL = os.environ.get("JAWSDB_URL" , "mysql://root:zrihan13@localhost:3306/herolo_mailing_sys") # get the environment.
db_info = urlparse(DB_URL)


def write_message_to_db(sender, receiver, subject, content):
    creation_time = datetime.now()
    connection = pymysql.connect(host=db_info.hostname,
                             user=db_info.username,
                             password=db_info.password,
                             db=db_info.path.replace('/', ''),
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

    query = "INSERT into all_emails (sender, receiver, subject, content, creation_time) VALUES ('%s', '%s', '%s', '%s' , '%s')"\
        %(sender, receiver, subject, content,creation_time)
    try:
        with connection.cursor() as cursor:
            cursor.execute(query)
        connection.commit()
    except Exception as e:
        print "Exception during insert to table" , e
    finally:
        connection.close()
