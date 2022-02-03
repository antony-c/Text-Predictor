from pprint import pprint
from re import sub
from time import sleep
import json, requests, wikipediaapi

class Trainer:

    @staticmethod
    def run(words=dict()): # Run word trainer

        # Next 3 lines simply take the text file of words
        # And seperate them into elements of  a list
        sample_words = open("raw_text.txt", encoding="utf8").read()
        base_string = sub(r"[^a-zA-Z0-9\s]", "", rf"{sample_words.lower()}")
        base_words = base_string.split()

        # Parses the list of words and returns dictionary object.
        for i, word in enumerate(base_words):
            if i < len(base_words) - 1:
                next_word = base_words[i + 1]
                if word not in words:
                    words[word] = {next_word: 1}
                elif next_word in words[word]:
                    words[word][next_word] += 1
                else:
                    words[word][next_word] = 1
        return words

class Get_Words:

    @staticmethod
    def run(iterations, delay): # Run word sample generator

        # Goes through {iterations} random wikipedia pages
        # Adds all content of pages to a text file for english writing samples
        base_url = "https://en.wikipedia.org/wiki/"

        wiki_settings = wikipediaapi.Wikipedia(
                language='en',
                extract_format=wikipediaapi.ExtractFormat.WIKI
        )

        for iteration in range(iterations):
            sleep(delay)

            page = requests.get("https://en.wikipedia.org/wiki/Special:Random")
            random_article = page.url.replace(base_url, "")
            wiki_page = wiki_settings.page(random_article)

            with open("raw_text.txt", "a", encoding="utf-8") as outfile:
                outfile.write(wiki_page.text)

# Get 1000 wikipedia articles, 1 every 4 seconds
# Get_Words.run(1000, 4)

data = json.load(open("data.json", "r+"))
words = Trainer.run(data)

# Dump word data into json file
with open("data.json", 'r+') as outfile:
    json.dump(words, outfile, indent=4)
