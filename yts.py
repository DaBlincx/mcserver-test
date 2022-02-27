from youtubesearchpython import VideosSearch
import json

channelsSearch = VideosSearch('never gonna give you up', limit = 1)

vd = channelsSearch.result()["result"]