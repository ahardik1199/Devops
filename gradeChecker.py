#!/usr/bin/env python3

def getGrade(score:int)->str:
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

def main()->None:
    try:
        score:int =int(input("Enter your score (0-100):"))
        if score < 0 or score > 100:
            raise ValueError
    except ValueError:
        print("Error: Please enter a valid integer between 0 and 100.")
        return
    grade:str =getGrade(score)
    print(f"Score: {score} → Grade: {grade}")

if __name__ == "__main__":
    main()