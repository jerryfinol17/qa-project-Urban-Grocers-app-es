import configuration
import requests
import data



def post_new_user(body):
    return requests.post( configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
        json=body,
        headers=data.headers
    )

user_response = post_new_user(data.user_body)
print(user_response.status_code)
print( user_response.json())


if user_response.status_code == 201:
    auth_token = user_response.json().get("authToken")
    if auth_token:
        print( auth_token)


def post_new_kit(auth_token, kit_body):

            headers = data.headers.copy()
            headers["Authorization"] = f"Bearer {auth_token}"
            return requests.post( configuration.URL_SERVICE + configuration.KITS_PATH,
                json=kit_body,
                headers=headers
            )

kit_response = post_new_kit(auth_token, data.kit_body)
print( kit_response.status_code)
print(kit_response.json())

