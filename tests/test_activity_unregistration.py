from fastapi.testclient import TestClient

from src.app import app


def test_unregister_participant_from_activity():
    client = TestClient(app)
    email = "newstudent@mergington.edu"

    signup_response = client.post(
        "/activities/Chess Club/signup",
        params={"email": email},
    )
    assert signup_response.status_code == 200

    unregister_response = client.delete(
        "/activities/Chess Club/unregister",
        params={"email": email},
    )

    assert unregister_response.status_code == 200
    payload = unregister_response.json()
    assert payload["message"] == f"Unregistered {email} from Chess Club"

    activities_response = client.get("/activities")
    activity = activities_response.json()["Chess Club"]
    assert email not in activity["participants"]
