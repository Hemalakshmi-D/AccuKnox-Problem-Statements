import requests

def check_application_status(url):
    try:
        response = requests.get(url)
        # Check the HTTP status code
        if response.status_code == 200:
            return 'Application is up and running.'
        else:
            return f'Application is down. Status code: {response.status_code}'
    except requests.exceptions.RequestException as e:
        return f'Failed to connect to the application: {e}'

if __name__ == '__main__':
    # Replace 'http://example.com' with your application's URL
    url_to_check = 'http://example.com'

    result = check_application_status(url_to_check)
    print(result)

