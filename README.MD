usage: python binkTest.py [option]

optional arguments:
  -h, --help            show this help message and exit
  -r, --rent            Ascending list of rent values
  -d, --rent-digest     Ascending list of five smallest rent values
  -f, --lease-25        List of masts with 25 year leases
  -l, --lease-25-rent   Total rent for all 25 year lease masts
  -i, --lease-inclusive
                        Rentals with start date between between 1st June 1999
                        and 31st August 2007 inclusive
  -t, --tenants         Total masts per tenant


To test 
pytest tests/*