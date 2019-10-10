import sys
import requests
import json
import urllib.parse
import argparse

def print_page(page_num, input_cast):
    endpoint = "https://swapi.co/api/people/?"
    type = 'json'

    #specifies api parameters
    url = endpoint + urllib.parse.urlencode({"format": type, "page": page_num})

    #gets info
    json_data = requests.get(url).json()
    if 'results' in json_data:
      for index in json_data['results']:
            if input_cast in index['name']:
              print_films_on(index)
            else:
                print(f'Character: {input_cast} was not found.')

def get_film_name(character):
    type = 'json'

    #specifies api parameters
    url = character 

    #gets info
    json_data = requests.get(url).json()
    return json_data["title"]

def print_films_on(character):
    for cast in character['films']:
       print(f"{character['name']} was in film: {get_film_name(cast)}")

def process(args):
    page_list = [1,2,3,4,5,6,7,8,9]
    # list to store names
    input_cast = args.character

    for page in page_list:
        print_page(page, input_cast)

def main():
    parser = argparse.ArgumentParser(description="See which Star Wars character was in each film")
    parser.add_argument("character", help="name a character in the Star Wars film")
    args = parser.parse_args()

    process(args)


if __name__ == '__main__':
    main()


