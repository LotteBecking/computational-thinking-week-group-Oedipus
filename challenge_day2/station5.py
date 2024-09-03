import pandas as pd

# read the CSV file
df = pd.read_csv("Student_Learning_Teams.csv")

# rename columns to match the header in your file
df.columns = ['Student', 'Team']

# convert the 'Team' column to integers
df['Team'] = df['Team'].astype(int)

# function to find the learning team for a given student name
def solution_station_5(student_name):
    # search for the student in the DataFrame
    result = df[df['Student'] == student_name]
    
    # if the student is found, return their team, otherwise return a message
    if not result.empty:
        return result.iloc[0]['Team']
    else:
        return "Student not found"
