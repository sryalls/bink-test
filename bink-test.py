import argparse

# setting up command line options
parser = argparse.ArgumentParser(prog='bink-test',
                                 usage='python bink-test.py [option]')

parser.add_argument('-r', '--rent', help='Ascending list of rent values',
                    action='store_true')

parser.add_argument('-d', '--rent-digest',
                    help='Ascending list of  five smallest rent values',
                    action='store_true')

parser.add_argument('-f', '--lease-25',
                    help='List of masts with 25 year leases',
                    action='store_true')

parser.add_argument('-l', '--lease-25-rent',
                    help='Total rent for all 25 year lease masts',
                    action='store_true')

parser.add_argument('-i', '--lease-inclusive',
                    help='Rentals with start date between between 1st June '
                         '1999 and 31st August 2007 inclusive',
                    action='store_true')

parser.add_argument('-t', '--tenants',
                    help='Total masts per tenant', action='store_true')

parser.print_help()

if __name__ == '__main__':
    pass