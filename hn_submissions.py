from operator import itemgetter

import requests

url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(r.status_code)

# обработка информации
submissions_ids = r.json()
submissions_dicts = []
for submission_id in submissions_ids[:30]:
    url = f'https://hacker-news.firebaseio.com/v0/item/{submission_id}.json'
    r = requests.get(url)
    print(f"id: {submission_id}\tstatus: {r.status_code}")
    response_dict = r.json()

    # словарь для каждой статьи
    submissions_dict = {
        'title': response_dict['title'],
        'hn_link': f"https://news.ycombinator.com/item?id={submission_id}",
        'comments': response_dict['descendants'],
    }
    submissions_dicts.append(submissions_dict)

submissions_dicts = sorted(submissions_dicts, key=itemgetter('comments'), reverse=True)

for submissions_dict in submissions_dicts:
    print(f'\nTitle: {submissions_dict["title"]}')
    print(f'Discussion: {submissions_dict["hn_link"]}')
    print(f'Comments: {submissions_dict["comments"]}')