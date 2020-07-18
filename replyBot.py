
import praw
import requests
import time
from bs4 import BeautifulSoup

previous_id = []
WAIT = 60

#FORMAT FOR BOT
#!rewardblockbot #BLOCK_NUMBER 
# example: !rewardblockbot 354543
def main():
    reddit = praw.Reddit('bot1') #@DEV bot1 is listed in praw.ini it holds your personal information
    #Choose your desired subreddit
    subreddit = reddit.subreddit('bitcoincashSV')
    global previous_id
    subreddit_comments = subreddit.comments()
    for c in subreddit_comments:
        body = c.body
        body = body.lower()


        if c.id in previous_id:
            return
        if "!rewardblockbot" in body:
            bodyArray = body.split()
            try:
                
                blockNum = int(bodyArray[1])
            except:
                return "Not a valid block"
            #There is roughly only 650k blocks on the BSV Blockchain 
            #@Dev Change based of blockchain overall blocks
            if blockNum > 650000:
                 return
            
            blockInfoArray = blockInfo(blockNum)
            previous_id.append(c.id)
            c.reply("Link: {} \n  Block Number: {} \n  Reward: {} ".format(blockInfoArray[0], blockInfoArray[1], blockInfoArray[2]))

#Currently only collects link, reward and block number but can be easily specialized to your need      
def blockInfo(i):
    #URL of the website you want to scrape
    url = 'https://blockchair.com/bitcoin-sv/block/' + str(i)
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')

    #@DEV This is dependent on the website, inspect the url wanted to be scraped to determine how to get to data
    #@DEV This needs to be changed to the desired block explorer
    listText = soup.find_all('li', class_='block__item')
    tier1 = listText[12].find_all('span')
    tier2 = tier1[1].find_all('span')[0]
    reward = tier2.text
    RewardArray = [url, i, reward]
    return RewardArray

if __name__ == "__main__":
    #Continuously checks every minute
    while True:
        try:
            main()
        except Exception as e:
            traceback.print_exc()
        print('Running again in %d seconds \n' % WAIT)
        time.sleep(WAIT)