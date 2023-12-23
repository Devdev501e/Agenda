import sqlite3

database = "identifier.sqlite"


def data_connection(data_base):
    conn = sqlite3.connect(data_base)
    cursor = conn.cursor()
    return cursor, conn


class DataTransaction:

    @staticmethod
    def get_data():
        cursor, conn = data_connection(database)
        cursor.execute("SELECT * FROM task")
        rows = cursor.fetchall()
        conn.close()
        return rows

    @staticmethod
    def write_data(date, month, hour, info, title):
        cursor, conn = data_connection(database)
        cursor.execute("INSERT INTO task (date,month,hour,title,info)VALUES (?, ?, ?, ?, ?)",
                       (date, int(month), int(hour), title, info))
        conn.commit()
        conn.close()

    @staticmethod
    def modify_data(date, month, hour, new_text, index):
        print("you work ?")
        cursor, conn = data_connection("identifier.sqlite")
        if index == 1:
            cursor.execute("UPDATE task SET title = ? WHERE date = ? AND month = ? AND hour = ?",
                           (new_text, date, int(month), int(hour)))
        else:
            cursor.execute("UPDATE task SET  info = ? WHERE date = ? AND month=? AND hour=?",
                           (new_text, date, int(month), int(hour)))
        conn.commit()
        conn.close()

    @staticmethod
    def delete_data(date, month, hour):
        cursor, conn = data_connection(database)
        cursor.execute("DELETE FROM task WHERE date = ? AND month = ? AND hour = ?",
                       (date, int(month), int(hour)))
        conn.commit()
        conn.close()
