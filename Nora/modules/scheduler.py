from datetime import datetime
from datetime import date
import csv

class schedule:
    @staticmethod
    def add(text):
        date = text[text.index('0'):(text.index('0') + 8)]
        event = text[(text.index('0') + 8):]
        current_time = datetime.now()
        new_data = [[f'{date.today()}, {current_time}'],
                    [date],
                    [event]]
        try:
            with open('schedule.csv', 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(new_data)
            
            print("scheduled event")
        except FileNotFoundError:
            print("Error: could not find 'log.csv'.")
        except Exception as e:
            print(f"an error occured: {e}")
