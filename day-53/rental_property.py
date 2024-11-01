from bs4 import BeautifulSoup
import requests


class RentalProperty:

    def __init__(self):
        self.zillow_url = 'https://appbrewery.github.io/Zillow-Clone'

    def fetch_properties(self):
        response = requests.get(self.zillow_url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        href_element = soup.find_all("a", {"class", "property-card-link"})
        href_list = [element.get('href') for element in href_element]
        price_element = soup.find_all("span", {"class", "PropertyCardWrapper__StyledPriceLine"})
        price_list = [element.text.split("+")[0] for element in price_element]
        address_element = soup.find_all("address")
        address_list = [element.text.strip().replace("|", "") for element in address_element]

        return {
            'hrefs': href_list,
            'prices': price_list,
            'addresses': address_list
        }
