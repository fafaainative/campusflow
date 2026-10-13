# campusflow/auth.py

USERS = {
    "engrA": {
        "password": "A@12345",
        "name": "Engineer A",
        "role": "Engineer"
    },
    "engrB": {
        "password": "B@12345",
        "name": "Engineer B",
        "role": "Engineer"
    }
}


def authenticate(username, password):
    """Verify a user's login details."""

    user = USERS.get(username)

    if user and user["password"] == password:
        return user

    return None
    