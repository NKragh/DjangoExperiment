import requests

url = "https://drmusicrest.azurewebsites.net/api/records"

def get_tasks():
    resp = requests.get(url)
    str1 = []
    for record in resp.json():
        str1.append([f'{record["id"]}, {record["title"]}, {record["artist"]}, {record["duration"]}, {record["yearOfPublication"]}'])
    return str1

'''
def describe_task(task_id):
    return requests.get(_url('/tasks/{:d}/'.format(task_id)))

def add_task(summary, description=""):
    return requests.post(_url('/tasks/'), json={
        'summary': summary,
        'description': description,
        })

def task_done(task_id):
    return requests.delete(_url('/tasks/{:d}/'.format(task_id)))

def update_task(task_id, summary, description):
    url = _url('/tasks/{:d}/'.format(task_id))
    return requests.put(url, json={
        'summary': summary,
        'description': description,
        })
'''
if __name__ == '__main__':
    print(get_tasks())