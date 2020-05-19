# -*- coding: utf-8 -*-
import sqlite3


# 数据库连接
class Connection:

    conn = None
    cursor = None

    def __init__(self, db_path):
        self.conn = sqlite3.connect(db_path, check_same_thread=False)
        self.cursor = self.conn.cursor()

    def get_connection(self):
        return self.conn

    def get_cursor(self):
        return self.conn