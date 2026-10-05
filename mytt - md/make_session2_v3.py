import os
import pptx
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE

# ==================== CONSTANTS & DESIGN SYSTEM ====================
FONT_TITLE = 'Gowun Dodum'
FONT_BODY = 'Noto Sans KR'

# Exact color hierarchy
COLOR_DARK_TEXT = RGBColor(0x3E, 0x2C, 0x21)   # #3E2C21 (제목 및 본문 메인 차콜 블랙)
COLOR_ORANGE = RGBColor(0xE7, 0x6F, 0x51)      # #E76F51 (포인트 웜 오렌지)
COLOR_MUTED = RGBColor(0x8C, 0x6A, 0x54)       # #8C6A54 (예시/보조 안내 웜그레이)
COLOR_CARD_BG = RGBColor(0xFF, 0xFD, 0xF8)     # #FFFDF8 (카드 박스 배경)
COLOR_CARD_LINE = RGBColor(0xED, 0xD8, 0xC8)   # #EDD8C8 (0.75pt 얇은 카드 테두리)
COLOR_WHITE = RGBColor(0xFF, 0xFF, 0xFF)

prs = Presentation()
prs.slide_width = Inches(13.333)
prs.slide_height = Inches(7.5)
blank_layout = prs.slide_layouts[6]

bg_img = '/Users/hnky/agyspace/slide_bg.png'
card_img = '/Users/hnky/agyspace/card_bg.png'
mission_img = '/Users/hnky/agyspace/mission_box.png'
pill_img = '/Users/hnky/agyspace/pill_box.png'

def create_slide():
    slide = prs.slides.add_slide(blank_layout)
    if os.path.exists(bg_img):
        slide.shapes.add_picture(bg_img, 0, 0, prs.slide_width, prs.slide_height)
    return slide

def add_navigator(slide, text):
    """좌상단 네비게이터: 오렌지 바 + Gowun Dodum 27pt"""
    bar = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.625), Inches(0.674), Inches(0.104), Inches(0.313))
    bar.fill.solid()
    bar.fill.fore_color.rgb = COLOR_ORANGE
    bar.line.fill.background()

    tbox = slide.shapes.add_textbox(Inches(0.867), Inches(0.625), Inches(12.0), Inches(0.454))
    tf = tbox.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
    p = tf.paragraphs[0]
    p.text = text
    p.font.name = FONT_TITLE
    p.font.size = Pt(27.0)
    p.font.bold = True
    p.font.color.rgb = COLOR_DARK_TEXT

def add_clean_box(slide, left, top, width, height, bg_color=COLOR_CARD_BG, line_color=COLOR_CARD_LINE):
    """얇고 은은한 시그니처 둥근 박스 (선 두께 0.75pt)"""
    box = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
    box.fill.solid()
    box.fill.fore_color.rgb = bg_color
    if line_color:
        box.line.color.rgb = line_color
        box.line.width = Pt(0.75)
    else:
        box.line.fill.background()
    return box

# ==================== SLIDE 1 ====================
# 1p : 소리는 off ~ Ai를 준비해주세요 ~ 챗 gpT등 박스 처리 (1회차 1p 스타일 적용)
s1 = create_slide()
# Center top title
tbox = s1.shapes.add_textbox(Inches(1.5), Inches(1.8), Inches(10.333), Inches(1.8))
tf = tbox.text_frame
tf.word_wrap = True
tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0

p0 = tf.paragraphs[0]
p0.text = "mytt 2회차 파일럿 클래스"
p0.alignment = PP_ALIGN.CENTER
p0.font.name = FONT_BODY
p0.font.size = Pt(16.5)
p0.font.bold = True
p0.font.color.rgb = COLOR_ORANGE
p0.space_after = Pt(14)

p1 = tf.add_paragraph()
p1.text = "“안녕하세요”"
p1.alignment = PP_ALIGN.CENTER
p1.font.name = FONT_TITLE
p1.font.size = Pt(43.5)
p1.font.bold = True
p1.font.color.rgb = COLOR_DARK_TEXT
p1.space_after = Pt(12)

p2 = tf.add_paragraph()
p2.text = "채팅창에 반갑게 인사 나누어 보아요"
p2.alignment = PP_ALIGN.CENTER
p2.font.name = FONT_BODY
p2.font.size = Pt(16.5)
p2.font.color.rgb = COLOR_DARK_TEXT

# Notice Box (1회차 1p와 동일한 박스)
add_clean_box(s1, Inches(1.8), Inches(4.5), Inches(9.733), Inches(1.5))
bbox = s1.shapes.add_textbox(Inches(2.0), Inches(4.65), Inches(9.333), Inches(1.2))
btf = bbox.text_frame
btf.word_wrap = True
btf.margin_left = btf.margin_top = btf.margin_right = btf.margin_bottom = 0

p3 = btf.paragraphs[0]
p3.text = "소리는 OFF / 화면은 ON 해주시면 진심으로 감사드리겠습니다… (필수 x 자유 o)"
p3.alignment = PP_ALIGN.CENTER
p3.font.name = FONT_BODY
p3.font.size = Pt(14.5)
p3.font.color.rgb = COLOR_MUTED
p3.space_after = Pt(10)

