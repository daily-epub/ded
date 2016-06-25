from newspaper import Article
import feedparser
import uuid

from . import Chapter, Appendix
from dominate.tags import *

metadata = {
  "name": "rss",
  "fullname": "RSS Reader",
  "description": "This source will parse an RSS feed and download its article.",
  "options": []
}

def build(config):
    source = config.get("source")
    limit = config.get("limit", 10)

    _feed = feedparser.parse(source)
    feed = _feed.get("feed")
    entries = _feed.get("entries", [])

    chapter = Chapter(feed.get("title", ""), feed.get("subtitle", ""))

    limit = min(limit, len(entries))
    for i in range(0, limit):
        entry = entries[i]
        title = entry.get("title", "<No title for this entry>")

        url = entry.get("link")

        if url is None:
            pass
        else:
            title = entry.get("title")

            text_anchor = str(uuid.uuid4())

            chapter.add(a(b(title), href="#"+text_anchor))
            chapter.add(br())
            chapter.add(hr())

            appendix = Appendix(title, "", name=text_anchor)
            article = Article(url)
            article.download()
            article.parse()
            
            if article.top_image:
                appendix.add(img(src=article.top_image))
            appendix.add(p(article.text))

            chapter.add_appendix(appendix)

    return chapter
