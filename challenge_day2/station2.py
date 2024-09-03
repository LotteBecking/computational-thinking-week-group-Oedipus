import datetime

def solution_station_2(date_str):
    # Mapping of days of the week to their Japanese equivalents
    days_in_japanese = {
        "Monday": "月曜日",
        "Tuesday": "火曜日",
        "Wednesday": "水曜日",
        "Thursday": "木曜日",
        "Friday": "金曜日",
        "Saturday": "土曜日",
        "Sunday": "日曜日"
    }

    date_obj = datetime.datetime.strptime(date_str, '%Y-%m-%d')
    
    english_day = date_obj.strftime('%A')
    
    japanese_day = weekday_map[english_day]
    
    return japanese_day

def find_matching_pattern(new_input, pattern_sets):
    for sample_input, _, sample_output in pattern_sets:
        if get_japanese_weekday(sample_input) == sample_output:
            return get_japanese_weekday(new_input)
    
    return "No matching pattern found."

pattern_sets = [
    ('2023-12-10', '2024-10-21', "日曜日"),
    ('2023-06-08', '2024-02-12', "木曜日"),
    ('2023-01-07', '2023-12-19', "土曜日")
]

new_input = input("Enter the new input date (YYYY-MM-DD): ")
output = find_matching_pattern(new_input, pattern_sets)
print(f"The output for {new_input} is {output}.")
