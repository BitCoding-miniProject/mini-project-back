# import model
# from case import Case
# import requests
# from bs4 import BeautifulSoup

# head_url = 'https://www.law.go.kr'

# def get_case_list(root):
#     result = []
#     for serial in root.findall('prec'):
#         title = serial.find('사건명').text
#         case_number = serial.find('사건번호').text
#         similar_case = {'?' : '?'}
#         cur_idx = 1
#         link = serial.find('판례상세링크').text
#         content = ''
#         soup = BeautifulSoup(requests.get((head_url + link)).content, 'html.parser')
#         soup2 = BeautifulSoup(requests.get(soup.find('input', {'id': 'url'})['value']).content, 'html.parser')
#         for t in soup2.find('div', {'id': 'conScroll'}).find_all('p'):
#             content += t.get_text().strip()
#         # print(f'{case_number} : {title}, {head_url + link} \n {content} \n\n\n')
#         vector = model.stringToVector(content[:1000])
#         result.append(Case(title=title.strip(),
#                         case_number=case_number,
#                         content=content,
#                         vector=vector,
#                         similar_case=similar_case,
#                         cur_idx=cur_idx,
#                         link=head_url + link))
#     return result


# #  ======== 2024.04.17 코드
# # import xml.etree.ElementTree as ET
# # import model
# # from case import Case

# # with open ('prec.xml', 'r', encoding='utf-8') as xml_file:
# #     xml_data = xml_file.read()

# # root = ET.fromstring(xml_data)


# # def get_case_list():
# #     result = []
# #     for serial in root.findall('prec'):
# #         title = serial.find('사건명').text
# #         case_number = serial.find('사건번호').text
# #         content = serial.find('판결유형').texparset
# #         vector = model.stringToVector(serial.find('사건명').text)
# #         similar_case = {'?' : '?'}
# #         cur_idx = 1
# #         link = serial.find('판례상세링크').text
# #         print(f'{case_number} : {title}')
# #         result.append(Case(title=title.strip(),
# #                         case_number=case_number,
# #                         content=content,
# #                         vector=vector,
# #                         similar_case=similar_case,
# #                         cur_idx=cur_idx,
# #                         link=link))
# #     return result

