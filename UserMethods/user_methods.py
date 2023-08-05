import whatismyip
import allure
import requests


class UserMainMethods:
    @classmethod
    def ip_getter(cls):
        with allure.step("Get user external IP"):
            user_ip = whatismyip.whatismyip()
            return user_ip

    @classmethod
    def post_user_method(cls, link, key=None, q_param=None):
        with allure.step("User POST request"):
            response = requests.post(link, headers=key, params=q_param)
            response_body = response.json()
            return response_body

    @classmethod
    def get_status_user_method_for_base_url(cls, link, key=None):
        with allure.step("User GET request"):
            response = requests.get(link)
            return response.status_code

    @classmethod
    def get_status_for_post_request_with_necessary_parameters(cls, link, key, q_param):
        with allure.step("User POST request with params"):
            response = requests.post(link, headers=key, params=q_param)
            return response.status_code
