import os
import requests
from bs4 import BeautifulSoup
from proxycrawl.proxycrawl_api import ProxyCrawlAPI

# Define the output folder and classes
OUTPUT_FOLDER = "galaxy_dataset"
OUTPUT_CLASSES = ["spiral", "elliptical", "irregular"]

# Define the search terms and number of images for each category
MASTER_DICT = {
    "spiral galaxy": 1,
    "elliptical galaxy": 1,
    "irregular galaxy": 1
}

# Configure the Google Images URL
Google_Image = 'https://www.google.com/search?site=&tbm=isch&source=hp&biw=1873&bih=990&'

# Function to download images for a given search term


def download_images(search_term, num_images):
    print("Processing.... Search Term:", search_term)

    # Creating the query for the image
    print('Searching Images....')
    search_url = Google_Image + 'q=' + search_term
    api = ProxyCrawlAPI({'token': '2iAOu9ttQrQVvwNKX8NbEA', "timeout": 600})
    response = api.get(
        search_url, {'scroll': 'true', 'scroll_interval': '60', 'ajax_wait': 'true'})

    if response['status_code'] == 200:
        b_soup = BeautifulSoup(response['body'], 'html.parser')
        results = b_soup.findAll('img', {'class': 'rg_i Q4LuWd'})

        count = 0
        imagelinks = []  # Create array to hold image links
        for res in results:
            try:
                link = res['data-src']
                imagelinks.append(link)
                count = count + 1
                if (count % 50 == 0):
                    print(str(count) + " / " + str(num_images) + " found.")
                if (count >= num_images):
                    break

            except KeyError:
                continue
        print(f'Found {len(imagelinks)} images')
        print('Start downloading...')

        # Use requests to download the image
        for i, imagelink in enumerate(imagelinks):
            response = requests.get(imagelink)

            # Open each image link and save the file as PNG
            imagename = os.path.join(
                OUTPUT_FOLDER, search_term, search_term + "_" + str(i + 1) + ".png")
            os.makedirs(os.path.dirname(imagename), exist_ok=True)
            with open(imagename, 'wb') as file:
                file.write(response.content)

            if ((i + 1) % 50 == 0):
                print(str(i + 1) + " / " + str(num_images) + " downloaded.")

        print('Download Completed!')


# Iterate over the categories and download images
for search_term in MASTER_DICT.keys():
    download_images(search_term, MASTER_DICT[search_term])
