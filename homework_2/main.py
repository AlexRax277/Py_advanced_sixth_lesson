import requests


Token = ''


class YandexDisk:

    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def create_folder(self, folder_name):
        url = 'https://cloud-api.yandex.net/v1/disk/resources'
        headers = self.get_headers()
        params = {"path": folder_name}
        response = requests.put(url, headers=headers, params=params)
        return response.status_code


if __name__ == '__main__':
    ya = YandexDisk(token=Token)
    print(ya.create_folder(folder_name='test_API_ya'))
    