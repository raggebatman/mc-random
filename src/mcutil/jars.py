from mcutil.parser import Options

import urllib.request
import json

MANIFEST_URL = "https://launchermeta.mojang.com/mc/game/version_manifest.json"

def _load_json_from_url(url: str) -> dict:
    with urllib.request.urlopen(url) as res:
        return json.load(res)


class Jar:
    def __init__(self, url: str) -> None:
        self._data = _load_json_from_url(url)
        self.version = self._data["assetIndex"]["id"]
        self.type = self._data["type"]
        self.url = self._data["downloads"]["client"]["url"]

    def open(self):
        return urllib.request.urlopen(self.url)

class Manifest:
    def __init__(self, url: str = MANIFEST_URL) -> None:
        self._data = _load_json_from_url(url)
    
    def fetch_version(self, version_string: str) -> Jar:
        if version_string == "latest":
            return self.fetch_version(self._data["latest"]["release"])

        for version in self._data["versions"]:
            if version["id"] == version_string:
                return Jar(version["url"])

        raise Exception(f"Version '{version_string}' could not be found")