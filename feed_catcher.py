import feedparser
from datetime import datetime, timedelta, timezone
from dateutil import parser, tz
import pytz

# List of RSS feed URLs
feeds = [
    'https://queue.acm.org/rss.xml',
    'https://www.sigarch.org/feed/',
    'https://technews.acm.org/technews.xml',
    'https://airbyte.com/blog/rss.xml',
    'https://www.allthingsdistributed.com/atom.xml',
    'https://aws.amazon.com/blogs/architecture/feed/',
    'https://aws.amazon.com/blogs/feed/',
    'https://arstechnica.com/feed/',
    'https://blog.booking.com/feed.xml',
    'https://canvatechblog.com/feed/',
    'https://www.chip.de/rss.xml',
    'https://www.computerworld.com/index.rss',
    'https://databricks.com/blog/category/engineering/feed',
    'https://community.databricks.com/feed',
    'https://www.dbta.com/ContentRSS.ashx',
    'https://www.dataengineeringweekly.com/feed',
    'https://data.world/blog/feed/',
    'https://www.datanami.com/feed/',
    'https://discord.com/blog/feed',
    'https://dropbox.tech/feed.xml',
    'https://tech.ebayinc.com/feed/',
    'https://engineering.fb.com/feed/',
    'https://quoraengineering.quora.com/rss',
    'https://www.etsy.com/codeascraft/feed.xml',
    'https://medium.com/feed/expedia-group-tech',
    'https://code.flickr.net/feed/',
    'https://rss.focus.de/digital/',
    'https://github.blog/category/engineering/feed/',
    'https://cloud.google.com/blog/rss/',
    'https://ai.googleblog.com/atom.xml',
    'https://blog.heroku.com/engineering/feed',
    'https://blog.hotstar.com/feed',
    'https://product.hubspot.com/blog/topic/engineering/rss.xml',
    'https://www.computer.org/feed/',
    'https://insidehpc.com/feed/',
    'https://instagram-engineering.com/feed',
    'https://www.kdnuggets.com/feed',
    'https://engineering.linkedin.com/blog.rss.html',
    'https://eng.lyft.com/feed',
    'https://lakefs.io/blog/rss/',
    'https://www.technologyreview.com/feed/',
    'https://www.montecarlodata.com/blog/feed/',
    'https://devblogs.microsoft.com/feed/',
    'https://netflixtechblog.com/feed',
    'https://www.nextplatform.com/feed/',
    'https://opendatascience.com/feed/',
    'https://medium.com/feed/pinterest-engineering',
    'https://www.pullrequest.com/blog/rss',
    'https://www.rishabhsoft.com/blog/feed',
    'https://www.sciencedaily.com/rss/computers_math.xml',
    'https://shopify.engineering/rss.xml',
    'https://engineering.atspotify.com/feed/',
    'https://staffeng.com/feed/',
    'https://stripe.com/blog/engineering/feed',
    'https://bytes.swiggy.com/feed',
    'https://techcrunch.com/tag/artificial-intelligence/feed/',
    'https://medium.com/feed/airbnb-engineering',
    'https://eng.uber.com/feed/',
    'https://www.top500.org/rss/news/',
    'https://towardsdatascience.com/feed',
    'https://blog.twitter.com/engineering/en_us.rss',
    'https://www.wired.com/feed/',
    'https://blog.zomato.com/category/technologyD/feed',
    'https://medium.com/feed/tag/data-analytics',
    'https://medium.com/feed/tag/data-engineering'    
]

# Mapping of timezone abbreviations to their corresponding UTC offsets
tzinfos = {
    "UTC": tz.tzutc(),
    "GMT": tz.tzutc(),
    "EDT": tz.gettz("America/New_York"),
    "EST": tz.gettz("America/New_York"),
    "CDT": tz.gettz("America/Chicago"),
    "CST": tz.gettz("America/Chicago"),
    "MDT": tz.gettz("America/Denver"),
    "MST": tz.gettz("America/Denver"),
    "PDT": tz.gettz("America/Los_Angeles"),
    "PST": tz.gettz("America/Los_Angeles")
}

def fetch_latest_posts(feed_url):
    feed = feedparser.parse(feed_url)
    latest_posts = []
    yesterday = datetime.now(timezone.utc) - timedelta(days=1)
    for entry in feed.entries:
        published_date = entry.get('published') or entry.get('updated')
        if published_date:
            try:
                post_date = parser.parse(published_date, tzinfos=tzinfos)
                # Ensure post_date is timezone-aware
                if post_date.tzinfo is None:
                    post_date = post_date.replace(tzinfo=timezone.utc)
                else:
                    post_date = post_date.astimezone(timezone.utc)
                if post_date >= yesterday:
                    latest_posts.append({
                        'title': entry.title,
                        'link': entry.link,
                        'date': post_date
                    })
            except (ValueError, parser.ParserError):
                print(f"Error parsing date: {published_date}")
    return latest_posts

def display_latest_posts():
    all_latest_posts = []
    for feed in feeds:
        all_latest_posts.extend(fetch_latest_posts(feed))
    
    all_latest_posts.sort(key=lambda x: x['date'], reverse=True)
    
    today_str = datetime.now(timezone.utc).strftime('%Y-%m-%d')
    
    with open("README.md", "w") as file:
        if not all_latest_posts:
            file.write(f"No new posts from yesterday until now ({today_str}).\n")
        else:
            file.write(f"## Latest Posts from yesterday until now ({today_str}):\n\n")
            for post in all_latest_posts:
                file.write(f"{post['date'].strftime('%Y-%m-%d %H:%M:%S')}\n{post['title']}\nLink: {post['link']}\n\n")

if __name__ == "__main__":
    display_latest_posts()
