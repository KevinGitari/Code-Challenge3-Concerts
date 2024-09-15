# Imported the sqlite3 module to interact with the SQLite databases
import sqlite3

def create_db_connection():
    """
    Connects to the SQLite database file.
    
    :return: sqlite3.Connection object for 'database.db'
    """
    return sqlite3.connect('database.db')

def initialize_database():
    """
    Initializes the database schema by creating the required tables.
    If the tables already exist, this function will not alter them.
    """
    # Obtain a connection to the database
    connection = create_db_connection()
    
    # Gets a cursor object and execute SQL commands
    cursor = connection.cursor()
    
    # SQL  creates the 'bands' table if it does not exist
    create_bands_table = '''
        CREATE TABLE IF NOT EXISTS bands (
            name TEXT PRIMARY KEY,  -- Unique name for each band
            hometown TEXT           -- Location where the band is based
        )
    '''
    
    # Executed the SQL command to create the 'bands' table
    cursor.execute(create_bands_table)
    
    # SQL  creates the 'venues' table if it does not exist
    create_venues_table = '''
        CREATE TABLE IF NOT EXISTS venues (
            title TEXT PRIMARY KEY,  -- Unique title for each venue
            city TEXT               -- City where the venue is located
        )
    '''
    
    # Executed the SQL command to create the 'venues' table
    cursor.execute(create_venues_table)
    
    # SQL  creates the 'concerts' table if it does not exist
    create_concerts_table = '''
        CREATE TABLE IF NOT EXISTS concerts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,  -- Auto-incremented unique ID
            band_name TEXT,                       -- Name of the band performing
            venue_title TEXT,                     -- Title of the venue
            date TEXT,                            -- Date of the concert
            FOREIGN KEY (band_name) REFERENCES bands(name),  -- Reference to the 'bands' table
            FOREIGN KEY (venue_title) REFERENCES venues(title)  -- Reference to the 'venues' table
        )
    '''
    
    # Execute the SQL command to create the 'concerts' table
    cursor.execute(create_concerts_table)
    
    # Committed all changes to the database
    connection.commit()
    
    # Close the connection to the database
    connection.close()

# Calling the function to set up the database schema directly
initialize_database()
