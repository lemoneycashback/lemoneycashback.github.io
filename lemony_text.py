from bs4 import BeautifulSoup
import requests

LEMONEY_URL = "https://www.lemoney.com/"
REFERRAL_URL = "https://www.lemoney.com/i/flatley?bb4e9716ca7b8f8e2a0c2d26561b0c3f"
def get_featured(soup):
    featured_html = soup.find_all(class_="l-featured--home")[0]
    for a in featured_html.find_all('a'):
        a['href'] = REFERRAL_URL
    return featured_html

def get_how_to(soup):
    for row in soup.find_all(class_="row"):
        if len(row.find_all(class_="l-how-it-works__header__title")) > 0:
            how_to_html = row
            break

    for a in how_to_html.find_all('a'):
        a['href'] = REFERRAL_URL

    return how_to_html

def get_content(url):
    r = requests.get(url)
    return r.content

def generate_content(url):
    content = get_content(url)
    soup = BeautifulSoup(content, "html.parser")
    featured_html = get_featured(soup)
    how_to_html = get_how_to(soup)
    content = str(featured_html) + str(how_to_html)
    return content

def main():
    content = generate_content(LEMONEY_URL)
    print(content)

if __name__ == '__main__':
    main()
