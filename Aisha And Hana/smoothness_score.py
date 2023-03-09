#import csv

with open("/Users/aisha/Documents/IP/coursework/IP_Lab/James And Indira/data.txt", "r") as file:
  #csvreader = csv.reader(file, delimiter=',')
    for line in file:
        
        #values = line.strip("[]")
        #values.split(",")
        #values = line[:-1]
        #values = values[:1]
        line.split(",")
        x,y,z = (float(x) for x in line[1:-2].split(","))
        x_val = int(x)
        y_val = int(y)
        z_val = int(z)
        def smoothness_score(x_val, y_val, z_val):

            x_jerk_list = []
            y_jerk_list = []
            z_jerk_list = []

            
            for i in range(1, len(x_val)):
                x_jerk = (x_val[i] - x_val[i-1]) / 0.1 #replace 0.1 with their value
                y_jerk = (y_val[i] - y_val[i-1]) / 0.1
                z_jerk = (z_val[i] - z_val[i-1]) / 0.1
                x_jerk_list.append(x_jerk)
                y_jerk_list.append(y_jerk)
                z_jerk_list.append(z_jerk)

            
            jerk_magnitudes = []

            
            for x_jerk in x_jerk_list:
                x_jerk_magnitude = abs(x_jerk)
                x_jerk_magnitudes = []
                x_jerk_magnitudes.append(x_jerk_magnitude)

            for y_jerk in y_jerk_list:
                y_jerk_magnitude = abs(y_jerk)
                y_jerk_magnitudes = []
                y_jerk_magnitudes.append(y_jerk_magnitude)

            for z_jerk in z_jerk_list:
                z_jerk_magnitude = abs(z_jerk)
                z_jerk_magnitudes = []
                z_jerk_magnitudes.append(z_jerk_magnitude)

            
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

file.close()

