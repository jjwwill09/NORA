import csv

class Train:
    file_path = 'raw_dataset.csv'

    @staticmethod
    def new(speaker, response):
        # Adds new data to the raw_dataset
        new_data = [[f'### Human: {speaker} ### Assistant: {response}.']]

        try:
            with open(Train.file_path, 'a', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerows(new_data)

            print("Successfully added to training data.")
        except FileNotFoundError:
            print(f"Error: could not find '{Train.file_path}'.")
        except Exception as e:
            print(f"An error occurred: {e}")