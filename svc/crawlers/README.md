# Launch
To launch a tsn crawler run
```
scrapy crawl tsn.ua
```

To be able to save and later continue crawl, you need to tell the directory, where the crawler will save its state
```
scrapy crawl tsn.ua -s JOBDIR=crawls/tsn_spider
```
When your are done for a sessions, you need to press Ctrl+C or send stop signal in other way and wait untill it gracefully shuts down

# Testing
Collect data to local jsonl file
```
scrapy crawl tsn.ua -O data.jsonl
```

Playing with one of tsn links

```
scrapy shell https://tsn.ua/prosport/arsenal-liverpul-de-divitisya-i-stavki-bukmekeriv-na-match-apl-2687376.html
```
