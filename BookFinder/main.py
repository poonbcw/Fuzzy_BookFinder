import csv
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

# Set up the fuzzy system
def set_up_system():
    # Define fuzzy variables for Mood, Pages, and Category
    mood = ctrl.Antecedent(np.arange(0, 11, 1), 'mood')  # Mood input from 0 to 10
    pages = ctrl.Antecedent(np.arange(0, 1001, 1), 'pages')  # Pages input from 0 to 1000
    category = ctrl.Consequent(np.arange(0, 11, 1), 'category')  # 5 categories: Fiction, Non-Fiction, Sci-Fi, Romance, Fantasy

    # Membership functions for mood 
    mood['Relaxed'] = fuzz.gaussmf(mood.universe, 1.5, 0.4)  
    mood['Excited'] = fuzz.gaussmf(mood.universe, 4, 0.5)    
    mood['Reflective'] = fuzz.gaussmf(mood.universe, 5.5, 0.5)  
    mood['Adventurous'] = fuzz.gaussmf(mood.universe, 6.5, 0.5)  
    mood['Melancholic'] = fuzz.gaussmf(mood.universe, 8.5, 0.4)  

    # Membership functions for pages
    pages['Very Short'] = fuzz.gaussmf(pages.universe, 50, 25)  
    pages['Short'] = fuzz.gaussmf(pages.universe, 225, 50)  
    pages['Average'] = fuzz.gaussmf(pages.universe, 400, 75)  
    pages['Long'] = fuzz.gaussmf(pages.universe, 600, 75)  
    pages['Very Long'] = fuzz.gaussmf(pages.universe, 850, 100)  

    # Membership functions for category (Genres)
    category['Fiction'] = fuzz.gaussmf(category.universe, 1, 0.75)  
    category['Non-Fiction'] = fuzz.gaussmf(category.universe, 3, 0.75)  
    category['Sci-Fi'] = fuzz.gaussmf(category.universe, 5, 0.75)  
    category['Romance'] = fuzz.gaussmf(category.universe, 7, 0.75)  
    category['Fantasy'] = fuzz.gaussmf(category.universe, 9, 0.75) 


    # Define fuzzy rules
    rules = [
        # Relaxed mood
        ctrl.Rule(mood['Relaxed'] & pages['Very Short'], category['Romance']),
        ctrl.Rule(mood['Relaxed'] & pages['Short'], category['Romance']),
        ctrl.Rule(mood['Relaxed'] & pages['Average'], category['Fiction']),
        ctrl.Rule(mood['Relaxed'] & pages['Long'], category['Fiction']),
        ctrl.Rule(mood['Relaxed'] & pages['Very Long'], category['Fiction']),
        
        # Adventurous mood
        ctrl.Rule(mood['Adventurous'] & pages['Very Short'], category['Sci-Fi']),
        ctrl.Rule(mood['Adventurous'] & pages['Short'], category['Sci-Fi']),
        ctrl.Rule(mood['Adventurous'] & pages['Average'], category['Fantasy']),
        ctrl.Rule(mood['Adventurous'] & pages['Long'], category['Fantasy']),
        ctrl.Rule(mood['Adventurous'] & pages['Very Long'], category['Fantasy']),
        
        # Reflective mood
        ctrl.Rule(mood['Reflective'] & pages['Very Short'], category['Non-Fiction']),
        ctrl.Rule(mood['Reflective'] & pages['Short'], category['Non-Fiction']),
        ctrl.Rule(mood['Reflective'] & pages['Average'], category['Fiction']),
        ctrl.Rule(mood['Reflective'] & pages['Long'], category['Fiction']),
        ctrl.Rule(mood['Reflective'] & pages['Very Long'], category['Fiction']),
        
        # Excited mood
        ctrl.Rule(mood['Excited'] & pages['Very Short'], category['Sci-Fi']),
        ctrl.Rule(mood['Excited'] & pages['Short'], category['Sci-Fi']),
        ctrl.Rule(mood['Excited'] & pages['Average'], category['Fantasy']),
        ctrl.Rule(mood['Excited'] & pages['Long'], category['Fantasy']),
        ctrl.Rule(mood['Excited'] & pages['Very Long'], category['Fantasy']),
        
        # Melancholic mood
        ctrl.Rule(mood['Melancholic'] & pages['Very Short'], category['Romance']),
        ctrl.Rule(mood['Melancholic'] & pages['Short'], category['Romance']),
        ctrl.Rule(mood['Melancholic'] & pages['Average'], category['Fiction']),
        ctrl.Rule(mood['Melancholic'] & pages['Long'], category['Fiction']),
        ctrl.Rule(mood['Melancholic'] & pages['Very Long'], category['Fiction']),
    ]
    # Create control system
    book_ctrl_system = ctrl.ControlSystem(rules)

    # Return control system and fuzzy variables for plotting
    return book_ctrl_system, mood, pages, category

