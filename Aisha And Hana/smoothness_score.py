import csv
import threading
import time

def read_data(file_path):
    x_vals = []
    y_vals = []
    z_vals = []
    with open(file_path, "r") as file:
        for line in file:
            x_val, y_val, z_val = [float(val) for val in line.split(",")]
            x_vals.append(x_val)
            y_vals.append(y_val)
            z_vals.append(z_val)
    return x_vals, y_vals, z_vals
    
def smoothness_score(x_vals, y_vals, z_vals):
    x_jerk_list = []
    y_jerk_list = []
    z_jerk_list = []

    for i in range(1, len(x_vals)):
        x_jerk = (x_vals[i] - x_vals[i-1]) / 0.1 #replace 0.1 with their value
        y_jerk = (y_vals[i] - y_vals[i-1]) / 0.1
        z_jerk = (z_vals[i] - z_vals[i-1]) / 0.1
        x_jerk_list.append(x_jerk)
        y_jerk_list.append(y_jerk)
        z_jerk_list.append(z_jerk)

    x_jerk_magnitudes = [abs(x_jerk) for x_jerk in x_jerk_list]
    y_jerk_magnitudes = [abs(y_jerk) for y_jerk in y_jerk_list]
    z_jerk_magnitudes = [abs(z_jerk) for z_jerk in z_jerk_list]

    average_x_jerk_magnitude = sum(x_jerk_magnitudes) / len(x_jerk_magnitudes)
    average_y_jerk_magnitude = sum(y_jerk_magnitudes) / len(y_jerk_magnitudes)
    average_z_jerk_magnitude = sum(z_jerk_magnitudes) / len(z_jerk_magnitudes)

    x_smoothness_score = 1 / average_x_jerk_magnitude
    y_smoothness_score = 1 / average_y_jerk_magnitude
    z_smoothness_score = 1 / average_z_jerk_magnitude
    max_smoothness_score = 1 / 0.1  # The maximum possible jerk magnitude is 0.1 m/s^2, assuming a perfectly smooth ride, #replace 0.1 with their value
    avrg_smoothness = (x_smoothness_score + y_smoothness_score + z_smoothness_score) / 3
    normalised_smoothness_score = avrg_smoothness / max_smoothness_score

    return normalised_smoothness_score


# Open the file for reading
file_path = "/Users/aisha/Documents/IP/coursework/IP_Lab/data.txt"
x_vals, y_vals, z_vals = read_data(file_path)

for i in range(len(x_vals)):
    # Calculate the smoothness score for the current line
    score = smoothness_score(x_vals, y_vals, z_vals)
    # Print the score to the console
    print(score)
    # Wait for a short time (e.g. 0.1 seconds) before reading the next line
    time.sleep(0.1)
