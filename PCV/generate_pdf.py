import os
from PIL import Image, ImageDraw, ImageFont

# Page settings: A4 Landscape at 200 DPI
W, H = 2338, 1654
FONT_PATH = '/System/Library/Fonts/AppleSDGothicNeo.ttc'

def get_font(size, weight=16): # 16: Heavy, 14: ExtraBold, 6: Bold, 4: SemiBold, 0: Regular
    return ImageFont.truetype(FONT_PATH, size, index=weight)

def draw_hud(draw, title="PROJECT COURT VISION (SUWON 2026)"):
    # Top HUD Bar
    draw.rectangle([(0, 0), (W, 70)], fill=(8, 9, 11))
    draw.line([(0, 70), (W, 70)], fill=(35, 39, 50), width=2)
    
    # REC Badge
    draw.rectangle([(40, 18), (140, 52)], fill=(40, 15, 20), outline=(255, 51, 68), width=2)
    draw.ellipse([(52, 29), (64, 41)], fill=(255, 51, 68))
    draw.text((72, 23), "REC", font=get_font(20, 16), fill=(255, 51, 68))
    
    # Meta
    f_meta = get_font(18, 4)
    draw.text((170, 24), "FPS: 24.00    SHUTTER: 180°    RES: 4K UHD (9:16)    TC: 00:00:10:00", font=f_meta, fill=(160, 170, 185))
    
    # Right Title
    f_hud_title = get_font(20, 14)
    draw.text((W - 540, 22), title, font=f_hud_title, fill=(255, 148, 77))

# ----------------- PAGE 1: COVER & MASTER BOARD -----------------
def create_page1():
    img = Image.new('RGB', (W, H), (12, 13, 16))
    draw = ImageDraw.Draw(img)
    draw_hud(draw)
    
    # Header area
    draw.text((60, 95), "OFFICIAL TEASER STORYBOARD DECK", font=get_font(18, 16), fill=(255, 107, 0))
    draw.text((60, 125), "프로젝트 코트비전 (PROJECT COURT VISION) 2026", font=get_font(44, 16), fill=(240, 243, 248))
    draw.text((60, 180), "\"우리의 코트는 계속 넓어진다.\"", font=get_font(26, 14), fill=(255, 148, 77))
    draw.text((60, 218), "2026 제1회 경기남부 여성 아마추어 농구 리그 공식 8컷 마스터 콘티북 (인스타그램 릴스 / 유튜브 쇼츠 티저)", font=get_font(18, 0), fill=(160, 170, 185))
    
    # Master Board Image (Target size: width ~ 2218, height ~ 1238)
    board_src = Image.open('/Users/hnky/agyspace/PCV/assets/court_vision_full_detailed_board.jpg')
    bw, bh = 2218, 1238
    board_resized = board_src.resize((bw, bh), Image.Resampling.LANCZOS)
    
    # Sleek outline
    draw.rectangle([(58, 258), (58 + bw + 3, 258 + bh + 3)], outline=(255, 107, 0), width=3)
    img.paste(board_resized, (60, 260))
    
    # Footer info
    f_foot = get_font(16, 4)
    draw.text((60, 1530), "• 러닝타임: 00:00:10:00 (8컷 인과관계 완급조절)   • 화면비: 9:16 Vertical   • 타겟 플랫폼: Instagram Reels / Shorts   • 프로덕션: PCV 2026 Production Team", font=f_foot, fill=(140, 150, 165))
    draw.text((W - 220, 1530), "PAGE 01 / 04", font=get_font(16, 14), fill=(255, 148, 77))
    
    return img