p4 = btf.add_paragraph()
p4.text = "Ai를 준비해주세요! (클로드, 제미나이, 챗GPT 등)"
p4.alignment = PP_ALIGN.CENTER
p4.font.name = FONT_BODY
p4.font.size = Pt(15.5)
p4.font.bold = True
p4.font.color.rgb = COLOR_ORANGE

# ==================== SLIDE 2 ====================
# 2p : 화면 4분할 시간영토 사진 + 딥워크 설명 텍스트 박스 얹힘
s2 = create_slide()
add_navigator(s2, "지난 시간 복습")

# 4 Quadrants layout
img_w = Inches(3.9)
img_h = Inches(2.55)
col_left = [Inches(2.4), Inches(7.0)]
row_top = [Inches(1.45), Inches(4.3)]

territory_imgs = [
    ('/Users/hnky/agyspace/territory_sea.png', col_left[0], row_top[0], "수면 (바다)"),
    ('/Users/hnky/agyspace/territory_hill.png', col_left[1], row_top[0], "고정스케줄 (언덕)"),
    ('/Users/hnky/agyspace/territory_plain.png', col_left[0], row_top[1], "휴식 (평원)"),
    ('/Users/hnky/agyspace/territory_farm.png', col_left[1], row_top[1], "일 (나의 시간농장)")
]

for img_path, left_pos, top_pos, label in territory_imgs:
    if os.path.exists(img_path):
        s2.shapes.add_picture(img_path, left_pos, top_pos, img_w, img_h)
    # subtle badge
    badge = s2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left_pos + Inches(0.15), top_pos + Inches(0.15), Inches(1.8), Inches(0.35))
    badge.fill.solid()
    badge.fill.fore_color.rgb = COLOR_CARD_BG
    badge.line.color.rgb = COLOR_CARD_LINE
    badge.line.width = Pt(0.5)
    btf = badge.text_frame
    btf.margin_left = btf.margin_top = btf.margin_right = btf.margin_bottom = 0
    bp = btf.paragraphs[0]
    bp.text = label
    bp.alignment = PP_ALIGN.CENTER
    bp.font.name = FONT_TITLE
    bp.font.size = Pt(11.5)
    bp.font.bold = True
    bp.font.color.rgb = COLOR_DARK_TEXT

# Deep Work caption box overlaid on bottom-right (나의 시간농장)
caption_box = s2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, col_left[1] + Inches(0.15), row_top[1] + Inches(1.4), Inches(3.6), Inches(1.0))
caption_box.fill.solid()
caption_box.fill.fore_color.rgb = COLOR_CARD_BG
caption_box.line.color.rgb = COLOR_ORANGE
caption_box.line.width = Pt(1.0)
c_tf = caption_box.text_frame
c_tf.word_wrap = True
c_tf.margin_left = c_tf.margin_top = c_tf.margin_right = c_tf.margin_bottom = Inches(0.08)

p_c1 = c_tf.paragraphs[0]
p_c1.text = "딥워크 (최대 4시간)"
p_c1.font.name = FONT_TITLE
p_c1.font.size = Pt(12.5)
p_c1.font.bold = True
p_c1.font.color.rgb = COLOR_ORANGE
p_c1.space_after = Pt(2)

p_c2 = c_tf.add_paragraph()
p_c2.text = "창작자, 연구가가 몰입해 결과물을 내는 시간"
p_c2.font.name = FONT_BODY
p_c2.font.size = Pt(11.0)
p_c2.font.color.rgb = COLOR_DARK_TEXT

# ==================== SLIDE 3 ====================
# 3p : 공통 피드백, 기타 피드백, 발전 약속 -> 세로 3단 박스 배치
s3 = create_slide()
add_navigator(s3, "1회차 피드백")

box_w = Inches(11.3)
box_x = Inches(1.0)

# Box 1: 공통 피드백
add_clean_box(s3, box_x, Inches(1.45), box_w, Inches(1.85))
b1 = s3.shapes.add_textbox(box_x + Inches(0.3), Inches(1.6), box_w - Inches(0.6), Inches(1.55))
tf1 = b1.text_frame
tf1.word_wrap = True
tf1.margin_left = tf1.margin_top = tf1.margin_right = tf1.margin_bottom = 0
p = tf1.paragraphs[0]
p.text = "공통"
p.font.name = FONT_TITLE
p.font.size = Pt(18.0)
p.font.bold = True
p.font.color.rgb = COLOR_ORANGE
p.space_after = Pt(8)

common_items = [
    "- 워크북에 입력할 내용이 많아 조금 부담스러웠다",
    "- 소감 나눔 시간이 조금 길었다",
    "- 워크북(이론)과 이후 활동(바이브 코딩)이 앞으로 유기적으로 연결되면 좋겠다"
]
for item in common_items:
    pi = tf1.add_paragraph()
    pi.text = item
    pi.font.name = FONT_BODY
    pi.font.size = Pt(15.0)
    pi.font.color.rgb = COLOR_DARK_TEXT
    pi.space_after = Pt(4)

