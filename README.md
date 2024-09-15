# Concert Management System

## Overview

This project manages concerts by interacting with a SQLite database. It includes functionalities to manage bands, venues, and concerts. The system allows adding concerts, fetching band introductions, checking if a concert is in the band’s hometown, and finding the most frequent bands at venues.

## Setup

### Prerequisites

- Python 3.10.12
- SQLite3 (usually comes with Python)

### Installation

1. **Clone the Repository**

   ```sh
   git clone https://github.com/KevinGitari/WK3-Code-Challenge3-Concerts
   cd your directory
   ```

2. **Install Dependencies**

   This project does not require additional Python packages beyond the standard library. Ensure you have Python 3.10.12 installed.

3. **Database Setup**

   Run the following script to set up the database and create the required tables:

   ```sh
   python3 classes.py
   ```

   This will create the database file `database.db` with the necessary schema.

## Usage

### Example Operations

1. **Adding a Concert**

   The following code snippet adds a concert for a band at a specified venue on a given date:

   ```python
   from models import Band

   Band.add_concert('The Rockers', 'Rock Arena', '2024-09-15')
   ```

2. **Fetching Band Introductions**

   Retrieve introductions for a band:

   ```python
   from models import Band

   introductions = Band.get_introductions('The Rockers')
   print(introductions)
   ```

3. **Checking if a Concert is in the Band's Hometown**

   Verify if a specific concert is held in the band’s hometown:

   ```python
   from models import Concert

   is_hometown = Concert.is_hometown_concert(1)
   print(f"Is hometown show: {is_hometown}")
   ```

4. **Finding the Band with the Most Performances**

   Determine which band has the most performances:

   ```python
   from models import Band

   most_performances_band = Band.find_most_performances()
   print(f"Band with most performances: {most_performances_band}")
   ```

5. **Finding the Most Frequent Band at a Venue**

   Identify the most frequent band at a specific venue:

   ```python
   from models import Venue

   most_frequent_band = Venue.find_most_frequent_band('Rock Arena')
   print(f"Most frequent band at Rock Arena: {most_frequent_band}")
   ```

## File Descriptions

- **`initialize.py`**: Contains the main script to set up the database and perform example operations.
- **`classes.py`**: Defines the `Band`, `Venue`, and `Concert` classes with methods to interact with the database.
- **`db_connection.py`**: Contains the `setup_database()` function to initialize the database schema (you may need to create this file if it's not included yet).

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
```