# Helper to draw 2x2 grid page
def draw_2x2_page(page_num, part_tag, part_title, cuts, hud_title):
    img = Image.new('RGB', (W, H), (12, 13, 16))
    draw = ImageDraw.Draw(img)
    draw_hud(draw, hud_title)
    
    # Header
    draw.text((60, 95), part_tag, font=get_font(18, 16), fill=(255, 107, 0))
    draw.text((60, 125), part_title, font=get_font(36, 16), fill=(240, 243, 248))
    
    # 2x2 Grid Coordinates
    # Col 1: 60, Col 2: 1195 (width 1083)
    # Row 1: 185, Row 2: 835 (height 630)
    card_w = 1083
    card_h = 630
    positions = [
        (60, 185),
        (1195, 185),
        (60, 840),
        (1195, 840)
    ]
    
    for (cut_num, title, timing, cam, act, snd, trans, prompt), (cx, cy) in zip(cuts, positions):
        # Card background & border
        draw.rectangle([(cx, cy), (cx + card_w, cy + card_h)], fill=(20, 22, 27), outline=(43, 48, 60), width=2)
        
        # Header bar
        draw.rectangle([(cx, cy), (cx + card_w, cy + 54)], fill=(28, 31, 38))
        draw.text((cx + 20, cy + 14), f"[컷 {cut_num}]  {title}", font=get_font(22, 16), fill=(240, 243, 248))
        
        # Timing badge
        draw.rectangle([(cx + card_w - 150, cy + 12), (cx + card_w - 20, cy + 42)], fill=(40, 20, 10), outline=(255, 107, 0), width=1)
        draw.text((cx + card_w - 138, cy + 16), timing, font=get_font(16, 14), fill=(255, 148, 77))
        
        # Body split: Left = Image + AI Prompt, Right = Director Specs
        left_w = 540
        right_x = cx + left_w + 35
        right_w = card_w - left_w - 55
        
        # 1. Left Side: Panel Image
        panel_img = Image.open(f'/Users/hnky/agyspace/PCV/assets/cut{cut_num}_panel.jpg')
        # Panel size: 520 x 292 (16:9)
        pw, ph = 520, 292
        p_resized = panel_img.resize((pw, ph), Image.Resampling.LANCZOS)
        img.paste(p_resized, (cx + 20, cy + 70))
        draw.rectangle([(cx + 19, cy + 69), (cx + 20 + pw, cy + 70 + ph)], outline=(70, 75, 90), width=1)
        
        # 2. Left Side: AI Video Prompt Box under Image
        prompt_y = cy + 70 + ph + 16
        draw.rectangle([(cx + 20, prompt_y), (cx + 20 + pw, cy + card_h - 18)], fill=(13, 14, 18), outline=(50, 55, 70), width=1)
        draw.text((cx + 32, prompt_y + 12), "AI VIDEO PROMPT (Gemini Omni / Veo / Runway):", font=get_font(13, 14), fill=(255, 107, 0))
        
        # Prompt wrap
        f_pr = get_font(13, 0)
        p_lines = []
        p_words = prompt.split(' ')
        cur_p = ""
        for pw_item in p_words:
            if len(cur_p + " " + pw_item) < 58:
                cur_p += (" " if cur_p else "") + pw_item
            else:
                p_lines.append(cur_p)
                cur_p = pw_item
        if cur_p: p_lines.append(cur_p)
        
        py_offset = prompt_y + 36
        for pl in p_lines[:8]:
            draw.text((cx + 32, py_offset), pl, font=f_pr, fill=(175, 185, 200))
            py_offset += 20
            
        # 3. Right Side: Director's Specs
        ry = cy + 76
        
        # Field 1: Camera
        draw.text((right_x, ry), "📷 카메라 & 렌즈", font=get_font(16, 14), fill=(255, 148, 77))
        draw.text((right_x, ry + 26), cam, font=get_font(17, 6), fill=(235, 240, 250))
        ry += 76
        
        # Field 2: Action Direction
        draw.text((right_x, ry), "🎬 액션 연출 지시", font=get_font(16, 14), fill=(255, 148, 77))
        # wrap action
        f_act = get_font(17, 6)
        act_lines = []
        words = act.split(' ')
        cur = ""
        for w in words:
            if len(cur + " " + w) < 26:
                cur += (" " if cur else "") + w
            else:
                act_lines.append(cur)
                cur = w
        if cur: act_lines.append(cur)
        for al in act_lines[:4]:
            draw.text((right_x, ry + 26), al, font=f_act, fill=(255, 220, 160))
            ry += 26
        ry += 45
        
        # Field 3: Sound Foley
        draw.text((right_x, ry), "🔊 사운드 폴리 (Foley)", font=get_font(16, 14), fill=(255, 148, 77))
        draw.text((right_x, ry + 26), snd, font=get_font(17, 6), fill=(245, 245, 245))
        ry += 76
        
        # Field 4: Transition / Key Point
        draw.text((right_x, ry), "⚡ 트랜지션 & 포인트", font=get_font(16, 14), fill=(255, 148, 77))
        # wrap transition
        f_tr = get_font(16, 4)
        tr_lines = []
        tr_words = trans.split(' ')
        cur_t = ""
        for tw in tr_words:
            if len(cur_t + " " + tw) < 28:
                cur_t += (" " if cur_t else "") + tw
            else:
                tr_lines.append(cur_t)
                cur_t = tw
        if cur_t: tr_lines.append(cur_t)
        for tl in tr_lines[:3]:
            draw.text((right_x, ry + 26), tl, font=f_tr, fill=(185, 195, 210))
            ry += 24

    draw.text((W - 220, 1530), f"PAGE 0{page_num} / 04", font=get_font(16, 14), fill=(255, 148, 77))
    return img

