from pathlib import Path
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import Paragraph
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.colors import HexColor, Color
from reportlab.lib.utils import ImageReader
from PIL import Image
import fitz

ROOT=Path(__file__).parent
OUT=ROOT/'downloads'
OUT.mkdir(exist_ok=True)
pdfmetrics.registerFont(TTFont('Korean','C:/Windows/Fonts/malgun.ttf'))
pdfmetrics.registerFont(TTFont('KoreanBold','C:/Windows/Fonts/malgunbd.ttf'))
W,H=595.276,841.89
M=42
INK=HexColor('#272336'); PURPLE=HexColor('#6741d9'); GRAY=HexColor('#615c6d')
style=ParagraphStyle('body',fontName='Korean',fontSize=10,leading=16,textColor=INK,wordWrap='CJK')
c=None
def text(x,y,s,size=10,bold=False,color=INK):
    c.setFillColor(color);c.setFont('KoreanBold' if bold else 'Korean',size);c.drawString(x,H-y,s)
def para(s,x,y,w,size=10,leading=16):
    st=ParagraphStyle('p',parent=style,fontSize=size,leading=leading)
    p=Paragraph(s,st);pw,ph=p.wrap(w,800);p.drawOn(c,x,H-y-ph);return ph
def box(x,y,w,h,fill='#ffffff',stroke='#b8b3c3',r=8):
    c.setFillColor(HexColor(fill));c.setStrokeColor(HexColor(stroke));c.setLineWidth(.65);c.roundRect(x,H-y-h,w,h,r,fill=1,stroke=1)
def line(x,y,w):
    c.setStrokeColor(HexColor('#c8c4ce'));c.setLineWidth(.5);c.line(x,H-y,x+w,H-y)
def lines(y,n=3,x=M+14,w=W-2*M-28,step=23):
    for k in range(n):line(x,y+k*step,w)
def head(k,title,sub,page):
    text(M,36,'한입의 세계  /  CULTURE LAB',9,True,PURPLE)
    text(W-142,36,k,9,False,GRAY)
    text(M,76,title,24,True)
    text(M,100,sub,9,False,GRAY)
    line(M,114,W-2*M)
    text(M,H-26,'중1 사회 · [9사(일사)02-03] · 세계 음식의 날',8,False,GRAY)
    text(W-64,H-26,str(page),9,True,PURPLE)
def identity(y=139):text(M,y,'학년 / 반 / 번호: ____________________     이름: ____________________',10)
def label(y,num,title):
    text(M,y,num,11,True,PURPLE);text(M+27,y,title,12,True)
