from datetime import date
from flask import request
import pymysql


# Boolean to check if the user_id is already exists
id_exists = False


def get_requests(user_id):
    # Establishing a connection to DB
    conn = pymysql.connect(host='remotemysql.com', port=3306, user='Q8WmovJgAJ', passwd='TLv9A4xUZ1',
                           db='Q8WmovJgAJ')
    conn.autocommit(True)

    # Getting a cursor from Database
    cursor = conn.cursor()

    try:
        # Getting data from table
        cursor.execute("SELECT user_name FROM Q8WmovJgAJ.users WHERE user_id LIKE " + user_id)
        for row in cursor:
            name = row[0]
        return {'status': "ok", 'user_name': name}, 200
    except:
        return {'status': "error", 'reason': "no such id"}, 500
    finally:
        cursor.close()
        conn.close()


def post_requests(user_id):
    # getting the json data payload from request
    request_data = request.json

    # treating request_data as a dictionary to get a specific value from key
    user_name = request_data.get('user_name')

    # Establishing a connection to DB
    conn = pymysql.connect(host='remotemysql.com', port=3306, user='Q8WmovJgAJ', passwd='TLv9A4xUZ1',
                           db='Q8WmovJgAJ')
    conn.autocommit(True)

    # Getting a cursor from Database
    cursor = conn.cursor()

    # Inserting data into table
    try:
        cursor.execute("INSERT into Q8WmovJgAJ.users (user_id, user_name, creation_date ) VALUES (%s, %s, %s)",
                       (user_id, user_name, date.today()))
        return {'status': "ok", 'user_added': user_name}, 200
    except:
        return {'status': "error", 'reason': "id already exists"}, 500
    finally:
        cursor.close()
        conn.close()


def put_requests(user_id):
    # getting the json data payload from request
    request_data = request.json

    # treating request_data as a dictionary to get a specific value from key
    new_user_name = request_data.get('user_name')

    # Establishing a connection to DB
    conn = pymysql.connect(host='remotemysql.com', port=3306, user='Q8WmovJgAJ', passwd='TLv9A4xUZ1',
                           db='Q8WmovJgAJ')
    conn.autocommit(True)

    # Getting a cursor from Database
    cursor = conn.cursor()

    try:
        # Getting all users from table - to check if user_id is exists.
        cursor.execute("SELECT * FROM Q8WmovJgAJ.users")
        for row in cursor:
            for passed_id in row:
                if passed_id == int(user_id):
                    id_exists = True
    finally:
        if not id_exists:
            return {'status': "error", 'reason': "no such id"}, 500
        else:
            try:
                # Updating data inside the table
                cursor.execute("UPDATE Q8WmovJgAJ.users SET user_name = " + '%s' + " WHERE user_id = " + '%s' + ";",
                               (new_user_name, user_id))
                return {'status': "ok", 'user_updated': new_user_name}, 200
            finally:
                cursor.close()
                conn.close()


def delete_requests(user_id):
    # Establishing a connection to DB
    conn = pymysql.connect(host='remotemysql.com', port=3306, user='Q8WmovJgAJ', passwd='TLv9A4xUZ1',
                           db='Q8WmovJgAJ')
    conn.autocommit(True)

    # Getting a cursor from Database
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT * FROM Q8WmovJgAJ.users")
        for row in cursor:
            for passed_id in row:
                if passed_id == int(user_id):
                    id_exists = True
    finally:
        if not id_exists:
            return {'status': "error", 'reason': "no such id"}, 500
        else:
            try:
                # Deleting data from table
                cursor.execute("DELETE FROM Q8WmovJgAJ.users WHERE user_id = " + '%s' + ";", user_id)
                return {'status': "ok", 'user_deleted': user_id}, 200
            finally:
                cursor.close()
                conn.close()


def get_user_name_from_db(user_id):
    # Establishing a connection to DB
    conn = pymysql.connect(host='remotemysql.com', port=3306, user='Q8WmovJgAJ', passwd='TLv9A4xUZ1',
                           db='Q8WmovJgAJ')
    conn.autocommit(True)

    # Getting a cursor from Database
    cursor = conn.cursor()

    try:
        # Getting data from table
        cursor.execute("SELECT user_name FROM Q8WmovJgAJ.users WHERE user_id LIKE " + user_id)
        for row in cursor:
            name = row[0]
        user_name = name
    except:
        user_name = 0
    finally:
        cursor.close()
        conn.close()

    return user_name


def db_checking_for_backend_testing(user_id):

    # Establishing a connection to DB
    conn = pymysql.connect(host='remotemysql.com', port=3306, user='Q8WmovJgAJ', passwd='TLv9A4xUZ1',
                       db='Q8WmovJgAJ')
    conn.autocommit(True)

    # Getting a cursor from Database
    cursor = conn.cursor()

    try:
        # Getting data from table
        cursor.execute("SELECT user_name FROM Q8WmovJgAJ.users WHERE user_id = " + str(user_id))
        for row in cursor:
            name = row[0]
        return {'status': "ok", 'user_name': name}, 200
    except Exception as e:
        return {'status': "error", 'reason': "no such id"}, 500
    finally:
        cursor.close()
        conn.close()


def db_checking_for_combined_testing(user_id):

    # Establishing a connection to DB
    conn = pymysql.connect(host='remotemysql.com', port=3306, user='Q8WmovJgAJ', passwd='TLv9A4xUZ1',
                       db='Q8WmovJgAJ')
    conn.autocommit(True)

    # Getting a cursor from Database
    cursor = conn.cursor()

    try:
        # Getting data from table
        cursor.execute("SELECT user_name FROM Q8WmovJgAJ.users WHERE user_id = " + str(user_id))
        for row in cursor:
            name = row[0]
        return {'status': "ok", 'user_name': name}, 200
    except Exception as e:
        return {'status': "error", 'reason': "no such id"}, 500
    finally:
        cursor.close()
        conn.close()