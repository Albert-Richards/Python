name = str(input("Please enter your name:"))
h_w = int(input("Please enter your homework mark:"))
assessment = int(input("Please enter your assessment mark:"))
final_exam = int(input("Please enter your final exam mark:"))

def grade_score(mark1, mark2, mark3):
    ICT = (mark1 + mark2 + mark3)*100/175
    return(f"Name: {name}, final ICT grade: {ICT}")

print(grade_score(h_w, assessment, final_exam))