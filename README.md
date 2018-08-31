# Self-Centered
Twitter Scraper that gathers a user's tweets based on "selfish," words such as "me, myself, I, etc..."


# From "Twitter Scraper"

written by: https://github.com/bpb27

Twitter makes it hard to get all of a user's tweets (assuming they have more than 3200). This is a way to get around that using Python, Selenium, and Tweepy.

Essentially, we will use Selenium to open up a browser and automatically visit Twitter's search page, searching for a single user's tweets on a single day. If we want all tweets from 2015, we will check all 365 days / pages. This would be a nightmare to do manually, so the `scrape.py` script does it all for you - all you have to do is input a date range and a twitter user handle, and wait for it to finish.

The `scrape.py` script collects tweet ids. If you know a tweet's id number, you can get all the information available about that tweet using Tweepy - text, timestamp, number of retweets / replies / favorites, geolocation, etc. Tweepy uses Twitter's API, so you will need to get API keys. Once you have them, you can run the `get_metadata.py` script.

## Requirements

- basic knowledge on how to use a terminal
- Safari 10+ with 'Allow Remote Automation' option enabled in Safari's Develop menu to control Safari via WebDriver.
- python3
  - to check, in your terminal, enter `python3`
  - if you don't have it, check YouTube for installation instructions
- pip or pip3
  - to check, in your terminal, enter `pip` or `pip3`
  - if you don't have it, again, check YouTube for installation instructions
- selenium (3.0.1)
  - `pip3 install selenium`
- tweepy (3.5.0)
  - `pip3 install tweepy`

## Running the scraper

- open up `scrape.py` and edit the user, start, and end variables (and save the file)
- run `python3 scrape.py`
- you'll see a browser pop up and output in the terminal
- do some fun other task until it finishes
- once it's done, it outputs all the tweet ids it found into `all_ids.json`
- every time you run the scraper with different dates, it will add the new ids to the same file
  - it automatically removes duplicates so don't worry about small date overlaps

## Troubleshooting the scraper

- do you get a `no such file` error? you need to cd to the directory of `scrape.py`
- do you get a driver error when you try and run the script?
  - open `scrape.py` and change the driver to use Chrome() or Firefox()
    - if neither work, google the error (you probably need to install a new driver)
- does it seem like it's not collecting tweets for days that have tweets?
  - open `scrape.py` and change the delay variable to 2 or 3

## Getting the metadata

- first you'll need to get twitter API keys
  - sign up for a developer account here https://dev.twitter.com/
  - get your keys here: https://apps.twitter.com/
- put your keys into the `sample_api_keys.json` file
- change the name of `sample_api_keys.json` to `api_keys.json`
- open up `get_metadata.py` and edit the user variable (and save the file)
- run `python3 get_metadata.py`
- this will get metadata for every tweet id in `all_ids.json`
- it will create 4 files
  - `username.json` (master file with all metadata)
  - `username.zip` (a zipped file of the master file with all metadata)
  - `username_short.json` (smaller master file with relevant metadata fields)
  - `username.csv` (csv version of the smaller master file)

# END OF TWITTER SCRAPER

## Now Time to Parse the Data

- In your terminal of choice, type: `python3 jsonParse.py`
- Once parsing is complete, the terminal will output all "selfish," tweets along with a total selfish tweet count divided by total tweets
- Enjoy!!

# FINAL STEP BY STEP TUTORIAL

## If Python, Selenium, and Tweepy are already installed skip to step _

1. Check python is installed by typing `python3`.
* Install python if needed.
2. Enter pip or pip3 by typing `pip` or `pip3` respectively.
* Install pip or pip3 if needed.
3. Type `pip3 install selenium` in your desired terminal.
4. Type `pip3 install tweepy` in your desired terminal.
5. In `scrape.py` edit lines 10-12 with your desired information.
6. Run `python3 scrape.py` in your desired terminal.
7. In `get_metadata.py` edit line 12 for your desired Twitter handle.
8. Run `python3 get_metadata.py` in your desired terminal.
9. Edit line 7 with the desired filepath to .json file outputted from step 8.
10. Read the output and enjoy your analysis of how selfish you are!!

## Disclaimers
- This scraper is still not fully developed. The parser is very simple and can sometimes confuse non selfish tweets for selfish ones.
- This application was purely developed for personal use and entertainment, not for commercial use.

# Thank you and Enjoy!!