import sqlite3 as sql


class DB:
    def __init__(self, db_url='src/my_db.db'):
        self.connection = sql.connect(db_url)
        self.cursor = self.connection.cursor()

        self._create_tables()

    def _create_tables(self):
        does_calcResults_table_exist = self.cursor.execute("""
            SELECT name FROM sqlite_master WHERE type='table' AND name='calcResults'
        """).fetchall()

        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS calcResults (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            stair_h TEXT NOT NULL,
            stair_w TEXT NOT NULL,
            stair_s TEXT NOT NULL,
            step_h TEXT NOT NULL,
            stair_angle_r TEXT,
            count_of_step TEXT NOT NULL,
            step_pitch TEXT NOT NULL,
            check_value TEXT NOT NULL,
            stairs_type TEXT NOT NULL
            )
            """
        )

        self.connection.commit()

    def add_item(self, data: dict, result: dict) -> None:
        sql_req = """
        INSERT INTO calcResults (
            stair_h, stair_w, stair_s, 
            step_h, stair_angle_r, count_of_step, step_pitch, check_value, stairs_type 
        )
        values(?, ?, ?, ?, ?, ?, ?, ?, ?)
        """
        write_data = (
            str(data['height']),
            str(data['width']),
            str(data['area']),
            str(data['stepHeight']),
            str(data['radiusAngle']),
            str(result['numOfSteps']),
            str(result['stepPitch']),
            str(round(result['checkValue'], 2)),
            str(data['type'])
        )
        self.cursor.execute(sql_req, write_data)
        self.connection.commit()

    def get_items(self) -> list:
        self.cursor.execute('SELECT * FROM calcResults')
        return self.cursor.fetchall()

    def db_close(self):
        self.connection.close()