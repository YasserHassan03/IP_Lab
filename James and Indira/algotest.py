import csv
import threading
import time

import decimal 
    
def smoothness_score(x_vals, y_vals, z_vals):
    
    x_jerk_list = []
    y_jerk_list = []
    z_jerk_list = []

    for i in range(1, len(x_vals)):
        x_jerk = [decimal.Decimal((((x_vals[i] - x_vals[i-1]) / (0.1))))]#replace 0.1 with their value
        y_jerk = [decimal.Decimal((((y_vals[i] - y_vals[i-1]) / 0.1)))]
        z_jerk = [decimal.Decimal((((z_vals[i] - z_vals[i-1]) / 0.1)))]
        x_jerk_list.append(x_jerk)
        y_jerk_list.append(y_jerk)
        z_jerk_list.append(z_jerk)

    x_jerk_magnitudes = [decimal.Decimal((([abs(x_jerk) for x_jerk in x_jerk_list])))]
    y_jerk_magnitudes = [decimal.Decimal((([abs(y_jerk) for y_jerk in y_jerk_list])))]
    z_jerk_magnitudes = [decimal.Decimal(([abs(z_jerk) for z_jerk in z_jerk_list]))]

    average_x_jerk_magnitude = sum(x_jerk_magnitudes) / len(x_jerk_magnitudes)
    average_y_jerk_magnitude = sum(y_jerk_magnitudes) / len(y_jerk_magnitudes)
    average_z_jerk_magnitude = sum(z_jerk_magnitudes) / len(z_jerk_magnitudes)


    x_smoothness_score = 1 / average_x_jerk_magnitude
    y_smoothness_score = 1 / average_y_jerk_magnitude
    z_smoothness_score = 1 / average_z_jerk_magnitude
    max_smoothness_score = 1 / 0.1  # The maximum possible jerk magnitude is 0.1 m/s^2, assuming a perfectly smooth ride, #replace 0.1 with their value
    avrg_smoothness = (x_smoothness_score + y_smoothness_score + z_smoothness_score) / 3
    normalised_smoothness_score = avrg_smoothness / max_smoothness_score

    return decimal.Decimal(((normalised_smoothness_score)))


# Open the file for reading
result = 0
with open("data.txt", "r") as file:
    threading.Timer(5.0, smoothness_score).start()

    contents = file.readlines()[1:]  # skip the first line (assuming it's a header)
    x_vals = [1]
    y_vals = [1]
    z_vals = [1]
    for line in contents:
        values = line.strip().split(",")
        if len(values) != 3:  # skip lines that don't contain exactly 3 values
            continue
        try:
           decimal.Decimal( x_vals.append(((values[0]))))
           decimal.Decimal(y_vals.append(((values[1]))))
           decimal.Decimal(z_vals.append(((values[2]))))
        except TypeError:  # skip lines that contain non-numeric data
            continue
    try:
        result = smoothness_score(decimal.Decimal(x_vals), decimal.Decimal(y_vals), decimal.Decimal(z_vals))
    except ValueError:
        print('no data')
    print(result)