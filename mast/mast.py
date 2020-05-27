import csv


class Mast(object):

    def __init__(self, name, address, tenant, lease_start,
                 lease_end, duration, rent):
        tenant.replace(" ", "")
        tenant.replace(".", "")
        self.name = name.upper()
        self.address = address.upper()
        self.tenant = tenant.upper()
        self.lease_start = lease_start
        self.leas_end = lease_end
        self.duration = duration
        self.rent = rent


class MastSet(object):
    def __init__(self):
        self.masts = self.load_from_csv('PythonDeveloperTestDataset.csv')

    def load_from_csv(self, file_location):
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
