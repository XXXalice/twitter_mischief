from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy.ext.declarative import declarative_base
from etc import driver, logger

class Database:
    def __init__(self):
        yml_path = './config.yml'
        self.param = driver.read_yaml(yml_path)

        self.DATABASE = 'mysql://%s:%s@%s/%s?charset=utf8' % (
            self.param['database']['user_name'],
            self.param['database']['password'],
            self.param['database']['host_ip'],
            self.param['database']['db_name']
        )

        self.ENGINE = create_engine(
            self.DATABASE,
            encoding='utf-8',
            echo=True
        )

        self.session = scoped_session(
            sessionmaker(
                autocommit=False,
                autoflush=False,
                bind=self.ENGINE
            )
        )
        self.Base = declarative_base()
        self.Base.query = self.session.query_property()

class Tweet(Database.Base):
    def __init__(self):
        __tablename__ = 'tweets'
        # sqlalchemyはプライマリキーが有効になっていると自動でオートインクリメントが適応される
        self.id = Column(Integer, primary_key=True)
        self.name = Column(String(15))
        self.sentence = Column(String(255), nullable=False)

    def __repr__(self):
        return "<Tweet(id={}, name={}, sentence={})>".format(str(self.id), self.name, self.sentence)

