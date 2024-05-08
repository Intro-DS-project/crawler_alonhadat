# crawler_alonhadat
# Installation

### Dependencies
Requires python 3.8+ or later



### Run
- Clone this repository

```bash
$ git clone https://github.com/Intro-DS-project/crawler_alonhadat.git
```

- Install dependencies
```bash
pip install -r requirements.txt
```

- In the root of the repository move to folder `crawler_alonhadat` and run : 
```bash
$ scrapy crawl alonhadat -o alonhadat.json --set FEED_EXPORT_ENCODING=utf-8
```

- Docker
``` bash 
$ docker build -t alonhadat .
$ docker run -v $(pwd):/app/data alonhadat 
```

### API_KEY 
