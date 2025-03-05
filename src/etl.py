import csv
import random


class Etl:
    def __init__(self, csv_file):
        self.data = []
        with open(csv_file, "r") as f:
            reader = csv.reader(f)
            self.data = list(reader)

    def derive_gender(self):
        # add a new column to self.data named Gender, the value is ramdomly selected from (0,1,2)
        if self.data:
            self.data[0].append("Gender")
            for row in self.data[1:]:  # Skip header row
                gender = random.choice([0, 1, 2])
                row.append(gender)

    def fix_age(self):
        if not self.data:
            return

        # Find the index of the 'age' column
        header = self.data[0]
        if "age" not in header:
            return

        age_index = header.index("age")

        # Collect non-outlier ages
        valid_ages = []
        for row in self.data[1:]:
            try:
                age = int(row[age_index])
                if 0 <= age <= 150:
                    valid_ages.append(age)
            except ValueError:
                continue

        if not valid_ages:
            return

        # Calculate the average of valid ages
        average_age = sum(valid_ages) / len(valid_ages)

        # Replace outlier ages with the average age
        for row in self.data[1:]:
            try:
                age = int(row[age_index])
                if age < 0 or age > 150:
                    row[age_index] = str(int(average_age))
            except ValueError:
                row[age_index] = str(int(average_age))
