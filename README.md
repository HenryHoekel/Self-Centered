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
- python3 (Firefox and Chrome work as well) :)
  - To check, in your terminal, enter `python3`
  - If you don't have it, check YouTube for installation instructions
- pip or pip3
  - To check, in your terminal, enter `pip` or `pip3`
  - If you don't have it, again, check YouTube for installation instructions
- selenium (3.0.1)
  - `pip3 install selenium`
- tweepy (3.5.0)
  - `pip3 install tweepy`

## Running the scraper

- Open up `automate_self_centered.py` and edit the user, start, and end variables (and save the file).
  - You can put multiple accounts in run_everything :)
- Run `python3 automate_self_centered.py`.
- You will see a browser pop up along with output in the terminal.
- Do some fun other task until it finishes.
- Once it's done, it outputs all the tweet ids it found into `all_ids.json`.
- Every time you run the scraper with different dates, it will add the new ids to the same file.
  - It automatically removes duplicates so don't worry about small date overlaps
  - It now cleans up these files once the function is over in `run_one_user()` in `automate_self_centered.py`.
    - You can comment this out if you'd like if you want the data :)

## Troubleshooting the scraper

- Do you get a `no such file` error? you need to cd to the directory of `automate_self_centered`.
- Do you get a driver error when you try and run the script?
  - Open `scrape.py` and change the driver to use Chrome() or Firefox()
    - If neither work, google the error (you probably need to install a new driver)
- Does it seem like it's not collecting tweets for days that have tweets?
  - Open `scrape.py` and change the delay variable to 2 or 3

## Getting the metadata

- First you'll need to get twitter API keys
  - Sign up for a developer account here https://dev.twitter.com/
  - Get your keys here: https://apps.twitter.com/
- Put your keys into the `sample_api_keys.json` file
- This will get metadata for every tweet id in `all_ids.json`
- It will create 4 files
  - `username.json` (master file with all metadata)
  - `username.zip` (a zipped file of the master file with all metadata)
  - `username_short.json` (smaller master file with relevant metadata fields)
  - `username.csv` (csv version of the smaller master file)
- Make sure you put your keys in prior to running `automate_self_centered()` - It will now get the metadata for you

# END OF TWITTER SCRAPER

## Now Time to Parse the Data

- Once parsing is complete, the terminal will output all "selfish," tweets along with a total selfish tweet count divided by total tweets
- Enjoy!!

# FINAL STEP BY STEP TUTORIAL

## If Python, Selenium, and Tweepy are already installed skip to step _

- If First time: run steps 1-4
- Else skip to steps 5-7
1. Check python is installed by typing `python3`.
* Install python if needed.
2. Enter pip or pip3 by typing `pip` or `pip3` respectively.
* Install pip or pip3 if needed.
3. Type `pip3 install selenium` in your desired terminal.
4. Type `pip3 install tweepy` in your desired terminal.
5. In `automate_self_centered.py` edit lines 31 (`run_everything()`) onwards with your desired information.
6. Run `python3 automate_self_centered.py` in your desired terminal.
7. Read the output and enjoy your analysis of how selfish you are!!

## Disclaimers
- This scraper is still not fully developed. The parser is very simple and can sometimes confuse non selfish tweets for selfish ones.
- This application was purely developed for personal use and entertainment, not for commercial use.

# Thank you and Enjoy!!
