# -*- coding: utf-8 -*-
from dao.connection import Connection


class Endpoints:

    __connection__ = Connection('db.sqlite3')
    conn = __connection__.get_connection()
    cursor = __connection__.get_cursor()

    def add_endpoint(self, endpoint):
        insert_sql = 'insert into endpoints(ip, port, `name`, create_time) values(%s, %s, %s, %s)'
        self.cursor.execute(insert_sql, endpoint)
        self.cursor.commit()
        return self.cursor