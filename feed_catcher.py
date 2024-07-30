import feedparser
from datetime import datetime, timedelta, timezone
from dateutil import parser, tz
import pytz

# List of RSS feed URLs
feeds = [
   'https://medium.com/feed/@shb8086'  
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
