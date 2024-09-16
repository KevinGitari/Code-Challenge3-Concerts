from db_connection import setup_database
from classes import Band, Venue, Concert

def setup_and_run():
    """Setup the database and perform example operations."""
    setup_database()
    
    # Example data

    band_name = 'The Star Gazers'
    venue_title = 'Forever Young'
    date = '2009-09-09'
    concert_id = 1
    
    # Add a new concert

    Band.add_concert(band_name, venue_title, date)
    
    # Retrieve and print band introductions

    introductions = Band.get_introductions(band_name)
    print("Introductions:")
    for intro in introductions:
        print(intro)
    
    # To check if a concert is in the band's hometown and print result

    is_hometown = Concert.is_hometown_concert(concert_id)
    print(f"Is hometown show: {is_hometown}")
    
    #To find and print the band with the most performances

    most_performances_band = Band.find_most_performances()
    print(f"Band with most performances: {most_performances_band}")
    
    #Io  Determine and print the most frequent band at a specific venue

    most_frequent_band = Venue.find_most_frequent_band(venue_title)
    print(f"Most frequent band at {venue_title}: {most_frequent_band}")

# To execute the setup and run function
setup_and_run()
