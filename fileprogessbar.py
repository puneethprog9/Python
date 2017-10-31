import progressbar
import requests

url = "http://google.com/"


def download_file(url):
    local_filename = 'test.html'
    r = requests.get(url, stream=True)
    f = open(local_filename, 'wb')
    file_size = int(r.headers['Content-Length'])
    chunk = 1
    print(file_size)
    num_bars = file_size / chunk
    bar =  progressbar.ProgressBar(maxval=num_bars).start()
    i = 0
    with open(local_filename,'wb') as fd:
     for chunk in r.iter_content(chunk_size=128):
        fd.write(chunk)
        bar.update(i)
        i+=1
     fd.close()
    return

download_file(url)

