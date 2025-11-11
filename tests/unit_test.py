import unittest
from app import app, cart


class TestPrinterStore(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.client = app.test_client()
        cart.clear()  # Reset cart before each test

    def test_index_page(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Printer Store", response.data)
        print("✅ Index page loads correctly.")

    def test_add_to_cart(self):
        response = self.client.post("/add_to_cart", data={"product_id": "printer-a"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(cart), 1)
        print("✅ Add to cart works.")

    def test_remove_from_cart(self):
        cart.append({"id": "printer-a", "name": "Printer A", "price": 150})
        response = self.client.post(
            "/remove_from_cart", data={"product_id": "printer-a"}
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(cart), 0)
        print("✅ Remove from cart works.")


if __name__ == "__main__":
    unittest.main()
