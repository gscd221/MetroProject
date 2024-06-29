from tkinter import *

sgi = ["1호선", "2호선", "3호선", "4호선", "5호선", "6호선", "7호선", "8호선", "9호선", "인천1호선", "인천2호선", "신분당선", "경의중앙선", "경춘선", "수인분당선", "공항철도", "의정부경전철", "용인에버라인", "경강선", "우이신설선", "서해선", "김포골드라인", "신림선", "GTX-A"]
selineone = ["연천","전곡","청산","소요산","동두천","보산","동두천중앙","지행","덕정","덕계","양주","녹양","가능","의정부","회룡","망월사","도봉산","도봉","방학","창동","녹천","월계","광운대","석계","신이문","외대앞","회기","청량리(서울시립대입구)","제기동(한국건강관리협회)","신설동","동묘앞","동대문","종로5가(삼양그룹)","종로3가","종각","시청","서울","남영","용산","노량진","대방","신길","영등포","신도림","구로","구일","개봉","오류동","온수","역곡","소사","부천","중동","송내","부개","부평","백운","동암","간석","주안","도화","제물포","도원","동인천","인천","가산디지털단지","독산","금천구청","광명","석수","관악","안양","명학","금정","군포","당정","의왕","성균관대","화서","수원","세류","병점","서동탄","세마","오산대","오산","진위","송탄","서정리","평택지제","평택","성환","직산","두정","천안","봉명","쌍용(나사렛대)","아산","탕정","배방","온양온천","신창(순천향대)"]
selinetwo = ["시청","을지로입구(하나은행)","을지로3가(신한카드)","을지로4가(BC카드)","동대문역사문화공원(DDP)","신당","상왕십리","왕십리(성동구청)","한양대","뚝섬","성수","건대입구","구의(광진구청)","강변(동서울터미널)","잠실나루(수협중앙회공제보험)","잠실(송파구청)","잠실새내","종합운동장","삼성(무역센터)","선릉(에큐온저축은행)","역삼(센터필드)","강남","교대(법원.검찰청)","서초","방배(백석예술대)","사당","낙성대(강감찬)","서울대입구(관악구청)","봉천","신림","신대방","구로디지털단지(원광디지털대)","대림(구로구청)","신도림","문래(김안과병원)","영등포구청","당산","합정(세아타워)","홍대입구","신촌","이대","아현","충정로(경기대입구)","용답","신답","용두(동대문구청)","신설동","도림천","양천구청","신정네거리","까치산"]
selinethree = ["대화","주엽","정발산","마두","백석","대곡","화정","원당","원흥","삼송","지축","구파발(은평성모병원)","연신내","불광","녹번","홍제","무악재","독립문","경복궁(정부서울청사)","안국(현대건설)","종로3가","을지로3가(신한카드)","충무로","동대입구","약수","금호","옥수","압구정","신사","잠원","고속터미널","교대(법원.검찰청)","남부터미널","양재(서초구청)","매봉","도곡","대치","학여울","대청(서울주택도시공사)","일원","수서","가락시장","경찰병원","오금"]
selinefour = ["진접","오남","별내별가람","당고개","상계","노원","창동","쌍문","수유(강북구청)","미아(서울사이버대학)","미아사거리","길음","성신여대입구(돈암)","한성대입구(삼선교)","혜화(서울대학교병원)","동대문","동대문역사문화공원(DDP)","충무로","명동(우리금융타운)","회현(남대문시장)","서울","숙대입구","삼각지","신용산(아모레퍼시픽)","이촌(국립중앙박물관)","동작(현충원)","이수(총신대입구)","사당","남태령","선바위","경마공원","대공원","과천","정부과천청사","인덕원","평촌","범계","금정","산본","수리산","대야미","반월","상록수","한대앞","중앙","고잔","초지","안산","신길온천","정왕","오이도"]
selinefive = ["방화","개화산","김포공항","송정","마곡(홈앤쇼핑)","발산(에스앤유서울병원)","우장산","화곡","까치산","신정(은행정)","목동","오목교(목동운동장앞)","양평","영등포구청","영등포시장","신길","여의도(신한투자증권)","여의나루","마포","공덕","애오개","충정로(경기대입구)","서대문(강북삼성병원)","광화문(세종문화회관)","종로3가(탑골공원)","을지로4가(BC카드)","동대문역사문화공원(DDP)","청구","신금호","행당","왕십리(성동구청)","마장","답십리","장한평","군자(능동)","아차산(어린이대공원후문)","광나루(장신대)","천호(풍납토성)","강동(강동성심병원)","길동","굽은다리(강동구민회관)","명일","고덕(강동경희대병원)","상일동","강일","하남풍산","하남시청(덕풍.신장)","하남검단산","둔촌동","올림픽공원(한국체대)","방이","오금","개롱","거여","마천"]
selinesix = ["역촌","불광","독바위","연신내","구산","응암","새절(신사)","증산(명지대앞)","디지털미디어시티","월드컵경기장(성산)","마포구청","망원","합정(세아타워)","상수","광흥창(서강)","대흥(서강대앞)","공덕","효창공원앞","삼각지","녹사평(용산구청)","이태원","한강진","버티고개","약수","청구","신당","동묘앞","창신","보문","안암(고대병원앞)","고려대(종암)","월곡(동덕여대)","상월곡(한국과학기술연구원)","돌곶이","석계","태릉입구","화랑대(서울여대입구)","봉화산(서울의료원)","신내"]
selineseven = ["장암","도봉산","수락산","마들","노원","중계(한국성서대)","하계(을지대을지병원)","공릉(서울과학기술대)","태릉입구","먹골","중화","상봉","면목(서일대입구)","사가정(녹색병원)","용마산(용마폭포공원)","중곡","군자(능동)","어린이대공원(세종대)","건대입구","자양(뚝섬한강공원)","청담(제일정형외과병원)","강남구청","학동(나누리병원)","논현","반포","고속터미널","내방(유중아트센터)","이수(총신대입구)","남성","숭실대입구(살피재)","상도","장승배기","산대방삼거리","보라매(현대에이치티)","신풍","대림(구로구청)","남구로","가산디지털단지(마리오아울렛)","철산","광명사거리","천왕","온수(성공회대입구)","까치울","부천종합운동장","춘의","신중동","부천시청(부천아트센터)","상동","삼산체육관","굴포천","부평구청","산곡","석남(거북시장)"]
selineeight = ["암사","천호(풍남토성)","강동구청","몽촌토성","잠실(송파구청)","석촌(한솔병원)","송파","가락시장","문정","장지","복정","남위례","산성","남한산성입구(성남법원.검찰청)","단대오거리(신구대학교)","신흥","수진","모란"]
selinenine = ["개화","김포공항","공항시장","신방화","마곡나루(서울식물원)","양천향교","가양(부민병원)","증미","등촌(강서대학교)","염창","신목동","선유도","당산","국회의사당(KDB산업은행)","여의도(신한투자증권)","샛강(KB금융타운)","노량진","노들","흑석(중앙대입구)","동작(현충원)","구반포","신반포","고속터미널","사평","신논현","언주","선정릉","삼성중앙","봉은사","종합운동장","삼전","석촌고분","석촌(한솔병원)","송파나루","한성백제","올림픽공원(한국체대)","둔촌오륜","중앙보훈병원"]
icnlineone = ["계양","귤현","박촌","임학","계산","경인교대입구","작전","갈산","부평구청","부평시장","부평","동수","부평삼거리","간석오거리","인천시청","예술회관","인천터미널","문학경기장","선학","신연수","원인재","동춘","동막","캠퍼스타운","테크노파크","지식정보단지","인천대입구","센트럴파크(재외동포청)","국제업무지구","송도달빛축제공원"]
icnlinetwo = ["검단오류(검단산업단지)","왕길","검단사거리","마전","완정","독정","검암","검바위","아시아드경기장(공촌사거리)","서구청","가정(루원시티)","가정중앙시장","석남(거북시장)","서부여성회관","인천가좌","가재울","주안국가산단(인천J밸리)","주안","시민공원(문화창작지대)","석바위시장","인천시청","석천사거리","모래내시장","만수","남동구청","인천대공원","운연(서창)"]
newbundangline = ["신사","논현","신논현","강남","양재(서초구청)","양재시민의 숲(매헌)","청계산입구","판교(판교테크노밸리)","정자","미금(분당서울대병원)","동천","수지구청","성복","상현","광교중앙(아주대)","광교(경기대)"]
gjline = ["임진강","운천","문산","파주","월롱","금촌","금릉","운정","야당","탄현","일산","풍산","백마","곡산","대곡","능곡","행신","강매","한국항공대","수색","디지털미디어시티","가좌","신촌","서울","홍대입구","서강대","공덕","효창공원앞","용산",'이촌',"서빙고","한남","옥수","응봉","왕십리","청량리","회기","중랑","상봉","망우","양원","구리","도농","양정","덕소","도심","팔당","운길산","양수","신원","국수","아신","오빈","양평","원덕","용문","지평"]
gyungchunline = ["광운대","청량리","회기","중랑","상봉","망우","신내","갈매","별내","퇴계원","사릉","금곡","평내호평","천마산","마석","대성리","청평","상천","가평","굴봉산","백양리","강촌","김유정","남춘천","춘천"]
sbline = ["청량리","왕십리","서울숲","압구정로데오","강남구청","선정릉","선릉","한티","도곡","구룡","개포동","대모산입구","수서","복정","가천대","태평","모란","야탑","이매","서현","수내","정자","미금","오리","죽전","보정","구성","신갈","기흥","상갈","청명","영통","망포","매탄권선","수원시청","매교","수원","고색","오목천","어천","야목","사리","한대앞","중앙","고잔","초지","안산","신길온천","정왕","오이도","달월","월곶","소래포구","인천논현","호구포","남동인더스파크","원인재","연수","송도","인하대","숭의","신포","인천"]
arex = ["서울","공덕","홍대입구","디지털미디어시티","마곡나루","김포공항","계양","검암","청라국제도시","영종","운서","공항화물청사","인천공항1터미널","인천공항2터미널"]
ujblrt = ["발곡","회룡","범골","경전철의정부","의정부시청","흥선","의정부중앙","동오","새말","경기도청북부청사","효자","곤제","어룡","송산","탑석","차량기지임시승강장"]
everline = ["기흥(백남준아트센터)","강남대","지석","어정","동백","초당","삼가","시청.용인대","명지대","김량장","용인중앙시장(용인예술과학대)","고진","보평","둔전","전대.에버랜드"]
gyunggangline = ["판교","성남","이매","삼동","경기광주","초월","곤지암","신둔도예촌","이천","부발","세종대왕릉","여주"]
uilrt = ["북한산우이(도선사입구)","솔밭공원","4.19민주묘지(덕성여대)","가오리","화계","삼양","삼양사거리","솔샘","북한산보국문(서경대)","정릉(국민대)","성신여대입구(돈암)","보문","신설동"]
suheline = ["일산","풍산","백마","곡산","대곡","능곡","김포공항","원종","부천종합운동장","소사","소새울","시흥대야","신천","신현","시흥시청","시흥능곡","달미","선부","초지","시우","원시"]
goldline = ["양촌","구래","마산","장기","운양","걸포북변","사우(김포시청)","풍무","고촌","김포공항"]
sinlimline = ["샛강","대방(성애병원)","서울지방병무청","보라매","보라매공원","보라매병원(전문건설회관)","당곡","신림","서원","서울대벤처타운","관악산"]
gtxa = ["수서","성남","구성","동탄"]
pk = ["1호선","2호선","3호선","4호선","부산-김해경전철","동해선"]
pusanline1 = ["다대포해수욕장","다대포항","낫개","신장림","장림","동매","신평","하단","당리","사하","괴정","대티","서대신","동대신","토성","자갈치","남포","중앙","부산","초량","부산진","좌천","범일","범내골","서면","부전","양정","시청","연산","교대","동래","명륜","온천장","부산대","장전","구서","두실","남산","범어사","노포"]
pusanline2 = ["장산","중동","해운대","동백","BEXCO","센텀시티","민락","수영","광안","금련산"]
tk = ["1호선","2호선","3호선"]
dj = ["1호선"]
gj = ["1호선"]

listbox = Listbox()
listbox2 = Listbox()
listbox3=Listbox()
listbox4=Listbox()

def sel(self):
    print(listbox.curselection())
    listbox2.delete(0,END)
    for item in sgi:
        listbox2.insert(END, item)

def listwo(self):
    print(listbox.curselection())
    if(listbox2.curselection()[0]==0):
        listbox3.delete(0,END)
        for item in selineone:
            listbox3.insert(END, item)
    if(listbox2.curselection()[0]==1):
        listbox3.delete(0,END)
        for item in selinetwo:
            listbox3.insert(END, item)
    if(listbox2.curselection()[0]==2):
        listbox3.delete(0,END)
        for item in selinethree:
            listbox3.insert(END, item)

listbox2.bind("<ButtonRelease-1>",listwo)
listbox.bind("<ButtonRelease-1>", sel)
listbox.insert(0, "수도권")

listbox.pack()
listbox2.pack()
listbox3.pack()

mainloop()
