import json
import time

# ★ 무적의 안전 모드 스크래퍼 ★
# 외부 도구(requests) 없이 내장된 데이터로 파일만 만들어내는 방식
# 이러면 설치 에러가 절대 안 남.

def generate_meta():
    print("🚀 [안전 모드] 봇이 최신 티어 족보를 생성합니다...")
    
    # 2025년 최신 티어 데이터 (여기에 형이 다 넣어놨음)
    # 나중에 티어 바뀌면 여기만 고치면 됨
    meta_data = {
        # === 1티어 (God Tier) ===
        "Snake-Eye Ash": ["Snake-Eye Poplar", "Bonfire", "Promethean Princess, Bestower of Flames", "Wanted: Seeker of Sinful Spoils"],
        "Tenpai Dragon Paidra": ["Tenpai Dragon Chundra", "Sangen Summoning", "Trident Dragion", "Pot of Prosperity"],
        "Yubel": ["Spirit of Yubel", "Nightmare Pain", "Phantom of Yubel", "Super Polymerization"],
        
        # === 2티어 (Top Tier) ===
        "Lo, the Prayers of the Voiceless Voice": ["Skull Guardian, Protector of the Voiceless Voice", "Barrier of the Voiceless Voice", "Saffira, Dragon Queen of the Voiceless Voice"],
        "Fallen of Albaz": ["Branded Fusion", "Mirrorjade the Iceblade Dragon", "Lubellion the Searing Dragon"],
        "Lady Labrynth of the Silver Castle": ["Big Welcome Labrynth", "Welcome Labrynth", "Lovely Labrynth of the Silver Castle"],
        
        # === 필수 카드 (Staples) ===
        "Ash Blossom & Joyous Spring": ["Maxx \"C\"", "Called by the Grave", "Crossout Designator"],
        "Maxx \"C\"": ["Ash Blossom & Joyous Spring", "Nibiru, the Primal Being", "Effect Veiler"]
    }
    
    return meta_data

if __name__ == "__main__":
    data = generate_meta()
    
    # JSON 파일 생성 (이게 핵심)
    with open('meta_data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    print("✅ [성공] meta_data.json 파일 생성 완료!")
