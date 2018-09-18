etag_list = []
key_list=[]
youtube_data = {
  "kind": "youtube#searchListResponse",
  "etag": "\"m2yskBQFythfE4irbTIeOgYYfBU/PaiEDiVxOyCWelLPuuwa9LKz3Gk\"",
  "nextPageToken": "CAUQAA",
  "regionCode": "KE",
  "pageInfo": {
    "totalResults": 4249,
    "resultsPerPage": 5
  },
  "items": [
    {
      "kind": "youtube#searchResult",
      "etag": "\"m2yskBQFythfE4irbTIeOgYYfBU/QpOIr3QKlV5EUlzfFcVvDiJT0hw\"",
      "id": {
        "kind": "youtube#channel",
        "channelId": "UCJowOS1R0FnhipXVqEnYU1A"
      }
    },
    {
      "kind": "youtube#searchResult",
      "etag": "\"m2yskBQFythfE4irbTIeOgYYfBU/AWutzVOt_5p1iLVifyBdfoSTf9E\"",
      "id": {
        "kind": "youtube#video",
        "videoId": "Eqa2nAAhHN0"
      }
    },
    {
      "kind": "youtube#searchResult",
      "etag": "\"m2yskBQFythfE4irbTIeOgYYfBU/2dIR9BTfr7QphpBuY3hPU-h5u-4\"",
      "id": {
        "kind": "youtube#video",
        "videoId": "IirngItQuVs"
      }
    }
  ]
}

print((youtube_data["items"][0]['id']['channelId']))
print(youtube_data["items"])
list_etag = []
for i in range(len(youtube_data["items"])):
    if youtube_data["items"][i]['id']['kind'] == 'youtube#video':
        list_etag.append(youtube_data["items"][i]['etag'])
print(list_etag)
print(list(youtube_data))

for key in youtube_data.keys():
  key_list.append(key)
  if key == 'etag':
    etag_list.append(youtube_data[key])
  if type(youtube_data[key]) == list:
    for i in range(len(youtube_data[key])):
      if type(youtube_data[key][i]) == dict:
        for key1 in youtube_data[key][i].keys():
          key_list.append(key1)
          if key1 == 'etag':
            etag_list.append(youtube_data[key][i][key1])

  if type(youtube_data[key]) == dict:
        for key2 in youtube_data[key].keys():
                key_list.append(key2)
                if key2 == 'etag':
                        etag_list.append(youtube_data[key][key2])



print(etag_list)
print(key_list)

print(youtube_data.keys())