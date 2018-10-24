#!/usr/bin/env python
# (c) 2016 John Strickler
#
from lxml import etree

from xml_book_tags import *
from xml_website_tags import *
from xml_bibliography_tags import BIBLIOGRAPHY, ENTRY

doc = BIBLIOGRAPHY(
    ENTRY(
        BOOK(
            BOOK_TITLE('Automate the Boring Stuff with Python'),
            BOOK_AUTHOR('Al Sweigart'),
            BOOK_PUB('No Starch Press'),
            BOOK_PUB_YEAR('2015')
        ),
        id="1",
    ),
    ENTRY(
        BOOK(
            BOOK_TITLE('Fundamentals of Python: Data Structures'),
            BOOK_AUTHOR('Ken Lambert'),
            BOOK_PUB('Cengage Learning PTR'),
            BOOK_PUB_YEAR('2013'),
        ),
        id="2",
    ),
    ENTRY(
        WEBSITE(
            WEBSITE_TITLE('Scraping images with Python and Scrapy'),
            WEBSITE_URL('http://www.pyimagesearch.com/2015/10/12/scraping-images-with-python-and-scrapy/'),
        ),
        id="3",
    ),
)

print(etree.tostring(doc, pretty_print=True).decode())
