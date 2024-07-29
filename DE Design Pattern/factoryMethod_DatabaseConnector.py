from abc import ABC, abstractmethod

# Abstract product
class DataConnector(ABC):
    @abstractmethod
    def connect(self):
        pass

# Concrete products
class MySQLConnector(DataConnector):
    def connect(self):
        return "Connecting to MySQL Database"

class PostgreSQLConnector(DataConnector):
    def connect(self):
        return "Connecting to PostgreSQL Database"

# Creator
class DataConnectorFactory(ABC):
    @abstractmethod
    def create_connector(self):
        pass

# Concrete Creators
class MySQLConnectorFactory(DataConnectorFactory):
    def create_connector(self):
        return MySQLConnector()

class PostgreSQLConnectorFactory(DataConnectorFactory):
    def create_connector(self):
        return PostgreSQLConnector()

# Client code
def client_code(factory: DataConnectorFactory):
    connector = factory.create_connector()
    print(connector.connect())

# Usage
client_code(MySQLConnectorFactory())
client_code(PostgreSQLConnectorFactory())
