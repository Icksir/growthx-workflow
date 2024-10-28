import requests
from bs4 import BeautifulSoup
from openai import OpenAI

def get_html(website_url):
    try:
        response = requests.get(website_url)
        soup = BeautifulSoup(response.text, 'html.parser')
        return soup
    except Exception as e:
        print(f"Error fetching page: {e}")
        return None
    
def clasificador_categoria(modelo, html):

    client = OpenAI()

    completion = client.chat.completions.create(
        model=modelo,
        messages=[
            {"role": "system", "content": "You are an expert from a sales team and you want to do a prospect company research"},
            {
                "role": "user",
                "content": f"Give a concise, informative article about this prospect: {html}"
            }
        ]
    )

    return completion.choices[0].message
    
if __name__ == '__main__':
    html = get_html('https://www.newtenberg.com/')
    print(clasificador_categoria('gpt-4o-mini', html))