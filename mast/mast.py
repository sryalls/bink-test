from datetime import datetime

import csv


tenant_misspellings = {'HUTCHISON': 'HUTCHISON',
                       'HUTCHINSON': 'HUTCHISON',
                       'HUTCHSION': 'HUTCHISON',
                       'HUTCHISON3GUKLTD': 'HUTCHISON3GUK',
                       'HUTCHISON3GLTD': 'HUTCHISON3GUK'
                       } # Arqiva and Arqiva services not included because they
                         # could be different companies

tenant_pretty = {
    'ARQIVASERVICESLTD': 'Arqiva Services Ltd',
    'ARQIVALTD': 'Arqiva Ltd',
    'VODAFONELTD': 'Vodafone Ltd',
    'O2(UK)LTD': 'O2 (UK) Ltd',
    'EVERYTHINGEVERYWHERELTDHUTCHISON3GUK':
        'Everything Everywhere Ltd & Hutchison 3G Ltd',
    'EVERYTHINGEVERYWHERELTD': 'Everything Everywhere Ltd',
    'CORNERSTONETELECOMMUNICATIONSINFRASTRUCTURE':
        'Cornerstone Telecommunications Infrastructure'
}


def _clean_tenant(tenant):
    """
    Clean variances from the input tenant string.

    :param tenant:
    :return: str
    """
    tenant = tenant.replace(' ', '')
    tenant = tenant.replace('.', '')
    for variant in tenant_misspellings.keys():
        tenant = tenant.replace(variant, tenant_misspellings[variant])

    parties = tenant.split('&')
    if len(parties) > 1:
        parties.sort()
        tenant = ''.join(parties)

    for variant in tenant_pretty:
        tenant = tenant.replace(variant, tenant_pretty[variant])
    return tenant


class Mast(object):
    """
    Contains the data for a single rented mast
    """

    def __init__(self, name, address, tenant, lease_start,
                 lease_end, duration, rent):
        """
        Constructor

        :param name:
        :param address:
        :param tenant:
        :param lease_start:
        :param lease_end:
        :param duration:
        :param rent:
        """
        tenant = _clean_tenant(tenant.upper())
        self.name = name
        self.address = address
        self.tenant = tenant
        self.lease_start = datetime.strptime(lease_start, '%d %b %Y')
        self.lease_end = datetime.strptime(lease_end, '%d %b %Y')
        self.duration = int(duration)
        self.rent = float(rent)


class MastSet(object):
    """
    Holds the set of rented masts
    """
    def __init__(self):
        """
        Constructor. Reads the mast set from csv file.
        """
        self.masts = self.load_from_csv('PythonDeveloperTestDataset.csv')

    def load_from_csv(self, file_location):
        """
        From a file location, return a list of loaded masts.

        :param file_location:
        :return: list
        """
        masts = []
        with open(file_location, mode='r') as infile:
            reader = csv.reader(infile)
            next(reader, None)
            for row in reader:
                mast = Mast(
                    name=row[0],
                    address=f'{row[1]}'
                            f'\n{row[2]}\n{row[3]}\n{row[4]}\n{row[5]}',
                    tenant=row[6],
                    lease_start=row[7],
                    lease_end=row[8],
                    duration=row[9],
                    rent=row[10]
                )
                masts.append(mast)
        return masts

    def get_masts_by_tenant(self):
        """
        From the stored list of all masts, return the count of all masts for
        each tenant.

        :return: dict
        """
        tenants = {}
        for mast in self.masts:
            if mast.tenant not in tenants.keys():
                tenants[mast.tenant] = 0
            tenants[mast.tenant] += 1
        return tenants

    def order_by_rent(self, limit=None):
        """
        From the stored list of all masts, return a list of all masts sorted by
        rent value

        :param limit:
        :return: list
        """
        self.masts = sorted(self.masts, key=lambda i: i.rent)
        if limit:
            return self.masts[0:limit]
        return self.masts

    def get_masts_by_lease_length(self, lease=25):
        """
        From the stored list of all masts, return a list of all masts with a
        given lease length.

        :param lease:
        :return: list
        """
        selected_masts = []
        for mast in self.masts:
            if mast.duration == lease:
                selected_masts.append(mast)
        return selected_masts

    def get_masts_by_lease_start(self,
                                 open_date='01 Jun 1999',
                                 close_date='31 Aug 2007'):
        """
        From the stored list of all masts, return a list of all masts with a
        lease start date between two given dates.

        :param open_date:
        :param close_date:
        :return: list
        """
        selected_masts = []
        for mast in self.masts:
            if datetime.strptime(open_date, '%d %b %Y') <= \
                    mast.lease_start <= datetime.strptime(close_date,
                                                          '%d %b %Y'):
                selected_masts.append(mast)

        return selected_masts
