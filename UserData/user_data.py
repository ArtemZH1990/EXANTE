import whatismyip


class UserApiData:
    base_url = "https://www.weatherapi.com/"
    url_current_json = "http://api.weatherapi.com/v1/current.json"
    url_ip_lookup = "http://api.weatherapi.com/v1/ip.json "
    user_key = {"key": "4f3ebd87d32d4d01984122314230408"}
    q_parameter = {"q": "London", "lang": "eng"}    # It's necessary param for work with this API
    country_checker = {"q": "Tbilisi", "lang": "eng"}
    external_IP = whatismyip.whatismyip()
    ip_checker = {"q": external_IP}


