import sqlite3


class ControllerDB:

    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()

    def user_exist(self, user_id):
        """Check user in database"""
        result = self.cursor.execute("SELECT id FROM users WHERE user_id = ?", (user_id,))
        return bool(len(result.fetchall()))

    def add_user(self, user_id):
        """Add user in database"""
        self.cursor.execute("INSERT INTO users (user_id) VALUES (?)", (user_id,))
        return self.conn.commit()

    def get_users(self):
        """Get all users Info"""
        result = self.cursor.execute("SELECT * FROM users")
        return result.fetchall()

    def upd_numb(self, summ, user_id):
        """update user lottery number"""
        self.cursor.execute("UPDATE users SET numb = ? WHERE user_id = ?", (summ, user_id,))
        return self.conn.commit()

    def get_us_by_numb(self, numb):
        result = self.cursor.execute("SELECT user_id FROM users WHERE numb = ?", (numb,))
        return result.fetchone()[0]

    def close(self):
        """close database connect"""
        self.close()