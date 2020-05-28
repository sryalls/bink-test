import argparse
from mast.mast import MastSet

# setting up command line options
parser = argparse.ArgumentParser(prog='bink-test',
                                 usage='python binkTest.py [option]')

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

# loading mast data
masts = MastSet()


def _rent_output(masts):
    for mast in masts:
        print(f'{mast.name} - {mast.tenant}\nrent: £{mast.rent}')


if __name__ == '__main__':

    options = parser.parse_args()
    if options.rent:
        masts = masts.order_by_rent()
        _rent_output(masts)

    if options.rent_digest:
        masts = masts.order_by_rent(5)
        _rent_output(masts)

    if options.lease_25:
        masts = masts.get_masts_by_lease_length()
        rent_total = 0
        for mast in masts:
            print(f'{mast.name}\n{mast.address}')
            print(f'Tenant: {mast.tenant}')
            print(f'Lease Start: {mast.lease_start}')
            print(f'Lease End: {mast.lease_end}')
            print(f'Lease Duration: {mast.duration} years')
            print(f'Rent: £{str(mast.rent)}\n----------\n')
            rent_total += mast.rent
        print(f'Total Value of leases: £{rent_total}')
    if options.lease_inclusive:
        pass
    if options.tenants:
        tenants = masts.get_masts_by_tenant()
        tenants = tenants.items()
        tenants = sorted(tenants)
        for tenant in tenants:
            print(f'{tenant[0]}\nmasts: {tenant[1]}\n')
    if True not in (vars(options)).values():
        parser.print_help()
