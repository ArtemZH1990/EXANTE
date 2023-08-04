import pytest
import allure
import requests
from UserData.user_data import UserApiData


class TestMainApi:
    @allure.description("API status code 200 checking")
    def test_status_code_is_200(self):
        print()
        print("API checking ...")
        response = requests.get(UserApiData.base_url)
        print(f"Response status is {response.status_code}")
        print("API status code compare")
        assert response.status_code == 200, "Status code is not OK. Connect denied"
        print("Test passed")

    @allure.description("Checking API status without user key. Status code will be 400 or 500 series")
    def test_checking_api_status_code_without_user_key(self):
        print()
        print("API checking ...")
        response = requests.post(UserApiData.url_for_correct_response)
        print(f"Response status is {response.status_code}")
        print("API status code compare")
        assert response.status_code != 200, "Status code isn't 400 or 500 series"
        print("Test passed")

    @allure.description("This test without one necessary parameter. Status code is can't be 200")
    def test_checking_api_status_code_with_user_key(self):
        print()
        print("API checking ...")
        print("Sending user key in POST method")
        response = requests.post(UserApiData.url_for_correct_response, headers=UserApiData.user_key)
        print(f"Response status is {response.status_code}")
        print("API status code compare")
        assert response.status_code != 200, "Status code is not OK. Connect denied"
        print("Test passed")

    @allure.description("Test with all necessary parameter. Status code will be 200")
    def test_checking_with_necessary_parameters(self):
        print()
        print("API checking ...")
        print("Sending user key and q-parameter in POST method")
        response = requests.post(UserApiData.url_for_correct_response, headers=UserApiData.user_key, params=UserApiData.q_parameter)
        print(f"Response status is {response.status_code}")
        print("API status code compare")
        assert response.status_code == 200, "Status code is not OK. Connect denied"
        print("Test passed")

    @allure.description("Country checker test. Country in sending parameter have to be equal in response body")
    def test_country_check_in_response_body(self):
        print()
        print("API checking ...")
        print("Sending user key and country checker parameter in POST method")
        response = requests.post(UserApiData.url_for_correct_response, headers=UserApiData.user_key, params=UserApiData.country_checker)
        response_body = response.json()
        response_API_country = response_body["location"]["name"]
        print(response_API_country)
        assert response_API_country == UserApiData.country_checker["q"], "Countries aren't equal! Check response body"
        print("Test passed")