def create_page2():
    cuts = [
        (1, "개구리+농구공 키링 손가락 툭툭!", "0.0s ~ 1.2s",
         "익스트림 클로즈업 (ECU 85mm Macro f/1.8)",
         "가방에 걸린 초록 개구리+미니 농구공 키링을 검지손가락으로 툭! 툭! 장난스럽게 때리고 튕기기",
         "찰랑- 톡! 톡! (가벼운 쇠소리 & 타격음)",
         "미니 농구공을 렌즈 정면으로 툭 튕기며 순간 암전!",
         "Extreme close-up macro of a gym backpack with a green frog plush & mini orange basketball keychain. An athletic woman's index finger playfully taps the mini basketball twice, making both charms swing and collide playfully. Crisp lighting, cinematic 85mm macro lens, 4K."),
        
        (2, "진짜 농구공 쿵! 매치컷", "1.2s ~ 2.4s",
         "지면 밀착 로우앵글 (Low-Angle Floor 24mm)",
         "암전이 걷히며 미니 공이 바닥에 닿는 순간 진짜 가죽 농구공으로 변신(Match-Cut)하여 바닥 쾅!",
         "쾅! (심장을 강타하는 808 베이스 비트 드랍)",
         "코트 바닥에 퍼지는 충격파 파티클과 바운스",
         "Floor-level low angle match-cut shot. The mini ball transitions seamlessly into a real full-sized official orange leather basketball slamming down hard onto the hardwood court with heavy bass shockwave vibration and dust particles, cinematic 4K."),
        
        (3, "1대1 수비 돌파 (백뷰)", "2.4s ~ 3.6s",
         "Dynamic Back View (선수 등 뒤 추적 샷)",
         "포니테일 머리칼이 날리는 주인공이 견고한 상대 여성 수비수를 페이크와 폭풍 크로스오버로 제치며 파고듦",
         "촥! 촥! (바람 가르는 드리블음 & 슈즈 스텝)",
         "수비수의 타이밍을 완벽하게 뺏는 페이크 돌파",
         "Dynamic back view follow shot of a female basketball player with a high ponytail sprinting forward, performing a sharp ankle-breaking crossover dribble past a female defender in defensive stance. Energetic camera tracking, intense focus, 4K."),
        
        (4, "스텝백 급제동 접지음", "3.6s ~ 4.8s",
         "농구화 접지 클로즈업 (Macro 120fps 슬로우)",
         "슛 공간 확보를 위해 순간적으로 뒤로 빠지는 스텝백 제동! 농구화 밑창이 코트 바닥을 짓이기며 급정지",
         "끼이익-! (가슴 찌릿한 스니커즈 접지 마찰음)",
         "코트 우드 바닥과 고무 밑창 사이의 강력한 마찰",
         "Extreme close-up macro on the bottom sole of a modern basketball sneaker executing an aggressive step-back brake on the hardwood floor. Rubber outsole gripping with high friction squeak, cinematic slow motion.")
    ]
    return draw_2x2_page(2, "PART 1: THE SPARK & BREAKTHROUGH", "컷 1 ~ 컷 4 상세 연출 지시서 & AI 비디오 프롬프트", cuts, "PROJECT COURT VISION - SCENE BREAKDOWN (PART 1)")

