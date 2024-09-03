import datetime

def get_japanese_weekday(date_str):
    weekday_map = {
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

def solution_station_3(new_date, pattern_sets):
    for sample_input, _, sample_output in pattern_sets:
        if get_japanese_weekday(sample_input) == sample_output:
            return get_japanese_weekday(new_date)