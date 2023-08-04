class UserApiData:
    base_url = "https://www.weatherapi.com/"
    url_for_correct_response = "http://api.weatherapi.com/v1/current.json"
    user_key = {"key": "4f3ebd87d32d4d01984122314230408"}
    q_parameter = {"q": "London", "lang": "eng"}    # It's necessary param for work with this API