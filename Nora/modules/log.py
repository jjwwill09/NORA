import pandas as pd
import csv
from datetime import datetime
from datetime import date

class Log:
    @staticmethod
    # Adds time and word count to logs
    def add_data(elapsed_time, user_query):
        words = user_query.split()
        word_count = len(words)
        
        current_time = datetime.now()
        new_data = [[f'{date.today()}, {current_time.time()}'],
                    [f'Response Time: {elapsed_time}'],
                    [f'User Query Count: {word_count}']
                    ]
        try:
            with open('logs.csv', 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(new_data)
            
            print("logged data")
        except FileNotFoundError:
            print("Error: could not find 'log.csv'.")
        except Exception as e:
            print(f"an error occured: {e}")

    @staticmethod
    # Logs conversation
    def new(speaker, response):
        current_time = datetime.now()

        # Formats with date and time
        new_data = [[f'{date.today()}, {current_time.time()}'], 
                    [f'Jesse: {speaker}'], 
                    [f'Nora: {response}'],
                    ]
        try:
            with open('logs.csv', 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(new_data)

            print("succesfully logged")
        except FileNotFoundError:
            print("Error: could not find 'log.csv'.")
        except Exception as e:
            print(f"an error occured: {e}")

    @staticmethod
    # Undoes the most recent log
    def undo(file_path='logs.csv', n=3):
        try:
           df = pd.read_csv(file_path)
           df_new = df.iloc[:-n]
           df_new.to_csv(file_path, index=False)

           print(f"Successfully removed the last {n} rows from '{file_path}'.")
        except FileNotFoundError:
            print(f"Error: The file '{file_path}' was not found.")
        except Exception as e:
            print(f"Could not undo log: {e}")
    
    @staticmethod
    # Clears the entirty of the log file
    def clear(file_path='logs.csv'):
        try:
            with open(file_path, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(['----- LOG START -----'])
            print(f"Content of '{file_path}' cleared successfully.")
        except IOError as e:
            print(f"Error clearing file '{file_path}': {e}")

            
        
    
    
