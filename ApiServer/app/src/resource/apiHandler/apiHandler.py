import os
import msal

class apiHandler():
    TENANT_ID = os.getenv('TENANT_ID')
    CLIENT_ID = os.getenv('CLIENT_ID')
    CLIENT_CREDENTIAL = os.getenv('MY_MICROSOFT_SECRET_VALUE')
    AUTHORITY = f'https://login.microsoftonline.com/{TENANT_ID}'

    def __init__(self):
        self.SCOPE = self._getScopeEnviron()
        self.APP = self._setApp()
        self.ACCESSTOKEN = self._setAccessToken()
    
    def _getScopeEnviron(self):
        allScope : str = os.getenv('SCOPE')
        if ('|' in allScope):
            return allScope.split('|')
        else:
            return allScope
    
    def _setApp(self):
        return msal.ConfidentialClientApplication(
            self.CLIENT_ID, 
            authority=self.AUTHORITY, 
            client_credential=self.CLIENT_CREDENTIAL
        )
    
    def _setAccessToken(self):
        result = self.APP.acquire_token_silent(
            scopes = [
                self.SCOPE
            ], 
            account=None
        )
        if not result: 
            result = self.APP.acquire_token_for_client(
                scopes = [
                    self.SCOPE
                ],
            )
        if "access_token" in result:
            return (result["access_token"])
        else:
            return None
    
    def getAccessToken(self):
        return self.ACCESSTOKEN