# Box 2: 기타 피드백
add_clean_box(s3, box_x, Inches(3.55), box_w, Inches(1.65))
b2 = s3.shapes.add_textbox(box_x + Inches(0.3), Inches(3.7), box_w - Inches(0.6), Inches(1.35))
tf2 = b2.text_frame
tf2.word_wrap = True
tf2.margin_left = tf2.margin_top = tf2.margin_right = tf2.margin_bottom = 0
p = tf2.paragraphs[0]
p.text = "기타"
p.font.name = FONT_TITLE
p.font.size = Pt(18.0)
p.font.bold = True
p.font.color.rgb = COLOR_ORANGE
p.space_after = Pt(8)

etc_items = [
    "- 나의 상황에 맞지 않는 부분이 있어 고민되었다",
    "- 주말 루틴도 추가해보고 싶다 (업데이트 예정)"
]
for item in etc_items:
    pi = tf2.add_paragraph()
    pi.text = item
    pi.font.name = FONT_BODY
    pi.font.size = Pt(15.0)
    pi.font.color.rgb = COLOR_DARK_TEXT
    pi.space_after = Pt(4)

# Box 3: 발전 다짐 (오렌지 포인트 박스)
b3_shape = add_clean_box(s3, box_x, Inches(5.45), box_w, Inches(0.95))
b3_shape.line.color.rgb = COLOR_ORANGE
b3 = s3.shapes.add_textbox(box_x + Inches(0.3), Inches(5.65), box_w - Inches(0.6), Inches(0.6))
tf3 = b3.text_frame
tf3.word_wrap = True
tf3.margin_left = tf3.margin_top = tf3.margin_right = tf3.margin_bottom = 0
p = tf3.paragraphs[0]
p.text = "-> 더 귀기울여 듣고 발전시켜보겠습니다!"
p.alignment = PP_ALIGN.CENTER
p.font.name = FONT_TITLE
p.font.size = Pt(18.0)
p.font.bold = True
p.font.color.rgb = COLOR_DARK_TEXT

# ==================== SLIDE 4 ====================
# 4p : 좌상단 네비게이터 + 중앙정렬 제목/본문 + ex- 예시 박스 처리
s4 = create_slide()
add_navigator(s4, "<나눔>")

# Central Question & Body
qbox = s4.shapes.add_textbox(Inches(1.5), Inches(1.4), Inches(10.333), Inches(2.2))
qtf = qbox.text_frame
qtf.word_wrap = True
qtf.margin_left = qtf.margin_top = qtf.margin_right = qtf.margin_bottom = 0

qp = qtf.paragraphs[0]
qp.text = "Q. 지난 시간 이후, 어떠셨나요?"
qp.alignment = PP_ALIGN.CENTER
qp.font.name = FONT_TITLE
qp.font.size = Pt(26.0)
qp.font.bold = True
qp.font.color.rgb = COLOR_ORANGE
qp.space_after = Pt(16)

items_4p = [
    "- 일상에서 나의 시간 사용/ 시간 도둑 관찰",
    "- 어렵고 힘들었던 점",
    "등등…"
]
for it in items_4p:
    pi = qtf.add_paragraph()
    pi.text = it
    pi.alignment = PP_ALIGN.CENTER
    pi.font.name = FONT_BODY
    pi.font.size = Pt(16.0)
    pi.font.color.rgb = COLOR_DARK_TEXT
    pi.space_after = Pt(6)

# Examples Box (중앙 박스 처리)
add_clean_box(s4, Inches(2.0), Inches(3.8), Inches(9.333), Inches(2.2))
ebox = s4.shapes.add_textbox(Inches(2.3), Inches(4.0), Inches(8.733), Inches(1.8))
etf = ebox.text_frame
etf.word_wrap = True
etf.margin_left = etf.margin_top = etf.margin_right = etf.margin_bottom = 0

ep1 = etf.paragraphs[0]
ep1.text = "ex- 저는 하루 4시간 딥워크 시간을 시도해보았는데,\n      마음 먹으니 2-3시간정도 가능하더라고요!"
ep1.font.name = FONT_BODY
ep1.font.size = Pt(15.0)
ep1.font.color.rgb = COLOR_MUTED
ep1.space_after = Pt(10)

ep2 = etf.add_paragraph()
ep2.text = "ex- 저는 시간 도둑이 너무 많아 작업 시작이 어렵다는 걸 깨달았어요."
ep2.font.name = FONT_BODY
ep2.font.size = Pt(15.0)
ep2.font.color.rgb = COLOR_MUTED

# Bottom prompt
p_act = s4.shapes.add_textbox(Inches(1.5), Inches(6.25), Inches(10.333), Inches(0.5))
ptf = p_act.text_frame
ptf.word_wrap = True
ptf.margin_left = ptf.margin_top = ptf.margin_right = ptf.margin_bottom = 0
pp = ptf.paragraphs[0]
pp.text = "-> 채팅창에 경험하고 느낀 점을 한 줄 나누어보세요"
pp.alignment = PP_ALIGN.CENTER
pp.font.name = FONT_BODY
pp.font.size = Pt(16.0)
pp.font.bold = True
pp.font.color.rgb = COLOR_DARK_TEXT

