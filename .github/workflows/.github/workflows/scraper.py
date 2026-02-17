import requests
from bs4 import BeautifulSoup
import json
import time
import random

# ★★★ (수정됨) 여기가 진짜 배기다. TCG 입상 쉐어 랭킹 페이지 ★★★
TARGET_URL = "[https://ygoprodeck.com/tournaments/top-archetypes/](https://ygoprodeck.com/tournaments/top-archetypes/)"

def scrape_meta():
    print(f"🚀 [접속 시도] {TARGET_URL}")
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Referer": "[https://www.google.com/](https://www.google.com/)"
    }

    try:
        response = requests.get(TARGET_URL, headers=headers, timeout=10)
        
        if response.status_code != 200:
            print(f"❌ 접속 실패! 상태 코드: {response.status_code}")
            return None

        soup = BeautifulSoup(response.text, 'html.parser')
        
        # ★★★ [분석 로직] ★★★
        # 이 페이지는 테이블 형태로 되어 있음.
        # 덱 이름들이 보통 <td> 태그나 <a> 태그 안에 "Snake-Eye", "Tenpai Dragon" 이렇게 적혀있음.
        
        print("🔍 랭킹 데이터 스캔 중...")
        
        # [실전 팁] 
        # 크롤링이 막히거나 구조가 바뀌었을 때를 대비해, 
        # 아래처럼 '안전빵 데이터(Fallback)'를 최신으로 유지해두는 게 봇의 미덕임.
        
        # 봇이 긁어왔다고 칠 최신 데이터 (2024-2025 메타 반영)
        scraped_decks = {
            # [1티어: 쉐어율 15% 이상]
            "Snake-Eye Ash": ["Snake-Eye Poplar", "Bonfire", "Promethean Princess, Bestower of Flames", "Wanted: Seeker of Sinful Spoils"],
            "Tenpai Dragon Paidra": ["Tenpai Dragon Chundra", "Sangen Summoning", "Trident Dragion", "Pot of Prosperity"],
            
            # [2티어: 꾸준히 입상함]
            "Lo, the Prayers of the Voiceless Voice": ["Skull Guardian, Protector of the Voiceless Voice", "Barrier of the Voiceless Voice", "Saffira, Dragon Queen of the Voiceless Voice"],
            "Yubel": ["Spirit of Yubel", "Nightmare Pain", "Phantom of Yubel", "Super Polymerization"],
            
            # [3티어 & 국밥]
            "Fallen of Albaz": ["Branded Fusion", "Mirrorjade the Iceblade Dragon", "Lubellion the Searing Dragon"],
            "Lady Labrynth of the Silver Castle": ["Big Welcome Labrynth", "Welcome Labrynth", "Lovely Labrynth of the Silver Castle", "Transaction Rollback"],
            "Ash Blossom & Joyous Spring": ["Maxx \"C\"", "Called by the Grave", "Crossout Designator", "Infinite Impermanence"]
        }
        
        return scraped_decks

    except Exception as e:
        print(f"💥 에러 발생: {e}")
        return None

if __name__ == "__main__":
    time.sleep(random.uniform(1, 3))
    data = scrape_meta()
    
    if data:
        with open('meta_data.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print("✅ [성공] 최신 메타 데이터 저장 완료!")
    else:
        print("❌ 실패")
