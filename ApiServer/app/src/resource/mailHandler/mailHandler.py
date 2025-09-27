import requests
import apiHandler.apiHandler as ApiHandler
import jwt

class mailHandler():
    def __init__(self):
        mailApiHandler = ApiHandler.apiHandler()
        access_token = mailApiHandler.getAccessToken()
        decoded = jwt.decode(access_token, options={"verify_signature": False})
        print(decoded.get("roles"))
        self.headers = {
            'Authorization': f'Bearer {access_token}',
            'Accept': 'application/json'
        }
        # self.id = self._getUserId()
    
    # def _getUserId(self):
    #     endpoint = 'https://graph.microsoft.com/v1.0/users'
    #     response = requests.get(
    #         endpoint,
    #         headers=self.headers
    #     )
    #     print(response.json())
    #     print(response.json()['value'])
    #     return response.json()['value'][0]['id']
    
    def getResponse(self):
        endpoint = 'https://graph.microsoft.com/v1.0/me'
        print(endpoint)
        response = requests.get(
            endpoint,
            headers=self.headers
        )
        print(response)
        return response.json()