import psutil
import time


# print(psutil.cpu_percent(2))  #will get me the CPU ultilization in Every 2 secs
        

while True:                                 #wull Run infite times till the block of code wrriten under While is satisfied as TRUE.
    try:
        c= psutil.cpu_percent()          
             
        if c > 80.0:
            print("Alert! CPU usage exceeds threshold:", c ,"%")

        else: 
            print("CPU Percentage is: ", c , "%")
        time.sleep(5)                 #will execute the code after every 5 secs

    except Exception as e:
        print("error encontred while running the script: ", e)
        
    
        
