import socket
import csv
#import csv
import threading 
import decimal
import numpy as np
def smoothness_score(x_vals, y_vals, z_vals, time_interval):
<<<<<<< HEAD
    if all([x_vals, y_vals, z_vals]) != []:
=======
    #x_vals = x_vals
    if x_vals or y_vals or z_vals == []:
        return 0
    else:
>>>>>>> 2550b25 (aaa)
        x_jerk_list = [1,1,1]
        y_jerk_list = [1,1,1]
        z_jerk_list = [1,1,1]
        x_jerk_magnitudes = [1,1,1]
        y_jerk_magnitudes = [1,1,1]
        z_jerk_magnitudes = [1,1,1]
        x_smoothness_scores = []
        y_smoothness_scores = []
        z_smoothness_scores = []
<<<<<<< HEAD

        for i in range(1, len(x_vals)-1):
=======
        
        for i in range(1, len(z_vals)):
>>>>>>> 2550b25 (aaa)
            x_jerk = decimal.Decimal((x_vals[i] - x_vals[i-1]) / time_interval)
            y_jerk = decimal.Decimal((y_vals[i] - y_vals[i-1]) / time_interval)
            print(len(z_vals))
            z_jerk = decimal.Decimal((z_vals[i] - z_vals[i-1]) / time_interval)
            
            x_jerk_list.append(x_jerk)
            y_jerk_list.append(y_jerk)
            z_jerk_list.append(z_jerk)
            
            x_jerk_magnitude = abs(decimal.Decimal(x_jerk))
            y_jerk_magnitude = abs(decimal.Decimal(y_jerk))
            z_jerk_magnitude = abs(decimal.Decimal(z_jerk))
            
            x_jerk_magnitudes.append(x_jerk_magnitude)
            y_jerk_magnitudes.append(y_jerk_magnitude)
            z_jerk_magnitudes.append(z_jerk_magnitude)
    
            window_size = 5
    
            for i in range(len(x_jerk_magnitudes)):
                start = max(0, i-window_size)
                end = min(len(x_jerk_magnitudes), i+window_size)
                x_jerk_window = x_jerk_magnitudes[start:end]
                y_jerk_window = y_jerk_magnitudes[start:end]
                z_jerk_window = z_jerk_magnitudes[start:end]
                
                try:
                    x_smoothness_score = 1 / decimal.Decimal(np.mean(x_jerk_window))
                    y_smoothness_score = 1 / decimal.Decimal(np.mean(y_jerk_window))
                    z_smoothness_score = 1 / decimal.Decimal(np.mean(z_jerk_window))
                except:
                    x_smoothness_score = 0
                    y_smoothness_score = 0
                    z_smoothness_score = 0
    
                x_smoothness_scores.append(x_smoothness_score)
                y_smoothness_scores.append(y_smoothness_score)
                z_smoothness_scores.append(z_smoothness_score)
            
            
        average_x_smoothness = decimal.Decimal(np.mean(x_smoothness_scores))
        average_y_smoothness = decimal.Decimal(np.mean(y_smoothness_scores))
        average_z_smoothness = decimal.Decimal(np.mean(z_smoothness_scores))
        
        x_smoothness_score = 1 / average_x_smoothness
        y_smoothness_score = 1 / average_y_smoothness
        z_smoothness_score = 1 / average_z_smoothness
        
        max_smoothness_score = 1 / decimal.Decimal(0.1)  # The maximum possible jerk magnitude is 0.1 m/s^2, assuming a perfectly smooth ride
        avrg_smoothness = (x_smoothness_score + y_smoothness_score + z_smoothness_score) / 3
        normalised_smoothness_score = avrg_smoothness / max_smoothness_score
        
        return decimal.Decimal(normalised_smoothness_score)

def process_file(filename):
    with open(filename, "r", encoding="utf-8") as file:
        contents = file.readlines()[1:]  # skip the first line (assuming it's a header)
        x_vals = [1]
        y_vals = [1]
        z_vals = [1]
        for line in contents:
            values = line.strip().split(",")
            if len(values) != 3:  # skip lines that don't contain exactly 3 values
                continue
            try:
                x_vals.append(int(values[0]))
                y_vals.append(int(values[1]))
                z_vals.append(int(values[2]))
            except ValueError:  # skip lines that contain non-numeric data
                continue
    file.close()
    return x_vals, y_vals, z_vals


    #file.close()



print("We're in server now..")
#deadfile= open('data.txt','w')
#deadfile.close()
#clear file for new data
#select port for server
resultscale = '000000' #test score val initial
server_port=12003
#create welcoming socket
welcome_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#bind server to local host
welcome_socket.bind(('0.0.0.0',server_port))
welcome_socket.listen(1)
#ready message
print("server running on port: ",server_port)
cmsg=''
#now server side loop

#print(score())

 #send score to client 
resultscale=1
while True:   
    connection_socket,caddr=welcome_socket.accept()
    x_vals, y_vals, z_vals = process_file("data.txt")
    if len(x_vals) and len(y_vals) and len(z_vals) != 0:
        resultround = decimal.Decimal((smoothness_score(x_vals, y_vals, z_vals, 1.0)))
        resultround = round(resultround, 6)
        resultscale= (resultround * 1000000)
    #if (len(str(resultscale))==5):
        resultscale = '0' + str(resultscale)
        print(resultscale)
    connection_socket.send((resultscale).encode())
    cmsg=connection_socket.recv(1024)     
    cmsg=cmsg.decode()
    print(cmsg.split('\r'))
    with open ('data.txt','w+',newline='\r') as file:
        file.write(cmsg)
        file.close()
    

    
        
