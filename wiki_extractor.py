import requests 
import json
import argparse
BASE_URL = "https://en.wikipedia.org/w/api.php"

parser = argparse.ArgumentParser()
parser.add_argument('--keyword', type=str, required=True)
parser.add_argument('--num_urls', type=int, required=True)
parser.add_argument('--output', type=str, required=True)

args = parser.parse_args()

#Tested
def get_titles(query, num_results):
    if num_results>500:
        raise ValueError("The number of results cannot exceed 500")

    params = {
            'action':'query',
            'format':'json',
            'list':'search',
            'utf8':1,
            'srsearch':query,
            'srlimit':num_results,
            'limit':num_results,
            'srinfo':'suggestion'
        }
    
    data = requests.get(BASE_URL, params=params).json()
    topics = []
    for d in data['query']['search']:
        topics.append(d['title'])
    
    return topics

def get_info(topics):
    data = []
    for title in topics:
        title_dict = {}
        params = {
        'action': 'query',
        'format': 'json',
        'titles': title,
        'prop': '|'.join(['extracts', 'info']),
        'exintro': True,
        'explaintext': True,
        'inprop':'url'
        }

        response = requests.get(BASE_URL, params=params)
        response_dict = response.json()
        page = response_dict['query']['pages']
        for k, v in page.items():
            title_dict['url'] = v['fullurl']
            title_dict['paragraph'] = v['extract']
        data.append(title_dict)
    return data

def write_json(data, output_file):
    jsonData = json.dumps(data)
    jsonfile = open(output_file, 'w')
    jsonfile.write(jsonData)
    jsonfile.close()


topics = get_titles(args.keyword, args.num_urls)
data = get_info(topics)
write_json(data, args.output)

