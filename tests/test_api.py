import unittest
from flask import json
from api.app import create_app

class APITestCase(unittest.TestCase):
    def setUp(self):
        """Set up a test client for the API."""
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()

    def test_get_items(self):
        """Test retrieving all items."""
        response = self.client.get('/api/items')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(json.loads(response.data), list)

    def test_create_item(self):
        """Test creating a new item."""
        # Example item data
        item_data = {'name': 'New Item', 'description': 'A brand new item'}
        response = self.client.post('/api/items', json=item_data)
        self.assertEqual(response.status_code, 201)
        self.assertIn('New Item', response.data.decode('utf-8'))

    def test_get_item(self):
        """Test retrieving a single item by ID."""
        response = self.client.get('/api/items/1')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Item One', response.data.decode('utf-8'))

    def test_update_item(self):
        """Test updating an existing item."""
        item_data = {'name': 'Updated Item', 'description': 'Updated description'}
        response = self.client.put('/api/items/1', json=item_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn('Updated Item', response.data.decode('utf-8'))

    def test_delete_item(self):
        """Test deleting an item."""
        response = self.client.delete('/api/items/1')
        self.assertEqual(response.status_code, 204)

    def tearDown(self):
        """Tear down any data added during tests."""
        pass

if __name__ == '__main__':
    unittest.main()