# ==================== SLIDE 5 ====================
s5 = create_slide()
add_clean_box(s5, Inches(2.2), Inches(2.0), Inches(8.933), Inches(3.6))
box5 = s5.shapes.add_textbox(Inches(2.5), Inches(2.3), Inches(8.333), Inches(3.0))
tf5 = box5.text_frame
tf5.word_wrap = True
tf5.margin_left = tf5.margin_top = tf5.margin_right = tf5.margin_bottom = 0

p = tf5.paragraphs[0]
p.text = "원래 저희의 의도"
p.alignment = PP_ALIGN.CENTER
p.font.name = FONT_TITLE
p.font.size = Pt(32.0)
p.font.bold = True
p.font.color.rgb = COLOR_ORANGE
p.space_after = Pt(20)

items_5 = [
    "-> 으쌰으쌰 인증샷 올리고 다같이 자신만의 루틴을 만들어가는 모임",
    "-> ???",
    "-> 제가 더 노력하겠습니다"
]
for it in items_5:
    pi = tf5.add_paragraph()
    pi.text = it
    pi.alignment = PP_ALIGN.CENTER
    pi.font.name = FONT_BODY
    pi.font.size = Pt(16.5)
    pi.font.color.rgb = COLOR_DARK_TEXT
    pi.space_after = Pt(10)

# ==================== SLIDE 6 ====================
# 6p : 좌상단 네비게이터 + 중앙정렬 제목/본문 + ex- 예시 박스 처리
s6 = create_slide()
add_navigator(s6, "<나눔>")

# Central Question
qbox = s6.shapes.add_textbox(Inches(1.5), Inches(1.6), Inches(10.333), Inches(2.0))
qtf = qbox.text_frame
qtf.word_wrap = True
qtf.margin_left = qtf.margin_top = qtf.margin_right = qtf.margin_bottom = 0

qp = qtf.paragraphs[0]
qp.text = "나의 Ai 사용 경험"
qp.alignment = PP_ALIGN.CENTER
qp.font.name = FONT_TITLE
qp.font.size = Pt(26.0)
qp.font.bold = True
qp.font.color.rgb = COLOR_ORANGE
qp.space_after = Pt(16)

items_6p = [
    "- 언제 무슨 용도로 사용해보았는지",
    "- 웹사이트 (html) 를 만들어본 적 있는지"
]
for it in items_6p:
    pi = qtf.add_paragraph()
    pi.text = it
    pi.alignment = PP_ALIGN.CENTER
    pi.font.name = FONT_BODY
    pi.font.size = Pt(16.5)
    pi.font.color.rgb = COLOR_DARK_TEXT
    pi.space_after = Pt(8)

# Examples Box
add_clean_box(s6, Inches(2.0), Inches(3.9), Inches(9.333), Inches(2.2))
ebox = s6.shapes.add_textbox(Inches(2.3), Inches(4.2), Inches(8.733), Inches(1.6))
etf = ebox.text_frame
etf.word_wrap = True
etf.margin_left = etf.margin_top = etf.margin_right = etf.margin_bottom = 0

ep1 = etf.paragraphs[0]
ep1.text = "ex- 그림 그려봐! 이렇게 갖고 놀아본 (?) 정도에요 ㅎㅎ"
ep1.alignment = PP_ALIGN.CENTER
ep1.font.name = FONT_BODY
ep1.font.size = Pt(15.0)
ep1.font.color.rgb = COLOR_MUTED
ep1.space_after = Pt(14)

ep2 = etf.add_paragraph()
ep2.text = "ex- 여행 갈 때 일정표를 html로 만들어 본 적 있습니다!"
ep2.alignment = PP_ALIGN.CENTER
ep2.font.name = FONT_BODY
ep2.font.size = Pt(15.0)
ep2.font.color.rgb = COLOR_MUTED

# ==================== SLIDE 7 ====================
s7 = create_slide()
add_clean_box(s7, Inches(2.5), Inches(2.4), Inches(8.333), Inches(2.7))
b7 = s7.shapes.add_textbox(Inches(2.8), Inches(2.8), Inches(7.733), Inches(1.9))
tf7 = b7.text_frame
tf7.word_wrap = True
tf7.margin_left = tf7.margin_top = tf7.margin_right = tf7.margin_bottom = 0

p = tf7.paragraphs[0]
p.text = "걱정마세요!"
p.alignment = PP_ALIGN.CENTER
p.font.name = FONT_TITLE
p.font.size = Pt(40.5)
p.font.bold = True
p.font.color.rgb = COLOR_ORANGE
p.space_after = Pt(16)

p_sub = tf7.add_paragraph()
p_sub.text = "차근차근 함께 해볼게요"
p_sub.alignment = PP_ALIGN.CENTER
p_sub.font.name = FONT_BODY
p_sub.font.size = Pt(18.0)
p_sub.font.color.rgb = COLOR_DARK_TEXT

