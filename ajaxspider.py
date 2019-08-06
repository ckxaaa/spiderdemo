import json
import requests
import string
html = 'http://example.webscraping.com/places/ajax/search.json?&search_term={}&page_size=10&page=0';

countries = set();

for letter in string.ascii_lowercase:
    page = 0;
    while True:
        html = html.format(letter,page);
        try:
            request = requests.get(html);
            print(request.text)
            j = json.loads(request.text);
        except ValueError as e:
            print(e);
            j = None;
        else:
            for record  in j['records']:
                countries.add(record['country'])
        page +=1;
        if j is None or page >= j['num_pages']:
            break

open('countries.txt','w').write('\n'.join(sorted(countries)))