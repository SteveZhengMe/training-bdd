import random
import csv


class BatchInfer:
    def __init__(self, source_data):
        # read the source data
        self.source_data = source_data

    def infer(self, target_file):
        # read the source data, add a column "target" to the csv file, the value is 0 or 1
        with open(self.source_data, "r") as f:
            reader = csv.reader(f)
            header = next(reader)
            data = list(reader)
        header.append("target")
        for row in data:
            row.append(random.choice([0, 1]))
        # save the file to target_file
        with open(target_file, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(header)
            writer.writerows(data)
