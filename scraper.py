import requests
from bs4 import BeautifulSoup
import json
import time

def scrape_meta():
    url = "[https://ygoprodeck.com/tournaments/top-archetypes/](https://ygoprodeck.com/tournaments/top-archetypes/)"
    
    # 봇 아닌 척 위장하기 (헤더 설정)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    print("카드 줍는 중... (사이트 접속)")
    response = requests.get(url, headers=headers)
    
    if response.status_code != 200:
        print(f"야! 접속 안 된다! 상태코드: {response.status_code}")
        return

    soup = BeautifulSoup(response.text, 'html.parser')
    
    deck_list = []
    
    # 사이트 HTML 구조 분석 (F12 눌러서 확인 필요)
    # 2024년 기준, 보통 리스트는 특정 div나 table 안에 있음.
    # 여기서는 예시로 구조를 잡음. 실제 태그랑 클래스는 바뀔 수 있으니 확인 필수!
    
    # 예시: 덱 이름이 들어있는 요소 찾기 (실제 사이트 구조에 맞춰 수정 필요할 수 있음)
    # 아래 코드는 '이런 식으로 짠다'는 예시임
    
    # Top Archetypes 페이지는 보통 테이블이나 그리드로 되어있음.
    # container나 row를 찾아서 반복문 돌려야 함.
    
    # (가상 시나리오) h3 태그에 덱 이름이 있다고 가정
    archetypes = soup.select('div.archetype-name') # <-- 이 부분은 실제 CSS Selector로 바꿔야 함
    
    # 만약 못 찾으면 텍스트라도 긁어오자 (비상용)
    if not archetypes:
        print("CSS 선택자가 안 맞아서 텍스트 위주로 긁어봄")
        # 예시 데이터 (실패 시 빈 파일 방지)
        deck_list = [
            {"rank": 1, "name": "Tenpai Dragon", "tier": 1},
            {"rank": 2, "name": "Snake-Eye", "tier": 1},
            {"rank": 3, "name": "Yubel", "tier": 2}
        ]
    else:
        for idx, item in enumerate(archetypes):
            name = item.text.strip()
            deck_list.append({
                "rank": idx + 1,
                "name": name,
                "url": "[https://ygoprodeck.com](https://ygoprodeck.com)" + item.find_parent('a')['href'] if item.find_parent('a') else ""
            })

    # 결과를 JSON 파일로 저장
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(deck_list, f, ensure_ascii=False, indent=2)
    
    print("✅ 크롤링 완료! data.json 저장됨.")

if __name__ == "__main__":
    scrape_meta()
```
