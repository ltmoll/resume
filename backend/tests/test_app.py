import unittest

from backend.app import app


class ResumeApiTests(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_health_endpoint(self):
        response = self.client.get("/api/health")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {"status": "ok"})

    def test_profile_endpoint_returns_resume_sections(self):
        response = self.client.get("/api/profile")
        profile = response.get_json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(profile["name"], "Lucas Tremblay-Moll")
        self.assertTrue(profile["experience"])
        self.assertTrue(profile["skills"])
        self.assertTrue(profile["education"])
        self.assertTrue(profile["languages"])


if __name__ == "__main__":
    unittest.main()
