# Justin Ventura

'''
This module contains the tests for the listings routes.

How to test: `python3 -m pytest -s api/tests/test_db.py`
OR
`python3 -m pytest -s api/tests/`
'''

# Imports for database:
# from api.models import db, ClientsModel, ListingsModel
from api.constants import OK, BAD_REQUEST, NOT_FOUND

from testing_data import listingsToSubmit


# Test route to insert a listing:
def test_listing_submit(client):
    '''
    This test checks that the listing submission route works correctly.

    Route:
        /listing-submit
    '''
    # Test that this route works correctly:
    # ------------------------------ TEST 1 ------------------------------
    for listingToSubmit in listingsToSubmit:
        valid_post = client.post('/listing-submit', json=listingToSubmit)
        assert valid_post.status_code == OK, 'Valid listing failed.'


# Test route to get listings by status:
def test_get_listings_bystatus(client):
    '''
    This test checks that the listings by status route works correctly.

    Route:
        /get-listings/<status>
    '''
    # Test that this route works correctly:
    # ------------------------------ TEST 1 ------------------------------
    invalid_get1 = client.get('/get-listings/joe')
    assert invalid_get1.status_code == BAD_REQUEST, 'Invalid status failed.'

    invalid_get2 = client.get('/get-listings/lsaddfj')
    assert invalid_get2.status_code == BAD_REQUEST, 'Invalid status failed.'

    invalid_get3 = client.get('/get-listings/')
    assert invalid_get3.status_code == NOT_FOUND, 'Missing status failed.'

    # ------------------------------ TEST 2 ------------------------------
    valid_get1 = client.get('/get-listings/inactive')
    assert valid_get1.status_code == OK, 'Valid status failed.'

    inactive_respose = valid_get1.get_json()

    # Check through inactive listings:
    for item in inactive_respose.values():

        listing = item['listing']

        # Ensure the correct ones were returned:
        assert listing['status'] == 'inactive', 'Inactive listings failed.'
        assert 'TEST3' in listing['position'], 'Inactive listings failed.'

    # ------------------------------ TEST 3 ------------------------------
    valid_get2 = client.get('/get-listings/active')
    assert valid_get2.status_code == OK, 'Valid status failed.'

    active_respose = valid_get2.get_json()

    # Check through active listings:
    for item in active_respose.values():

        listing = item['listing']

        # Ensure the correct ones were returned:
        assert listing['status'] == 'active', 'Active listings failed.'
        assert 'TEST1' in listing['position'], 'Active listings failed.'

    # ------------------------------ TEST 4 ------------------------------
    valid_get3 = client.get('/get-listings/pending')
    assert valid_get3.status_code == OK, 'Valid status failed.'

    pending_respose = valid_get3.get_json()

    # Check through pending listings:
    for item in pending_respose.values():

        listing = item['listing']

        # Ensure the correct ones were returned:
        assert listing['status'] == 'pending', 'Pending listings failed.'
        assert 'TEST2' in listing['position'], 'Pending listings failed.'


def test_get_listings_byid(client):
    '''
    This test checks that the listings by id route works correctly.

    Route:
        /get-listings/<id>
    '''
    # Test that this route works correctly:
    # ------------------------------ TEST 1 ------------------------------
    invalid_get1 = client.get('/get-listings/joe')
    assert invalid_get1.status_code == BAD_REQUEST, 'Invalid id failed.'

    invalid_get2 = client.get('/get-listings/one')
    assert invalid_get2.status_code == BAD_REQUEST, 'Invalid id failed.'

    invalid_get3 = client.get('/get-listings/')
    assert invalid_get3.status_code == NOT_FOUND, 'Missing id failed.'

    # ------------------------------ TEST 2 ------------------------------
    valid_get1 = client.get('/get-listing/1')
    assert valid_get1.status_code == OK, 'Valid id failed.'
    assert 'TEST1' in valid_get1.get_json()['listing']['position'],\
        'Valid id incorrect.'

    valid_get2 = client.get('/get-listing/2')
    assert valid_get2.status_code == OK, 'Valid id failed.'
    assert 'TEST2' in valid_get2.get_json()['listing']['position'],\
        'Valid id incorrect.'

    valid_get3 = client.get('/get-listing/3')
    assert valid_get3.status_code == OK, 'Valid id failed.'
    assert 'TEST3' in valid_get3.get_json()['listing']['position'],\
        'Valid id incorrect.'

    valid_get4 = client.get('/get-listing/4')
    assert valid_get4.status_code == OK, 'Valid id failed.'
    assert 'TEST2' in valid_get4.get_json()['listing']['position'],\
        'Valid id incorrect.'

    valid_get5 = client.get('/get-listing/5')
    assert valid_get5.status_code == OK, 'Valid id failed.'
    assert 'TEST2' in valid_get5.get_json()['listing']['position'],\
        'Valid id incorrect.'