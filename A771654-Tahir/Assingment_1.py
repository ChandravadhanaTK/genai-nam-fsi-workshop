import random
# Develop a program that generates random quizzes with multiple-choice questions from a 
# pool of questions and evaluates user answers

# Define a pool of questions with their correct answers
question_pool = {
    "What is the capital of France?": ["A. Paris", "B. Berlin", "C. Madrid", "D. Rome"],
    "Which planet is known as the Red Planet?": ["A. Mars", "B. Venus", "C. Jupiter", "D. Saturn"],
    "What is the largest mammal in the world?": ["A. Elephant", "B. Blue Whale", "C. Giraffe", "D. Dolphin"],
    # Add more questions as needed
}

answer_pool= {
    "What is the capital of France?": 'A',
    "Which planet is known as the Red Planet?": 'B',
    "What is the largest mammal in the world?": 'C',
    # Add more questions as needed
}

def generate_quiz(num_questions):
    # Randomly select questions from the pool
    try:

        selected_questions = random.sample(list(question_pool.items()), num_questions)
        
        
        # Create a quiz with questions and answer choices
        quiz = {}
        for question, choices in selected_questions:
            quiz[question] = choices
        
        return quiz
    except:
        return "Nothing"

def present_quiz(quiz):
    # Display each question and its choices to the user
    for question, choices in quiz.items():
        print(question)
        for choice in choices:
            print(choice)
        print()

def evaluate_answers(quiz, user_answers):
    # Evaluate user answers and calculate the score
    score = 0
    for question, answer in quiz.items():
      if user_answers[question] == answer_pool[question]:
        score += 1

    return score

def main():
    # Set the number of questions in the quiz
    num_questions = 2
    
    # Generate a random quiz
    quiz = generate_quiz(num_questions)
    
    # Present the quiz to the user
    present_quiz(quiz)
    
    # Collect user answers
    user_answers = {}
    for question in quiz.keys():
        user_answer = input(f"Your answer for '{question}': ").strip().upper()
        user_answers[question] = user_answer
    print(user_answers)
    # Evaluate user answers and display the score
    score = evaluate_answers(quiz, user_answers)
    print(f"Your score: {score}/{num_questions}")

if __name__ == "__main__":
    main()