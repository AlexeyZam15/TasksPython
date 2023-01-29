# Напишите программу, которая вычислит:
# Сколько раз встретятся часовая и минутная стрелка механических часов с 0:05 до 23:55
# Если часовая стрелка двигается только после того как минутная пройдёт отрезок в 60 минут.

def count_meet_hour_and_minute_hands(start_hour, start_minute, end_hour, end_minute):
    count = 0
    end_minute_1 = 60
    i = 1 if start_hour > 12 else 0
    while i < 2:
        hours = start_hour
        while hours < 12:
            if hours + 12 * i == end_hour:
                end_minute_1 = end_minute
            minutes = start_minute
            while minutes <= end_minute_1:
                if minutes / 5 == hours:
                    # print(hours + 12 * i, minutes, end="|")
                    count += 1
                # print(hours + 12 * i, minutes, end="|")
                minutes += 1
            hours += 1
            start_minute = 0
            if hours + 12 * i > end_hour:
                break
        start_hour = 0
        i += 1
    return count

start_hour = 0
start_minute = 5
end_hour = 23
end_minute = 55

count_meet1 = count_meet_hour_and_minute_hands(start_hour, start_minute, end_hour, end_minute)
print(f"\n Часовая и минутная стрелки сходятся раз: {count_meet1}")
