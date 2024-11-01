from rental_property import RentalProperty
from form import Form

FORM_URL = 'https://forms.gle/GWMhXrnRAyQcV2td8'
ZILLOW_URL = 'https://appbrewery.github.io/Zillow-Clone'

rental_property = RentalProperty()
properties_dict = rental_property.fetch_properties()

form = Form()
for i in range(len(properties_dict.get('hrefs'))):
    print(properties_dict.get('addresses'))
    address = properties_dict.get('addresses')[i]
    price = properties_dict.get('prices')[i]
    href = properties_dict.get('hrefs')[i]
    form.fill_form(address, price, href)

    if i == len(properties_dict.get('hrefs')) - 1:
        form.send_another_report()

form.save_to_spreed_sheet()
