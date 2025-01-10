import datetime #importing datetime module
import time #importing time module

end_time = datetime.datetime(2025, 1, 12) #setting the end time
site_block=[] #creating an empty list
website_name=input("Enter the website you want to block: ") #taking input from the user Ex. www.facebook.com or facebook.com
site_block.append(website_name) #appending the website name to the list
host_path="C:/Windows/System32/drivers/etc/hosts" #setting the path of the host file
redirect="127.0.0.1" #setting the redirect address

while True: #running an infinite loop
    if datetime.datetime.now()<end_time: #checking if the current time is less than the end time
        print("Start blocking") #printing the message
        with open(host_path,"r+") as host_file: #opening the host file
            content=host_file.read() #reading the content of the host file
            for website in site_block: #iterating through the list
                if website not in content:#checking if the website is not in the content
                    host_file.write(redirect  +" "+website+"\n") #writing the website name to the host file
                else:
                    pass

    else:
        with open(host_path,"r+") as host_file: #opening the host file
            content=host_file.readlines() #reading the content of the host file
            host_file.seek(0) #setting the cursor to the beginning of the file
            for lines in content: #iterating through the content
                if not any(website in lines for website in site_block): #checking if the website is not in the content
                    host_file.write(lines) #writing the content to the host file
            host_file.truncate() #truncating the file to the current position
        time.sleep(5) #pausing the execution for 5 seconds
    
