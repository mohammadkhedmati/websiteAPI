import whois
import requests
import re
from bs4 import BeautifulSoup
import urllib
from requests_html import HTMLSession
import urllib.request
from html_to_etree import parse_html_bytes
from extract_social_media import find_links_tree

import json

def google_api(url):
    # Define URL  
    url = url

    # API request url
    result = urllib.request.urlopen('https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url={}/&strategy=mobile'\
    .format(url)).read().decode('UTF-8')
    print(result)

    # Convert to json format
    result_json = json.loads(result)

    print(result_json)
    return result


def AllInfo(url):
    info = {}
    info["domain age"] = DomainAge(url)
    info["alexa rank"] = AlexaRank(url)
    info["bounce rate"] = BounceRate(url)
    info["indexed page"] = IndexedPage(url)
    info["page size"] = PageSize(url)
    info["social media links"] = SocialMedia(url)

    return info


def DomainAge(url):

    domain = url.split("//")[-1].split("/")[0].split('?')[0]
    w = whois.whois(domain)
    return w.creation_date


def AlexaRank(url):
    alexa_base_url = "https://www.alexa.com/siteinfo/"
    url.lower()
    domain = url.split("//")[-1].split("/")[0].split('?')[0]
    url_rank = alexa_base_url+domain

    # request formatted url for rank
    page = requests.get(url_rank)
    soup = BeautifulSoup(page.content, 'html.parser')

    # get country rank text in a list
    country_rank = soup.find_all('div', id='CountryRank')

    # select data with class='rank-global' and class ='data'
    global_rank = soup.select('.rank-global .data')

    rank = {}
    # global rank:
    try:
        match = re.search(r'[\d,]+', global_rank[0].text.strip())
        rank['global rank'] = match.group()

    except:
        e = "no global rank"
        return e

    # country rank:
    try:
        temp_ranks_list = country_rank[0].text.strip().split("\n")
        # print(temp_ranks_list)
        # rank_list=[]
        # for rank in temp_ranks_list:
        #     if rank!='' or rank!='#':
        #         rank_list.append(rank)
        rank['country rank'] = temp_ranks_list
    except:
        e = "no country rank"
        return e

    return rank


def BounceRate(url):

    alexa_base_url = "https://www.alexa.com/siteinfo/"
    url.lower()
    domain = url.split("//")[-1].split("/")[0].split('?')[0]
    url_rank = alexa_base_url+domain
    response = requests.get(url_rank)
    soup = BeautifulSoup(response.text, 'html.parser')

    engagement_div = soup.find("section", {"class": "engagement"})
    engagement_metrics = engagement_div.find_all("p", {"class": "data"})
    metrics_text = [metric.text for metric in engagement_metrics]

    pageviews = metrics_text[0].split(' ')
    time_on_site = metrics_text[1].split(' ')
    bounce_rate = metrics_text[2].split(' ')

    engagement_dict = {
        'pageviews': {
            'value': None,
            'delta': None
        },
        'time_on_site': {
            'value': None,
            'delta': None
        },
        'bounce_rate': {
            'value': None,
            'delta': None
        }
    }

    for l in [pageviews, time_on_site, bounce_rate]:
        for i in l:
            if '.' in i:
                if l == pageviews:
                    if engagement_dict['pageviews']['value']:
                        engagement_dict['pageviews']['delta'] = i
                    else:
                        engagement_dict['pageviews']['value'] = i

                if l == time_on_site:
                    if engagement_dict['time_on_site']['value']:
                        engagement_dict['time_on_site']['delta'] = i
                    else:
                        engagement_dict['time_on_site']['value'] = i

                if l == bounce_rate:
                    if engagement_dict['bounce_rate']['value']:
                        engagement_dict['bounce_rate']['delta'] = i
                    else:
                        engagement_dict['bounce_rate']['value'] = i

    return engagement_dict


def IndexedPage(indexurl):

    def get_source(url):

        try:
            session = HTMLSession()
            response = session.get(url)
            return response

        except requests.exceptions.RequestException as e:
            print(e)

    def get_results(url):

        query = urllib.parse.quote_plus(url)
        response = get_source(
            "https://www.google.co.uk/search?q=site%3A" + url)

        return response

    def parse_results(response):
        string = response.html.find("#result-stats", first=True).text
        indexed = int(string.split(' ')[1].replace(',', ''))
        return indexed

    def count_indexed_pages(url):
        response = get_results(url)
        return parse_results(response)

    indexed_pages = count_indexed_pages(indexurl)
    return indexed_pages


def PageSize(url):

    r = urllib.request.urlopen(url)
    page_size = len(r.read())
    return page_size


def SocialMedia(url):

    resp = requests.get(url)
    tree = parse_html_bytes(resp.content, resp.headers.get('content-type'))

    links = list(find_links_tree(tree))
    return links
