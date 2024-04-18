import model
from models import Sentence
import requests
from bs4 import BeautifulSoup

head_url = 'https://www.law.go.kr'

def get_case_list(root):
    result = []

    for serial in root.findall('prec'):
        title = serial.find('사건명').text
        case_number = serial.find('사건번호').text
        similar_case = {'?' : '?'}
        cur_idx = 1
        link = serial.find('판례상세링크').text
        content = ''

        soup = BeautifulSoup(requests.get((head_url + link)).content, 'html.parser')
        soup2 = BeautifulSoup(requests.get(soup.find('input', {'id': 'url'})['value']).content, 'html.parser')
        
        for t in soup2.find('div', {'id': 'conScroll'}).find_all('p'):
            content += t.get_text().strip()

        vector = model.stringToVector(title)
        # vector = model.stringToVector(content[:1000])

        result.append(Sentence(title=title.strip(),
                        case_number=case_number,
                        content=content,
                        vector=vector,
                        similar_case=similar_case,
                        cur_idx=cur_idx,
                        link=head_url + link))
    return result


