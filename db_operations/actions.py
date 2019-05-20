import os
import pymysql as pymysql
from urlparse import urlparse

ENV = os.environ.get("ENV" , "LOCAL") # get the environment.
DB_URL = os.environ.get("JAWSDB_URL" , "mysql://root:zrihan13@localhost:3306/herolo_mailing_sys") # get the environment.


db_info = urlparse(DB_URL)
# Connect to the database
connection = pymysql.connect(host=db_info.host,
                             user=db_info.username,
                             password=db_info.password,
                             db=db_info.database,
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

def write_message_to_db(sender, receiver, subject, content):
    # TODO Do not forget to add date and time.
    print "Write message to db here:"
    # try:
    #     with connection.cursor() as cursor:
    #         # Read a single record
    #         sql = "SELECT * FROM quotes WHERE value = " + str(gematric_value)
    #         cursor.execute(sql)
    #         res = cursor.fetchall()
    #         res_bundle = []
    #         for row in res:
    #             res_bundle.append({
    #                 "quote":row.get("quote" ,""),
    #                 "value": row.get("value" , ""),
    #                 "id": row.get("id" , ""),
    #                 "source" : row.get("source" , "")
    #             })
    #         return jsonify(res_bundle)
    # finally:
    #     connection.close()