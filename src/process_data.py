import math
import random
import pandas as pd
import numpy as np



def process_data(composite_df):
    
    normalized_df = composite_df
    column = normalized_df["Group Rating"]
    normalized_df["Group Rating"] = (column - column.mean()) / column.std()
    column = normalized_df["Quiz Score"]
    normalized_df["Quiz Score"] = (column - column.mean()) / column.std()
    

    # Adjustable weights ******************************************
    # as this increases, group weight becomes more significant
    group_weight = 0.25
    # as this increases, quiz weight becomes more significant
    quiz_weight = 0.75
    # as this increases, group choice approaches normal distribution
    random_weight = 0.1
    # *************************************************************

    epsilon = np.random.normal(size = normalized_df.shape[0]) * random_weight
    normalized_df["Weighted Score"] = normalized_df["Group Rating"] * group_weight + normalized_df["Quiz Score"] * quiz_weight
    normalized_df["Weighted + Rand"] = normalized_df["Weighted Score"] + epsilon

    sorted_df = normalized_df.sort_values(by = "Weighted + Rand")

    sorted_names = sorted_df["Name"].tolist()


    groups = {}
    # group size
    k = 4
    for i, name in enumerate(sorted_names):
        if math.floor(i / k) in groups:
            groups[math.floor(i / k)].append(name)
        else:
            groups[math.floor(i / k)] = [name]

    grouplist = list(groups.values())
    random.shuffle(grouplist)
    
    return grouplist


def output_to_tex(starterdoc, grouplist):
    assignment_num = input("Enter assignment number: ").strip()
    starterdoc = starterdoc.replace("NUMBER_HERE", assignment_num)

    table_text = ""
    for i, group in enumerate(grouplist):
        table_text = table_text + str(i + 1)
        for member in group:
            table_text = table_text + " & " + member
        table_text = table_text + r" \\" + "\n" + r"\hline" + "\n"
        
    starterdoc = starterdoc.replace("TABLE_HERE", table_text)

    output_filepath = input("Enter output tex file path: ").strip()
    f = open(output_filepath, "w")
    f.write(starterdoc)
    f.close()

    print("Process completed.")
