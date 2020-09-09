import logging
import os

import twitter
from dotenv import load_dotenv

from retweeter.helpers import probably_english

load_dotenv(override=True)
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("retweeter")
logger.setLevel(logging.INFO)

def retweet_account(api, user, last_id):
    statuses = api.GetUserTimeline(
        screen_name=user,
        include_rts=False,
        count=100,
        since_id=last_id,
    )

    logger.info(f"Found {len(statuses)} statuses for {user}")
    statuses.reverse()

    retweets = 0
    for status in statuses:
        if not probably_english(status.text):
            continue
        try:
            api.PostRetweet(status.id)
            retweets += 1
        except twitter.TwitterError as e:
            logger.error(e)

    logger.info(f"Retweeted {user} {retweets} times")

def main():
    api = twitter.Api(
        consumer_key=os.environ["TWITTER_API_KEY"],
        consumer_secret=os.environ["TWITTER_API_TOKEN"],
        access_token_key=os.environ["TWITTER_ACCESS_TOKEN"],
        access_token_secret=os.environ["TWITTER_ACCESS_TOKEN_SECRET"],
    )

    rts = api.GetUserRetweets()
    last_id_retweeted = None
    if rts:
        last_id_retweeted = rts[0].retweeted_status.id


    for user in ("cityofsanjose", "sccgov"):
        retweet_account(api, user, last_id_retweeted)

if __name__ == "__main__":
    main()
