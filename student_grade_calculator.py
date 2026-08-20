scores = []
name = input("Enter your name: ")
maths_score = int(input("Enter your maths score: "))
scores.append(maths_score)

science_score = int(input("Enter your science score: "))
scores.append(science_score)

english_score = int(input("Enter your english score: "))
scores.append(english_score)

history_score = int(input("Enter your history score: "))
scores.append(history_score)

computer_score = int(input("Enter your computer score: "))
scores.append(computer_score)

average_score = sum(scores)/len(scores)

print()

def calculate_grade(average):
    if average >= 90:
        return "A"
    if average >= 80:
        return "B"
    if average >= 70:
        return "C"
    if average >= 60:
        return "D"
    if average >= 50:
        return "E"
    else:
        return "F"

grade = calculate_grade(average_score)
print(f'{name.capitalize()} your average score is {average_score}%. And your grade is {grade}.')


