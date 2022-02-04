import re
import pandas as pd
import numpy as np
from src.utilities import name_to_first_last

# returns pd dataframe of data needed to create student groups
def get_data():
    q_filepath = input("Enter Qualtrics csv filepath: ").strip()
    f = open(q_filepath, "r")
    q_text = f.read()
    f.close()

    gradebook_filepath = input("Enter gradebook filepath: ").strip()
    grade_df = pd.read_csv(gradebook_filepath)
    grade_df = grade_df.iloc[2:]
    quiz_num = input("Enter quiz number: ").strip()

    students = grade_df["Student"].tolist()

    composite_rating_list = []

    relevant_cols = []
    for col in list(grade_df):
        if "Quiz " + quiz_num in col:
            relevant_cols.append(col)

    for student in students:

        if student == "Student, Test":
            continue
        
        matches = re.findall(name_to_first_last(str(student)) + ",\d", q_text)
        scores = [int(match.split(",")[1]) for match in matches]

        # default rating if student is rated by no one (can occur if student enrolls late)
        student_avg_rating = 6
        if len(scores) != 0:
            student_avg_rating = sum(scores) / len(scores)

        student_quiz_score = 0
        quiz_scores = [grade_df[grade_df["Student"] == student][relevant_col].values for relevant_col in relevant_cols]
        for x in quiz_scores:
            if x.size != 0 and not pd.isna(x):
                student_quiz_score = float(x[0])

        composite_rating_list.append([student, student_avg_rating, student_quiz_score])

    composite_df = pd.DataFrame(composite_rating_list,
                                    columns = ["Name", "Group Rating", "Quiz Score"])

    return composite_df