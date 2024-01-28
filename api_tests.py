import requests
import unittest
from unittest import TestCase

class FlightApiTest(TestCase):
    def test_get_response_status_200(self):
        response = requests.get("https://flights-api.buraky.workers.dev/")
        assert response.status_code == 200, f"Expected response to be 200 but it was: {response.status_code}"



    def test_response_structure_is_correct(self):
        response = requests.get("https://flights-api.buraky.workers.dev/")
        response_json = response.json()
        flight_list = response_json["data"]
        for flight in flight_list:
            assert isinstance(flight["id"], int), f"Expected flight 'id' to be integer but it was not: {flight['id']}"
            assert isinstance(flight["from"], str), f"Expected flight 'from' to be string but it was not: {flight['from']}"
            assert isinstance(flight["to"], str), f"Expected flight 'to' to be string but it was not: {flight['to']}"
            assert isinstance(flight["date"], str), f"Expected flight 'date' to be string but it was not: {flight['date']}"


    def test_content_type_is_json(self):
        response = requests.get("https://flights-api.buraky.workers.dev/")
        assert response.headers["Content-Type"] == "application/json", "Content-Type is not application/json."

if __name__ == "__main__":
    unittest.main()

