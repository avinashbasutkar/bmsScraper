import requests
from bs4 import BeautifulSoup
import telepot
import creds

# Go to site
url = 'https://in.bookmyshow.com/explore/movies-hyderabad?languages=english'
response = requests.get(url).text

soup = BeautifulSoup(response, 'html.parser')

# Get the HTML elements of movie details
movies = soup.find_all("div", {"class":"style__StyledText-sc-7o7nez-0 gBgfCW"}) 

movies_list = []
for movie in movies:
    movies_list.append(movie.text)

# Store & update movie list somewhere like Google Sheet

# If there is a new name, send it in Telegram via Pam
bot = telepot.Bot(creds.TELEGRAM_BOT_PAM_ID) # calling Pam on Telegram
bot.sendMessage(creds.TELEGRAM_MY_PERSONAL_ID, "my ID is working") # my personal ID on telegram.

# for movie in movies_list:
#     bot.sendMessage(creds.TELEGRAM_MY_PERSONAL_ID, movie) # my personal ID on telegram.

print("success")

# Include Image of the Movie

# Include YouTube URL for the trailer of the movie.