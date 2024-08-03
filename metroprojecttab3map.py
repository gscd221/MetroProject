import folium

center = [37.554530651, 126.970713923]
m=folium.Map(location=center,zoom_start=13)

byeongjeomstn = ["병점역", "서동탄역"]
exgyeongbu = ["금천구청역", "광명역"]
gyeongbustn = ["가산디지털단지역", "독산역", "금천구청역", "광명역", "석수역", "관악역", "안양역", "명학역", "금정역", "군포역", "당정역", "의왕역", "성균관대역", "화서역", "수원역", "세류역", "병점역", "서동탄역", "세마역", "오산대역", "오산역", "진위역", "송탄역", "서정리역", "평택지제역", "평택역", "성환역", "직산역", "두정역", "천안역", "봉명역", "쌍용역", "아산역", "배방역", "온양온천역", "신창역"]
sel1stn = ["연천역", "전곡역", "청산역", "소요산역", "동두천역", "보산역", "동두천중앙역", "지행역", "덕정역", "덕계역", "양주역", "녹양역", "가능역", "의정부역", "회룡역", "망월사역", "도봉산역", "도봉역", "방학역", "창동역", "녹천역", "월계역", "광운대역", "석계역", "신이문역", "외대앞역", "회기역", "청량리역", "제기동역", "신설동역", "동묘앞역", "동대문역", "종로5가역", "종로3가역", "종각역", "시청역", "서울역", "남영역", "용산역", "노량진역", "대방역", "신길역", "영등포역", "신도림역", "구로역", "구일역", "개봉역", "오류동역", "온수역", "역곡역", "소사역", "부천역", "중동역", "송내역", "부개역", "부평역", "백운역", "동암역", "간석역", "주안역", "도화역", "제물포역", "도원역", "동인천역", "인천역"]
sinjeongstn = ["신도림역", "도림천역", "양천구청역", "신정네거리역", "까치산역"]
seongsustn = ["성수역", "용답역", "신답역", "용두역", "신설동역"]
sel2stn = ["시청역", "을지로입구역", "을지로3가역", "을지로4가역", "동대문역사문화공원역", "신당역", "상왕십리역", "왕십리역", "한양대역", "뚝섬역", "성수역", "건대입구역", "구의역", "강변역", "잠실나루역", "잠실역", "잠실새내역", "종합운동장역", "삼성역", "선릉역", "역삼역", "강남역", "교대역", "서초역", "방배역", "사당역", "낙성대역", "서울대입구역", "봉천역", "신림역", "신대방역", "구로디지털단지역", "대림역", "신도림역", "문래역", "영등포구청역", "당산역", "합정역", "홍대입구역", "신촌역", "이대역", "아현역", "충정로역"]
sel3stn = ["대화역", "주엽역", "정발산역", "마두역", "백석역", "대곡역", "화정역", "원당역", "원흥역", "삼송역", "지축역", "구파발역", "연신내역", "불광역", "녹번역", "홍제역", "무악재역", "독립문역", "경복궁역", "안국역", "종로3가역", "을지로3가역", "충무로역", "동대입구역", "약수역", "금호역", "옥수역", "압구정역", "신사역", "잠원역", "고속터미널역", "교대역", "남부터미널역", "양재역", "매봉역", "도곡역", "대치역", "학여울역", "대청역", "일원역", "수서역", "가락시장역", "경찰병원역", "오금역"]
sel4stn = ["진접역", "오남역", "별내별가람역", "당고개역", "상계역", "노원역", "창동역", "쌍문역", "수유역", "미아역", "미아사거리역", "길음역", "성신여대입구역", "한성대입구역", "혜화역", "동대문역", "동대문역사문화공원역", "충무로역", "명동역", "회현역", "서울역", "숙대입구역", "삼각지역", "신용산역", "이촌역", "동작역", "이수역", "사당역", "남태령역", "선바위역", "경마공원역", "대공원역", "과천역", "정부과천청사역", "인덕원역", "평촌역", "범계역", "금정역", "산본역", "수리산역", "대야미역", "반월역", "상록수역", "한대앞역", "중앙역", "고잔역", "초지역", "안산역", "신길온천역", "정왕역", "오이도역"]
macheonstn = ["강동역", "둔촌동역", "올림픽공원역", "방이역", "오금역", "개롱역", "거여역", "마천역"]
sel5stn = ["방화역", "개화산역", "김포공항역", "송정역", "마곡역", "발산역", "우장산역", "화곡역", "까치산역", "신정역", "목동역", "오목교역", "양평역", "영등포구청역", "영등포시장역", "신길역", "여의도역", "여의나루역", "마포역", "공덕역", "애오개역", "충정로역", "서대문역", "광화문역", "종로3가역", "을지로4가역", "동대문역사문화공원역", "청구역", "신금호역", "행당역", "왕십리역", "마장역", "답십리역", "장한평역", "군자역", "아차산역", "광나루역", "천호역", "강동역", "길동역", "굽은다리역", "명일역", "고덕역", "상일동역", "강일역", "미사역", "하남풍산역", "하남시청역", "하남검단산역"]
sel6stn = ["응암역", "역촌역", "불광역", "독바위역", "연신내역", "구산역", "응암역", "새절역", "증산역", "디지털미디어시티역", "월드컵경기장역", "마포구청역", "망원역", "합정역", "상수역", "광흥창역", "대흥역", "공덕역", "효창공원앞역", "삼각지역", "녹사평역", "이태원역", "한강진역", "버티고개역", "약수역", "청구역", "신당역", "동묘앞역", "창신역", "보문역", "안암역", "고려대역", "월곡역", "상월곡역", "돌곶이역", "석계역", "태릉입구역", "화랑대역", "봉화산역", "신내역"]
sel7stn = ["장암역", "도봉산역", "수락산역", "마들역", "노원역", "중계역", "하계역", "공릉역", "태릉입구역", "먹골역", "중화역", "상봉역", "면목역", "사가정역", "용마산역", "중곡역", "군자역", "어린이대공원역", "건대입구역", "자양(뚝섬한강공원)역", "청담역", "강남구청역", "학동역", "논현역", "반포역", "고속터미널역", "내방역", "이수역", "남성역", "숭실대입구역", "상도역", "장승배기역", "신대방삼거리역", "보라매역", "신풍역", "대림역", "남구로역", "가산디지털단지역", "철산역", "광명사거리역", "천왕역", "온수역", "까치울역", "부천종합운동장역", "춘의역", "신중동역", "부천시청역", "상동역", "삼산체육관역", "굴포천역", "부평구청역", "산곡역", "석남역"]
sel8stn = ["별내역", "다산역", "동구릉역", "구리역", "장자호수공원역", "암사역사공원역", "암사역", "천호역", "강동구청역", "몽촌토성역", "잠실역", "석촌역", "송파역", "가락시장역", "문정역", "장지역", "복정역", "남위례역", "산성역", "남한산성입구역", "단대오거리역", "신흥역", "수진역", "모란역"]
sel9stn = ["개화역", "김포공항역", "공항시장역", "신방화역", "마곡나루역", "양천향교역", "가양역", "증미역", "등촌역", "염창역", "신목동역", "선유도역", "당산역", "국회의사당역", "여의도역", "샛강역", "노량진역", "노들역", "흑석역", "동작역", "구반포역", "신반포역", "고속터미널역", "사평역", "신논현역", "언주역", "선정릉역", "삼성중앙역", "봉은사역", "종합운동장역", "삼전역", "석촌고분역", "석촌역", "송파나루역", "한성백제역", "올림픽공원역", "둔촌오륜역", "중앙보훈병원역"]
icn1stn = ["계양역", "귤현역", "박촌역", "임학역", "계산역", "경인교대입구역", "작전역", "갈산역", "부평구청역", "부평시장역", "부평역", "동수역", "부평삼거리역", "간석오거리역", "인천시청역", "예술회관역", "인천터미널역", "문학경기장역", "선학역", "신연수역", "원인재역", "동춘역", "동막역", "캠퍼스타운역", "테크노파크역", "지식정보단지역", "인천대입구역", "센트럴파크역", "국제업무지구역", "송도달빛축제공원역"]
icn2stn = ["검단오류역", "왕길역", "검단사거리역", "마전역", "완정역", "독정역", "검암역", "검바위역", "아시아드경기장역", "서구청역", "가정역", "가정중앙시장이역", "석남역", "서부여성회관역", "인천가좌역", "가재울역", "주안국가산단역", "주안역", "시민공원역", "석바위시장역", "인천시청역", "석천사거리역", "모래내시장역", "만수역", "남동구청역", "인천대공원역", "운연역"]
suinbundangstn = ["청량리역", "왕십리역", "서울숲역", "압구정로데오역", "강남구청역", "선정릉역", "선릉역", "한티역", "도곡역", "구룡역", "개포동역", "대모산입구역", "수서역", "복정역", "가천대역", "태평역", "모란역", "야탑역", "이매역", "서현역", "수내역", "정자역", "미금역", "오리역", "죽전역", "보정역", "구성역", "신갈역", "기흥역", "상갈역", "청명역", "영통역", "망포역", "매탄권선역", "수원시청역", "매교역", "수원역", "고색역", "오목천역", "어천역", "야목역", "사리역", "한대앞역", "중앙역", "고잔역", "초지역", "안산역", "신길온천역", "정왕역", "오이도역", "달월역", "월곶역", "소래포구역", "인천논현역", "호구포역", "남동인더스파크역", "원인재역", "연수역", "송도역", "인하대역", "숭의역", "신포역", "인천역"]
sinbundangstn = ["신사역", "논현역", "신논현역", "강남역", "양재(서초구청)역", "양재시민의숲(매헌)역", "청계산입구역", "판교역", "정자역", "미금역", "동천역", "수지구청역", "성복역", "상현역", "광교중앙역", "광교역"]
gyeonguistn = ["가좌역","신촌역","서울역"]
gyeonguijungangstn = ["임진강역", "운천역", "문산역", "파주역", "월롱역", "금촌역", "금릉역", "운정역", "야당역", "탄현역", "일산역", "풍산역", "백마역", "곡산역", "대곡역", "능곡역", "행신역", "강매역", "한국항공대역", "수색역", "디지털미디어시티역", "가좌역", "홍대입구역", "서강대역", "공덕역", "효창공원앞역", "용산역", "이촌역", "서빙고역", "한남역", "옥수역", "응봉역", "왕십리역", "청량리역", "회기역", "중랑역", "상봉역", "망우역", "양원역", "구리역", "도농역", "양정역", "덕소역", "도심역", "팔당역", "운길산역", "양수역", "신원역", "국수역", "아신역", "오빈역", "양평역", "원덕역", "용문역", "지평역"]
mangwoostn = ["광운대역","상봉역","망우역"]
gyeongchunstn = ["청량리역", "회기역", "중랑역", "상봉역", "망우역", "신내역", "갈매역", "별내역", "퇴계원역", "사릉역", "금곡역", "평내호평역", "천마산역", "마석역", "대성리역", "청평역", "상천역", "가평역", "굴봉산역", "백양리역", "강촌역", "김유정역", "남춘천역", "춘천역"]
arexstn = ["서울역", "공덕역", "홍대입구역", "디지털미디어시티역", "마곡나루역", "김포공항역", "계양역", "검암역", "청라국제도시역", "영종역", "운서역", "공항화물청사역", "인천공항1터미널역", "인천공항2터미널역"]
uijeongbustn = ["발곡역", "회룡역", "범골역", "경전철의정부역", "의정부시청역", "흥선역", "의정부중앙역", "동오역", "새말역", "경기도청북부청사역", "효자역", "곤제역", "어룡역", "송산역", "탑석역", "차량기지 임시승강장"]
yonginstn = ["기흥역", "강남대역", "지석역", "어정역", "동백역", "초당역", "삼가역", "시청·용인대역", "명지대역", "김량장역", "용인중앙시장역", "고진역", "보평역", "둔전역", "전대·에버랜드역"]
gyeonggangstn = ["판교역", "성남역", "이매역", "삼동역", "경기광주역", "초월역", "곤지암역", "신둔도예촌역", "이천역", "부발역", "세종대왕릉역", "여주역"]
uistn = ["북한산우이역","솔밭공원역","4.19민주묘지역","가오리역","화계역","삼양역","삼양사거리역","솔샘역","북한산보국문역","정릉역","성신여대입구역","보문역","신설동역"]
seohaestn  = ["일산역", "풍산역", "백마역", "곡산역", "대곡역","능곡역","김포공항역","원종역","부천종합운동장역","소사역","소새울역","시흥대야역","신천역","신현역","시흥시청역","시흥능곡역","달미역","선부역","초지역","시우역","원시역"]
gimpostn = ["양촌역","구래역","마산역","장기역","운양역","걸포북변역","사우(김포시청)역","풍무역","고촌역","김포공항역"]
sinlimstn = ["샛강역","대방역","서울지방병무청역","보라매역","보라매공원역","보라매병원역","당곡역","신림역","서원역","서울대벤처타운역",'관악산(서울대)역']
gtx_astn = ["수서역","성남역","구성역","동탄역"]

