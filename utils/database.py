import psycopg2

IP = '109.172.115.223'
PORT = '5432'
USERNAME = 'postgres'
PASSWORD = 2556505535
DBNAME = 'database'

class DB:
    def __init__(self) -> None:
        self.conn = psycopg2.connect(dbname=DBNAME, user=USERNAME, password=PASSWORD, host=IP, port=PORT)
        self.cursor = self.conn.cursor()
        
    async def create_table_if_not_exists(self, table_name, columns):
        try:
            self.cursor.execute(f"SELECT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name = '{table_name}')")
            table_exists = self.cursor.fetchone()[0]

            if not table_exists:
                create_table_query = f"""
                CREATE TABLE {table_name} (
                    {columns}
                );
                """
                self.cursor.execute(create_table_query)
                self.conn.commit()
                print(f"Таблица '{table_name}' успешно создана.")
            else:
                print(f"Таблица '{table_name}' уже существует.")

        finally:
            if self.conn:
                self.cursor.close()
                self.conn.close()
                print("Соединение с PostgreSQL закрыто.")
                           
    async def insert(self, table_name, values):
        self.cursor.execute(f'INSERT INTO {table_name} (name, href) VALUES (%s, %s)', values)
        self.conn.commit()

