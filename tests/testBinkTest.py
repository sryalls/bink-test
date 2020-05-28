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
def test_rent(capfd):
    """
    Test that the 'Order by Rent' functionality works as expected
    """

    call(['python', 'binkTest.py', '-r'])
    captured = capfd.readouterr()
    assert captured.out[0:34] == 'Potternewton Crescent - Arqiva Ltd'
    assert len(captured.out) == 3148
    assert captured.out[-9:-1] == "28327.09"


# test rent-digest
def test_rent_digest(capfd):
    """
    Test that the 'Order by Rent' functionality works as expected when limited
    to five results
    """
    call(['python', 'binkTest.py', '-d'])
    captured = capfd.readouterr()
    assert captured.out[0:34] == 'Potternewton Crescent - Arqiva Ltd'
    assert len(captured.out) == 302
    assert captured.out[-8:-1] == "12750.0"


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
def test_tenants(capfd):
    """
    Test that the 'get masts by tenant' functionality outputs the expected
    result
    """

    call(['python', 'binkTest.py', '-t'])
    captured = capfd.readouterr()
    assert captured.out[0:10] == 'Arqiva Ltd'
    assert len(captured.out) == 245
    assert captured.out[-10:-1] == "masts: 2\n"

