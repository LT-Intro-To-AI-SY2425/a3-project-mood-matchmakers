import random

# Expanded arrays for each mood
happy_movies = [
    "The Intouchables", "Paddington 2", "Ferris Bueller's Day Off", 
    "Crazy Rich Asians", "Zootopia", "The Grand Budapest Hotel",
    "Little Miss Sunshine", "Coco", "Jumanji: Welcome to the Jungle"
]
happy_music = [
    "Happy by Pharrell Williams", "Good Vibrations by The Beach Boys", 
    "Walking on Sunshine by Katrina and the Waves", "Shake It Off by Taylor Swift", 
    "Can't Stop the Feeling! by Justin Timberlake", "Best Day of My Life by American Authors"
]
happy_activities = [
    "Go for a walk in nature", "Try a new recipe or bake something sweet", 
    "Host a game night with friends", "Take a day trip to a nearby city", 
    "Start a gratitude journal", "Do some light gardening"
]

sad_movies = [
    "The Pursuit of Happyness", "A Monster Calls", "Eternal Sunshine of the Spotless Mind",
    "The Fault in Our Stars", "Forrest Gump", "Room", 
    "The Shawshank Redemption", "Blue is the Warmest Color"
]
sad_music = [
    "Someone Like You by Adele", "Fix You by Coldplay", 
    "The Night We Met by Lord Huron", "Hallelujah by Jeff Buckley",
    "Let Her Go by Passenger", "Back to December by Taylor Swift"
]
sad_activities = [
    "Write in a journal to express your feelings", "Take a warm bath with calming scents", 
    "Watch a comforting show or read a favorite book", "Create a vision board of happier times",
    "Reach out to a friend or family member", "Practice self-care with a cozy blanket and tea"
]

anxious_movies = [
    "Inside Out", "A Beautiful Mind", "Little Miss Sunshine", 
    "The Perks of Being a Wallflower", "The Secret Life of Walter Mitty", 
    "Joker", "Good Will Hunting"
]
anxious_music = [
    "Weightless by Marconi Union", "Breathe Me by Sia", 
    "River by Leon Bridges", "Ocean Eyes by Billie Eilish", 
    "Peace by Taylor Swift", "Dreams by Fleetwood Mac"
]
anxious_activities = [
    "Practice mindfulness or meditation", "Try yoga or gentle stretching", 
    "Go for a nature walk to clear your mind", "Create a calming playlist", 
    "Practice deep breathing exercises", "Engage in a creative hobby like painting"
]

energized_movies = [
    "Scott Pilgrim vs. The World", "Baby Driver", "Rocky", 
    "Mad Max: Fury Road", "The Avengers", "Guardians of the Galaxy",
    "Rush"
]
energized_music = [
    "Uptown Funk by Mark Ronson ft. Bruno Mars", "Can’t Stop the Feeling! by Justin Timberlake", 
    "Thunder by Imagine Dragons", "Stronger by Kanye West", 
    "Happy Now by Kygo", "Blinding Lights by The Weeknd"
]
energized_activities = [
    "Join a dance class or Zumba session", "Go for a run or workout at the gym", 
    "Explore a new hobby like painting or crafting", "Try rock climbing or a new sport",
    "Attend a local fitness class", "Take a spontaneous road trip"
]

reflective_movies = [
    "Before Sunrise", "Her", "Dead Poets Society", 
    "The Tree of Life", "Life of Pi", "The Secret Life of Walter Mitty"
]
reflective_music = [
    "The Night We Met by Lord Huron", "Slow Burn by Kacey Musgraves", 
    "Breathe by Pink Floyd", "Both Sides Now by Joni Mitchell", 
    "Landslide by Fleetwood Mac", "River by Leon Bridges"
]
reflective_activities = [
    "Take a solo trip to a quiet place", "Spend time in nature with a sketchbook", 
    "Try meditative art or coloring", "Engage in a deep conversation with a friend",
    "Write a letter to your future self", "Reflect on personal goals and aspirations"
]

overwhelmed_movies = [
    "Julie & Julia", "The Secret Life of Walter Mitty", "The Intern", 
    "Eat Pray Love", "About Time", "The Hundred-Foot Journey"
]
overwhelmed_music = [
    "Let It Be by The Beatles", "Rise Up by Andra Day", 
    "Stronger by Kelly Clarkson", "Fight Song by Rachel Platten", 
    "Three Little Birds by Bob Marley", "Don't Stop Believin' by Journey"
]
overwhelmed_activities = [
    "Declutter a small space in your home", "Create a vision board for your goals", 
    "Practice deep breathing exercises", "Write a list of things you're grateful for", 
    "Take a break and watch a feel-good movie", "Spend time organizing your thoughts in a journal"
]

# Function to get suggestions based on emotion
def get_suggestions(emotion):
    suggestions = {
        "happy": (happy_movies, happy_music, happy_activities),
        "sad": (sad_movies, sad_music, sad_activities),
        "anxious": (anxious_movies, anxious_music, anxious_activities),
        "energized": (energized_movies, energized_music, energized_activities),
        "reflective": (reflective_movies, reflective_music, reflective_activities),
        "overwhelmed": (overwhelmed_movies, overwhelmed_music, overwhelmed_activities)
    }
    return suggestions.get(emotion)

# Main program loop
def main():
    while True:
        print("\nWelcome to the Emotion-Based Suggestion Tool!")
        emotion = input("What emotion are you feeling? (happy, sad, anxious, energized, reflective, overwhelmed or 'exit' to quit): ").strip().lower()
        
        if emotion == "exit":
            print("Goodbye! Take care!")
            break
        
        options = get_suggestions(emotion)
        
        if options:
            movies, music, activities = options
            
            print("\nWhat would you like to do?")
            print("1. Try an activity")
            print("2. Watch a movie")
            print("3. Listen to music")
            action = input("Please enter 1, 2, or 3: ").strip()
            
            if action == "1":
                print("Here's an activity you can try: ", random.choice(activities))
            elif action == "2":
                print("Here's a movie you can watch: ", random.choice(movies))
            elif action == "3":
                print("Here's a song you can listen to: ", random.choice(music))
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")
        else:
            print("Sorry, I don't recognize that emotion. Please try again.")

if __name__ == "__main__":
    main()
