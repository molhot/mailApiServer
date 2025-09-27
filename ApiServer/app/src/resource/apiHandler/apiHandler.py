import os
import msal

class apiHandler():
    TENANT_ID = os.getenv('TENANT_ID')
    CLIENT_ID = os.getenv('CLIENT_ID')
    CLIENT_CREDENTIAL = os.getenv('MY_MICROSOFT_SECRET_VALUE')
    AUTHORITY = "https://login.microsoftonline.com/common"

    def __init__(self):
        self.API_SCOPE = self._getApiScopseEnviron()
        self.SCOPE = self._getScopeEnviron()
        self.APP = self._setApp()
        self.ACCESSTOKEN = self._setAccessToken()
    
    def _getScopeEnviron(self):
        allScope : str = os.getenv('SCOPE')
        if ('|' in allScope):
            return allScope.split('|')
        else:
            return [allScope]
    
    def _getApiScopseEnviron(self):
        spiAllScope : str = os.getenv('API_SCOPE')
        if ('|' in spiAllScope):
            return spiAllScope.split('|')
        else:
            return [spiAllScope]
    
    def _setApp(self):
        return msal.ConfidentialClientApplication(
            self.CLIENT_ID,
            authority=self.AUTHORITY,
            client_credential=self.CLIENT_CREDENTIAL
        )
    
    def _setAccessToken(self):
        app = msal.PublicClientApplication(self.CLIENT_ID, authority=self.AUTHORITY)

        flow = app.initiate_device_flow(scopes=self.SCOPE)
        if "user_code" not in flow:
            raise Exception("Failed to create device flow. Check your client ID and scopes.")

        print(flow["message"])  # ここに表示されるURLとコードでサインインする

        result = app.acquire_token_by_device_flow(flow)  # ユーザーがサインイン完了まで待つ
        if "access_token" in result:
            print("Access token acquired!")
            return result["access_token"]
        else:
            print("Failed to acquire token:")
            print(result.get("error"))
            print(result.get("error_description"))
            return None
    
    def getAccessToken(self):
        return self.ACCESSTOKEN