import re

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