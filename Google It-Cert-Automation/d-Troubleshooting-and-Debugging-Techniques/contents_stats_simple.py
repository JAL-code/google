#!/usr/bin/env python3

# contents_stats_simple.py

from bs4 import BeautifulSoup

import heapq

import zimply
import zimply.zimply

from tqdm import tqdm

from memory_profiler import profile

def html_text(content):

    soup = BeautifulSoup(content, features="html.parser")

    # kill all script and style elements
    for script in soup(["script", "style"]):
        script.extract()  # rip it out

    # get text

    text = soup.get_text()

    return text

def generate_stats(words):
    heap = [
        (- amount, word, refs) for word, (amount, refs) in words.items()
    ]
    heapq.heapify(heap)

    for n_amount, word, refs in heapq.nsmallest(50, heap):
        amount = - n_amount
        print(f'{word} with {amount}')

# tell the profiler to analyze the memory comsumption of it.

@profile
def main():
    zim = zimply.zimply.ZIMFile('data.zim', 'utf-8')
    words = {}

    limit = 50
    for i, content in tqdm(enumerate(zim), total=limit):
        if (i > limit):
            break

        idx = content[2]

        try:
            article = zim._get_article_by_index(idx)
            html_data = article.data
        except Exception:
            print(f'ERROR: in idx={idx}')
            continue
        if not html_data:
            continue

        text = html_text(html_data)
        for word in text.split():
            word in word.lower()

            # If the word is not in the dictionary, init. an empty container

            if word not in words:
                words[word] = [0, set()]

            # Get the entry for the word, add to count and the ref

            value = words[word]
            value[0] += 1
            value[1].add(article)

    generate_stats(words)