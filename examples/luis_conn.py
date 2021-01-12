# See the following tutorial
# https://docs.microsoft.com/en-us/azure/cognitive-services/luis/luis-get-started-get-intent-from-rest?pivots=programming-language-python

import requests
import json

app_id = '3d9d496d-c71a-48f7-85d8-34f321d1a15a'
pk = 'b5840b0276804c3cbe7e73269f857d16'
endpoint = 'https://westus.api.cognitive.microsoft.com/'

utterance = 'Please tell me Sir Mujtaba Haider\'s email address'
# The headers to use in this REST call.
headers = {
}

# The URL parameters to use in this REST call.
params ={
    'query': utterance,
    'timezoneOffset': '0',
    'verbose': 'true',
    'show-all-intents': 'true',
    'spellCheck': 'false',
    'staging': 'false',
    'subscription-key': pk
}

try:

    # Make the REST call.
    response = requests.get(f'{endpoint}luis/prediction/v3.0/apps/{app_id}/slots/production/predict', headers=headers, params=params)
    # Display the results on the console.
    print(json.dumps(response.json(), indent=4, sort_keys=True))
except Exception as e:
    print(e)