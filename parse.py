import urllib.request

def split_data(url):
    data_list = []
    with urllib.request.urlopen("https://raw.githubusercontent.com/elastic/examples/master/Common%20Data%20Formats/nginx_logs/nginx_logs") as resp:
        html = resp.read().decode("utf-8")

        data_list.append(html)



    return data_list
   # print(html)
