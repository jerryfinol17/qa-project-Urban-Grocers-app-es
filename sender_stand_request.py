import configuration
import requests
import data



def post_new_user(body):
    return requests.post( configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
        json=body,
        headers=data.headers
    )

def get_auth_token():
    response = post_new_user(data.user_body)
    assert response.status_code == 201
    auth_token=response.json().get("authToken")
    assert auth_token is not None, "No auth token returned"
    return auth_token

def post_new_kit(auth_token, kit_body):

            headers = data.headers.copy()
            headers["Authorization"] = f"Bearer {auth_token}"
            return requests.post( configuration.URL_SERVICE + configuration.KITS_PATH,
                json=kit_body,
                headers=headers
            )

