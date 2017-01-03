#!/usr/bin/env python
import re

####
# Data from: Code-Point Open, CSV
# https://www.ordnancesurvey.co.uk/opendatadownload/products.html
# cat CSV/*.csv | sed -e 's/^"//g' | sed -e 's/".*//g' | sed -E -e "s/ +//g" > uk_postal_codes.txt  # noqa
# Regular expressions from:
# https://stackoverflow.com/questions/164979/uk-postcode-regex-comprehensive
# https://www.gov.uk/government/uploads/system/uploads/attachment_data/file/488478/Bulk_Data_Transfer_-_additional_validation_valid_from_12_November_2015.pdf
# Testing:
# sudo apt-get install linux-perf-4.6
# sudo perf stat -t 8 -d python uk_postal_codes.py
####

# Settings
use_file = True
file_path = 'uk_postal_codes.txt'

select_pattern = False
pattern_number = 0
####

patterns = (
    r'^([Gg][Ii][Rr] 0[Aa]{2})|((([A-Za-z][0-9]{1,2})|(([A-Za-z][A-Ha-hJ-Yj-y][0-9]{1,2})|(([AZa-z][0-9][A-Za-z])|([A-Za-z][A-Ha-hJ-Yj-y][0-9]?[A-Za-z]))))[0-9][A-Za-z]{2})$',  # noqa
    r'^(GIR\s?0AA|[A-PR-UWYZ]([0-9]{1,2}|([A-HK-Y][0-9]([0-9ABEHMNPRV-Y])?)|[0-9][A-HJKPS-UW])\s?[0-9][ABD-HJLNP-UW-Z]{2})$',  # noqa
    r'^([A-PR-UWYZ]([A-HK-Y][0-9]([0-9]|[ABEHMNPRV-Y])?|[0-9]([#\s0-9]|[A-HJKPSTUW])?)\s?[0-9][ABD-HJLNP-UW-Z]{2})$',  # noqa
    r'^(GIR\s0AA)|([A-PR-UWYZ](([0-9]([0-9A-HJKPSTUW])?)|([A-HK-Y][0-9]([0-9ABEHMNPRVWXY])?))\s?[0-9][ABD-HJLNP-UW-Z]{2})$',  # noqa
)

samples = (
    # "AA9A 9AA",
    # "A9A 9AA",
    # "A9 9AA",
    # "A99 9AA",
    # "AA9 9AA",
    # "AA99 9AA",

    "AA9A9AA",
    "A9A9AA",
    "A99AA",
    "A999AA",
    "AA99AA",
    "AA999AA",

    # "AA9A\t9AA",
    # "A9A\t9AA",
    # "A9\t9AA",
    # "A99\t9AA",
    # "AA9\t9AA",
    # "AA99\t9AA",
)

if not use_file:
    source = samples
else:
    source = open(file_path).read().splitlines()
if select_pattern:
    patterns = [patterns[pattern_number]]

count = len(source)
matches_count = []
for pattern in patterns:
    regex = re.compile(pattern)
    match_count = 0
    for string in source:
        if re.match(regex, string) is not None:
            match_count += 1
    matches_count.append(match_count)

print matches_count, 'of', count
