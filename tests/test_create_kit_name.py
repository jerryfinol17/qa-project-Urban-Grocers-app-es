import sender_stand_request
import data


def get_kit_body(name):
    body=data.kit_body.copy()
    body["name"]= name
    return body

def positive_assert(name):
    token= sender_stand_request.get_auth_token()
    kit_response = sender_stand_request.post_new_kit(token, get_kit_body(name))
    assert kit_response.status_code == 201

def negative_assert(name):
    token= sender_stand_request.get_auth_token()
    kit_response = sender_stand_request.post_new_kit(token, get_kit_body(name))
    assert kit_response.status_code == 400

def get_kit_body_missing_param():
    body = data.kit_body.copy()
    body.pop("name", None)
    return body

def test_1_letter():  positive_assert("a")
def test_511_letters(): positive_assert("A"*511)
def test_special_chars():         positive_assert("\"№%@,")
def test_spaces():                positive_assert("A Aaa")
def test_numbers():               positive_assert("123")
def test_empty_name():            negative_assert("")
def test_512_letters():           negative_assert("A" * 512)
def test_number_type():           negative_assert(123)
def test_missing_name_param():    negative_assert(None)
def test_missing_name_key():
    token = sender_stand_request.get_auth_token()
    response = sender_stand_request.post_new_kit(token, get_kit_body_missing_param())
    assert response.status_code == 400
