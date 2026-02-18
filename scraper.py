import requests
from bs4 import BeautifulSoup
import data.json
import time

def scrape_meta():
    # URL 깔끔하게 수정
    url = "[https://ygoprodeck.com/tournaments/top-archetypes/](https://ygoprodeck.com/tournaments/top-archetypes/)"
    
    # 봇 아닌 척 위장하기 (헤더 설정)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    print("카드 줍는 중... (사이트 접속)")
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status() # 404나 500 에러 나면 바로 예외 발생
    except Exception as e:
        print(f"접속 실패: {e}")
        return

    soup = BeautifulSoup(response.text, 'html.parser')
    
    deck_list = []
    
    # 아래 선택자(selector)는 사이트 구조에 따라 바뀔 수 있음
    # F12 눌러서 실제 덱 이름이 있는 태그를 확인해야 함
    # 일단 일반적인 구조로 가정하고 작성함
    
    # 예: div 태그 중 class가 'archetype-name' 인 것 찾기 (예시임!)
    # 실제로는 사이트 가서 F12로 찍어보고 class 이름 바꿔줘야 할 수도 있음
    archetypes = soup.select('div.archetype-name') 
    
    # 만약 못 찾으면 비상용 데이터라도 넣어서 파일이 생성되게 함 (에러 방지)
    if not archetypes:
        print("경고: CSS 선택자로 요소를 못 찾음. 비상용 데이터 저장.")
        deck_list = [
            {"rank": 1, "name": "Tenpai Dragon (Fallback)", "tier": 1},
            {"rank": 2, "name": "Snake-Eye (Fallback)", "tier": 1},
            {"rank": 3, "name": "Yubel (Fallback)", "tier": 2}
        ]
    else:
        for idx, item in enumerate(archetypes):
            name = item.text.strip()
            # 링크 주소도 깔끔하게 처리
            link_tag = item.find_parent('a')
            link_url = ""
            if link_tag and link_tag.has_attr('href'):
                 link_url = "[https://ygoprodeck.com](https://ygoprodeck.com)" + link_tag['href']

            deck_list.append({
                "rank": idx + 1})
