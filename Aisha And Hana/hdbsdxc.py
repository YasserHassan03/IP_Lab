from pprint import pprint
import boto3



with open("/home/ubuntu/Python Scripts and data for Lab 6/xyz.txt", "r") as file:
    contents = file.readlines()[1:]  # skip the first line (assuming it's a header)
    x_vals = []
    y_vals = []
    z_vals = []
    for line in contents:
        values = line.strip().split(",")
        if len(values) != 3:  # skip lines that don't contain exactly 3 values
            continue
        try:
            x_vals.append(float(values[0]))
            y_vals.append(float(values[1]))
            z_vals.append(float(values[2]))
        except ValueError:  # skip lines that contain non-numeric data
            continue
    result = smoothness_score(x_vals, y_vals, z_vals)