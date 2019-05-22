import os
import pymysql as pymysql
from urlparse import urlparse
from datetime import datetime

DB_URL = os.environ.get("JAWSDB_URL" , "mysql://root:zrihan13@localhost:3306/herolo_mailing_sys") # get the environment.
db_info = urlparse(DB_URL)

def set_message_opened_by_id(id):
    creation_time = datetime.now()
    connection = pymysql.connect(host=db_info.hostname,
                             user=db_info.username,
                             password=db_info.password,
                             db=db_info.path.replace('/', ''),
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
    query = "UPDATE all_emails SET opened = 1 WHERE id = '%s'"%(id,)
    try:
        with connection.cursor() as cursor:
            cursor.execute(query)
        connection.commit()
    except Exception as e:
        print "Exception during updating opened attribute", e
    finally:
        connection.close()

def delete_message_by_id(id):
    row_count = 0
    connection = pymysql.connect(host=db_info.hostname,
                             user=db_info.username,
                             password=db_info.password,
                             db=db_info.path.replace('/', ''),
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
    query = "DELETE FROM all_emails WHERE id = '%s'"%(id,)
    try:
        with connection.cursor() as cursor:
            cursor.execute(query)
            row_count = cursor.rowcount
        connection.commit()
    except Exception as e:
        print "Exception during delete", e
    finally:
        connection.close()
        if row_count == 1:
            return {
                "response": "Success",
                "status": 200
            }
        else :
            return {
                "response": "No such id",
                "status": 400
            }


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

def get_all_messages_by_user(user, only_unread=False):
    result = []
    connection = pymysql.connect(host=db_info.hostname,
                             user=db_info.username,
                             password=db_info.password,
                             db=db_info.path.replace('/', ''),
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

    query = "SELECT * FROM all_emails WHERE opened = 0 AND receiver = '%s'"%(user,) if only_unread \
        else "SELECT * FROM all_emails WHERE receiver = '%s'"%(user,)

    try:
        with connection.cursor() as cursor:
            cursor.execute(query)
            result = cursor.fetchall()
    except Exception as e:
        print "Exception getting data from DB" , e
    finally:
        connection.close()

        for row in result:
            set_message_opened_by_id(row.get("id",""))

        messages_list = [{
            "From": row.get("sender",""),
            "To": row.get("receiver",""),
            "Subject": row.get("subject",""),
            "Content": row.get("content",""),
            "Time": str(row.get("creation_time","")),
            "Message ID": row.get("id","")
            }
            for row in result]
        if messages_list == []:
            messages_list = "No messages"
    return messages_list

def get_specific_message_by_id(id):
    result, messages= [] , {}
    connection = pymysql.connect(host=db_info.hostname,
                             user=db_info.username,
                             password=db_info.password,
                             db=db_info.path.replace('/', ''),
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

    query = "SELECT * FROM all_emails WHERE id= '%s'"%(id,)

    try:
        with connection.cursor() as cursor:
            cursor.execute(query)
            result = cursor.fetchall()
    except Exception as e:
        print "Exception getting data from DB" , e
    finally:
        connection.close()

        if result :
            result = result[0]
            set_message_opened_by_id(result.get("id",""))
            messages = {
                "From": result.get("sender",""),
                "To": result.get("receiver",""),
                "Subject": result.get("subject",""),
                "Content": result.get("content",""),
                "Time": str(result.get("creation_time","")),
                "Message ID": result.get("id","")
                }

    return messages or "Id is not exist"
