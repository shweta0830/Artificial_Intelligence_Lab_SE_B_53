def suggest_career(interests):
    interests = [i.strip().lower() for i in interests]

    if 'maths' in interests and 'physics' in interests:
        print("Suggested Career Path: Mechanical Engineering")
    elif 'programming' in interests and 'maths' in interests:
        print("Suggested Career Path: Computer Engineering")
    elif 'biology' in interests and 'chemistry' in interests:
        print("Suggested Career Path: Biotechnology")
    elif 'circuits' in interests and 'maths' in interests:
        print("Suggested Career Path: Electronics Engineering")
    elif 'programming' in interests and 'statistics' in interests:
        print("Suggested Career Path: Artificial Intelligence and Data Science")
    elif 'programming' in interests and 'ai concepts' in interests:
        print("Suggested Career Path: Artificial Intelligence and Machine Learning Engineering")
    else:
        print("Sorry, no specific career path suggestion available for the given interests.")

def main():
    print("Welcome to the Career Path Expert System!")
    interests_input = input("Enter your interests separated by commas (e.g., Maths, Physics, Programming): ")
    interests = interests_input.split(',')
    suggest_career(interests)

if __name__ == "__main__":
    main()

