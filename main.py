# # importing os module for environment variables
# import os
# # importing necessary functions from dotenv library
# from dotenv import load_dotenv, dotenv_values
# # loading variables from .env file
# load_dotenv()
#
# # accessing and printing value
# print(os.getenv("MY_KEY"))


from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get the credentials
EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")

print(EMAIL, PASSWORD)