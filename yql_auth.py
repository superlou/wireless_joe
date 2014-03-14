import os
import yql
from yql.storage import FileTokenStore
import webbrowser


class YqlAuth:
    y = None
    token = None

    def __init__(self, stored_token_name, key, secret):
        API_KEY = key
        SECRET = secret

        y = yql.ThreeLegged(API_KEY, SECRET)

        path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'cache'))
        token_store = FileTokenStore(path, secret='apples')

        stored_token = token_store.get(stored_token_name)

        if not stored_token:
            request_token, auth_url = y.get_token_and_auth_url()
            webbrowser.open(auth_url)
            verifier = raw_input("Enter the code: ")
            token = y.get_access_token(request_token, verifier)
            token_store.set(stored_token_name, token)
        else:
            token = y.check_token(stored_token)
            if token != stored_token:
                token_store.set(stored_token_name, token)

        self.y = y
        self.token = token

    def execute(self, query):
        return self.y.execute(query, token=self.token)