def source_page():
    head('읽기 자료','다른 맛, 같은 식탁','두 문화 사례에서 생활의 배경을 찾고, 토론의 근거를 모아 봅시다.',1)
    img=Image.open(ROOT/'assets/cafeteria.png')
    c.drawImage(ImageReader(img),M,H-293,width=245,height=163,mask='auto')
    para('학생자치회의 제안',304,132,248,12,18)
    para('“우리 학교가 매달 한 번씩 여러 나라의 음식을 급식으로 제공하려고 합니다. 새로운 음식을 먹어 보고 싶다는 학생도 있고, 입맛에 맞지 않을까 걱정하는 학생도 있습니다. 여러분은 어떻게 생각하나요?”',304,158,248,10.2,17)
    text(M,308,'수업용 가상 상황 · AI 생성 그림',8,False,GRAY)
    box(M,322,W-2*M,61,fill='#f3f0f8')
    text(M+14,343,'기대: “새로운 음식과 문화를 만나 보고 싶어!”',10,True)
    text(M+14,366,'걱정: “먹기 어려운 음식이면 점심을 거르게 될까?”',10,True)
    label(414,'A','김장, 함께 만들고 나누다')
    para('한국의 김장은 김치를 많이 담가 겨울을 준비하며 함께 나누는 문화입니다. 늦가을에 사람들이 모여 김치를 만들고 나누는 과정에는 협력과 이웃 간 관계가 담겨 있습니다. 맛뿐 아니라 계절에 맞춰 음식을 준비하고 나누는 생활도 살펴볼 수 있습니다.',M,426,W-2*M,10.4,17)
    label(526,'B','멕시코 전통 음식, 땅과 이어지다')
    para('멕시코 전통 음식 문화에서는 옥수수, 콩, 고추가 중요한 재료입니다. 여기에는 작물을 기르는 방법, 조리 기술, 의례와 공동체의 관습이 함께 담겨 있습니다. 재료의 맛뿐 아니라 그 재료를 길러 온 환경과 지식을 전해 온 사람들의 삶도 살펴봐야 합니다.',M,538,W-2*M,10.4,17)
    box(M,635,W-2*M,66,fill='#faf9f6')
    para('읽으며 할 일: 문화의 배경을 보여 주는 표현에 밑줄을 그으세요.<br/>생각할 점: 같은 나라 안에서도 지역·가정·개인에 따라 식생활은 다릅니다. 문화 존중은 모든 음식을 반드시 먹는다는 뜻이 아닙니다.',M+13,645,W-2*M-26,9.5,15)
    para('출처: UNESCO 무형문화유산 소개를 수업용으로 재구성(2026-10-28 확인).<br/>A. Kimjang, making and sharing kimchi in the Republic of Korea (00881)<br/>B. Traditional Mexican cuisine – the Michoacán paradigm (00400)<br/>원문: ich.unesco.org / 웹 수업 화면의 자료 A·B 출처 링크에서 열람',M,719,W-2*M,8,12)
    c.linkURL('https://ich.unesco.org/en/RL/kimjang-making-and-sharing-kimchi-in-the-republic-of-korea-00881',(M,H-747,W-M,H-732),relative=0)
    c.linkURL('https://ich.unesco.org/en/RL/traditional-mexican-cuisine-ancestral-ongoing-community-culture-the-michoacan-paradigm-00400',(M,H-759,W-M,H-747),relative=0)
    c.showPage()
def worksheet_one(page):
    head('활동지 1 / 2','내 생각에 근거를 더하면','자료 속 단서 → 나의 주장 → 근거와 연결',page);identity()
    label(174,'01','문화 탐험 기록')
    box(M,188,W-2*M,123)
    text(M+14,211,'A 김장의 문화적 배경과 자료 속 단서',10,True);lines(237,1)
    text(M+14,267,'B 멕시코 전통 음식의 문화적 배경과 자료 속 단서',10,True);lines(294,1)
    text(M,338,'두 사례의 공통점은 무엇인가요?',10,True);lines(365,1,x=M,w=W-2*M)
    label(405,'02','나의 주장과 근거')
    para('논제: 우리 학교는 매달 한 번 ‘세계 음식의 날’을 운영해야 한다.',M,418,W-2*M,10.5,16)
    text(M,455,'나의 입장:  □ 찬성     □ 반대     □ 조건부 찬성',11,True)
    text(M,484,'나의 주장 한 문장 (조건이 있다면 함께 쓰세요.)',10,True)
    lines(512,2,x=M,w=W-2*M)
    text(M,566,'근거 1. 자료 A 또는 B에서 찾은 내용 + 내 주장을 뒷받침하는 이유',10,True)
    lines(594,3,x=M,w=W-2*M)
    text(M,674,'근거 2. 다른 자료, 경험 또는 예상되는 문제 + 주장과의 연결',10,True)
    text(M,693,'경험·예상은 자료에 나온 사실과 구분해서 써요.',8,False,GRAY)
    lines(719,3,x=M,w=W-2*M)
    c.showPage()
