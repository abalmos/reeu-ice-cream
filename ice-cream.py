#!/usr/bin/env python

import pprint
import nass

api = nass.NassApi('<INSERT-API-KEY_HERE>')

pp = pprint.PrettyPrinter(indent=2)

q = api.query()
q \
    .filter('program_desc', 'SURVEY') \
    .filter('group_desc', 'DAIRY') \
    .filter('commodity_desc', 'ICE CREAM') \
    .filter('agg_level_desc', 'STATE') \
    .filter('freq_desc', 'MONTHLY') \
    .filter('state_alpha', 'IN') \

print("Number of records", q.count())

recs = q.execute()
print("Example record:")
pp.pprint(recs[0])

data = {}

for r in recs:
    if r['state_name'] != 'INDIANA':
        continue

    year = r['year']
    month = r['reference_period_desc']
    # Sigh, `int()` chokes on commas ... this is *probably* broken.
    try:
        gals_millions = int(r['Value'].replace(',', '')) / 1000000
    except ValueError:
        # Just skip this data point ... this is also *probably* broken
        continue

    if year not in data:
        data[year] = {}

    if month not in data[year]:
        data[year][month] = 0

    data[year][month] += gals_millions

print("")
print("Millions of gallons produced:")

headers = ['YEAR', 'JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG',
           'SEP', 'OCT', 'NOV', 'DEC']

print(("{:<8}"*13).format(*headers))
print(("{:<8}"*13).format(*(['----']*13)))

for year, d in sorted(data.items()):
    print(("{:<8}" + "{:<8.2f}"*12).format(year, d['JAN'], d['FEB'], d['MAR'], d['APR'],
                                           d['MAY'], d['JUN'], d['JUL'], d['AUG'], d['SEP'], d['OCT'], d['NOV'], d['DEC']))
