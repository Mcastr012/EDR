from datetime import datetime
from db.postgres import PSQL as db
import uuid


class Session():

    @classmethod
    def create_session_id(cls):
        return str(uuid.uuid1())

    @classmethod
    def start_session(cls, session, uid, start_time):
        sql = """INSERT INTO public.user_session (session_id, user_id, start_time) VALUES (%s,%s,%s);"""
        args = (session, uid, start_time)
        return db.execute(sql, args, False)

    @classmethod
    def get_session(cls, session_id='%'):
        sql = """   SELECT session_id, user_id, start_time,end_time 
                    FROM public.user_session
                    WHERE   session_id::text LIKE %s"""

        arg = (session_id,)
        return db.execute(sql, arg, True)

    @classmethod
    def end_session(cls, session_id='%', uid='%', end_time=datetime.utcnow()):
        sql = """
                UPDATE public.user_session SET end_time = %s 
                WHERE 
                    session_id::text LIKE %s 
                AND user_id::text LIKE %s;
                """
        args = (end_time, session_id, str(uid))
        return db.execute(sql, args, False)
