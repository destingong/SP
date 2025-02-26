import numpy as np
import pandas as pd

def get_url(search_term, date):
  import http.client, urllib.parse

  params = urllib.parse.urlencode({
      'api_token': 'PWzpkUXdNA8AVZwWnTT90qXfhziPxxQwBBSeyOGH',
      'categories': 'business,tech',
      'limit': 3,
      'published_on': date,
      'language': 'en',
      'search': search_term,
      })

  url = '/v1/news/all?{}'.format(params)
  return url


def parse_news_json(url, date):
  import http.client, urllib.parse
  conn = http.client.HTTPSConnection('api.thenewsapi.com')
  conn.request('GET', url)
  res = conn.getresponse()
  data = res.read()
  print(data[:100])
  
  import json
  try:
    data_text = data.decode('utf-8')
    data_jsonl = json.loads(data_text)['data']

    titles = [i['title'] for i in data_jsonl]
    descriptions = [i['description'] for i in data_jsonl]
    snip = [i['snippet'] for i in data_jsonl]
    content = titles + descriptions + snip
    content_str = '; '.join(x for x in content)
  
    news_json = {'date': date, 'content': content_str}
  
  except Exception as e:
    print(e)

  return news_json

def main(args=None):
  import argparse
  parser = argparse.ArgumentParser()
  parser.add_argument('--start', type=str)
  parser.add_argument('--end', type=str)
  args = parser.parse_args(args=args)
  print("Start Date is: ", args.start)
  print("End Date is: ", args.end)

  work_dir = '/content/drive/MyDrive/MLOps/stock'
  date_range = pd.date_range(start=args.start, end=args.end)
  content_lst = []

  for date in date_range:
    date = date.strftime('%Y-%m-%d')
    url = get_url('apple+stock', date)
    content_json = parse_news_json(url, date)
    content_lst.append(content_json)
    
  fn_start = args.start.replace('-', '')
  fn_end = args.end.replace('-', '')
  filename = 'apple_news_' + fn_start + '_' + fn_end + '.jsonl'
  filepath = work_dir + '/data/' + filename

  # save news data
  import json
  with open(filepath, 'w') as f:
    for item in content_lst:
      json.dump(item, f)
      f.write('\n')
  print('File Created', filename)

if __name__ == "__main__":
    main()
