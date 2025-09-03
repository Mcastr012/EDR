import psycopg2
import psycopg2.extras
from config import *


class PSQL:
    conn = None

    @classmethod
    def connect(cls):
        try:
            cls.conn = psycopg2.connect("dbname='{}' user='{}' host='{}' password='{}'".format(
                DB_NAME, DB_USER, DB_HOST, DB_PASS))
        except:
            raise RuntimeError("Fail to connect to database.")

    @classmethod
    def close(cls):
        if cls.conn is not None:
            cls.conn.close()

    @classmethod
    def execute(cls, sql, args, isSELECT=True):
        cur = cls.conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        try:
            if isSELECT:
                cur.execute(sql, args)
                ret = cur.fetchall()
            else:
                cur.execute(sql, args)
                ret = 0
                cls.conn.commit()

        except psycopg2.Error as e:
            print(e)
            return None

        return ret


PSQL.connect()
