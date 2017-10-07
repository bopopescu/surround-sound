########### Python 3.6 #############
import http.client, urllib.request, urllib.parse, urllib.error, base64, json
import requests

###############################################
#### Update or verify the following values. ###
###############################################

def analyze_tone(text):
    username = 'df2b64b3-62e3-4bce-81b7-4d9e6a033fdc'
    password = 'Ml46ZGhmHmlJ'
    watsonUrl = 'https://gateway.watsonplatform.net/tone-analyzer/api/v3/tone?version=2017-09-21'
    headers = {"content-type": "text/plain"}
    try:
        r = requests.post(watsonUrl, auth=(username,password),headers = headers,
         data=data)
        return r.text
    except:
        return False

# Replace the subscription_key string value with your valid subscription key.
subscription_key = 'e4b9a137799440129d7ce61b414c70b2'

# Replace or verify the region.
#
# You must use the same region in your REST API call as you used to obtain your subscription keys.
# For example, if you obtained your subscription keys from the westus region, replace
# "westcentralus" in the URI below with "westus".
#
# NOTE: Free trial subscription keys are generated in the westcentralus region, so if you are using
# a free trial subscription key, you should not need to change this region.
uri_base = 'westcentralus.api.cognitive.microsoft.com'

headers = {
    # Request headers.
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': subscription_key,
}

params = urllib.parse.urlencode({
    # Request parameters. All of them are optional.
    'visualFeatures': 'Categories,Description,Color',
    'language': 'en',
})

# Replace the three dots below with the URL of a JPEG image of a celebrity.
body = "{'url':'https://moderatorsampleimages.blob.core.windows.net/samples/img_1.png'}"

try:
    # Execute the REST API call and get the response.
    conn = http.client.HTTPSConnection('westcentralus.api.cognitive.microsoft.com')
    conn.request("POST", "/vision/v1.0/analyze?%s" % params, body, headers)
    response = conn.getresponse()
    data = response.read()

    # 'data' contains the JSON data. The following formats the JSON data for display.
    parsed = json.loads(data)
    # print ("Response:")
    # print (json.dumps(parsed, sort_keys=True, indent=2))
    tags = parsed["description"]["tags"]
    stringTags = ""
    for tag in tags:
        stringTags = stringTags + " " + tag
    results = analyze_tone(stringTags)
    if results != False:
        parsed = json.loads(results)
        print(parsed["document_tone"]['tones'][0]['tone_name'])
    conn.close()

except Exception as e:
    print('Error:')
    print(e)

####################################
