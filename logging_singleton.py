import logging

class LoggingManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.logger = logging.getLogger("OpenSourceDataProject")
            handler = logging.StreamHandler()
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            handler.setFormatter(formatter)
            cls._instance.logger.addHandler(handler)
            cls._instance.logger.setLevel(logging.DEBUG)
        return cls._instance

    def get_logger(self):
        return self.logger

# Usage
if __name__ == "__main__":
    logger_1 = LoggingManager().get_logger()
    logger_2 = LoggingManager().get_logger()
    
    logger_1.debug("This is a debug message.")
    logger_2.info("This is an info message.")
    
    # Both loggers should be the same
    print(logger_1 is logger_2)
