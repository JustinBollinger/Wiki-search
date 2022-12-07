# **Wiki-Searcher**

This web-application allows a user to search Wikipedia for a term of their choice in an alternative way and returns a list of that term's URL(s) in JSON format.

## **Installation**

**Requirements**

Python
* Download the most recent stable version of **[Python](https://www.python.org/downloads/)**

Flask
* Once Python has been successfully installed, follow these instructions to install the most stable version of Flask:
    1. Create a project folder and a new virtual environment in shell prompt:

        macOS/Linux:
        ```
        $ mkdir myproject
        $ cd myproject
        $ python3 -m venv venv
        ```
        Windows:
        ```
        > mkdir myproject
        > cd myproject
        > py -3 -m venv venv
        ```

    2. Activate the environment:

        macOS/Linux:
        ```
        $ . venv/bin/activate
        ```
        Windows:
        ```
        > venv\Scripts\activate
        ```
        
    3. Install Flask

        All Operating Systems:
        ```
        $ pip install Flask
        ```
        If the above command is unsuccessful, try:
        ```
        $ pip3 install Flask
        ```

* Please see this **[Installation Guide](https://flask.palletsprojects.com/en/2.2.x/installation/)** for more information.

## **Usage**

1. In your main app, ensure the following modules have been imported at the top of the script like so:
    ```
    import json
    import wikipedia as wp
    from flask import Flask
    ```

2. To start running your local server, type the following into your IDE's terminal:
    ```
    $ flask run
    ```
    - Successfully running the server will result in the following message:
    ```
    WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
    * Running on http://127.0.0.1:5000
    Press CTRL+C to quit
    ```
    - **Important:** If you do not see the above message, make sure both Python and Flask have been successfully installed and that you are using the most recent stable versions of both. See the Flask Installation Guide above for further assistance.

3. Open your server's local IP address by holding CTRL + clicking on it in the terminal:
    ```
    Running on http://127.0.0.1:5000  <<<<<
    ```

4. At the landing page, copy/paste the provided URL, replace "[YOUR SEARCH TERM]" with any search term and hit enter. There are 3 possible outcomes:
    * Exact match (1 URL returned):
        ```
        # http://127.0.0.1:5000/tree.wiki-search.com
        
        {"links": ["https://en.wikipedia.org/wiki/Tree"]}
        ```
    
    * DisambiguationError (Multiple URLs returned):
        ```
        # http://127.0.0.1:5000/bake.wiki-search.com

        {"links": ["https://en.wikipedia.org/wiki/Bake,_Chongqing", "https://en.wikipedia.org/wiki/Bake,_Cornwall", "https://en.wikipedia.org/wiki/Bake_Fishing_Lakes", ...]}
        ```

    * PageError (Search term does not match any page; Zero URLs returned):
        ```
        # http://127.0.0.1:5000/1Q.wiki-search.com

        No page matches your search term. Please try searching for a different term.
        ```

## **Credits**
Script by: **[Justin Bollinger](https://github.com/JustinBollinger)**