# Plot membership functions with shading
def plot_membership_functions(mood, pages, category):
    # Plotting mood membership functions with shading
    plt.figure(figsize=(15, 10))

    plt.subplot(3, 1, 1)
    for label in mood.terms:
        plt.plot(mood.universe, mood[label].mf, label=label)
        plt.fill_between(mood.universe, mood[label].mf, alpha=0.3) 
    plt.title('Mood Membership Functions')
    plt.xlabel('Mood Level')
    plt.ylabel('Membership Degree')
    plt.legend()

    # Plotting pages membership functions with shading
    plt.subplot(3, 1, 2)
    for label in pages.terms:
        plt.plot(pages.universe, pages[label].mf, label=label)
        plt.fill_between(pages.universe, pages[label].mf, alpha=0.3)  
    plt.title('Pages Membership Functions')
    plt.xlabel('Number of Pages')
    plt.ylabel('Membership Degree')
    plt.legend()

    # Plotting category membership functions with shading
    plt.subplot(3, 1, 3)
    for label in category.terms:
        plt.plot(category.universe, category[label].mf, label=label)
        plt.fill_between(category.universe, category[label].mf, alpha=0.3) 
    plt.title('Category Membership Functions')
    plt.xlabel('Category Level')
    plt.ylabel('Membership Degree')
    plt.legend()

    plt.tight_layout()
    plt.show()

def plot_input_output_shaded(mood, pages, category, mood_input, pages_input, category_output):
    # Plotting mood membership functions with shading for the input value
    plt.figure(figsize=(15, 10))

    plt.subplot(3, 1, 1)
    for label in mood.terms:
        plt.plot(mood.universe, mood[label].mf, label=label)
        plt.fill_between(mood.universe, mood[label].mf, where=(mood.universe == mood_input), color='orange', alpha=0.5)
    plt.axvline(x=mood_input, color='orange', linestyle='--')  
    plt.title('Mood Membership Functions with Input Highlighted')
    plt.xlabel('Mood Level')
    plt.ylabel('Membership Degree')
    plt.legend()

    # Plotting pages membership functions with shading for the input value
    plt.subplot(3, 1, 2)
    for label in pages.terms:
        plt.plot(pages.universe, pages[label].mf, label=label)
        plt.fill_between(pages.universe, pages[label].mf, where=(pages.universe == pages_input), color='orange', alpha=0.5)
    plt.axvline(x=pages_input, color='orange', linestyle='--')  
    plt.title('Pages Membership Functions with Input Highlighted')
    plt.xlabel('Number of Pages')
    plt.ylabel('Membership Degree')
    plt.legend()

    # Plotting category membership functions with shading for the output value
    plt.subplot(3, 1, 3)
    for label in category.terms:
        plt.plot(category.universe, category[label].mf, label=label)
        plt.fill_between(category.universe, category[label].mf, where=(category.universe == category_output), color='green', alpha=0.5)
    plt.axvline(x=category_output, color='green', linestyle='--')  
    plt.title('Category Membership Functions with Output Highlighted')
    plt.xlabel('Category Level')
    plt.ylabel('Membership Degree')
    plt.legend()

    plt.tight_layout()
    plt.show()


