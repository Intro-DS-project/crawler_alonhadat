#!/bin/sh
current_date_time=$(date +'%Y-%m-%d_%H-%M-%S')
scrapy crawl alonhadat -O "/app/data/${current_date_time}_alonhadat_output.json"