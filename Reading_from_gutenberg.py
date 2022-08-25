#Importing library to get text file from a website
import requests
text = requests.get('https://www.gutenberg.org/files/1661/1661-0.txt').text

#Writing the text into a local text file
with open("sherlock-holmes.txt", "w") as text_file:
    text_file.write(text)
