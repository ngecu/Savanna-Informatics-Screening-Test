import africastalking

# TODO: Initialize Africa's Talking

africastalking.initialize(
    username='sandbox',
    api_key='8c5334a5474611cf5667f37807da6b2c3b2f8044ee252cfa3dac2aabe5c25cea'
)
PORT = 3000

sms = africastalking.SMS

class send_sms():

    def send(self):
        
        #TODO: Send message

        pass #delete this code

    def sending(self):
            # Set the numbers in international format
            recipients = ["+254707583092"]
            # Set your message
            message = "Hey AT Ninja!"
            # Set your shortCode or senderId
            sender = "XXYYZZ"
            try:
                response = self.sms.send(message, recipients, sender)
                print (response)
            except Exception as e:
                print (f'Houston, we have a problem: {e}')


send_sms().sending()