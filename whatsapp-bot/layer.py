from yowsup.layers.interface import YowInterfaceLayer, ProtocolEntityCallback
from yowsup.layers.protocol_receipts.protocolentities import OutgoingReceiptProtocolEntity
from yowsup.layers.protocol_acks.protocolentities import OutgoingAckProtocolEntity
from utils import get_text_or_none
from config import joiner_tokens, leaver_tokens

def BotLayer():

  class MessageLogic(YowInterfaceLayer):

    @ProtocolEntityCallback("message")
    def onMessage(self, message):

      self.receipt(message)

      message_text = get_text_or_none(message)

      if message_text is None:
        return
      
      if any([word.lower() in message_text.lower() for word in joiner_tokens]):
        print("joining", message_text)

      if any([word.lower() in message_text.lower() for word in leaver_tokens]):
        print("leaving", message_text)

    @ProtocolEntityCallback("receipt")
    def onReceipt(self, entity):
      ack = OutgoingAckProtocolEntity(entity.getId(), "receipt", entity.getType(), entity.getFrom())
      self.toLower(ack)

    def receipt(self, message):
      receipt = OutgoingReceiptProtocolEntity(message.getId(), message.getFrom(), 'read', message.getParticipant())
      self.toLower(receipt)

  return MessageLogic