def worksheet_two(page):
    head('활동지 2 / 2','찬반을 넘어, 함께 만들기','친구의 걱정을 듣고, 문화 이해와 선택권을 함께 생각해 봅시다.',page);identity()
    label(173,'03','친구의 생각을 듣고 응답하기')
    text(M,197,'친구의 주장과 근거를 정확히 요약해 보세요.',10)
    lines(224,2,x=M,w=W-2*M)
    text(M,278,'내가 인정하는 점 / 질문하거나 보완하고 싶은 점',10)
    lines(305,2,x=M,w=W-2*M)
    label(365,'04','우리 모둠의 ‘세계 음식의 날’ 운영안')
    text(M,389,'먹지 않더라도 문화를 배우며 참여할 수 있는 방법을 생각해 보세요.',9,False,GRAY)
    for y,num in [(404,'1'),(514,'2')]:
        box(M,y,W-2*M,100)
        text(M+13,y+23,'제안 '+num+':',10,True);line(M+65,y+29,W-2*M-80)
        text(M+13,y+50,'해결할 걱정:',9);line(M+91,y+56,W-2*M-106)
        text(M+13,y+77,'문화 이해·존중에 도움이 되는 이유:',9);line(M+208,y+84,W-2*M-223)
    text(M,640,'실행 조건 한 가지 (예: 비용, 조리 시간, 영양교사와의 협의)',9,True)
    lines(665,1,x=M,w=W-2*M)
    label(699,'05','오늘의 생각 변화')
    text(M,722,'처음에는… / 지금은… (생각이 같다면 더 분명해진 근거)',9)
    lines(748,2,x=M,w=W-2*M)
    c.showPage()
def teacher_page_one():
    head('교사용 1 / 2','45분 수업 운영 가이드','교사 화면 + 종이 학습지 · 4인 모둠 권장 · 실제 시식 없이 운영',1)
    label(147,'01','성취기준과 목표')
    para('[9사(일사)02-03] 여러 집단에서 나타나는 다양한 문화 사례들을 조사하고, 문화를 이해하는 바람직한 태도에 대하여 토의한다.',M,162,W-2*M,10.3,17)
    para('출처: 교육과정 MCP get_standard 조회 원문. 국가교육위원회 고시 제2024-3호 별책 7 사회과 교육과정, PDF 62쪽.<br/>목표: 두 음식 문화의 배경을 자료에서 찾고, 자료에 근거하여 토론한 뒤, 문화 이해와 개인의 선택을 존중하는 운영안을 제안한다.',M,211,W-2*M,9.2,15)
    label(299,'02','수업 흐름')
    rows=[('5분','상황 만나기','그림과 가상 상황을 제시합니다. 기대와 걱정이 각각 지키려는 가치를 찾아 말하게 합니다.'),('10분','문화 탐험','개별 읽기 4분 → 짝 확인 3분 → 기록 3분. 자료 A·B에서 생활 배경을 찾아 밑줄 긋고 활동지 01에 기록합니다.'),('12분','근거로 토론','개별 주장·근거 쓰기 4분 → 양쪽 입장 발표 4분 → 상대 의견 요약·질문 2분 → 생각 보완 2분. 활동지 02·03을 사용합니다.'),('13분','함께 디자인','모둠 제안 7분 → 발표·비교 4분 → 수정 2분. 선택권과 문화 배경 이해를 함께 고려한 제안 2개를 활동지 04에 씁니다.'),('5분','성찰','활동지 05에 생각 변화 또는 강화된 근거를 적고 공유합니다. 교사 화면의 목표를 기준으로 자기 점검합니다.')]
    y=315
    for minutes,title,body in rows:
        box(M,y,W-2*M,77,fill='#faf9fc')
        text(M+13,y+25,minutes,12,True,PURPLE);text(M+65,y+25,title,11,True)
        para(body,M+65,y+34,W-2*M-80,9.2,14)
        y+=85
    para('준비: 학생용 세트 1인 1부(3쪽), 필기도구, 교사용 화면. 활동지만 출력 시 A4 양면 1장. 인쇄는 실제 크기 또는 페이지 맞춤을 사용하고 흑백 출력도 가능합니다.',M,751,W-2*M,9,14)
    c.showPage()