# ==================== SLIDE 8 ====================
s8 = create_slide()
add_clean_box(s8, Inches(2.2), Inches(2.5), Inches(8.933), Inches(2.5))
b8 = s8.shapes.add_textbox(Inches(2.5), Inches(2.9), Inches(8.333), Inches(1.7))
tf8 = b8.text_frame
tf8.word_wrap = True
tf8.margin_left = tf8.margin_top = tf8.margin_right = tf8.margin_bottom = 0

p = tf8.paragraphs[0]
p.text = "예제 : 나의 몰입 시간을 지켜줄"
p.alignment = PP_ALIGN.CENTER
p.font.name = FONT_BODY
p.font.size = Pt(17.0)
p.font.color.rgb = COLOR_DARK_TEXT
p.space_after = Pt(8)

p2 = tf8.add_paragraph()
p2.text = "[딥워크 타이머 만들기]"
p2.alignment = PP_ALIGN.CENTER
p2.font.name = FONT_TITLE
p2.font.size = Pt(36.0)
p2.font.bold = True
p2.font.color.rgb = COLOR_ORANGE

# ==================== SLIDE 9 ====================
s9 = create_slide()
add_clean_box(s9, Inches(2.2), Inches(2.4), Inches(8.933), Inches(2.8))
b9 = s9.shapes.add_textbox(Inches(2.5), Inches(2.8), Inches(8.333), Inches(2.0))
tf9 = b9.text_frame
tf9.word_wrap = True
tf9.margin_left = tf9.margin_top = tf9.margin_right = tf9.margin_bottom = 0

p = tf9.paragraphs[0]
p.text = "얼마나 걸렸을까요?"
p.alignment = PP_ALIGN.CENTER
p.font.name = FONT_TITLE
p.font.size = Pt(40.5)
p.font.bold = True
p.font.color.rgb = COLOR_DARK_TEXT
p.space_after = Pt(18)

p_sub = tf9.add_paragraph()
p_sub.text = "(이미지 : 클로드를 활용하는 깨굴이 옆에서 구경하는 꿀차)"
p_sub.alignment = PP_ALIGN.CENTER
p_sub.font.name = FONT_BODY
p_sub.font.size = Pt(15.0)
p_sub.font.color.rgb = COLOR_MUTED

# ==================== SLIDE 10 ====================
s10 = create_slide()
add_clean_box(s10, Inches(2.2), Inches(2.4), Inches(8.933), Inches(2.8))
b10 = s10.shapes.add_textbox(Inches(2.5), Inches(2.8), Inches(8.333), Inches(2.0))
tf10 = b10.text_frame
tf10.word_wrap = True
tf10.margin_left = tf10.margin_top = tf10.margin_right = tf10.margin_bottom = 0

p = tf10.paragraphs[0]
p.text = "단 5분이면 충분합니다"
p.alignment = PP_ALIGN.CENTER
p.font.name = FONT_TITLE
p.font.size = Pt(40.5)
p.font.bold = True
p.font.color.rgb = COLOR_ORANGE
p.space_after = Pt(18)

p_sub = tf10.add_paragraph()
p_sub.text = "(이미지 : 깨굴이 옆의 놀래는 꿀차)"
p_sub.alignment = PP_ALIGN.CENTER
p_sub.font.name = FONT_BODY
p_sub.font.size = Pt(15.0)
p_sub.font.color.rgb = COLOR_MUTED

# ==================== SLIDE 11 ====================
s11 = create_slide()
add_clean_box(s11, Inches(2.0), Inches(2.0), Inches(9.333), Inches(3.6))
b11 = s11.shapes.add_textbox(Inches(2.3), Inches(2.3), Inches(8.733), Inches(3.0))
tf11 = b11.text_frame
tf11.word_wrap = True
tf11.margin_left = tf11.margin_top = tf11.margin_right = tf11.margin_bottom = 0

p = tf11.paragraphs[0]
p.text = "내가 만들고 싶은 것의\n‘의도’와 ‘기능’을 잘 전달해주었기 때문에"
p.alignment = PP_ALIGN.CENTER
p.font.name = FONT_TITLE
p.font.size = Pt(30.0)
p.font.bold = True
p.font.color.rgb = COLOR_DARK_TEXT
p.space_after = Pt(20)

p2 = tf11.add_paragraph()
p2.text = "-> Ai와 3번 정도 대화하니 완벽하게 만들어졌다"
p2.alignment = PP_ALIGN.CENTER
p2.font.name = FONT_BODY
p2.font.size = Pt(16.5)
p2.font.bold = True
p2.font.color.rgb = COLOR_ORANGE
p2.space_after = Pt(8)

p3 = tf11.add_paragraph()
p3.text = "(사실 5분은 뻥이고 수정까지 10분)"
p3.alignment = PP_ALIGN.CENTER
p3.font.name = FONT_BODY
p3.font.size = Pt(14.5)
p3.font.color.rgb = COLOR_MUTED

