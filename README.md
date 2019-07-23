# Indiana Ice Cream Production

This tool uses the NASS database API to print historical records of ice cream
production by month in Indiana.

Data source: https://quickstats.nass.usda.gov

_Caution:_ I am not Python programmer. I'm quite certain this is not
\*'pythonic' ... but it works!

# How to run

1. Run `pip install nass` to install the `nass` library.
1. Go to
   [https://quickstats.nass.usda.gov/api](https://quickstats.nass.usda.gov/api)
   and register an API key.
1. Add your API key to `ice-cream.py` line 6.
1. Run `python ice-cream.py`.
