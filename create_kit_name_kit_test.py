import sender_stand_request
import data

def get_kit_body(kit_name):
    current_body = data.kit_body.copy()
    current_body['name'] = kit_name
    return current_body


def positive_assert(name):
    user_response = sender_stand_request.post_new_user(data.user_body)
    assert user_response.status_code == 201
    auth_token = user_response.json().get("authToken")
    assert auth_token is not None, "No se obtuvo auth_token"

    kit_body = get_kit_body(name)
    kit_response = sender_stand_request.post_new_kit(auth_token, kit_body)

    assert kit_response.status_code == 201


def negative_assert_symbol(name):

    user_response = sender_stand_request.post_new_user(data.user_body)
    assert user_response.status_code == 201
    auth_token = user_response.json().get("authToken")
    assert auth_token is not None, "No se obtuvo auth_token"


    kit_body = get_kit_body(name)
    kit_response = sender_stand_request.post_new_kit(auth_token, kit_body)

    assert kit_response.status_code == 400
    assert kit_response.json()["code"] == 400


def test_create_kit_1_letter_in_kit_name_get_success_response():
    positive_assert('a')

def test_create_kit_511_letters_in_kit_name_get_success_response():
    positive_assert('AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC')

def test_create_kit_0_letter_in_kit_name_get_error_response():
    negative_assert_symbol('')

def test_create_kit_512_letters_in_kit_name_get_error_response():
    negative_assert_symbol('AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD')

def test_create_kit_with_special_characters_in_kit_name_get_success_response():
    positive_assert("\"№%@\",")

def test_create_kit_with_a_space_on_the_kit_name_get_success_response():
    positive_assert("A Aaa")

def test_create_kit_with_numbers_in_the_kit_name_get_error_response():
    positive_assert("123")

def test_create_kit_when_parameter_is_not_passed_in_the_request_error_response():
    negative_assert_symbol()

def test_create_kit_when_parameter_is_different_passed_in_the_request_error_response():
    negative_assert_symbol(123)

