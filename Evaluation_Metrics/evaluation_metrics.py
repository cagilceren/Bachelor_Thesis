import numpy as np
import csv
import os

path = './results'
path_to_created_file = './evaluation_metrics'
path_to_created_file_mean = './evaluation_metrics/MAPE_result'
                  
def MAPE(path, path_to_created_file):
    for root, dirs, files in os.walk(path):
        for file in files:
            if file != '.DS_Store':
                with open(f'{path_to_created_file}/{file}', "w", newline="") as csv_file_to_write:
                    pass
                with open(f'{path}/{file}') as csv_file_to_read:
                    csv_reader_file_to_read = csv.DictReader(csv_file_to_read, delimiter=',')
                    values = []
                    for row in csv_reader_file_to_read: 
                        print(row)
                        with open("./data/actual_counts.csv") as actual_counts_file:
                           actual_counts_file = csv.DictReader(actual_counts_file, delimiter=",")
                           for row_actual_counts in actual_counts_file:
                             if row['image_name'].split('.')[0] == row_actual_counts['image'].split('.')[0]:
                                actual_count = row_actual_counts['label']
                                #actual_count = row['image_name'].split('_')[1]
                                predicted_count = row[' count;'].split(';')[0]
                                if predicted_count == 'many' or actual_count == 0:
                                    continue
                                values.append(np.abs((int (actual_count) - int (predicted_count)) / int (actual_count)))
                                print("actual:", actual_count, "predicted:", predicted_count)
                    mape = np.mean(values)
                    with open(f'{path_to_created_file}/{file}', "a", newline="") as csv_file_to_write:
                        csv_file_to_write.write(f'{str(mape)}, {len(values)}') 

MAPE(path, path_to_created_file)