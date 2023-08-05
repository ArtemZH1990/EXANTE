# API testing. Site: Weather API. 
"https://www.weatherapi.com/"

Use my user_key = "4f3ebd87d32d4d01984122314230408" as one of necessary UserData parameter to work with API or you'll can pass authorization by yourself
# For allure report:
- Download repos
- Copy absolute downloaded file's path and paste it in CMD(for Windows)
- Use "allure serve test_results" in command line
- Wait allure report generation

# For testing:
- Use "python -m pytest -s -v tests.py" in ...\EXANTE_PROJ\APITests directory for your Terminal