# Map category number to string for book categories
def category_to_genre(category_output):
    genre_map = {
        0: "Fiction",
        1: "Non-Fiction",
        2: "Sci-Fi",
        3: "Romance",
        4: "Fantasy"
    }
    
    if 0 <= category_output < 2:
        return "Fiction"
    elif 2 <= category_output < 4:
        return "Non-Fiction"
    elif 4 <= category_output < 6:
        return "Sci-Fi"
    elif 6 <= category_output < 8:
        return "Romance"
    elif 8 <= category_output <= 10:
        return "Fantasy"
    else:
        return "Unknown"

# Read book data from CSV and return matching books
def get_books_by_genre(genre):
    matching_books = []
    try:
        with open('Data/books_fuzzy.csv', mode='r', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header
            for row in reader:
                if row[2].lower() == genre.lower():  # Genre is in the third column
                    matching_books.append(row)
    except FileNotFoundError:
        print("Error: 'books_fuzzy.csv' file not found.")
    return matching_books

# Find the best matching book based on review score and page proximity
def find_best_match(books, pages_input):
    if not books:
        return None
    # Find the book closest to the number of pages input
    return min(books, key=lambda x: abs(int(x[3]) - pages_input))  # pages are in the 4th column

# Simulation and running the fuzzy system
def simulate_recommendation(mood_input, pages_input):
    # Input validation
    if not (0 <= mood_input <= 10):
        raise ValueError("Mood input must be between 0 and 10.")
    if not (100 <= pages_input <= 1000):
        raise ValueError("Pages input must be between 100 and 1000.")

    # Set up the system
    book_ctrl_system, mood, pages, category = set_up_system() 
    book_simulation = ctrl.ControlSystemSimulation(book_ctrl_system)  

    # Input user data for mood and pages
    book_simulation.input['mood'] = mood_input
    book_simulation.input['pages'] = pages_input

    # Compute the recommendation
    try:
        book_simulation.compute()
        category_output = book_simulation.output['category']
        print(f"Input Mood: {mood_input}, Input Pages: {pages_input}")
        print(f"Category Output before mapping: {category_output}")

    except Exception as e:
        print(f"Error in fuzzy system computation: {e}")
        return None, None

    # Map category number to genre name
    genre = category_to_genre(category_output)

    # Find matching books from the CSV file
    matching_books = get_books_by_genre(genre)

    # Find the best match
    best_book = find_best_match(matching_books, pages_input)

    return genre, best_book, category_output

if __name__ == '__main__':
    try:
        # Set up the fuzzy system and plot membership functions
        book_ctrl_system, mood, pages, category = set_up_system()
        # plot_membership_functions(mood, pages, category)    

        # Get user input and simulate recommendation
        mood_input = float(input("Enter your mood level (0-10): "))
        pages_input = int(input("Enter the number of pages you're interested in (100-1000): "))

        # Simulate book recommendation
        genre, best_book, category_output = simulate_recommendation(mood_input, pages_input)

        plot_input_output_shaded(mood, pages, category, mood_input, pages_input, category_output)

        # Print the recommendation
        if genre and best_book:
            title, author, genre, pages, year, score, language, popularity, publisher = best_book
            print(f"\nRecommended Genre: {genre}")
            print(f"Best Match Book: '{title}' by {author} ({genre}, {pages} pages, {year}, Score: {score})")
            print(f"Language: {language}, Popularity: {popularity}, Publisher: {publisher}")
        else:
            print("No suitable book found based on your inputs.")
    except ValueError as e:
        print(f"Invalid input. {e}")
