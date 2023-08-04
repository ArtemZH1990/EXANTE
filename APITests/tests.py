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
        assert response.status_code == 200, "Status code is not OK. Connect denied"
        print("API status code compare")
        print("Test passed")

    @allure.description("Checking API status without user key. Status code will be 400 or 500 series")
    def test_checking_api_status_code_without_user_key(self):
        print()
        print("API checking ...")
        response = requests.post(UserApiData.url_current_json)
        print(f"Response status is {response.status_code}")
        assert response.status_code != 200, "Status code isn't 400 or 500 series"
        print("API status code compare")
        print("Test passed")

    @allure.description("This test without one necessary parameter. Status code is can't be 200")
    def test_checking_api_status_code_with_user_key(self):
        print()
        print("API checking ...")
        print("Sending user key in POST method")
        response = requests.post(UserApiData.url_current_json, headers=UserApiData.user_key)
        print(f"Response status is {response.status_code}")
        assert response.status_code != 200, "Status code is not OK. Connect denied"
        print("API status code compare")
        print("Test passed")

    @allure.description("Test with all necessary parameter. Status code will be 200")
    def test_checking_with_necessary_parameters(self):
        print()
        print("API checking ...")
        print("Sending user key and q-parameter in POST method")
        response = requests.post(UserApiData.url_current_json, headers=UserApiData.user_key, params=UserApiData.q_parameter)
        print(f"Response status is {response.status_code}")
        assert response.status_code == 200, "Status code is not OK. Connect denied"
        print("API status code compare")
        print("Test passed")

    @allure.description("Country checker test. Country in sending parameter have to be equal in response body")
    def test_country_check_in_response_body(self):
        print()
        print("API checking ...")
        print("Sending user key and country checker parameter in POST method")
        response = requests.post(UserApiData.url_current_json, headers=UserApiData.user_key, params=UserApiData.country_checker)
        response_body = response.json()
        response_API_country = response_body["location"]["name"]
        assert response_API_country == UserApiData.country_checker["q"], "Countries aren't equal! Check response body"
        print(f"""Response country - {response_API_country}. User chosen country - {UserApiData.country_checker["q"]} """)
        print("Test passed")


    @allure.description("Temperature Celsius parameter existing test")
    def test_temperature_celsius_parameter_exist(self):
        print()
        print("API checking ...")
        print("Sending user key and q-parameter in POST method")
        response = requests.post(UserApiData.url_current_json, headers=UserApiData.user_key, params=UserApiData.country_checker)
        response_body = response.json()
        response_temp_c = response_body["current"]["temp_c"]
        assert response_temp_c != None, "Response temperature Celsius parameter doesn't exist "
        print(f"Response temperature Celsius parameter  is {response_temp_c}")
        print("Test passed")

    @allure.description("Temperature Fahrenheit parameter existing test")
    def test_temperature_fahrenheit_parameter_exist(self):
        print()
        print("API checking ...")
        print("Sending user key and q-parameter in POST method")
        response = requests.post(UserApiData.url_current_json, headers=UserApiData.user_key, params=UserApiData.country_checker)
        response_body = response.json()
        response_temp_f = response_body["current"]["temp_f"]
        assert response_temp_f != None, "Response temperature Fahrenheit parameter doesn't exist "
        print(f"Response temperature Fahrenheit parameter is {response_temp_f}")
        print("Test passed")

    @allure.description("Response humidity parameter existing test")
    def test_humidity_parameter_exist(self):
        print()
        print("API checking ...")
        print("Sending user key and q-parameter in POST method")
        response = requests.post(UserApiData.url_current_json, headers=UserApiData.user_key, params=UserApiData.country_checker)
        response_body = response.json()
        response_humidity = response_body["current"]["humidity"]
        assert response_humidity != None, "Response parameter humidity doesn't exist "
        print(f"Response parameter humidity is {response_humidity}")
        print("Test passed")

    @allure.description("Response external IP test")
    def test_ip_checker(self):
       print()
       print("Sending user key and q-parameter in POST method")
       response = requests.post(UserApiData.url_ip_lookup, headers=UserApiData.user_key, params=UserApiData.ip_checker)
       response_body = response.json()
       print(response_body)
       response_ip = response_body["ip"]
       assert  response_ip == UserApiData.external_IP, "Wrong response IP"
       print(f"Response IP is {response_ip}. User external IP is {UserApiData.external_IP}")
       print("Test passed")



