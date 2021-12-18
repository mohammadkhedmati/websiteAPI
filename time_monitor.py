# Import required packages
import json
import requests
import pandas as pd
import urllib
import time
# from google.colab import files
import io
from time import sleep

# # Define URL
# url = 'https://www.example.co.uk'

# # API request url
# result = urllib.request.urlopen('https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url={}/&strategy=mobile'
#                                 .format(url)).read().decode('UTF-8')

# print(result)

# # Convert to json format
# result_json = json.loads(result)

# print(result_json)

# with open('result.json', 'w') as outfile:
#     json.dump(result_json, outfile)

# # files.download('result.json')

API_Key = "AIzaSyDElNXqQ4sF8MJS7TUsSMrHgFZaoduZ1QU"
baseURL = "https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url="


def get_pagespeed(API_Key, page_URL, baseURL, strategy):
    response_url = baseURL+page_URL+'&key='+API_Key+'&strategy='+strategy
    response = requests.get(response_url)
    json_data = response.json()
    lighthouseResult = json_data["lighthouseResult"]
    categories = lighthouseResult["categories"]
    performance = categories["performance"]
    score = performance["score"]
    return (score*100)
    sleep(1)

# myFile = open('url_list.csv','r')
# outputFile = open('results/pagespeed_results.csv', 'w', newline='')
# outputWriter = csv.writer(outputFile)
# reader = csv.reader(myFile)
# outputWriter.writerow(["URL","Desktop Pagespeed","Mobile Pagespeed"])
# for row in reader:
#     url = row[1]
#     if url == "URL":
#         pass
#     else:
#         try:
#             desktop_pagespeed = get_pagespeed(API_Key, url, baseURL, "desktop")
#             mobile_pagespeed = get_pagespeed(API_Key, url, baseURL, "mobile")
#             print (url, desktop_pagespeed, mobile_pagespeed)
#             outputWriter.writerow([url,desktop_pagespeed,mobile_pagespeed])
#         except:
#             outputWriter.writerow([url, "Error", "Error"])
#             print('ERROR WITH URL: ', url)
# myFile.close()
# outputFile.close()


desktop_pagespeed = get_pagespeed(API_Key, 'digikala.com', baseURL, "desktop")
mobile_pagespeed = get_pagespeed(API_Key, 'digikala.com', baseURL, "mobile")
print(desktop_pagespeed, mobile_pagespeed)
