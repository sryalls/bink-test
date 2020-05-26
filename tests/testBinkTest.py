from subprocess import call


def test_no_args(capfd):
    """
    Test that when run with no option arguments, the script presents the
    help text
    """

    call(['python', 'binkTest.py'])
    captured = capfd.readouterr()
    assert captured.out[0:34] == 'usage: python binkTest.py [option]'
    assert captured.out[-42:-1] == ' --tenants         Total masts per tenant'


# test rent
def test_rent():
    pass


# test rent-digest
def test_rent_digest():
    pass


# test lease-25
def test_lease_25():
    pass


# test lease-25-rent
def test_lease_25_rent():
    pass


# test lease-inclusive
def test_lease_inclusive():
    pass


# test tenants
def test_tenants():
    pass
