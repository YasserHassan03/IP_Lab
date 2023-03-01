def smoothness_score(acceleration_data):

    jerk_list = []

    
    for i in range(1, len(acceleration_data)):
        jerk = (acceleration_data[i] - acceleration_data[i-1]) / 0.1 #replace 0.1 with their value
        jerk_list.append(jerk)

    
    jerk_magnitudes = []

    
    for jerk in jerk_list:
        jerk_magnitude = abs(jerk)
        jerk_magnitudes.append(jerk_magnitude)

    
    average_jerk_magnitude = sum(jerk_magnitudes) / len(jerk_magnitudes)

    
    smoothness_score = 1 / average_jerk_magnitude
    max_smoothness_score = 1 / 0.1  # The maximum possible jerk magnitude is 0.1 m/s^2, assuming a perfectly smooth ride, #replace 0.1 with their value
    normalised_smoothness_score = smoothness_score / max_smoothness_score

    return normalised_smoothness_score
