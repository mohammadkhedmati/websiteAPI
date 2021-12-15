from bs4 import BeautifulSoup  # scraper
import requests as r  # for get page information
import re  # regex
from datetime import datetime
import time

# this function get our rank


def rank(domain):
    url = "https://www.alexa.com/siteinfo/" + domain
    respone = r.get(url)  # get information from page
    soup = BeautifulSoup(respone.content, 'html.parser')
    # regional_rank = soup.select('p.small.data')
    # regional_rank = str(regional_rank[0].contents[2])
    for match in soup.find_all('span'):  # remove all span tag
        match.unwrap()
    # select any p tag with big and data class
    global_rank = soup.select('p.big.data')
    global_rank = str(global_rank[0])
    G_rank = re.findall(r"([0-9,]{1,12})", global_rank)  # find rank
    # R_rank = re.findall(r"([0-9,]{1,12})", regional_rank)  # find rank

    # return(res[0])  # return rank
    print(G_rank[0])


# org_rank = rank(domain)
# print("Your Rank is: ", org_rank)
# while True:
#     if org_rank != rank(domain):
#         myFile = open('log.txt', 'a')
#         str_write = "Your Rank was " + str(org_rank) + " but it change to: " + str(
#             rank()) + " on:" + str(datetime.now()) + "\r\n"  # write log with time and info
#         myFile.write(str(rank(domain)) + "\r\n")
#         myFile.write(str_write)
#         myFile.close()
#         org_rank = rank(domain)
#         print(org_rank)

#     time.sleep(1)
