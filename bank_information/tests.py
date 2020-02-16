from django.test import TestCase
from django.test import Client


class BranchAutocompleteTests(TestCase):
    def test_branch_details(self):
        """ Test to compare the expected returned lists """
        c = Client()
        response = c.get('/api/branches/autocomplete', {'q': 'RTGS', 'limit': 4, 'offset': 0})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()['data']), 4)
        self.assertEqual(response.json()['message'], 'Branch details retrieved successfully!')

    def test_branch_fail_case(self):
        """ Test to compare the expected returned lists """
        c = Client()
        response = c.get('/api/branches/autocomplete', {'q': 'No data return for this test', 'limit': 5, 'offset': 2})
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json()['message'], 'No matching data for the search entries!')
