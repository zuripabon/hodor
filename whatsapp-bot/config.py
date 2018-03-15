import json

def _decode_list(data):
  rv = []
  for item in data:
    if isinstance(item, unicode):
        item = item.encode('utf-8')
    elif isinstance(item, list):
        item = _decode_list(item)
    elif isinstance(item, dict):
        item = _decode_dict(item)
    rv.append(item)
  return rv

def _decode_dict(data):
  rv = {}
  for key, value in data.iteritems():
    if isinstance(key, unicode):
      key = key.encode('utf-8')
    if isinstance(value, unicode):
      value = value.encode('utf-8')
    elif isinstance(value, list):
      value = _decode_list(value)
    elif isinstance(value, dict):
      value = _decode_dict(value)
    rv[key] = value
  return rv

def load(path):
  with open(path) as data_file:
    return json.load(data_file, object_hook=_decode_dict)

joiner_tokens = ['joining', 'abre', 'entro', 'winter is coming']
leaver_tokens = ['leaving', 'salgo', 'me piro', 'summer is coming']
