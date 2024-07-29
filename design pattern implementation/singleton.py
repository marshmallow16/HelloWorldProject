class Singleton:
    _instance = None  # Class attribute to hold the single instance

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.data = None  # You can initialize your attributes here
        return cls._instance

# Demonstration
if __name__ == "__main__":
    # Trying to create multiple instances
    s1 = Singleton()
    s2 = Singleton()

    # Setting data in one instance
    s1.data = "Singleton Data"

    # Accessing data from the other instance
    print(s2.data)  # Output: Singleton Data

    # Checking if both instances are the same
    print(s1 is s2)  # Output: True