def create_page3():
    cuts = [
        (5, "수원화성 네온 & 스페이싱", "4.8s ~ 6.0s",
         "하이앵글 풀코트 (Bird's Eye / High Angle)",
         "발끝 충격파로 바닥에 수원화성 성곽 네온 라인이 켜지며 팀원들이 양 코너로 와르르 스페이싱",
         "위이잉-! (웅장한 네온 가동음 & 체육관 울림)",
         "1인의 돌파에서 팀 전체의 시야 확장으로 점프!",
         "High-angle full court wide shot. As the sneaker steps back, glowing orange and neon green lines radiate outward across the court floor, illuminating the architectural outline of Suwon Hwaseong fortress ramparts. Teammates sprint outward, spacing into the corners."),
        
        (6, "정점 체공 점프슛", "6.0s ~ 7.2s",
         "Medium Back View (120fps 초슬로우모션)",
         "스텝백 공간 위로 붕 떠오른 점프슛 릴리즈, 등판에 'PROJECT COURT VISION 26' 선명 노출",
         "순간 무음 ➔ 슉- (공이 공기를 가르는 소리)",
         "가장 높은 정점에서 공을 릴리즈하는 팔로우스루",
         "Medium back view slow motion shot at 120fps. The female player elevates high into the air for a floating jump shot above the outstretched hand of a defender. Bold typography 'PROJECT COURT VISION 26' clearly visible on jersey back. Perfect wrist release."),
        
        (7, "클린샷 스위시!", "7.2s ~ 8.4s",
         "Low-Angle Rim Extreme Close-Up",
         "공이 백보드도 안 스치고 림 정중앙 통과, 순백색 그물망이 위로 촥- 뒤집히는 쾌감의 스위시",
         "솨아악-! (가장 시원하고 묵직한 그물 소리)",
         "완벽한 득점 순간의 카타르시스 극대화",
         "Low angle extreme close-up on the basketball rim. The orange basketball drops cleanly through the center of the hoop without touching the rim. Pure white nylon net snaps and flutters violently upward in slow-motion swish, satisfying motion blur."),
        
        (8, "하이파이브 환호 & 공식 타이틀", "8.4s ~ 10.0s",
         "주인공 등 뒤(Back View) & 림 주변 샷",
         "팀원들의 하이파이브 손뼉 릴레이 + 펄럭이는 벤치 타월 + 화면 중앙 공식 타이틀 쿵! 등장",
         "손뼉 촥! 촥! & 환호성 ➔ 심판 호각 삑-! ➔ 808 쿵!",
         "\"우리의 코트는 계속 넓어진다\" / 프로젝트 코트비전 2026 in 수원",
         "Back view celebration shot. Multiple teammates' hands reach into the frame from all angles, high-fiving the shooter's raised hand in rapid succession. Towels wave in celebration. Bold centered typography: '우리의 코트는 계속 넓어진다', '프로젝트 코트비전 2026 in 수원'.")
    ]
    return draw_2x2_page(3, "PART 2: EXPANSION & CELEBRATION", "컷 5 ~ 컷 8 상세 연출 지시서 & AI 비디오 프롬프트", cuts, "PROJECT COURT VISION - SCENE BREAKDOWN (PART 2)")

