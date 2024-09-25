import csv

# Generate diverse book data based on categories and page ranges
books = [
    ["Title", "Author", "Genre", "Pages", "PublicationYear", "ReviewScore", "Language", "Popularity", "Publisher"],
    
    # Fiction
    ["Winds of Fate", "Alice Grey", "Fiction", 120, 2019, 4.0, "English", "Medium", "Penguin Books"],  # Very Short
    ["Under the Stars", "Emma Stone", "Fiction", 150, 2018, 3.9, "Spanish", "Medium", "Casa del Mar Press"],  # Very Short
    ["Twilight Dreams", "Hannah Rivers", "Fiction", 200, 2021, 4.2, "Japanese", "Medium", "Tokyo Books"],  # Short
    ["The Lost City", "Mark Hamilton", "Fiction", 350, 2020, 4.1, "English", "High", "Scribe Publications"],  # Average
    ["Shadows of the Past", "Linda Green", "Fiction", 500, 2017, 4.3, "English", "High", "Sage Press"],  # Long
    ["Echoes of Eternity", "David Black", "Fiction", 800, 2022, 4.6, "English", "Medium", "Everest Books"],  # Very Long
    
    # Non-Fiction
    ["Science of Life", "Dr. John Miles", "Non-Fiction", 180, 2017, 4.1, "English", "High", "Oxford University Press"],  # Short
    ["Mind and Matter", "Dr. Elena Clark", "Non-Fiction", 220, 2020, 4.2, "English", "Medium", "Harvard Press"],  # Short
    ["The Human Condition", "Prof. Samuel Ryan", "Non-Fiction", 240, 2023, 4.3, "English", "High", "Yale University Press"],  # Short
    ["The Art of Thinking", "Jill Carson", "Non-Fiction", 320, 2019, 4.0, "English", "Medium", "Insight Books"],  # Average
    ["Global Perspectives", "Michael Scott", "Non-Fiction", 450, 2021, 4.4, "English", "Medium", "Global Press"],  # Long
    ["History Unveiled", "Emma Wilson", "Non-Fiction", 600, 2022, 4.7, "English", "High", "Epoch Publishing"],  # Very Long
    
    # Sci-Fi
    ["Galactic Journey", "Ethan Stark", "Sci-Fi", 320, 2021, 4.5, "English", "High", "Orbit Books"],  # Average
    ["Space Odyssey", "Lucas Silva", "Sci-Fi", 310, 2016, 4.1, "English", "High", "Tor Books"],  # Average
    ["Starlight Chronicles", "Zara Lee", "Sci-Fi", 180, 2020, 3.9, "English", "Medium", "Quantum Books"],  # Short
    ["Nebula Nights", "Aaron Quinn", "Sci-Fi", 400, 2023, 4.2, "English", "Medium", "Stellar Publications"],  # Long
    ["Galactic Wars", "Nina Clark", "Sci-Fi", 700, 2019, 4.8, "English", "High", "Infinity Books"],  # Very Long
    
    # Romance
    ["Hearts in Bloom", "Sophia Reed", "Romance", 450, 2020, 4.3, "French", "Low", "L'Édition Paris"],  # Long
    ["Lovers at Dawn", "Maria Hernandez", "Romance", 470, 2019, 4.0, "Spanish", "High", "Luna Roja"],  # Long
    ["A Love to Remember", "Isabelle Grace", "Romance", 500, 2018, 3.8, "English", "Medium", "HarperCollins"],  # Long
    ["Love in the City", "Claire Adams", "Romance", 300, 2022, 4.1, "English", "Medium", "Urban Books"],  # Average
    ["Whispers of Love", "Rose Parker", "Romance", 150, 2017, 4.2, "English", "High", "Sweetheart Press"],  # Very Short
    
    # Fantasy
    ["Dragons of the North", "Christopher Flynn", "Fantasy", 765, 2023, 4.8, "English", "High", "Ace Books"],  # Very Long
    ["Kingdom of Shadows", "Alex North", "Fantasy", 800, 2022, 4.6, "English", "Medium", "Random House"],  # Very Long
    ["Enchanted Forest", "Lily Evans", "Fantasy", 600, 2018, 4.3, "English", "High", "Mystic Books"],  # Long
    ["The Lost Realm", "Hannah Green", "Fantasy", 350, 2019, 4.2, "English", "Medium", "Fantasy Press"],  # Average
    ["Tales of Magic", "Rosa Lee", "Fantasy", 220, 2021, 4.1, "English", "Medium", "Legend Books"],  # Short
    ["Magic Sparks", "Ella Johnson", "Fantasy", 130, 2020, 3.9, "English", "Medium", "Dreamscape Publishing"],  # Very Short
]

# Write the book data to a CSV file
with open('books_fuzzy.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerows(books)

print("CSV file with diverse book categories and page lengths created successfully.")
