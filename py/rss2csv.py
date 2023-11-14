import azure.functions as func
import csv
import feedparser
import io
import logging
import os
import re
import requests
import time
from ..shared_code import utilities


def fetchRSSandOutputCSV(url):
    ''' fetch the specified RSS feed and return in CSV format '''

    # test mode: if 3-digit "url" provided, return as an HTTP status code
    matches = re.search(r"^(\d\d\d)$", url)
    if matches:
        statuscode = matches[1]
        return func.HttpResponse(
            f"Test mode, returning status {statuscode}\n",
            status_code=statuscode
        )

    if not re.search(r"^https?:\/\/", url):
        return func.HttpResponse(
             "Invalid 'url' parameter.\n",
             status_code=400
        )

    start = time.time()
    rss = feedparser.parse(url)
    delta = int((time.time() - start) * 1000)
    logging.info(f"time-feedparser: {delta} ms")
    if rss.status not in [200, 301, 302]:
        return func.HttpResponse(
            f"Error fetching {url}: {rss.status}\n", status_code=400
        )

    output = io.StringIO()
    headers = {
        "Content-Type": "text/csv; charset=utf-8",
        "Content-Disposition": "attachment; filename=\"export.csv\"",
        "Pragma": "no-cache",
        "URL-Actual": rss.href
    }
    csv_writer = csv.writer(
        output,
        delimiter=',',
        quotechar='"',
        quoting=csv.QUOTE_ALL
    )

    csv_writer.writerow([
        'Title',
        'Link',
        'Description',
        'pubDate',
        'guid']
    )

    for item in rss.entries:
        csv_writer.writerow([
            item.get('title', 'No Title'),
            item.get('link', ''),
            item.get('summary', ''),
            item.get('published', ''),
            item.get('id', '')
        ])

    result = output.getvalue()
    output.close()
    return func.HttpResponse(result, headers=headers)
