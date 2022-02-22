from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

from .singleton import Singleton
from .config import Config


class BaseRepo(Singleton):
    def __init__(self) -> None:
        self.__config = Config()
        self.__engine = create_engine(
            f"{self.__config.driver_name}://"
            f"{self.__config.user}:{self.__config.password}@"
            f"{self.__config.host}:{self.__config.port}/{self.__config.database}"
        )
        self._session: Session = sessionmaker(self.__engine)()
