#!/usr/bin/env python
import lxml.etree as ET


def fetch_marc_subfield(marcrec, tag, code):
    for data_field in marcrec.findall('datafield'):
        if data_field.get('tag') == tag:
            for subfield in data_field.findall('subfield'):
                if subfield.get('code') == code:
                    return subfield.text


book_root = ET.parse('DATA/books.xml')

for num, rec in enumerate(book_root.getiterator('record')):
    print("Record:", num + 1)
    print("\tAuthor:", fetch_marc_subfield(rec, '100', 'a'))
    print("\tTitle:", fetch_marc_subfield(rec, '245', 'a'))
    print("\tISBN:", fetch_marc_subfield(rec, '020', 'a'))
