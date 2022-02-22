from homework_30.core.singleton import Singleton


class Config(Singleton):
    def __init__(self):
        self.driver_name = "postgresql+psycopg2"
        self.host = "127.0.0.1"
        self.port = "5432"
        self.database = "mydb"
        self.user = "postgres"
        self.password = "mitya232"