seoulline3 = [[37.676200421, 126.747511311], [37.670174410, 126.761224056], [37.659620754, 126.773304954], [37.652051940, 126.777736096], [37.643016055, 126.788051193], [37.631956474, 126.809858189], [37.634681479, 126.832587791], [37.653102738, 126.842892677], [37.650738823, 126.872834782], [37.653109308, 126.895550254], [37.648105616, 126.913848936], [37.636966220, 126.918818537], [37.618484691, 126.920403162], [37.610849993, 126.929330306], [37.600910147, 126.935810084], [37.588687989, 126.944267066], [37.582482840, 126.950294691], [37.574376909, 126.958065735], [37.575832064, 126.973856905], [37.576536842, 126.985482839], [37.572583105, 126.990414851], [37.566383287, 126.992604455], [37.561261210, 126.994172534], [37.559112355, 127.005360436], [37.553952702, 127.010171252], [37.548299438, 127.015849830], [37.540429916, 127.018709461], [37.526362213, 127.028476085], [37.516152086, 127.019497385], [37.512886090, 127.011391496], [37.505990498, 127.004280784], [37.492883501, 127.013853578], [37.485026405, 127.016271761], [37.483523265, 127.035078348], [37.486946472, 127.046654070], [37.491083969, 127.055362094], [37.494489232, 127.063179939], [37.496854427, 127.071018712], [37.493659417, 127.079564537], [37.484019706, 127.084512236], [37.486829966, 127.101383991], [37.493123556, 127.118286530], [37.495796771, 127.124279916], [37.502164089, 127.127950435]]
seoulline4 = [[37.719510972, 127.203284938], [37.705533086, 127.191731897], [37.667603585, 127.115521464], [37.670225173, 127.079061244], [37.660626672, 127.073333424], [37.654639037, 127.060514872], [37.653233719, 127.047777802], [37.648517160, 127.034630307], [37.637797794, 127.025414191], [37.626526308, 127.026112696], [37.613325895, 127.030072215], [37.603344115, 127.024994781], [37.592356890, 127.016539959], [37.588525294, 127.006115480], [37.582083337, 127.001914726], [37.570883623, 127.009328824], [37.564645584, 127.005713128], [37.561261210, 126.994172534], [37.560954203, 126.986147976], [37.558565370, 126.978248589], [37.553263391, 126.969793498], [37.544661674, 126.972096886], [37.535558663, 126.974149586], [37.529190431, 126.967905391], [37.522408422, 126.973602647], [37.502848520, 126.977986269], [37.485306540, 126.981654803], [37.477439613, 126.981703362], [37.464685558, 126.988692120], [37.452245917, 127.001891634], [37.443978868, 127.007846802], [37.435779705, 127.006591725], [37.432799728, 126.996566564], [37.425989843, 126.989127260], [37.401529870, 126.976662056], [37.394250876, 126.963778937], [37.389781635, 126.950834369], [37.371838475, 126.943650313], [37.358048376, 126.933062953], [37.350249976, 126.925524880], [37.327988775, 126.916892698], [37.312291793, 126.903711467], [37.302848978, 126.866603108], [37.309825661, 126.853618315], [37.316032200, 126.838545702], [37.316839102, 126.823122233], [37.320202241, 126.808131314], [37.327243997, 126.788910350], [37.337506879, 126.767367673], [37.351836439, 126.742808813], [37.361927530, 126.738518735]]
macheonbranchline = [[37.535879184, 127.132420621], [37.527662237, 127.136224276], [37.516363615, 127.130485047], [37.508707408, 127.126067133], [37.502164089, 127.127950435], [37.498002530, 127.135067786], [37.493316022, 127.143783426], [37.495003087, 127.152810603]]
seoulline5 = [[37.577557216, 126.812798469], [37.572365848, 126.806194994], [37.562291758, 126.802921066], [37.561180919, 126.812341450], [37.560265469, 126.824926588], [37.558639303, 126.837628971], [37.548753560, 126.836320751], [37.541654832, 126.840443702], [37.531816382, 126.846748039], [37.525022134, 126.856036962], [37.526131449, 126.864570411], [37.524552881, 126.875190195], [37.525591310, 126.886371186], [37.524225544, 126.895310221], [37.522720157, 126.905131476], [37.517677463, 126.914877170], [37.521715859, 126.924290018], [37.527118100, 126.932956014], [37.539617153, 126.945979636], [37.544561510, 126.951447204], [37.553375302, 126.956652975], [37.560378214, 126.963009680], [37.565731208, 126.966617760], [37.571648599, 126.976372775], [37.572583105, 126.990414851], [37.567330674, 126.998050279], [37.564645584, 127.005713128], [37.560313373, 127.013816536], [37.554485205, 127.020481285], [37.557339474, 127.029434305], [37.561431868, 127.038589542], [37.566138049, 127.043003531], [37.567008153, 127.052546019], [37.561619242, 127.063639796], [37.557199218, 127.079545751], [37.552272627, 127.089524808], [37.545291995, 127.103485810], [37.538033508, 127.123234069], [37.535879184, 127.132420621], [37.537843606, 127.140021894], [37.545521189, 127.142887841], [37.551376274, 127.144042006], [37.555039624, 127.154115763], [37.556681487, 127.165900673], [37.557465805, 127.175864188], [37.563132227, 127.192968763], [37.552125316, 127.203912245], [37.541682994, 127.206869475], [37.539809355, 127.223249315]]
seoulline6 = [[37.598429768, 126.915504322], [37.606304968, 126.922879337], [37.610849993, 126.929330306], [37.618415966, 126.933061013], [37.618484691, 126.920403162], [37.611229571, 126.917256665], [37.598429768, 126.915504322], [37.590751901, 126.913542857], [37.583694046, 126.909429955], [37.577554421, 126.897806812], [37.569648162, 126.899078322], [37.563425990, 126.903512265], [37.556034031, 126.910131170], [37.549328709, 126.913624675], [37.547767159, 126.922543620], [37.547502768, 126.932145632], [37.547638878, 126.942437550], [37.542389384, 126.952451437], [37.538687088, 126.962532447], [37.535558663, 126.974149586], [37.534752072, 126.986499322], [37.534522948, 126.994243914], [37.539708333, 127.001750990], [37.548105481, 127.006520975], [37.553952702, 127.010171252], [37.560313373, 127.013816536], [37.566156037, 127.016160639], [37.572156726, 127.015726121], [37.579418797, 127.015308772], [37.584995315, 127.019583897], [37.586331295, 127.029230599], [37.590284815, 127.035889839], [37.601725616, 127.041359329], [37.606574577, 127.048870540], [37.610522071, 127.056370720], [37.614769726, 127.066035276], [37.618424358, 127.075431317], [37.619835683, 127.083562759], [37.617338639, 127.091403709], [37.612691611, 127.103232276]]
seoulline7 = [[37.700119503, 127.053130257], [37.689101071, 127.046603267], [37.677846324, 127.055358878], [37.665272031, 127.057695673], [37.654639037, 127.060514872], [37.645046151, 127.064149978], [37.636457597, 127.068028649], [37.625588720, 127.073025701], [37.618424358, 127.075431317], [37.610602262, 127.077767833], [37.602510333, 127.079333509], [37.596725984, 127.085759161], [37.588791454, 127.087527670], [37.581033170, 127.088514853], [37.573916767, 127.086559368], [37.565953590, 127.084320325], [37.557199218, 127.079545751], [37.547850180, 127.074454848], [37.540815459, 127.071075946], [37.531321473, 127.066688539], [37.519399039, 127.053228093], [37.516714253, 127.041482039], [37.514298092, 127.031688100], [37.511115491, 127.021564717], [37.508138910, 127.011519428], [37.505990498, 127.004280784], [37.487488201, 126.993074416], [37.485306540, 126.981654803], [37.484817850, 126.970958810], [37.496237122, 126.953697779], [37.502848133, 126.947993764], [37.504844035, 126.938944627], [37.499774296, 126.928126112], [37.500990611, 126.920685467], [37.500131159, 126.909827842], [37.492732036, 126.896561308], [37.486290468, 126.887400303], [37.480384140, 126.882547586], [37.476197255, 126.868128490], [37.479299250, 126.854906520], [37.486810631, 126.838677809], [37.492113429, 126.823197389], [37.506303529, 126.811084958], [37.505006930, 126.797392847], [37.503730780, 126.787024811], [37.503071019, 126.776180967], [37.504741144, 126.763972865], [37.505818168, 126.753112053], [37.506515181, 126.741980800], [37.507050020, 126.731313635], [37.508164904, 126.720587607], [37.508692342, 126.702531136], [37.507320810, 126.676265350]]
seoulline8 = [[37.642112682, 127.126970642], [37.624089908, 127.149731930], [37.611309243, 127.138048693], [37.603209077, 127.143306700], [37.587689861, 127.137957068], [37.557185993, 127.137499269], [37.550165411, 127.127520372], [37.538033508, 127.123234069], [37.529963545, 127.120324541], [37.517708490, 127.112635577], [37.514634749, 127.104260695], [37.505183318, 127.107244893], [37.499607630, 127.112303042], [37.493123556, 127.118286530], [37.486109492, 127.122436395], [37.478591098, 127.126222853], [37.470591857, 127.126718104], [37.462882421, 127.139002132], [37.457073779, 127.150340094], [37.451808327, 127.159902088], [37.445045887, 127.156791310], [37.440967152, 127.147573249], [37.437389621, 127.140594418], [37.432129498, 127.129138960]]
seoulline9 = [[37.578511748, 126.797473364], [37.562291758, 126.802921066], [37.563727983, 126.810617468], [37.567482065, 126.817246640], [37.565304182, 126.827148847], [37.568017969, 126.842096688], [37.561357605, 126.854560787], [37.558143814, 126.860588069], [37.558143814, 126.860588069], [37.558143814, 126.860588069], [37.544171297, 126.883149157], [37.538090340, 126.893511603], [37.533615666, 126.902546562], [37.528086192, 126.917917078], [37.521697747, 126.924145806], [37.517415856, 126.929530814], [37.513598348, 126.941018722], [37.512896618, 126.953461271], [37.508971822, 126.963676922], [37.502848520, 126.977986269], [37.501390255, 126.987265873], [37.503566812, 126.996273520], [37.505990498, 127.004280784], [37.504241637, 127.015273617], [37.504370023, 127.024497017], [37.507373216, 127.034048978], [37.510825402, 127.043673035], [37.512934472, 127.052929418], [37.514255453, 127.060226017], [37.511444073, 127.076251001], [37.504385920, 127.088083605], [37.502459186, 127.096920768], [37.505183318, 127.107244893], [37.510888352, 127.112655539], [37.515581466, 127.115522417], [37.516363615, 127.130485047], [37.519411170, 127.138820852], [37.528419263, 127.148551941]]
incheonline1 = [[37.571790263, 126.736394447], [37.566428456, 126.742623211], [37.566428456, 126.742623211], [37.566428456, 126.742623211], [37.543320492, 126.727698356], [37.538082875, 126.722614484], [37.538082875, 126.722614484], [37.516852752, 126.721516693], [37.508164904, 126.720587607], [37.498330012, 126.722309249], [37.490196614, 126.723447491], [37.485481820, 126.718557747], [37.477722053, 126.710232036], [37.466985257, 126.707877045], [37.456907591, 126.701167284], [37.448650389, 126.700941618], [37.441822016, 126.699674928], [37.435154232, 126.697792015], [37.426935308, 126.698898357], [37.417984396, 126.693895923], [37.413219999, 126.686484049], [37.404718350, 126.680803006], [37.397832041, 126.673276832], [37.388019254, 126.661812800], [37.382074016, 126.656081001], [37.377664489, 126.645725155], [37.386029778, 126.639537434], [37.392948615, 126.634812147], [37.399814267, 126.630430711], [37.407259230, 126.625838193]]
incheonline2 = [[37.594957647, 126.627903744], [37.595128706, 126.642436327], [37.601648268, 126.656396269], [37.597831453, 126.667001483], [37.592843354, 126.673041857], [37.584922741, 126.675974871], [37.569173744, 126.673637743], [37.561086855, 126.677560803], [37.551318882, 126.677121930], [37.543929958, 126.676842622], [37.524748211, 126.675375547], [37.517661325, 126.676825853], [37.507320810, 126.676265350], [37.500255830, 126.675854805], [37.489825041, 126.675244056], [37.484104406, 126.683822201], [37.473965649, 126.681236505], [37.465170291, 126.679007466], [37.458404557, 126.680980442], [37.457691218, 126.692291667], [37.456907591, 126.701167284], [37.456778226, 126.710735291], [37.455871765, 126.719690186], [37.454981115, 126.731922432], [37.448175705, 126.736698840], [37.448494324, 126.752813199], [37.439619834, 126.759599698]]
suinbundangline = [[37.580565478, 127.048188418], [37.561431868, 127.038589542], [37.543574174, 127.044727503], [37.527441001, 127.040588586], [37.516714253, 127.041482039], [37.510825402, 127.043673035], [37.504664971, 127.048936922], [37.496270382, 127.052923309], [37.491083969, 127.055362094], [37.487047755, 127.059381584], [37.489112052, 127.066006480], [37.491522656, 127.072971306], [37.487260862968,127.10155515462], [37.470591857, 127.126718104], [37.448665752, 127.126703714], [37.439816679, 127.127739682], [37.432129498, 127.129138960], [37.411451592, 127.128730699], [37.394705393, 127.127329941], [37.384989791, 127.123389658], [37.378443999, 127.114278647], [37.367571801, 127.108516029], [37.350048635, 127.108993049], [37.339812976, 127.108955686], [37.324366181, 127.107438437], [37.312561807, 127.108355125], [37.298340438,127.104203899], [37.286156486, 127.111268974], [37.275479596, 127.116678079], [37.261828427, 127.108817882], [37.259495898, 127.078930063], [37.251391382, 127.071245584], [37.245848709, 127.056903817], [37.252601950, 127.040719662], [37.261966824, 127.030646396], [37.265519838, 127.015834058], [37.266268761, 127.000188838], [37.249794107, 126.980774942], [37.243623717, 126.964435320], [37.250126306, 126.908915871], [37.261440108, 126.884214812], [37.291100239, 126.857242222], [37.309825661, 126.853618315], [37.316032200, 126.838545702], [37.316839102, 126.823122233], [37.320202241, 126.808131314], [37.327243997, 126.788910350], [37.337506879, 126.767367673], [37.351836439, 126.742808813], [37.361927530, 126.738518735], [37.379905046, 126.745679668], [37.391875420, 126.742697493], [37.400946503, 126.733574789], [37.400632537, 126.722428743], [37.401671674, 126.708679951], [37.407737737, 126.695260548], [37.413219999, 126.686484049], [37.417799563, 126.678986647], [37.429781229, 126.654375724], [37.448327436, 126.649791158], [37.460785827, 126.638469628], [37.468517699, 126.624420894], [37.476428580, 126.617417216]]
sinbundangline = [[37.516152086, 127.019497385], [37.511115491, 127.021564717], [37.504370023, 127.024497017], [37.496486063, 127.028361548], [37.483523265, 127.035078348], [37.470016063, 127.038508586], [37.448457483, 127.054658245], [37.394766715, 127.111197814], [37.367571801, 127.108516029], [37.350048635, 127.108993049], [37.337878960, 127.102864848], [37.322514177, 127.094698076], [37.313388355, 127.080280861], [37.297744299, 127.069312703], [37.288472630, 127.051666616], [37.301776947, 127.044916648]]
gyeonguiline = [[37.568782058, 126.914762449], [37.559901686, 126.942906303], [37.553263391, 126.969793498]]
gyeonguijungangline = [[37.888599396, 126.746922571], [37.879685153, 126.770180599], [37.854648387, 126.787324393], [37.815225820, 126.792798680], [37.796340810, 126.792056413], [37.766218578, 126.774569926], [37.751464563, 126.765217517], [37.725401277, 126.767128199], [37.712961221, 126.761541889], [37.694053312, 126.761052545], [37.682208866, 126.769541935], [37.672311739, 126.786348404], [37.658171992, 126.794588276], [37.645746291, 126.801806356], [37.631956474, 126.809858189], [37.619184431, 126.821013810], [37.612175933, 126.834157342], [37.612641672, 126.845386023], [37.603290386, 126.868490516], [37.580982041, 126.895762897], [37.577554421, 126.897806812], [37.568782058, 126.914762449], [37.557434302, 126.926960224], [37.552502661, 126.934998613], [37.542389384, 126.952451437], [37.538687088, 126.962532447], [37.529521713, 126.964540921], [37.522408422, 126.973602647], [37.519910625, 126.989530775], [37.529089761, 127.008281374], [37.540429916, 127.018709461], [37.550868740, 127.035172128], [37.561431868, 127.038589542], [37.580565478, 127.048188418], [37.589584585, 127.057846664], [37.594930730, 127.075936961], [37.596725984, 127.085759161], [37.599980839, 127.091716530], [37.606656838, 127.108080981], [37.603209077, 127.143306700], [37.608812677, 127.161194605], [37.604361340, 127.194389102], [37.586825750, 127.208931975], [37.579574207, 127.222921405], [37.546944134, 127.243719241], [37.554714782, 127.310170795], [37.545995845, 127.329145313], [37.525547738, 127.373084723], [37.515910425, 127.399601317], [37.513718902, 127.443125486], [37.505846530, 127.473858433], [37.492760023, 127.491381934], [37.468494597, 127.547082229], [37.482510789, 127.594404665], [37.476876007, 127.629660854]]
mangwooline = [[37.623662704, 127.061441277], [37.596725984, 127.085759161], [37.599980839, 127.091716530]]
gyeongchunline = [[37.580565478, 127.048188418], [37.589584585, 127.057846664], [37.594930730, 127.075936961], [37.596725984, 127.085759161], [37.599980839, 127.091716530], [37.612691611, 127.103232276], [37.633953300, 127.114721194], [37.642112682, 127.126970642], [37.648224378, 127.143949803], [37.651477117, 127.176931857], [37.637447609, 127.208044054], [37.653248185, 127.244645610], [37.658989574, 127.285769252], [37.652342060, 127.311773346], [37.683926439, 127.379217599], [37.735561128, 127.426617729], [37.770338581, 127.454244548], [37.814230152, 127.511029576], [37.832134947, 127.557067520], [37.830821416, 127.589090374], [37.805987187, 127.634143907], [37.818072314, 127.714581835], [37.864004001, 127.723849390], [37.884621359, 127.717298987]]
arex = [[37.553263391, 126.969793498], [37.542389384, 126.952451437], [37.557434302, 126.926960224], [37.577554421, 126.897806812], [37.565304182, 126.827148847], [37.562291758, 126.802921066], [37.571790263, 126.736394447], [37.569173744, 126.673637743], [37.555150591, 126.625346018], [37.512064848, 126.524258616], [37.492783735, 126.493695906], [37.459047502, 126.477534573], [37.447145682, 126.452744135], [37.468741034, 126.433512468]]
uijeongbulrt = [[37.726924680, 127.052921115], [37.724974282, 127.047129084], [37.728786722, 127.043671683], [37.737183901, 127.043307905], [37.739186854, 127.034862534], [37.743263040, 127.037150639], [37.743672860, 127.049705119], [37.745205753, 127.056910960], [37.748860205, 127.063710447], [37.750774748, 127.071581245], [37.754010134, 127.077269464], [37.750577498, 127.083790411], [37.742706527, 127.085205434], [37.737267664, 127.087275326], [37.733495862, 127.088938523], [37.728747516, 127.094956017]]
yongineverline = [[37.275479596, 127.116678079], [37.270187633, 127.126055928], [37.269698357, 127.136624880], [37.274934002, 127.143726441], [37.269097527, 127.152712260], [37.260790028, 127.159470611], [37.242112987, 127.168098117], [37.239340016, 127.178865974], [37.237993277, 127.190222637], [37.237218208, 127.198560171], [37.237776798, 127.209064952], [37.244584068, 127.214172459], [37.258938782, 127.218496759], [37.267219190, 127.213644661], [37.285418481, 127.219492350]]
gyeonggangline = [[37.394766715, 127.111197814], [37.394724096, 127.119652136], [37.394705393, 127.127329941], [37.408713575, 127.203347840], [37.398972102, 127.253115616], [37.373381654, 127.299975795], [37.350563222, 127.346165111], [37.315541926, 127.405247699], [37.264586599, 127.442295690], [37.259846556, 127.490481984], [37.293947006, 127.570674983], [37.282547913, 127.628695040]]
uisinseolline = [[37.662949661, 127.012736174], [37.655899422, 127.013250602], [37.649565464, 127.013685743], [37.641559825, 127.016766139], [37.634126592, 127.017500871], [37.626923111, 127.018139223], [37.621336605, 127.020493947], [37.620265436, 127.013510463], [37.612175045, 127.008259432], [37.602655602, 127.013535589], [37.592356890, 127.016539959], [37.584995315, 127.019583897], [37.576516310, 127.023192923]]
seohaeline = [[37.682208866, 126.769541935], [37.672311739, 126.786348404], [37.658171992, 126.794588276], [37.645746291, 126.801806356], [37.631956474, 126.809858189], [37.619184431, 126.821013810], [37.562291758, 126.802921066], [37.524031758, 126.804871934], [37.505006930, 126.797392847], [37.482745711, 126.795215545], [37.468517256, 126.797179359], [37.450038976, 126.792949323], [37.439233885, 126.786786811], [37.409493265, 126.787853819], [37.381466607, 126.805976005], [37.370019780, 126.808734618], [37.349111858, 126.809405677], [37.334351650, 126.809964863], [37.320202241, 126.808131314], [37.313156091, 126.795759123], [37.302572476, 126.786718498]]
gimpoline = [[37.641661112, 126.614805425], [37.645343361, 126.628350334], [37.640514268, 126.643545347], [37.644017801, 126.668965465], [37.653914201, 126.683926788], [37.631663805, 126.705772203], [37.620366709, 126.719802610], [37.612356452, 126.732559687], [37.601348458, 126.770248528], [37.562291758, 126.802921066]]
sinlimline=[[37.516583192, 126.929207206], [37.512880035, 126.925483346], [37.504354053, 126.922029926], [37.500990611, 126.920685467], [37.495919799, 126.918117949], [37.492804242, 126.924782263], [37.490272954, 126.927529428], [37.484171739, 126.929784067], [37.478070329, 126.933425794], [37.472147062, 126.933816904], [37.468660507, 126.945355066]]
gtx_aline=[[37.487260862968,127.10155515462],[37.394724096,127.119652136],[37.298340438,127.104203899],[37.200138454,127.09553409]]

