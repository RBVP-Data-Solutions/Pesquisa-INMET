import requests, zipfile, io
r = requests.get('https://bdmep.inmet.gov.br/$2a$10$mwzyjeScvWM7EvtZ3Z1ZDezZWIZTzRcbdMNULILAmfFQeNQD07LXe.zip')
z = zipfile.ZipFile(io.BytesIO(r.content))
z.extractall("/home/rodrigo/Dev")
