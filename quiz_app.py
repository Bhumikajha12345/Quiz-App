# quiz_app.py

questions = [
    {
        "question": "What is the capital of India?",
        "options": ["A. Mumbai", "B. Delhi", "C. Kolkata", "D. Chennai"],
        "answer": "B"
    },
    {
        "question": "Which language is used for web development?",
        "options": ["A. Python", "B. Java", "C. HTML", "D. C++"],
        "answer": "C"
    },
    {
        "question": "What does CPU stand for?",
        "options": ["A. Central Program Unit", "B. Central Processing Unit", "C. Central Power Unit", "D. Control Processing Unit"],
        "answer": "B"
    },
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": ["A. define", "B. def", "C. function", "D. fun"],
        "answer": "B"
    },
    {
        "question": "Who developed Python language?",
        "options": ["A. Dennis Ritchie", "B. Bjarne Stroustrup", "C. James Gosling", "D. Guido van Rossum"],
        "answer": "D"
    }
]

score = 0

print("\n🎉 Welcome to the Python Quiz App! 🎉\n")

for i, q in enumerate(questions, 1):
    print(f"Q{i}: {q['question']}")
    for option in q['options']:
        print(option)
    user_ans = input("👉 Enter your answer (A/B/C/D): ").strip().upper()

    if user_ans == q['answer']:
        print("✅ Correct!\n")
        score += 1
    else:
        print(f"❌ Wrong! Correct answer is: {q['answer']}\n")

print("🎯 Quiz Completed!")
print(f"📝 Your Final Score is: {score}/{len(questions)}\n")
