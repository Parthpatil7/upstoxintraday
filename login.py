import requests
from selenium import webdriver

# Upstox API credentials
api_key = ''
api_secret = ''
redirect_uri = ''

# Construct Upstox login URL
login_url = f'https://api-v2.upstox.com/login/authorization/dialog?response_type=code&client_id={api_key}&redirect_uri={redirect_uri}'
print(f'Please visit the following URL to log in: {login_url}')

# Set up Selenium WebDriver (you may need to download the appropriate driver for your browser)
driver = webdriver.Chrome()  # Make sure to have chromedriver or geckodriver in your PATH

# Open the Upstox login URL
driver.get(login_url)

# Add a delay to allow the user to interact with the login page
input("Please log in and press Enter when done...")

# Once the user is logged in, retrieve the current URL
current_url = driver.current_url

# Extract the authorization code from the URL
auth_code = current_url.split('code=')[1].split('&')[0]

# Close the browser window
driver.quit()

# Exchange the authorization code for an access token
url = 'https://api-v2.upstox.com/login/authorization/token'

headers = {
    'accept': 'application/json',
    'Api-Version': '2.0',
    'Content-Type': 'application/x-www-form-urlencoded'
}

data = {
    'code': auth_code,
    'client_id': api_key,
    'client_secret': api_secret,
    'redirect_uri': redirect_uri,
    'grant_type': 'authorization_code'
}

response = requests.post(url, headers=headers, data=data)


# Check if the request was successful
if 'access_token' in response.json():
    access_token = response.json()['access_token']
    print(f'Successfully obtained access token: {access_token}')
else:
    print('Error in obtaining access token. Check your credentials and try again.')