# ==================== SLIDE 12 ====================
s12 = create_slide()
add_clean_box(s12, Inches(2.2), Inches(2.2), Inches(8.933), Inches(3.2))
b12 = s12.shapes.add_textbox(Inches(2.5), Inches(2.5), Inches(8.333), Inches(2.6))
tf12 = b12.text_frame
tf12.word_wrap = True
tf12.margin_left = tf12.margin_top = tf12.margin_right = tf12.margin_bottom = 0

p = tf12.paragraphs[0]
p.text = "당황하지 마세요"
p.alignment = PP_ALIGN.CENTER
p.font.name = FONT_TITLE
p.font.size = Pt(38.0)
p.font.bold = True
p.font.color.rgb = COLOR_ORANGE
p.space_after = Pt(18)

p2 = tf12.add_paragraph()
p2.text = "처음 해보면 생각과 다를 수 있어요"
p2.alignment = PP_ALIGN.CENTER
p2.font.name = FONT_BODY
p2.font.size = Pt(16.5)
p2.font.color.rgb = COLOR_DARK_TEXT
p2.space_after = Pt(10)

p3 = tf12.add_paragraph()
p3.text = "하지만 고쳐나가면 됩니다"
p3.alignment = PP_ALIGN.CENTER
p3.font.name = FONT_BODY
p3.font.size = Pt(16.5)
p3.font.bold = True
p3.font.color.rgb = COLOR_DARK_TEXT

# ==================== SLIDE 13 (스크립트 14번) ====================
# 13p : 좌상단 네비게이터 + 중앙정렬 + 박스 처리
s13 = create_slide()
add_navigator(s13, "바이브 코딩의 3가지 요소")

add_clean_box(s13, Inches(2.0), Inches(2.0), Inches(9.333), Inches(4.2))
b13 = s13.shapes.add_textbox(Inches(2.4), Inches(2.4), Inches(8.533), Inches(3.4))
tf13 = b13.text_frame
tf13.word_wrap = True
tf13.margin_left = tf13.margin_top = tf13.margin_right = tf13.margin_bottom = 0

items_14 = [
    ("기획", "내가 만들고 싶은 것은? (의도와 쓰임새, 용어)"),
    ("기능", "작동 규칙 (클릭, 타이머, 저장 기능 등)"),
    ("디자인", "보면 기분이 좋거든요 (색감, 무드 등)")
]
for idx, (title, desc) in enumerate(items_14):
    p = tf13.paragraphs[0] if idx == 0 else tf13.add_paragraph()
    p.text = f"{title} - {desc}"
    p.alignment = PP_ALIGN.CENTER
    p.font.name = FONT_BODY
    p.font.size = Pt(16.5)
    p.font.bold = True if idx == 0 else False
    p.font.color.rgb = COLOR_DARK_TEXT
    p.space_after = Pt(22)

# ==================== SLIDE 14 (스크립트 15번) ====================
# 14p : 좌상단 네비게이터 + 중앙정렬 + 박스 처리
s14 = create_slide()
add_navigator(s14, "2회차 모임에 집중할 것")

add_clean_box(s14, Inches(2.0), Inches(2.0), Inches(9.333), Inches(4.2))
b14 = s14.shapes.add_textbox(Inches(2.4), Inches(2.4), Inches(8.533), Inches(3.4))
tf14 = b14.text_frame
tf14.word_wrap = True
tf14.margin_left = tf14.margin_top = tf14.margin_right = tf14.margin_bottom = 0

items_15 = [
    "기획 - 내가 쓰고 싶은 것은? (의도과 쓰임새, 용어)  ✅",
    "기능 - 작동 규칙 (클릭, 타이머, 저장기능 등)  ✅",
    "디자인 - 보면 기분이 좋거든요 (색감, 무드 등)"
]
for idx, text in enumerate(items_15):
    p = tf14.paragraphs[0] if idx == 0 else tf14.add_paragraph()
    p.text = text
    p.alignment = PP_ALIGN.CENTER
    p.font.name = FONT_BODY
    p.font.size = Pt(17.0)
    p.font.bold = True if '✅' in text else False
    p.font.color.rgb = COLOR_ORANGE if '✅' in text else COLOR_MUTED
    p.space_after = Pt(22)

# ==================== SLIDE 15 (스크립트 16번) ====================
# 15p : 좌상단 네비게이터 + 중앙정렬 + 박스 처리
s15 = create_slide()
add_navigator(s15, "[기획하기]")

add_clean_box(s15, Inches(1.8), Inches(1.8), Inches(9.733), Inches(4.5))
b15 = s15.shapes.add_textbox(Inches(2.2), Inches(2.2), Inches(8.933), Inches(3.7))
tf15 = b15.text_frame
tf15.word_wrap = True
tf15.margin_left = tf15.margin_top = tf15.margin_right = tf15.margin_bottom = 0

p = tf15.paragraphs[0]
p.text = "예제 : 나의 몰입 시간을 지켜줄\n[딥워크 타이머 만들기]"
p.alignment = PP_ALIGN.CENTER
p.font.name = FONT_TITLE
p.font.size = Pt(28.0)
p.font.bold = True
p.font.color.rgb = COLOR_ORANGE
p.space_after = Pt(24)

