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





