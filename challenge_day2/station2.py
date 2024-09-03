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
    
    # Convert the string date into a datetime object
    date_obj = datetime.datetime.strptime(date_str, "%Y-%m-%d")
    
    # Get the day of the week in English
    day_of_week = date_obj.strftime("%A")
    
    # Return the corresponding day in Japanese
    return days_in_japanese[day_of_week]