import re
import json

joiner_tokens = ['joining', 'hi', 'entro', 'entrar','winter is coming']
leaver_tokens = ['leaving', 'bye', 'salgo', 'salir', 'summer is coming']

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

def get_text_or_none(message):

  if not message:
    return None

  if message.getType() == "text":
    return get_text_message_body(message)

  return None

def get_text(message):

  if message.getType() == "text":
    return get_text_message_body(message)

  elif message.getType() == "media":
    return get_media_message_body(message)

  else:
    return "Unknown message type %s " % message.getType()

def get_text_message_body(message):
  return message.getBody()

def get_media_message_body(message):

  if message.getMediaType() in ("image", "audio", "video"):
    return get_downloadable_media_message_body(message)
  else:
    return "[Media Type: %s]" % message.getMediaType()

def get_downloadable_media_message_body(message):
  return "[Media Type:{media_type}, Size:{media_size}, URL:{media_url}]".format(
    media_type = message.getMediaType(),
    media_size = message.getMediaSize(),
    media_url = message.getMediaUrl()
  )