def teacher_page_two():
    head('교사용 2 / 2','정답보다, 근거와 태도','찬반 입장 자체를 평가하지 않습니다.',2)
    label(149,'03','발문과 예상 응답')
    pairs=[('“맛만 보고 판단하면 무엇을 놓칠까요?”','김장의 계절적 준비와 나눔, 멕시코 전통 음식의 농업·공동체 맥락을 놓칠 수 있습니다.'),('“반대하면 문화를 존중하지 않는 걸까요?”','아닙니다. 운영 방식에 대한 걱정과 문화에 대한 비하는 구분해야 합니다. 먹지 않는 선택도 존중합니다.'),('“누구나 즐긴다는 것은 모두가 먹는다는 뜻일까요?”','메뉴 소개, 문화 이야기 전시, 설문 참여 등 먹지 않고 참여할 방법도 있습니다.')]
    y=169
    for q,a in pairs:
        text(M,y,q,10.5,True);para(a,M,y+12,W-2*M,9.5,15);y+=72
    label(399,'04','주장·근거 연결 예시 (토론 후 참고)')
    para('조건부 찬성: “문화 배경 소개와 선택 메뉴를 함께 제공한다면 찬성한다. 자료 A의 김장은 음식이 이웃 간 나눔과 연결됨을 보여 준다. 따라서 배경을 소개하는 세계 음식의 날은 맛보기 이상의 문화 학습이 될 수 있다. 다만 먹기 어려운 학생의 선택권을 보장해야 한다.”',M,414,W-2*M,9.8,16)
    para('보완 질문: “새로운 문화를 알 수 있어요”에서 멈추면 “어떤 자료의 어떤 내용이 네 주장과 연결되니?”라고 묻습니다. 이 예시와 같은 결론을 요구하지 않습니다.',M,493,W-2*M,9.5,15)
    label(552,'05','관찰과 피드백')
    para('① 자료 이해: 두 사례에서 문화의 배경과 자료 속 단서를 찾았는가?<br/>② 주장·근거: 자료의 내용이 주장을 뒷받침하는 이유를 설명했는가?<br/>③ 존중·적용: 상대의 걱정을 요약하고 선택권과 문화 이해를 반영했는가?<br/>피드백 예: “자료에서 배경을 잘 찾았어요. 그 배경을 학생들에게 어떻게 소개할지 제안에 더해 볼까요?”',M,568,W-2*M,9.5,16)
    box(M,655,W-2*M,119,fill='#faf9f6')
    para('수업 중 배려할 점',M+13,666,W-2*M-26,10,16)
    para('• 특정 나라의 음식 하나로 전체 문화를 일반화하지 않습니다.<br/>• 학생에게 알레르기·종교·가정 배경의 공개를 요구하지 않습니다.<br/>• “이상한 음식” 같은 표현은 “내게 낯선 음식”으로 바꿔 말합니다.<br/>• 실제 급식 도입의 메뉴·안전·조리 가능성은 영양교사와 협의합니다.<br/>• 교사 화면의 체크·타이머는 저장되지 않으며 답안을 수집하지 않습니다.',M+13,691,W-2*M-26,9,14)
    c.showPage()
def build(name,funcs):
    global c
    c=canvas.Canvas(str(OUT/name),pagesize=(W,H))
    c.setTitle('한입의 세계 - '+name);c.setAuthor('한입의 세계 · 수업 자료')
    for fn in funcs:fn()
    c.save()
build('student-set.pdf',[source_page,lambda:worksheet_one(2),lambda:worksheet_two(3)])
build('worksheet.pdf',[lambda:worksheet_one(1),lambda:worksheet_two(2)])
build('teacher-guide.pdf',[teacher_page_one,teacher_page_two])
# A smaller web asset keeps the page usable on school networks.
im=Image.open(ROOT/'assets/cafeteria.png'); im.save(ROOT/'assets/cafeteria.webp','WEBP',quality=88)
qa=ROOT/'qa';qa.mkdir(exist_ok=True)
for name in ['student-set.pdf','worksheet.pdf','teacher-guide.pdf']:
    doc=fitz.open(OUT/name)
    print(name,'pages:',len(doc),'text chars:',sum(len(p.get_text()) for p in doc))
    for i,page in enumerate(doc):
        page.get_pixmap(matrix=fitz.Matrix(1.2,1.2)).save(qa/(name.replace('.pdf','')+f'-{i+1}.png'))
    # Visual contact sheet for all pages of each deliverable.
    thumbs=[]
    for i in range(len(doc)):
        t=Image.open(qa/(name.replace('.pdf','')+f'-{i+1}.png'));t.thumbnail((596,843));thumbs.append(t)
    sheet=Image.new('RGB',(596*len(thumbs),843),'#ddd')
    for i,t in enumerate(thumbs):sheet.paste(t,(596*i,0))
    sheet.save(qa/(name.replace('.pdf','')+'-all.png'))
