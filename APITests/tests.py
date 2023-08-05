import pytest
import allure
import requests
from UserData.user_data import UserApiData
from UserMethods.user_methods import UserMainMethods


class TestMainApi:
    @allure.description("API status code 200 checking")
    def test_status_code_is_200(self):
        print()
        print("API checking ...")
        response_status = UserMainMethods.get_status_user_method_for_base_url(UserApiData.base_url)
        print(f"Response status is {response_status}")
        assert response_status == 200, "Status code is not OK. Connect denied"
        print("API status code compare")
        print("Test passed")

    @allure.description("Checking API status without user key. Status code will be 400 or 500 series")
    def test_api_status_code_without_user_key(self):
        print()
        print("API checking ...")
        response_status = UserMainMethods.get_status_user_method_for_base_url(UserApiData.url_current_json)
        print(f"Response status is {response_status}")
        assert response_status != 200, "Status code isn't 400 or 500 series"
        print("API status code compare")
        print("Test passed")

    @allure.description("This test without one necessary parameter. Status code is can't be 200")
    def test_api_status_code_with_user_key(self):
        print()
        print("API checking ...")
        print("Sending user key in POST method")
        response_status = UserMainMethods.get_status_user_method_for_base_url(UserApiData.url_current_json, UserApiData.user_key)
        print(f"Response status is {response_status}")
        print("API status code compare")
        assert response_status != 200, "Status code isn't 400 or 500 series"
        print("Test passed")

    @allure.description("Test with all necessary parameter. Status code will be 200")
    def test_status_checking_with_necessary_parameters(self):
        print()
        print("API checking ...")
        print("Sending user key and q-parameter in POST method")
        response_status = UserMainMethods.get_status_for_post_request_with_necessary_parameters(UserApiData.url_current_json, UserApiData.user_key,
                                                    UserApiData.q_parameter)
        print(f"Response status is {response_status}")
        print("API status code compare")
        assert response_status == 200, "Status code is not OK. Connect denied"
        print("Test passed")

    @allure.description("Country checker test. Country in sending parameter have to be equal in response body")
    def test_country_check_in_response_body(self):
        print()
        print("API checking ...")
        print("Sending user key and country checker parameter in POST method")
        response = UserMainMethods.post_user_method(UserApiData.url_current_json, UserApiData.user_key,
                                                    UserApiData.country_checker)
        response_API_country = response["location"]["name"]
        print(f"""Response country - {response_API_country}. User chosen country - {UserApiData.country_checker["q"]} """)
        assert response_API_country == UserApiData.country_checker["q"], "Countries aren't equal! Check response body"
        print("Test passed")


    @allure.description("Temperature Celsius parameter existing test")
    def test_temperature_celsius_parameter_exist(self):
        print()
        print("API checking ...")
        print("Sending user key and q-parameter in POST method")
        response = UserMainMethods.post_user_method(UserApiData.url_current_json, UserApiData.user_key,
                                                    UserApiData.country_checker)
        response_temp_c = response["current"]["temp_c"]
        print(f"Response temperature Celsius parameter  is {response_temp_c}")
        assert response_temp_c != None, "Response temperature Celsius parameter doesn't exist "
        print("Test passed")

    @allure.description("Temperature Fahrenheit parameter existing test")
    def test_temperature_fahrenheit_parameter_exist(self):
        print()
        print("API checking ...")
        print("Sending user key and q-parameter in POST method")
        response = UserMainMethods.post_user_method(UserApiData.url_current_json, UserApiData.user_key,
                                                    UserApiData.country_checker)
        response_temp_f = response["current"]["temp_f"]
        print(f"Response temperature Fahrenheit parameter is {response_temp_f}")
        assert response_temp_f != None, "Response temperature Fahrenheit parameter doesn't exist "
        print("Test passed")

    @allure.description("Response humidity parameter existing test")
    def test_humidity_parameter_exist(self):
        print()
        print("API checking ...")
        print("Sending user key and q-parameter in POST method")
        response = UserMainMethods.post_user_method(UserApiData.url_current_json, UserApiData.user_key,
                                                    UserApiData.country_checker)
        response_humidity = response["current"]["humidity"]
        print(f"Response parameter humidity is {response_humidity}")
        assert response_humidity != None, "Response parameter humidity doesn't exist "
        print("Test passed")

    @allure.description("Response external IP test")
    def test_ip_checker(self):
       print()
       print("Sending user key and q-parameter in POST method")
       response = UserMainMethods.post_user_method(UserApiData.url_ip_lookup, UserApiData.user_key, UserApiData.ip_checker)
       response_ip = response["ip"]
       print(f"Response IP is {response_ip}. User external IP is {UserApiData.external_IP}")
       assert  response_ip == UserApiData.external_IP, "Wrong response IP"
       print("Test passed")



