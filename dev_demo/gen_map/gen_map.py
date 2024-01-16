import json

filename = './bl'
target_len = 15

js = open(filename + '.json', 'r').read()
gj = json.loads(js)
output = {"type": "FeatureCollection", "features": []}


# ref: https://staedi.github.io/posts/multipolygon

def process_geojson(filename):
    js = open(filename + '.json', 'r').read()
    gj = json.loads(js)
    output = {"type": "FeatureCollection", "features": []}

    for feature in gj['features']:
        if feature['geometry'] is not None:
            if feature['geometry']['type'] == 'MultiPolygon':
                len_list = sorted([[idx, len(elem[0])] for idx, elem in enumerate(feature['geometry']['coordinates'])],
                                  key=lambda x: x[1], reverse=True)[:target_len]
                reg_len = [i[0] for i in len_list]

                for idx, poly in enumerate(feature['geometry']['coordinates']):
                    if len(feature['geometry']['coordinates']) < target_len or idx in reg_len:
                        xfeature = {"type": "Feature", "properties": feature["properties"],
                                    "geometry": {"type": "Polygon"}}
                        xfeature['geometry']['coordinates'] = poly
                        output['features'].append(xfeature)
            else:
                for idx, poly in enumerate(feature['geometry']['coordinates']):
                    xfeature = {"type": "Feature", "properties": feature["properties"], "geometry": feature["geometry"]}
                    output['features'].append(xfeature)

    open(filename + '.geojson', 'w').write(
        json.dumps(output, separators=(',', ':'), ensure_ascii=False).replace('}},', '}},\n'))


if __name__ == '__main__':
    process_geojson(filename)