for i in range(4):
    folium.Marker(gtx_aline[i],popup="표시",tooltip=gtx_astn[i]).add_to(m)
for i in range(11):
    folium.Marker(sinlimline[i],popup="표시",tooltip=sinlimstn[i]).add_to(m)
for i in range(10):
    folium.Marker(gimpoline[i],popup="표시",tooltip=gimpostn[i]).add_to(m)
for i in range(21):
    folium.Marker(seohaeline[i],popup="표시",tooltip=seohaestn[i]).add_to(m)
for i in range(13):
    folium.Marker(uisinseolline[i],popup="표시",tooltip=uistn[i]).add_to(m)
for i in range(12):
    folium.Marker(gyeonggangline[i],popup="표시",tooltip=gyeonggangstn[i]).add_to(m)
for i in range(15):
    folium.Marker(yongineverline[i],popup="표시",tooltip=yonginstn[i]).add_to(m)
for i in range(16):
    folium.Marker(uijeongbulrt[i],popup="표시",tooltip=uijeongbustn[i]).add_to(m)
for i in range(14):
    folium.Marker(arex[i],popup="표시",tooltip=arexstn[i]).add_to(m)
for i in range(24):
    folium.Marker(gyeongchunline[i],popup="표시",tooltip=gyeongchunstn[i]).add_to(m)
