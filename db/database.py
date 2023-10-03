import sqlite3


class ControllerDB:

    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()

    def user_exist(self, user_id):
        """Проверяем, есть ли юзер в базе"""
        result = self.cursor.execute("SELECT id FROM users WHERE user_id = ?", (user_id,))
        return bool(len(result.fetchall()))

    def add_user(self, user_id):
        """Добавляем юзера в базу"""
        self.cursor.execute("INSERT INTO users (user_id) VALUES (?)", (user_id,))
        return self.conn.commit()

    def get_users(self):
        result = self.cursor.execute("SELECT * FROM users")
        return result.fetchall()

    def update_pay(self, user_id, updater_numb):
        self.cursor.execute("UPDATE users SET is_pay = ? WHERE user_id = ?", (updater_numb, user_id,))
        return self.conn.commit()

    def get_pay(self, user_id):
        result = self.cursor.execute("SELECT is_pay FROM users WHERE user_id = ?", (user_id,))
        return result.fetchone()[0]

    def add_summ(self, summ, user_id):
        self.cursor.execute("UPDATE users SET summ = ? WHERE user_id = ?", (summ, user_id,))
        return self.conn.commit()

    def get_summ(self, user_id):
        result = self.cursor.execute("SELECT summ FROM users WHERE user_id = ?", (user_id,))
        return result.fetchone()[0]

    def add_timestamp(self, timestamp, user_id):
        self.cursor.execute("UPDATE users SET timestamp = ? WHERE user_id = ?", (timestamp, user_id,))
        return self.conn.commit()

    def get_timestamp(self, user_id):
        result = self.cursor.execute("SELECT timestamp FROM users WHERE user_id = ?", (user_id,))
        return result.fetchone()[0]

    def close(self):
        """Закрываем соединение с БД"""
        self.close()