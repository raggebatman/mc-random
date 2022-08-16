from mcutil.jars import Manifest

# personal note because i forget lol
# pip3 freeze > requirements.txt

m = Manifest()

j = m.fetch_version("latest")

print(j.version, j.type, j.url)

# with jar.open() as res:
#     zip_obj = zipfile.ZipFile(io.BytesIO(res.read()))
#     ... now you've opened the zip-file in memory