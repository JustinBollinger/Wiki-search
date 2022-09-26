# importing required modules
import json
import wikipedia as wp
from flask import Flask

# initializing the app
app = Flask(__name__)


@app.route('/')
def prompt():
    """
    Routing to basic landing page 
    prompting user to use wiki-search.
    """
    return 'Greetings! Type your search term into the URL in the following format >>> http://127.0.0.1:5000/[YOUR SEARCH TERM].wiki-search.com.'


@app.route('/<search>.wiki-search.com')
def wiki_search(search):
    """
    Routes to a page which makes a call 
    to Wikipedia API based on user search term 
    and displays one or more URLs in a list 
    within a dictionary, then dumps it into JSON format.
    """
    # instantiating dictionary with key:value pair
    url_dict = {'links': []}
    try:
        # storing URL from exact match of search term without Wikipedia assistance into result variable, then appending result to dict
        result = wp.page(search, auto_suggest=False).url
        url_dict['links'].append(result)
    # handling thrown exceptions when URLs > 1
    except wp.DisambiguationError as e:
        for option in e.options:
            try:
                # storing and appending all disambiguation result URLs to dict after replacing double-quotes with nothing when applicable
                url = wp.page(option.replace('"', ''), auto_suggest=False).url
                url_dict['links'].append(url)
            except wp.DisambiguationError:
                # disregarding possible recurring Disamb exception
                pass
            except wp.PageError:
                return 'No page matches your search term. Please try searching for a different term.'
    return json.dumps(url_dict)

# guarding script from unintentional invocation
if __name__ == '__main__':
    app.run()