for i in range(3):
    folium.Marker(mangwooline[i],popup="표시",tooltip=mangwoostn[i]).add_to(m)
for i in range(55):
    folium.Marker(gyeonguijungangline[i],popup="표시",tooltip=gyeonguijungangstn[i]).add_to(m)
for i in range(3):
    folium.Marker(gyeonguiline[i],popup="표시",tooltip=gyeonguistn[i]).add_to(m)
for i in range(16):
    folium.Marker(sinbundangline[i],popup="표시",tooltip=sinbundangstn[i]).add_to(m)
for i in range(63):
    folium.Marker(suinbundangline[i],popup="표시",tooltip=suinbundangstn[i]).add_to(m)
for i in range(27):
    folium.Marker(incheonline2[i],popup="표시",tooltip=icn2stn[i]).add_to(m)
for i in range(30):
    folium.Marker(incheonline1[i],popup="표시",tooltip=icn1stn[i]).add_to(m)
for i in range(38):
    folium.Marker(seoulline9[i],popup="표시",tooltip=sel9stn[i]).add_to(m)
for i in range(24):
    folium.Marker(seoulline8[i],popup="표시",tooltip=sel8stn[i]).add_to(m)
for i in range(53):
    folium.Marker(seoulline7[i],popup="표시",tooltip=sel7stn[i]).add_to(m)