p2 = tf15.add_paragraph()
p2.text = "내가 쓰고 싶은 것은?"
p2.alignment = PP_ALIGN.CENTER
p2.font.name = FONT_TITLE
p2.font.size = Pt(19.0)
p2.font.bold = True
p2.font.color.rgb = COLOR_DARK_TEXT
p2.space_after = Pt(14)

p3 = tf15.add_paragraph()
p3.text = "* 나의 집중 시간을 도와줄 딥워크 타이머. 시간의 흐름에 따라, 산을 오르는 컨셉으로."
p3.alignment = PP_ALIGN.CENTER
p3.font.name = FONT_BODY
p3.font.size = Pt(16.0)
p3.font.color.rgb = COLOR_DARK_TEXT

# ==================== SLIDE 16 (스크립트 17번) ====================
# 16p : 좌상단 네비게이터 + 중앙정렬 + 박스 처리
s16 = create_slide()
add_navigator(s16, "[기획하기]")

add_clean_box(s16, Inches(1.8), Inches(1.6), Inches(9.733), Inches(4.9))
b16 = s16.shapes.add_textbox(Inches(2.2), Inches(1.9), Inches(8.933), Inches(4.3))
tf16 = b16.text_frame
tf16.word_wrap = True
tf16.margin_left = tf16.margin_top = tf16.margin_right = tf16.margin_bottom = 0

p = tf16.paragraphs[0]
p.text = "각 탭의 핵심 목적을 한줄로 적어봅시다."
p.alignment = PP_ALIGN.CENTER
p.font.name = FONT_TITLE
p.font.size = Pt(25.0)
p.font.bold = True
p.font.color.rgb = COLOR_ORANGE
p.space_after = Pt(20)

tabs17 = [
    "- 산오르기 : ",
    "- 딥워크: ",
    "- 바구니: ",
    "- 업무시간: "
]
for t in tabs17:
    pi = tf16.add_paragraph()
    pi.text = t
    pi.alignment = PP_ALIGN.CENTER
    pi.font.name = FONT_BODY
    pi.font.size = Pt(16.5)
    pi.font.color.rgb = COLOR_DARK_TEXT
    pi.space_after = Pt(12)

p_end = tf16.add_paragraph()
p_end.space_before = Pt(14)
p_end.text = "완벽한 정답은 없으니, ‘한 줄’로 정리해보고 채팅창에 올려보세요!"
p_end.alignment = PP_ALIGN.CENTER
p_end.font.name = FONT_BODY
p_end.font.size = Pt(15.0)
p_end.font.bold = True
p_end.font.color.rgb = COLOR_MUTED

# ==================== SLIDE 17 (스크립트 18번) ====================
s17 = create_slide()
add_navigator(s17, "[기획하기]")

add_clean_box(s17, Inches(1.8), Inches(1.6), Inches(9.733), Inches(4.9))
b17 = s17.shapes.add_textbox(Inches(2.2), Inches(1.9), Inches(8.933), Inches(4.3))
tf17 = b17.text_frame
tf17.word_wrap = True
tf17.margin_left = tf17.margin_top = tf17.margin_right = tf17.margin_bottom = 0

p = tf17.paragraphs[0]
p.text = "예시"
p.alignment = PP_ALIGN.CENTER
p.font.name = FONT_TITLE
p.font.size = Pt(26.0)
p.font.bold = True
p.font.color.rgb = COLOR_ORANGE
p.space_after = Pt(20)

tabs18 = [
    ("- 산오르기 : ", "내 하루의 작업량을 측정하는 산오르기 컨셉의 타이머."),
    ("- 딥워크: ", "내가 집중할 업무를 선택하고 산오르기에 설정할 수 있는 탭."),
    ("- 바구니: ", "딥워크 외에, 그때그때 생각나는 일거리를 적는 체크리스트."),
    ("- 업무시간: ", "내가 산을 얼마나 올랐는지 시간이 기록되는 탭.")
]
for label, desc in tabs18:
    pi = tf17.add_paragraph()
    pi.text = label + desc
    pi.alignment = PP_ALIGN.CENTER
    pi.font.name = FONT_BODY
    pi.font.size = Pt(16.0)
    pi.font.color.rgb = COLOR_DARK_TEXT
    pi.space_after = Pt(12)

# ==================== SLIDE 18 (스크립트 19번) ====================
# 18p : 기존 1회차 피피티 16p 레이아웃 참고, 2열 디자인 (5.83 x 2.88 인치 카드 2개)
s18 = create_slide()
add_navigator(s18, "3회차 모임 미리보기")

card_w = Inches(5.833)
card_h = Inches(3.6)
card_top = Inches(2.2)

# Left Column Card (깃허브 아이디 만들기)
add_clean_box(s18, Inches(0.625), card_top, card_w, card_h)
b_l = s18.shapes.add_textbox(Inches(0.95), card_top + Inches(0.4), card_w - Inches(0.65), card_h - Inches(0.6))
tf_l = b_l.text_frame
tf_l.word_wrap = True
tf_l.margin_left = tf_l.margin_top = tf_l.margin_right = tf_l.margin_bottom = 0

