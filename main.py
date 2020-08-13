import json
import os

import fire
import requests



def sendRequests(start: int=0, end: int=100, out: str="hello.dump"):
    """
        Returns sum of a and b
        :param start: Defines the beginning ID to be displayed
        :param end : Defines the ending ID to be displayed
        :param out : Defines the fileName where the results are stored
        :return: A list of items with specific ids
    """
    for i in range(start, end+1, 1):
     allItems = []
     allItems = requests.get(f"https://jsonplaceholder.typicode.com/posts/{i}").text

     print(allItems)

     a = []
     if not os.path.isfile(out):
         a.append(allItems)
         with open(out, mode='w') as f:
             f.write(json.dumps(a, indent=2))
     else:
         with open(out) as feedsjson:
             feeds = json.load(feedsjson)

         feeds.append(allItems)
         with open(out, mode='w') as f:
             f.write(json.dumps(feeds, indent=2))


if __name__ == "__main__":
    fire.Fire({
        "get_posts": sendRequests
    })