# ----------------- PAGE 4: PRODUCTION BIBLE & WORKFLOW -----------------
def create_page4():
    img = Image.new('RGB', (W, H), (12, 13, 16))
    draw = ImageDraw.Draw(img)
    draw_hud(draw, "PROJECT COURT VISION - PRODUCTION BIBLE & CHECKLIST")
    
    # Header
    draw.text((60, 95), "DIRECTOR'S PRODUCTION BIBLE", font=get_font(18, 16), fill=(255, 107, 0))
    draw.text((60, 125), "핵심 연출 원칙, 소품 체크리스트 & AI 비디오 제작 워크플로우", font=get_font(36, 16), fill=(240, 243, 248))
    
    # 3 Large Cards (Height: 1280, from y=190 to y=1470)
    card_w = 712
    card_gap = 28
    start_x = 60
    y = 190
    ch = 1290
    
    # Card 1: Core Directing Principles
    x1 = start_x
    draw.rectangle([(x1, y), (x1 + card_w, y + ch)], fill=(20, 22, 27), outline=(43, 48, 60), width=2)
    draw.rectangle([(x1, y), (x1 + card_w, y + 68)], fill=(28, 31, 38))
    draw.text((x1 + 24, y + 20), "핵심 연출 3대 원칙", font=get_font(26, 16), fill=(255, 148, 77))
    
    cy = y + 100
    principles = [
        ("01. 얼굴 없는 세련미 (Back-View & Silhouette)",
         "AI 영상 생성 시 발생할 수 있는 부자연스러운 얼굴 표정이나 왜곡을 100% 원천 차단하기 위해, 메인 선수를 완벽한 등 뒤(Back-View), 강렬한 포니테일 실루엣, 등판 번호 클로즈업으로 세련되게 연출합니다."),
        
        ("02. 키링과 농구공의 인과관계 매치컷 (Match-Cut)",
         "1컷의 미니 농구공 키링을 툭! 튕기는 장난스러운 일상의 액션이 2컷에서 코트 바닥을 쾅! 찍는 진짜 가죽 농구공으로 완벽하게 변신 연결되어, 보는 이에게 가슴 뛰는 808 베이스 드랍 카타르시스를 전달합니다."),
        
        ("03. 지역성과 공간의 확장 (수원화성 성곽 네온)",
         "단순한 체육관이 아니라 스텝백 접지의 충격파로 바닥에 수원화성 성곽 네온 라인이 촥 번지며, 팀원들이 양 코너로 스페이싱을 벌려 1인의 고군분투가 팀 전체의 승리로 확장되는 메시지를 시각화합니다.")
    ]
    for p_title, p_desc in principles:
        draw.text((x1 + 24, cy), p_title, font=get_font(21, 16), fill=(255, 215, 160))
        cy += 40
        words = p_desc.split(' ')
        cur = ""
        for w in words:
            if len(cur + " " + w) < 35:
                cur += (" " if cur else "") + w
            else:
                draw.text((x1 + 24, cy), cur, font=get_font(17, 0), fill=(185, 195, 210))
                cy += 28
                cur = w
        if cur:
            draw.text((x1 + 24, cy), cur, font=get_font(17, 0), fill=(185, 195, 210))
            cy += 28
        cy += 48
        
    # Card 2: Props & Branding Checklist
    x2 = start_x + card_w + card_gap
    draw.rectangle([(x2, y), (x2 + card_w, y + ch)], fill=(20, 22, 27), outline=(43, 48, 60), width=2)
    draw.rectangle([(x2, y), (x2 + card_w, y + 68)], fill=(28, 31, 38))
    draw.text((x2 + 24, y + 20), "공식 소품 & 브랜딩 체크리스트", font=get_font(26, 16), fill=(255, 148, 77))
    
    cy = y + 100
    props = [
        ("소품 1: 개구리+농구공 일체형 키링",
         "하나의 메탈 링에 초록 개구리 봉제인형과 미니 오렌지 가죽 농구공이 나란히 매달려 있어, 손가락으로 칠 때 서로 부딪히며 찰랑거리는 디테일 유지."),
        
        ("유니폼: PROJECT COURT VISION 26",
         "주인공 등판에 볼드한 화이트 폰트로 'PROJECT COURT VISION 26'을 선명하게 인쇄. 6컷 정점 체공 샷에서 리그 브랜드 아이덴티티 극대화."),
        
        ("공식 대회 타이틀 & 슬로건",
         "• 메인 공식 타이틀: 프로젝트 코트비전 2026 in 수원 (Project Court Vision 2026 in Suwon)\n• 공식 슬로건: \"우리의 코트는 계속 넓어진다\" (골드 오렌지 자막)"),
        
        ("음향 사운드 디자인 (Foley Cue)",
         "• 0.0s: 키링 찰랑- 톡! 톡!\n• 1.2s: 심장 강타 808 베이스 쿵!\n• 3.6s: 스니커즈 접지음 끼이익-!\n• 4.8s: 네온 가동음 위이잉-!\n• 7.2s: 백색 그물 찢는 스위시 솨아악-!\n• 8.4s: 하이파이브 촥! 촥! + 심판 휘슬 삑-!")
    ]
    for p_title, p_desc in props:
        draw.text((x2 + 24, cy), p_title, font=get_font(21, 16), fill=(255, 215, 160))
        cy += 40
        for line in p_desc.split('\n'):
            words = line.split(' ')
            cur = ""
            for w in words:
                if len(cur + " " + w) < 35:
                    cur += (" " if cur else "") + w
                else:
                    draw.text((x2 + 24, cy), cur, font=get_font(17, 0), fill=(185, 195, 210))
                    cy += 28
                    cur = w
            if cur:
                draw.text((x2 + 24, cy), cur, font=get_font(17, 0), fill=(185, 195, 210))
                cy += 28
        cy += 40
        
    # Card 3: AI Video Workflow & CapCut
    x3 = start_x + (card_w + card_gap) * 2
    draw.rectangle([(x3, y), (x3 + card_w, y + ch)], fill=(20, 22, 27), outline=(43, 48, 60), width=2)
    draw.rectangle([(x3, y), (x3 + card_w, y + 68)], fill=(28, 31, 38))
    draw.text((x3 + 24, y + 20), "AI 영상 제작 & 편집 워크플로우", font=get_font(26, 16), fill=(255, 148, 77))
    
    cy = y + 100
    steps = [
        ("STEP 1. 제미나이 옴니 / 비오 접속 (1분)",
         "구글 제미나이 웹(gemini.google.com) 또는 Google AI Studio 비디오 생성 모드로 접속합니다."),
        
        ("STEP 2. 콘티 이미지 첨부 + 프롬프트 복붙 (10분)",
         "본 PDF에 수록된 각 컷별 이미지(또는 cut1_keyring_tap.jpg)를 첨부하고 하단 프롬프트를 복사하여 8개 비디오 클립을 순차적으로 렌더링합니다. (탭 2~3개 동시 실행 시 5분 내 완료)"),
        
        ("STEP 3. 캡컷(CapCut) 타임라인 조립 (10분)",
         "다운로드받은 8개 클립을 모바일/PC 캡컷에 올리고, 808 베이스 쿵!(2컷)과 접지음 끼익!(4컷) 박자에 맞춰 컷편집합니다."),
        
        ("STEP 4. 사운드 믹싱 & 엔딩 자막 삽입 (5분)",
         "무료 라이브러리에서 '스니커즈 마찰음', '그물 스위시음', '하이파이브 박수'를 얹고, 8컷에 공식 슬로건 및 대회명을 얹으면 즉시 인스타 릴스 업로드 준비 완료!"),
        
        ("• 총 예상 소요 시간: 25분 ~ 30분",
         "콘티와 프롬프트가 모두 완성되어 있어, 오늘 바로 실제 릴스 영상을 완성하여 홍보를 시작할 수 있습니다.")
    ]
    for s_title, s_desc in steps:
        draw.text((x3 + 24, cy), s_title, font=get_font(21, 16), fill=(255, 148, 77) if "총 예상" in s_title else (255, 215, 160))
        cy += 40
        words = s_desc.split(' ')
        cur = ""
        for w in words:
            if len(cur + " " + w) < 35:
                cur += (" " if cur else "") + w
            else:
                draw.text((x3 + 24, cy), cur, font=get_font(17, 0), fill=(185, 195, 210))
                cy += 28
                cur = w
        if cur:
            draw.text((x3 + 24, cy), cur, font=get_font(17, 0), fill=(185, 195, 210))
            cy += 28
        cy += 40

    draw.text((W - 220, 1530), "PAGE 04 / 04", font=get_font(16, 14), fill=(255, 148, 77))
    return img

print("Generating Page 1...")
p1 = create_page1()
print("Generating Page 2 (2x2 Grid)...")
p2 = create_page2()
print("Generating Page 3 (2x2 Grid)...")
p3 = create_page3()
print("Generating Page 4...")
p4 = create_page4()

pdf_out = '/Users/hnky/agyspace/PCV/PROJECT_COURT_VISION_STORYBOARD.pdf'
print("Saving PDF...")
p1.save(pdf_out, "PDF", resolution=200.0, save_all=True, append_images=[p2, p3, p4])
print("PDF created successfully at:", pdf_out)