for i in range(39):
    folium.Marker(seoulline6[i],popup="표시",tooltip=sel6stn[i]).add_to(m)
for i in range(49):
    folium.Marker(seoulline5[i],popup="표시",tooltip=sel5stn[i]).add_to(m)
for i in range(8):
    folium.Marker(macheonbranchline[i],popup="표시",tooltip=macheonstn[i]).add_to(m)
for i in range(51):
    folium.Marker(seoulline4[i],popup="표시",tooltip=sel4stn[i]).add_to(m)
for i in range(44):
    folium.Marker(seoulline3[i],popup="표시",tooltip=sel3stn[i]).add_to(m)

folium.PolyLine(locations=suinbundangline,color="#FABE00",).add_to(m)
folium.PolyLine(locations=gtx_aline,color="#9A6292",).add_to(m)
folium.PolyLine(locations=sinlimline,color="#6789CA",).add_to(m)
folium.PolyLine(locations=gimpoline,color="#AD8605",).add_to(m)
folium.PolyLine(locations=seohaeline,color="#8FC31F",).add_to(m)
folium.PolyLine(locations=uisinseolline,color="#B7C450",).add_to(m)
folium.PolyLine(locations=gyeonggangline,color="#0054A6",).add_to(m)
folium.PolyLine(locations=yongineverline,color="#56AD2D",).add_to(m)
folium.PolyLine(locations=uijeongbulrt,color="#FD8100",).add_to(m)
folium.PolyLine(locations=arex,color="#0090D2",).add_to(m)
folium.PolyLine(locations=gyeongchunline,color="#178C72",).add_to(m)
folium.PolyLine(locations=mangwooline,color="#178C72",).add_to(m)
folium.PolyLine(locations=gyeonguijungangline,color="#77C4A3",).add_to(m)
folium.PolyLine(locations=gyeonguiline,color="#77C4A3",).add_to(m)
folium.PolyLine(locations=sinbundangline,color="#D31145",).add_to(m)
folium.PolyLine(locations=incheonline2,color="#F5A251",).add_to(m)
folium.PolyLine(locations=incheonline1,color="#759CCE",).add_to(m)
folium.PolyLine(locations=seoulline9,color="#BDB092",).add_to(m)
folium.PolyLine(locations=seoulline8,color="#E6186C",).add_to(m)
folium.PolyLine(locations=seoulline7,color="#747F00",).add_to(m)
folium.PolyLine(locations=seoulline6,color="#CD7C2F",).add_to(m)
folium.PolyLine(locations=seoulline5,color="#996CAC",).add_to(m)
folium.PolyLine(locations=macheonbranchline,color="#996CAC",).add_to(m)
folium.PolyLine(locations=seoulline4,color="#00A4E3",).add_to(m)
folium.PolyLine(locations=seoulline3,color="#EF7C1C",).add_to(m)

m.save("seoulmap.html")