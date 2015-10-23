import csv

def read_temp_csv(filename):
    """
    :return list of tuples with month, avg_low, avg_high
    """
    avg_temps_list = []

    with open('data/'+ filename +'.csv') as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)
            avg_temps_list.append((row[2], int(row[1]), int(row[0])))

    return avg_temps_list
