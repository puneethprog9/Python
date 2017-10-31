import progressbar
import requests
file_url = 'http://google.com/'
r = requests.get(file_url)
size = int(r.headers['Content-Length'].strip())
self.bytes = 0
widgets = [name, ": ", Bar(marker="|", left="[", right=" "),
    Percentage(), " ",  FileTransferSpeed(), "] ",
    self,
    " of {0}MB".format(str(round(size / 1024 / 1024, 2))[:4])]
pbar = ProgressBar(widgets=widgets, maxval=size).start()
file = []
for buf in r.iter_content(1024):
    if buf:
        file.append(buf)
        self.bytes += len(buf)
        pbar.update(self.bytes)
pbar.finish()