p_l = tf_l.paragraphs[0]
p_l.text = "깃허브 아이디 만들기 (배포)"
p_l.font.name = FONT_TITLE
p_l.font.size = Pt(21.0)
p_l.font.bold = True
p_l.font.color.rgb = COLOR_ORANGE
p_l.space_after = Pt(16)

p_l_desc = tf_l.add_paragraph()
p_l_desc.text = "- 실제로 인터넷에서 접속할 수 있게 만들어요."
p_l_desc.font.name = FONT_BODY
p_l_desc.font.size = Pt(16.0)
p_l_desc.font.color.rgb = COLOR_DARK_TEXT

# Right Column Card (시간관리툴 발전시키기)
add_clean_box(s18, Inches(6.875), card_top, card_w, card_h)
b_r = s18.shapes.add_textbox(Inches(7.2), card_top + Inches(0.4), card_w - Inches(0.65), card_h - Inches(0.6))
tf_r = b_r.text_frame
tf_r.word_wrap = True
tf_r.margin_left = tf_r.margin_top = tf_r.margin_right = tf_r.margin_bottom = 0

p_r = tf_r.paragraphs[0]
p_r.text = "내가 만든 시간관리툴 발전시키기"
p_r.font.name = FONT_TITLE
p_r.font.size = Pt(21.0)
p_r.font.bold = True
p_r.font.color.rgb = COLOR_ORANGE
p_r.space_after = Pt(16)

items_r = [
    "- 예제 : 딥워크 타이머 발전시키기",
    "- 나만의 아이디어로 만들어보기"
]
for it in items_r:
    pi = tf_r.add_paragraph()
    pi.text = it
    pi.font.name = FONT_BODY
    pi.font.size = Pt(16.0)
    pi.font.color.rgb = COLOR_DARK_TEXT
    pi.space_after = Pt(8)

# ==================== SLIDE 19 (스크립트 20번) ====================
# 19p : 기존 1회차 피피티 20p 참고, 동일한 디자인 (상단 큰 제목 + 중앙 박스 미션 + 하단 옾챗 안내)
s19 = create_slide()

# Top Big Title
tbox19 = s19.shapes.add_textbox(Inches(0.5), Inches(1.0), Inches(12.333), Inches(0.8))
tf19 = tbox19.text_frame
tf19.word_wrap = True
tf19.margin_left = tf19.margin_top = tf19.margin_right = tf19.margin_bottom = 0
p = tf19.paragraphs[0]
p.text = "2회차 숙제"
p.alignment = PP_ALIGN.CENTER
p.font.name = FONT_TITLE
p.font.size = Pt(43.5)
p.font.bold = True
p.font.color.rgb = COLOR_DARK_TEXT

# Center Mission Box (1회차 20p와 동일한 위치/크기)
mbox_w = Inches(9.4)
mbox_h = Inches(2.6)
mbox_left = Inches(1.96)
mbox_top = Inches(2.4)
add_clean_box(s19, mbox_left, mbox_top, mbox_w, mbox_h)

mb = s19.shapes.add_textbox(mbox_left + Inches(0.4), mbox_top + Inches(0.35), mbox_w - Inches(0.8), mbox_h - Inches(0.6))
mtf = mb.text_frame
mtf.word_wrap = True
mtf.margin_left = mtf.margin_top = mtf.margin_right = mtf.margin_bottom = 0

mp_head = mtf.paragraphs[0]
mp_head.text = "📝 이번 주 미션!"
mp_head.font.name = FONT_TITLE
mp_head.font.size = Pt(17.0)
mp_head.font.bold = True
mp_head.font.color.rgb = COLOR_ORANGE
mp_head.space_after = Pt(16)

missions_19 = [
    "1.  나의 딥워크 시간 기록 ‘인증샷’ 올려보기 (선택)",
    "2.  내가 만든 타이머 직접 사용하고 아쉬운 점 수정해보기"
]
for m in missions_19:
    mpi = mtf.add_paragraph()
    mpi.text = m
    mpi.font.name = FONT_BODY
    mpi.font.size = Pt(15.5)
    mpi.font.color.rgb = COLOR_DARK_TEXT
    mpi.space_after = Pt(10)

# Bottom openchat notice
bot_box = s19.shapes.add_textbox(Inches(0.6), Inches(5.3), Inches(12.133), Inches(0.6))
btf19 = bot_box.text_frame
btf19.word_wrap = True
btf19.margin_left = btf19.margin_top = btf19.margin_right = btf19.margin_bottom = 0
bp = btf19.paragraphs[0]
bp.text = "-> 언제든 오픈채팅방에 질문하면 봐드릴게요! 자랑도 환영!"
bp.alignment = PP_ALIGN.CENTER
bp.font.name = FONT_BODY
bp.font.size = Pt(16.0)
bp.font.bold = True
bp.font.color.rgb = COLOR_ORANGE

output_path = '/Users/hnky/agyspace/mytt_2회차_강의슬라이드_구원파트_v3.pptx'
prs.save(output_path)
print("Saved v3 clean presentation:", output_path, "Slide count:", len(prs.slides))
