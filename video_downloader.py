import pytube

link = input('Enter youtube link: ')
yt = pytube.Youtube(link)
yt.stream.first().download()
print('download done', link)