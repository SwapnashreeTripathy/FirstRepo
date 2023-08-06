import time
import requests
from tabulate  import tabulate
import socket


#Check Subdomains Available for the Input Domain
domain = input("Enter your domain: ")
subd=(open("list_subdomain.txt").read())                                    #reading Subdomain names from list_subdomain.txt
subd_seprt = subd.splitlines()                                              #splitlines() converts each string into a list, the spliting is done at each line breaks.   
while True:
    for i in subd_seprt:
        urls= f"http://{i}.{domain}"                                            # https://vlearnv.herovired.com/
        try:
            requests.get(urls)
            subdomain=urls.strip("http://")                                     # subdomain = "vlearn.herovired.com"
                      
            #Get IP of Subdomains
            def subdomain_status(subdomain):                                    
                port = (80,443)
                ip = socket.gethostbyname(subdomain)  

                try:
                    for p in port:
                        int_p = int(p)
                        with socket.create_connection((ip,int_p),timeout=1):        #Check if IP is UP or Down while conneecting with ports.
                            return (subdomain, ip,int_p,"UP")
                       
                except socket.timeout:
                    return (subdomain, ip,int_p,"Down")
        
            #Append all_values to an Empty List "all_values_list"
            all_values=subdomain_status(subdomain)
            all_values_list = []
            if all_values:
                all_values_list.append(all_values)

            #Print "all_values_list" Values into Table format
            print(tabulate(all_values_list, headers=["Subdomain", "IP Address", "Accessible Ports","Status"],tablefmt="grid"))
         
        except Exception as ex:
            pass
    time.sleep(60)              #While True: Run the code every Minute











