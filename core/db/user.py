from db.postgres import PSQL as db


class User:

    @classmethod
    def get_user(cls, uid='%', name='%', email='%', password='%', phone='%', enable=True):
        sql = """   SELECT user_id, name, email, phone,password,enable
                    FROM public.user_account
                    WHERE   user_id::text   LIKE %s AND
                            name        LIKE %s AND 
                            email       LIKE %s AND 
                            phone       LIKE %s AND 
                            password    LIKE %s AND 
                            enable = %s"""

        args = (str(uid), name, email, phone, password, enable)
        return db.execute(sql, args, True)

    @classmethod
    def add_user(cls, args):
        sql = """
                INSERT INTO 
                    public.user_account (
                        name,
                        email, 
                        phone, 
                        password, 
                        enable
                    ) 
                VALUES (
                    %(Name)s, 
                    %(Email)s, 
                    %(Phone)s, 
                    %(Password)s, 
                    %(Enable)s
                )
                """
        return db.execute(sql, args, False)

    @classmethod
    def delete_user(cls, uid):
        sql = """UPDATE public.user_account SET enable = FALSE WHERE user_id = %s;"""
        args = (uid,)
        return db.execute(sql, args, False)

    @classmethod
    def update_user(cls, args):
        sql = """   UPDATE 
                        public.user_account 
                    SET 
                        name        = %(Name)s, 
                        email       = %(Email)s,
                        phone       = %(Phone)s,
                        password    = %(Password)s
                    WHERE 
                        user_id = %(UID)s;
                    """
        return db.execute(sql, args, False)
