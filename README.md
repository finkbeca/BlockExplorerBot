# BlockExplorerBot
Blockchain Explorer Bot &amp; Reddit Web Scraping Bot

## Purpose
Provide further documentation and examples for building reddit bots. A lot of the simplified examples focus out many of the nesscessties and purposes of reddit bots for simplified example. Provided below are two sample reddit bots.

## Reddit Web Scraping Bot
This reddit bot scrapes a subreddit for post data and pushes it to a csv file. Alternative to cron, this bot is set to continuiosly loop checking in set time intervals.
## Blockchain Explorer Bot
Blockchain Explorer Bot purpose was buildt from a reward block webscraper meant to anaylze block rewards. The reddit bot responds to comments made on the BitcoincashSV subreddit with a link to the desired block, the block number and the block reward size. To call the bot simply reply to a post with the format __!rewardblockbot BLOCK_NUMBER__. Example: !rewardblockbot 456753. The bot was buildt using https://blockchair.com/bitcoin-sv BSV Block Explorer but could easily be adapted to alternative blockchains and block explorers.

## Praw.ini
Both files use the same local Praw.ini file to store personal login information. To use/edit either bots you only need to fill in your personal login information to run.
