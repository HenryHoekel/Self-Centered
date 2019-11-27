from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from time import sleep
import json
import datetime

#System.setProperty("webdriver.chrome.driver", "C:\\Users\\Hank\\Documents\\Self-Centered\\chromedriver.exe");
#webdriver driver = new ChromeDriver();

def format_day(date):
    day   = '0' + str(date.day)   if len(str(date.day))   == 1 else str(date.day)
    month = '0' + str(date.month) if len(str(date.month)) == 1 else str(date.month)
    year = str(date.year)
    return '-'.join([year, month, day])
# end format_day

def form_url(user, since, until):
    p1 = 'https://twitter.com/search?f=tweets&vertical=default&q=from%3A'
    p2 =  user + '%20since%3A' + since + '%20until%3A' + until + 'include%3Aretweets&src=typd'
    return p1 + p2
# end form_url

def increment_day(date, i):
    return date + datetime.timedelta(days=i)
# end increment_day

def scrape_all(user, start_date, end_date):

    # Only edit these if you're having problems
    delay = 1  # time to wait on each page load before reading the page
    driver = webdriver.Firefox()  # options are Chrome() Firefox() Safari()

    # Parse user input (remove 0s) - format: year, month, day
    start = start_date.split('/')
    end   = end_date.split('/')
    start = datetime.datetime(int(start[2]), int(start[0].lstrip('0')), int(start[1].lstrip('0')))
    end   = datetime.datetime(int(end[2])  , int(end[0].lstrip('0'))  , int(end[1].lstrip('0')  ))

    # don't mess with this stuff
    user = user.lower()
    twitter_ids_filename = str(user) + '.json'
    days = (end - start).days + 1
    id_selector = '.time a.tweet-timestamp'
    tweet_selector = 'li.js-stream-item'
    user = user.lower()
    ids = []

    for day in range(days):
        d1 = format_day(increment_day(start, 0))
        d2 = format_day(increment_day(start, 1))
        url = form_url(user, d1, d2)
        print(url)
        print(d1)
        driver.get(url)
        sleep(delay)

        try:
            found_tweets = driver.find_elements_by_css_selector(tweet_selector)
            increment = 10

            while len(found_tweets) >= increment:
                print('scrolling down to load more tweets')
                driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
                sleep(delay)
                found_tweets = driver.find_elements_by_css_selector(tweet_selector)
                increment += 10

            print('{} tweets found, {} total'.format(len(found_tweets), len(ids)))

            for tweet in found_tweets:
                try:
                    id = tweet.find_element_by_css_selector(id_selector).get_attribute('href').split('/')[-1]
                    ids.append(id)
                except StaleElementReferenceException as e:
                    print('lost element reference', tweet)

        except NoSuchElementException:
            print('no tweets on this day')

        start = increment_day(start, 1)

    try:
        with open(twitter_ids_filename) as f:

            all_ids = ids + json.load(f)
            data_to_write = list(set(all_ids))
            print('total tweet count: ', len(data_to_write))

    except FileNotFoundError:

        with open(twitter_ids_filename, 'w') as f:
            all_ids = ids
            data_to_write = list(set(all_ids))
            print('tweets found on this scrape: ', len(ids))
            print('total tweet count: ', len(data_to_write))

    with open(twitter_ids_filename, 'w') as outfile:
        json.dump(data_to_write, outfile)

    driver.close()

    print('Done Scraping' + str(user))

# end scrape
