class NotificationManager:

    def __init__(self):
        pass

    def notify_low_price(self, prices, user_email):
        print(f'Sending to {user_email}')
        for price in prices:
            message_text = f"Lowest price! Only ${price['price']} " \
                           f"to fly from {price['cityFrom']}-{price['cityCodeFrom']} " \
                           f"to {price['cityTo']}-{price['cityCodeTo']} "
            print(message_text)