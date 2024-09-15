import sqlite3

class Band:
    @staticmethod
    def play_in_venue(band_name, venue_title, date):
        """Add a concert for a band at a specified venue on a given date."""
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO concerts (band_name, venue_title, date)
            VALUES (?, ?, ?)
        ''', (band_name, venue_title, date))
        conn.commit()
        conn.close()

    @staticmethod
    def all_introductions(band_name):
        """Fetch all introductions for a specified band."""
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute('''
            SELECT venues.city, bands.hometown
            FROM concerts
            JOIN bands ON concerts.band_name = bands.name
            JOIN venues ON concerts.venue_title = venues.title
            WHERE bands.name = ?
        ''', (band_name,))
        results = cursor.fetchall()
        conn.close()
        
        introductions = [
            f"Hello {city}!!!!! We are {band_name} and we're from {hometown}"
            for city, hometown in results
        ]
        return introductions

    @staticmethod
    def most_performances():
        """Find the band with the most performances."""
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute('''
            SELECT band_name
            FROM concerts
            GROUP BY band_name
            ORDER BY COUNT(*) DESC
            LIMIT 1
        ''')
        result = cursor.fetchone()
        conn.close()
        return result[0] if result else None

class Venue:
    @staticmethod
    def most_frequent_band(venue_title):
        """Find the most frequent band at a specified venue."""
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute('''
            SELECT band_name
            FROM concerts
            WHERE venue_title = ?
            GROUP BY band_name
            ORDER BY COUNT(*) DESC
            LIMIT 1
        ''', (venue_title,))
        result = cursor.fetchone()
        conn.close()
        return result[0] if result else None

class Concert:
    @staticmethod
    def hometown_show(concert_id):
        """Check if the concert is in the band's hometown."""
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute('''
            SELECT venues.city, bands.hometown
            FROM concerts
            JOIN bands ON concerts.band_name = bands.name
            JOIN venues ON concerts.venue_title = venues.title
            WHERE concerts.id = ?
        ''', (concert_id,))
        result = cursor.fetchone()
        conn.close()
        return result[0] == result[1] if result else False
