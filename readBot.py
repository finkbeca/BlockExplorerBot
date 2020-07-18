import praw
import pandas as pd
import time

previous_ids = []
#Time intervals in which it checks new posts
WAIT = 20

def main():
    #@dev Referencing Bot1 provides user information, note that bot1 is defined in praw.ini
    reddit = praw.Reddit('bot1')

    posts = []
    
    #Change to desired subreddit
    subreddit = reddit.subreddit('bitcoincashSV')
    for post in subreddit.new(limit=100):
        if post.id in previous_ids:
            return
        posts.append([post.title, post.score, post.id, post.subreddit, post.url, post.num_comments, post.selftext, post.created])
        previous_ids.append(post.id)

    #post new information to a csv
    with open('new_subreddit_posts.csv', 'a') as f:
        posts = pd.DataFrame(posts, columns=['title', 'score', 'id', 'subreddit', 'url', 'num_comments', 'body', 'created'])
        posts.to_csv(f)



if __name__ == "__main__":
    #Runs Once every 12 hours checking for new content to be added to the link
    #init()
    print("Works")
    while True:
        try:
            main()
        except Exception as e:
            traceback.print_exc()
        print('Running again in %d seconds \n' % WAIT)
        time.sleep(WAIT)