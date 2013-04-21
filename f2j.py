# -*- coding: utf-8 -*-

# class Jianti:
# To translate the traditional chinese words to simplyfied ones

import sys
from sys import argv, exit, stdout, stderr
import os

# a mapping table from Wikipedia, maybe the best 

table = {
"錒":"锕",
"鎄":"锿",
"皚":"皑",
"噯":"嗳",
"藹":"蔼",
"靄":"霭",
"愛":"爱",
"嬡":"嫒",
"礙":"碍",
"曖":"暧",
"璦":"瑷",
"菴":"庵",
"諳":"谙",
"鵪":"鹌",
"鞌":"鞍",
"垵":"埯",
"銨":"铵",
"闇":"暗",
"晻":"暗",
"翶":"翱",
"翺":"翱",
"鰲":"鳌",
"鼇":"鳌",
"襖":"袄",
"媼":"媪",
"嶴":"岙",
"奧":"奥",
"驁":"骜",
"鈀":"钯",
"垻":"坝",
"壩":"坝",
"罷":"罢",
"鮁":"鲅",
"覇":"霸",
"擺":"摆",
"唄":"呗",
"敗":"败",
"粺":"稗",
"頒":"颁",
"岅":"坂",
"闆":"板",
"鈑":"钣",
"辦":"办",
"絆":"绊",
"幫":"帮",
"綁":"绑",
"牓":"榜",
"艕":"膀",
"謗":"谤",
"鎊":"镑",
"齙":"龅",
"裦":"褒",
"寶":"宝",
"飽":"饱",
"鴇":"鸨",
"緥":"褓",
"報":"报",
"鮑":"鲍",
"盃":"杯",
"桮":"杯",
"鵯":"鹎",
"貝":"贝",
"狽":"狈",
"備":"备",
"揹":"背",
"鋇":"钡",
"誖":"悖",
"憊":"惫",
"輩":"辈",
"韝":"鞴",
"逩":"奔",
"犇":"奔",
"賁":"贲",
"錛":"锛",
"綳":"绷",
"繃":"绷",
"偪":"逼",
"粃":"秕",
"筆":"笔",
"幣":"币",
"畢":"毕",
"閉":"闭",
"嗶":"哔",
"蓽":"荜",
"斃":"毙",
"鉍":"铋",
"篳":"筚",
"潷":"滗",
"痺":"痹",
"蹕":"跸",
"闢":"辟",
"獘":"弊",
"邊":"边",
"籩":"笾",
"編":"编",
"鯿":"鳊",
"貶":"贬",
"變":"变",
"緶":"缏",
"辯":"辩",
"辮":"辫",
"標":"标",
"颮":"飑",
"驃":"骠",
"臕":"膘",
"鏢":"镖",
"飆":"飙",
"飇":"飙",
"飈":"飚",
"鑣":"镳",
"錶":"表",
"鰾":"鳔",
"鱉":"鳖",
"鼈":"鳖",
"別":"别",
"彆":"别",
"癟":"瘪",
"賓":"宾",
"賔":"宾",
"儐":"傧",
"濱":"滨",
"繽":"缤",
"檳":"槟",
"鑌":"镔",
"瀕":"濒",
"擯":"摈",
"殯":"殡",
"臏":"膑",
"髕":"髌",
"髩":"鬓",
"鬢":"鬓",
"氷":"冰",
"餅":"饼",
"稟":"禀",
"並":"并",
"併":"并",
"竝":"并",
"撥":"拨",
"剝":"剥",
"缽":"钵",
"鉢":"钵",
"餑":"饽",
"駁":"驳",
"駮":"驳",
"鈸":"钹",
"鉑":"铂",
"愽":"博",
"鵓":"鹁",
"鈽":"钸",
"蔔":"卜",
"補":"补",
"佈":"布",
"鈈":"钚",
"財":"财",
"埰":"采",
"寀":"采",
"採":"采",
"綵":"彩",
"倸":"睬",
"跴":"踩",
"參":"参",
"葠":"参",
"蓡":"参",
"驂":"骖",
"殘":"残",
"蠶":"蚕",
"慚":"惭",
"慙":"惭",
"慘":"惨",
"黲":"黪",
"燦":"灿",
"倉":"仓",
"傖":"伧",
"滄":"沧",
"蒼":"苍",
"艙":"舱",
"撡":"操",
"艸":"艹",
"冊":"册",
"側":"侧",
"厠":"厕",
"廁":"厕",
"惻":"恻",
"測":"测",
"筞":"策",
"筴":"策",
"層":"层",
"挿":"插",
"餷":"馇",
"鍤":"锸",
"査":"查",
"詧":"察",
"鑔":"镲",
"詫":"诧",
"釵":"钗",
"儕":"侪",
"蠆":"虿",
"覘":"觇",
"摻":"掺",
"攙":"搀",
"嬋":"婵",
"讒":"谗",
"禪":"禅",
"饞":"馋",
"纏":"缠",
"蟬":"蝉",
"鐔":"镡",
"產":"产",
"産":"产",
"諂":"谄",
"剷":"铲",
"鏟":"铲",
"闡":"阐",
"蕆":"蒇",
"囅":"冁",
"懺":"忏",
"顫":"颤",
"倀":"伥",
"閶":"阊",
"鯧":"鲳",
"長":"长",
"腸":"肠",
"萇":"苌",
"嘗":"尝",
"嚐":"尝",
"償":"偿",
"厰":"厂",
"廠":"厂",
"塲":"场",
"場":"场",
"悵":"怅",
"暢":"畅",
"鈔":"钞",
"車":"车",
"硨":"砗",
"撦":"扯",
"徹":"彻",
"塵":"尘",
"陳":"陈",
"訦":"谌",
"諶":"谌",
"硶":"碜",
"磣":"碜",
"闖":"闯",
"襯":"衬",
"稱":"称",
"齔":"龀",
"趂":"趁",
"櫬":"榇",
"讖":"谶",
"檉":"柽",
"蟶":"蛏",
"鐺":"铛",
"撐":"撑",
"棖":"枨",
"誠":"诚",
"乗":"乘",
"鋮":"铖",
"懲":"惩",
"堘":"塍",
"澂":"澄",
"騁":"骋",
"喫":"吃",
"鴟":"鸱",
"癡":"痴",
"馳":"驰",
"遲":"迟",
"齒":"齿",
"恥":"耻",
"飭":"饬",
"熾":"炽",
"勅":"敕",
"沖":"冲",
"衝":"冲",
"蟲":"虫",
"寵":"宠",
"銃":"铳",
"儔":"俦",
"幬":"帱",
"綢":"绸",
"疇":"畴",
"籌":"筹",
"詶":"酬",
"酧":"酬",
"醻":"酬",
"躊":"踌",
"讎":"雠",
"讐":"雠",
"醜":"丑",
"矁":"瞅",
"齣":"出",
"芻":"刍",
"廚":"厨",
"耡":"锄",
"鋤":"锄",
"雛":"雏",
"櫥":"橱",
"躕":"蹰",
"礎":"础",
"儲":"储",
"処":"处",
"處":"处",
"絀":"绌",
"觸":"触",
"傳":"传",
"舩":"船",
"釧":"钏",
"囪":"囱",
"瘡":"疮",
"窓":"窗",
"牎":"窗",
"牕":"窗",
"牀":"床",
"創":"创",
"愴":"怆",
"搥":"捶",
"箠":"棰",
"錘":"锤",
"鎚":"锤",
"旾":"春",
"純":"纯",
"脣":"唇",
"蒓":"莼",
"蓴":"莼",
"湻":"淳",
"鶉":"鹑",
"醕":"醇",
"綽":"绰",
"輟":"辍",
"齪":"龊",
"詞":"词",
"辤":"辞",
"辭":"辞",
"鶿":"鹚",
"鷀":"鹚",
"餈":"糍",
"賜":"赐",
"從":"从",
"怱":"匆",
"悤":"匆",
"蓯":"苁",
"樅":"枞",
"蔥":"葱",
"驄":"骢",
"聰":"聪",
"樷":"丛",
"叢":"丛",
"湊":"凑",
"輳":"辏",
"觕":"粗",
"麤":"粗",
"蹵":"蹴",
"攛":"撺",
"鑹":"镩",
"躥":"蹿",
"竄":"窜",
"簒":"篡",
"脃":"脆",
"邨":"村",
"鹺":"鹾",
"銼":"锉",
"錯":"错",
"噠":"哒",
"達":"达",
"遝":"沓",
"韃":"鞑",
"獃":"呆",
"紿":"绐",
"帶":"带",
"蝳":"玳",
"貸":"贷",
"單":"单",
"擔":"担",
"鄲":"郸",
"殫":"殚",
"癉":"瘅",
"簞":"箪",
"膽":"胆",
"撣":"掸",
"誕":"诞",
"啗":"啖",
"噉":"啖",
"彈":"弹",
"憚":"惮",
"當":"当",
"儅":"当",
"噹":"当",
"襠":"裆",
"擋":"挡",
"攩":"挡",
"黨":"党",
"讜":"谠",
"氹":"凼",
"碭":"砀",
"蕩":"荡",
"盪":"荡",
"檔":"档",
"導":"导",
"島":"岛",
"搗":"捣",
"擣":"捣",
"禱":"祷",
"燾":"焘",
"盜":"盗",
"鍀":"锝",
"悳":"德",
"燈":"灯",
"鄧":"邓",
"櫈":"凳",
"鐙":"镫",
"隄":"堤",
"鏑":"镝",
"糴":"籴",
"敵":"敌",
"滌":"涤",
"覿":"觌",
"詆":"诋",
"牴":"抵",
"觝":"抵",
"遞":"递",
"諦":"谛",
"締":"缔",
"蔕":"蒂",
"顛":"颠",
"巔":"巅",
"癲":"癫",
"點":"点",
"電":"电",
"墊":"垫",
"鈿":"钿",
"澱":"淀",
"彫":"雕",
"琱":"雕",
"鵰":"雕",
"鯛":"鲷",
"弔":"吊",
"釣":"钓",
"調":"调",
"銱":"铞",
"諜":"谍",
"啑":"喋",
"曡":"叠",
"疉":"叠",
"疊":"叠",
"蜨":"蝶",
"鰈":"鲽",
"釘":"钉",
"頂":"顶",
"訂":"订",
"矴":"碇",
"椗":"碇",
"錠":"锭",
"丟":"丢",
"銩":"铥",
"東":"东",
"鼕":"冬",
"崬":"岽",
"崠":"岽",
"鶇":"鸫",
"動":"动",
"凍":"冻",
"峝":"峒",
"棟":"栋",
"腖":"胨",
"兠":"兜",
"鬥":"斗",
"鬦":"斗",
"鬭":"斗",
"鈄":"钭",
"荳":"豆",
"竇":"窦",
"讀":"读",
"凟":"渎",
"瀆":"渎",
"匵":"椟",
"櫝":"椟",
"牘":"牍",
"犢":"犊",
"黷":"黩",
"獨":"独",
"篤":"笃",
"賭":"赌",
"覩":"睹",
"妬":"妒",
"鍍":"镀",
"耑":"端",
"斷":"断",
"緞":"缎",
"煆":"煅",
"鍛":"锻",
"籪":"簖",
"隊":"队",
"對":"对",
"兌":"兑",
"懟":"怼",
"鐓":"镦",
"噸":"吨",
"墪":"墩",
"躉":"趸",
"燉":"炖",
"鈍":"钝",
"頓":"顿",
"遯":"遁",
"奪":"夺",
"鐸":"铎",
"朶":"朵",
"垜":"垛",
"綞":"缍",
"墮":"堕",
"跥":"跺",
"訛":"讹",
"譌":"讹",
"峩":"峨",
"鋨":"锇",
"鵝":"鹅",
"鵞":"鹅",
"額":"额",
"娿":"婀",
"戹":"厄",
"阨":"厄",
"軛":"轭",
"堊":"垩",
"惡":"恶",
"噁":"恶",
"餓":"饿",
"諤":"谔",
"閼":"阏",
"蕚":"萼",
"齶":"腭",
"鍔":"锷",
"鶚":"鹗",
"顎":"颚",
"鰐":"鳄",
"鱷":"鳄",
"兒":"儿",
"鴯":"鸸",
"鮞":"鲕",
"爾":"尔",
"邇":"迩",
"餌":"饵",
"鉺":"铒",
"貳":"贰",
"發":"发",
"髮":"发",
"罰":"罚",
"罸":"罚",
"閥":"阀",
"灋":"法",
"琺":"珐",
"颿":"帆",
"飜":"翻",
"繙":"翻",
"凣":"凡",
"礬":"矾",
"釩":"钒",
"煩":"烦",
"緐":"繁",
"氾":"泛",
"汎":"泛",
"飯":"饭",
"範":"范",
"販":"贩",
"鈁":"钫",
"魴":"鲂",
"徬":"仿",
"倣":"仿",
"髣":"仿",
"訪":"访",
"紡":"纺",
"飛":"飞",
"緋":"绯",
"鯡":"鲱",
"誹":"诽",
"廢":"废",
"費":"费",
"疿":"痱",
"鐨":"镄",
"紛":"纷",
"雰":"氛",
"墳":"坟",
"奮":"奋",
"僨":"偾",
"憤":"愤",
"糞":"粪",
"鱝":"鲼",
"豐":"丰",
"風":"风",
"灃":"沣",
"楓":"枫",
"瘋":"疯",
"碸":"砜",
"峯":"峰",
"鋒":"锋",
"馮":"冯",
"縫":"缝",
"諷":"讽",
"鳳":"凤",
"彿":"佛",
"伕":"夫",
"膚":"肤",
"麩":"麸",
"粰":"麸",
"鳧":"凫",
"紱":"绂",
"紼":"绋",
"輻":"辐",
"襆":"幞",
"嘸":"呒",
"撫":"抚",
"俛":"俯",
"頫":"俯",
"輔":"辅",
"訃":"讣",
"婦":"妇",
"負":"负",
"坿":"附",
"駙":"驸",
"複":"复",
"復":"复",
"賦":"赋",
"縛":"缚",
"鮒":"鲋",
"賻":"赙",
"鰒":"鳆",
"釓":"钆",
"嘠":"嘎",
"該":"该",
"賅":"赅",
"匃":"丐",
"匄":"丐",
"鈣":"钙",
"蓋":"盖",
"槩":"概",
"幹":"干",
"榦":"干",
"桿":"杆",
"尲":"尴",
"尷":"尴",
"稈":"秆",
"趕":"赶",
"紺":"绀",
"贛":"赣",
"岡":"冈",
"剛":"刚",
"崗":"岗",
"綱":"纲",
"疘":"肛",
"鋼":"钢",
"槓":"杠",
"戇":"戆",
"臯":"皋",
"橰":"槔",
"餻":"糕",
"縞":"缟",
"槀":"稿",
"鎬":"镐",
"誥":"诰",
"鋯":"锆",
"紇":"纥",
"肐":"胳",
"鴿":"鸽",
"擱":"搁",
"謌":"歌",
"閣":"阁",
"鎘":"镉",
"個":"个",
"箇":"个",
"鉻":"铬",
"給":"给",
"亙":"亘",
"畊":"耕",
"賡":"赓",
"綆":"绠",
"骾":"鲠",
"鯁":"鲠",
"宮":"宫",
"躳":"躬",
"龔":"龚",
"鞏":"巩",
"貢":"贡",
"溝":"沟",
"鈎":"钩",
"鉤":"钩",
"緱":"缑",
"搆":"构",
"構":"构",
"詬":"诟",
"購":"购",
"夠":"够",
"覯":"觏",
"軲":"轱",
"鴣":"鸪",
"轂":"毂",
"鶻":"鹘",
"詁":"诂",
"穀":"谷",
"鈷":"钴",
"蠱":"蛊",
"鵠":"鹄",
"皷":"鼓",
"顧":"顾",
"僱":"雇",
"錮":"锢",
"鯝":"鲴",
"颳":"刮",
"鴰":"鸹",
"剮":"剐",
"詿":"诖",
"掛":"挂",
"枴":"拐",
"柺":"拐",
"恠":"怪",
"関":"关",
"關":"关",
"觀":"观",
"鰥":"鳏",
"舘":"馆",
"館":"馆",
"琯":"管",
"筦":"管",
"貫":"贯",
"慣":"惯",
"摜":"掼",
"鸛":"鹳",
"鑵":"罐",
"廣":"广",
"獷":"犷",
"歸":"归",
"媯":"妫",
"嬀":"妫",
"龜":"龟",
"規":"规",
"槼":"规",
"閨":"闺",
"瓌":"瑰",
"鮭":"鲑",
"軌":"轨",
"匭":"匦",
"詭":"诡",
"劊":"刽",
"劌":"刿",
"櫃":"柜",
"貴":"贵",
"鱖":"鳜",
"袞":"衮",
"緄":"绲",
"輥":"辊",
"滾":"滚",
"鮌":"鲧",
"鯀":"鲧",
"咼":"呙",
"堝":"埚",
"鍋":"锅",
"蟈":"蝈",
"囯":"国",
"國":"国",
"幗":"帼",
"摑":"掴",
"菓":"果",
"槨":"椁",
"過":"过",
"鉿":"铪",
"駭":"骇",
"頇":"顸",
"圅":"函",
"韓":"韩",
"漢":"汉",
"猂":"悍",
"釬":"焊",
"銲":"焊",
"頷":"颔",
"絎":"绗",
"頏":"颃",
"蠔":"蚝",
"獋":"嗥",
"號":"号",
"暠":"皓",
"皜":"皓",
"顥":"颢",
"灝":"灏",
"訶":"诃",
"閤":"合",
"郃":"合",
"咊":"和",
"閡":"阂",
"覈":"核",
"盇":"盍",
"頜":"颌",
"闔":"阖",
"賀":"贺",
"鶴":"鹤",
"恆":"恒",
"橫":"横",
"轟":"轰",
"鬨":"哄",
"紅":"红",
"閎":"闳",
"葒":"荭",
"鴻":"鸿",
"黌":"黉",
"訌":"讧",
"餱":"糇",
"鱟":"鲎",
"虖":"呼",
"嘑":"呼",
"謼":"呼",
"軤":"轷",
"衚":"胡",
"鬍":"胡",
"壺":"壶",
"鶘":"鹕",
"餬":"糊",
"滸":"浒",
"戶":"户",
"沍":"冱",
"護":"护",
"滬":"沪",
"鸌":"鹱",
"芲":"花",
"蘤":"花",
"華":"华",
"嘩":"哗",
"譁":"哗",
"驊":"骅",
"鏵":"铧",
"劃":"划",
"畫":"画",
"話":"话",
"樺":"桦",
"懷":"怀",
"壞":"坏",
"懽":"欢",
"歡":"欢",
"貛":"獾",
"還":"还",
"環":"环",
"鍰":"锾",
"繯":"缳",
"緩":"缓",
"奐":"奂",
"喚":"唤",
"換":"换",
"渙":"涣",
"煥":"焕",
"瘓":"痪",
"鯇":"鲩",
"黃":"黄",
"鰉":"鳇",
"怳":"恍",
"謊":"谎",
"詼":"诙",
"噅":"咴",
"揮":"挥",
"暉":"晖",
"琿":"珲",
"煇":"辉",
"輝":"辉",
"幑":"徽",
"囘":"回",
"囬":"回",
"廻":"回",
"迴":"回",
"蚘":"蛔",
"痐":"蛔",
"蛕":"蛔",
"蜖":"蛔",
"匯":"汇",
"彙":"汇",
"滙":"汇",
"會":"会",
"諱":"讳",
"噦":"哕",
"澮":"浍",
"繪":"绘",
"薈":"荟",
"誨":"诲",
"檜":"桧",
"燴":"烩",
"賄":"贿",
"穢":"秽",
"繢":"缋",
"燬":"毁",
"譭":"毁",
"毀":"毁",
"昬":"昏",
"葷":"荤",
"閽":"阍",
"渾":"浑",
"餛":"馄",
"諢":"诨",
"鍃":"锪",
"鈥":"钬",
"貨":"货",
"獲":"获",
"穫":"获",
"禍":"祸",
"鑊":"镬",
"譏":"讥",
"擊":"击",
"嘰":"叽",
"飢":"饥",
"饑":"饥",
"機":"机",
"璣":"玑",
"磯":"矶",
"雞":"鸡",
"鷄":"鸡",
"跡":"迹",
"蹟":"迹",
"積":"积",
"勣":"绩",
"績":"绩",
"緝":"缉",
"賫":"赍",
"齎":"赍",
"躋":"跻",
"齏":"齑",
"羈":"羁",
"級":"级",
"極":"极",
"檝":"楫",
"輯":"辑",
"幾":"几",
"蟣":"虮",
"擠":"挤",
"計":"计",
"記":"记",
"紀":"纪",
"際":"际",
"劑":"剂",
"嚌":"哜",
"濟":"济",
"繼":"继",
"覬":"觊",
"薊":"蓟",
"霽":"霁",
"鱭":"鲚",
"鯽":"鲫",
"驥":"骥",
"夾":"夹",
"裌":"夹",
"浹":"浃",
"傢":"家",
"鎵":"镓",
"郟":"郏",
"莢":"荚",
"鋏":"铗",
"蛺":"蛱",
"頰":"颊",
"賈":"贾",
"鉀":"钾",
"價":"价",
"駕":"驾",
"戔":"戋",
"姦":"奸",
"堅":"坚",
"殲":"歼",
"間":"间",
"艱":"艰",
"監":"监",
"牋":"笺",
"箋":"笺",
"緘":"缄",
"縑":"缣",
"鰹":"鲣",
"鶼":"鹣",
"韉":"鞯",
"揀":"拣",
"梘":"枧",
"儉":"俭",
"繭":"茧",
"撿":"捡",
"筧":"笕",
"減":"减",
"檢":"检",
"瞼":"睑",
"襇":"裥",
"鐧":"锏",
"簡":"简",
"譾":"谫",
"戩":"戬",
"鹼":"碱",
"堿":"碱",
"見":"见",
"餞":"饯",
"劍":"剑",
"劒":"剑",
"薦":"荐",
"賤":"贱",
"澗":"涧",
"艦":"舰",
"漸":"渐",
"諫":"谏",
"濺":"溅",
"踐":"践",
"鋻":"鉴",
"鑑":"鉴",
"鑒":"鉴",
"鍵":"键",
"檻":"槛",
"薑":"姜",
"將":"将",
"漿":"浆",
"殭":"僵",
"繮":"缰",
"韁":"缰",
"講":"讲",
"獎":"奖",
"槳":"桨",
"蔣":"蒋",
"絳":"绛",
"醬":"酱",
"嬌":"娇",
"澆":"浇",
"驕":"骄",
"膠":"胶",
"鮫":"鲛",
"鷦":"鹪",
"僥":"侥",
"撟":"挢",
"絞":"绞",
"餃":"饺",
"矯":"矫",
"腳":"脚",
"鉸":"铰",
"攪":"搅",
"勦":"剿",
"繳":"缴",
"呌":"叫",
"嶠":"峤",
"轎":"轿",
"較":"较",
"階":"阶",
"堦":"阶",
"癤":"疖",
"稭":"秸",
"節":"节",
"訐":"讦",
"刦":"劫",
"刧":"劫",
"刼":"劫",
"傑":"杰",
"詰":"诘",
"潔":"洁",
"結":"结",
"頡":"颉",
"鮚":"鲒",
"屆":"届",
"誡":"诫",
"觔":"斤",
"僅":"仅",
"巹":"卺",
"緊":"紧",
"謹":"谨",
"錦":"锦",
"饉":"馑",
"盡":"尽",
"儘":"尽",
"勁":"劲",
"進":"进",
"藎":"荩",
"晉":"晋",
"燼":"烬",
"賮":"赆",
"贐":"赆",
"縉":"缙",
"覲":"觐",
"涇":"泾",
"經":"经",
"莖":"茎",
"荊":"荆",
"驚":"惊",
"鯨":"鲸",
"穽":"阱",
"剄":"刭",
"頸":"颈",
"淨":"净",
"弳":"弪",
"徑":"径",
"逕":"径",
"脛":"胫",
"痙":"痉",
"競":"竞",
"靚":"靓",
"靜":"静",
"鏡":"镜",
"逈":"迥",
"埛":"炯",
"糾":"纠",
"鳩":"鸠",
"鬮":"阄",
"揫":"揪",
"韮":"韭",
"舊":"旧",
"廄":"厩",
"廐":"厩",
"捄":"救",
"鷲":"鹫",
"駒":"驹",
"鋦":"锔",
"侷":"局",
"跼":"局",
"舉":"举",
"擧":"举",
"櫸":"榉",
"齟":"龃",
"詎":"讵",
"鉅":"钜",
"劇":"剧",
"懼":"惧",
"據":"据",
"颶":"飓",
"鋸":"锯",
"窶":"窭",
"屨":"屦",
"鵑":"鹃",
"鎸":"镌",
"鐫":"镌",
"捲":"卷",
"錈":"锩",
"勌":"倦",
"棬":"桊",
"獧":"狷",
"絹":"绢",
"雋":"隽",
"睠":"眷",
"決":"决",
"訣":"诀",
"玨":"珏",
"絕":"绝",
"覺":"觉",
"譎":"谲",
"橜":"橛",
"鐝":"镢",
"钁":"镢",
"軍":"军",
"鈞":"钧",
"皸":"皲",
"儁":"俊",
"濬":"浚",
"駿":"骏",
"哢":"咔",
"開":"开",
"鐦":"锎",
"凱":"凯",
"剴":"剀",
"塏":"垲",
"愷":"恺",
"鎧":"铠",
"嘅":"慨",
"鍇":"锴",
"愾":"忾",
"龕":"龛",
"埳":"坎",
"偘":"侃",
"闞":"阚",
"矙":"瞰",
"粇":"糠",
"穅":"糠",
"閌":"闶",
"匟":"炕",
"鈧":"钪",
"攷":"考",
"銬":"铐",
"軻":"轲",
"痾":"疴",
"鈳":"钶",
"頦":"颏",
"顆":"颗",
"殼":"壳",
"欬":"咳",
"剋":"克",
"尅":"克",
"課":"课",
"騍":"骒",
"緙":"缂",
"錁":"锞",
"肎":"肯",
"墾":"垦",
"懇":"恳",
"阬":"坑",
"鏗":"铿",
"摳":"抠",
"瞘":"眍",
"敂":"叩",
"釦":"扣",
"宼":"寇",
"庫":"库",
"絝":"绔",
"嚳":"喾",
"褲":"裤",
"誇":"夸",
"塊":"块",
"儈":"侩",
"鄶":"郐",
"噲":"哙",
"獪":"狯",
"膾":"脍",
"寬":"宽",
"髖":"髋",
"欵":"款",
"誆":"诓",
"誑":"诳",
"鄺":"邝",
"壙":"圹",
"纊":"纩",
"況":"况",
"曠":"旷",
"礦":"矿",
"鑛":"矿",
"貺":"贶",
"虧":"亏",
"巋":"岿",
"窺":"窥",
"闚":"窥",
"匱":"匮",
"憒":"愦",
"媿":"愧",
"潰":"溃",
"蕢":"蒉",
"餽":"馈",
"饋":"馈",
"簣":"篑",
"聵":"聩",
"堃":"坤",
"崐":"昆",
"崑":"昆",
"錕":"锟",
"鯤":"鲲",
"梱":"捆",
"綑":"捆",
"閫":"阃",
"睏":"困",
"擴":"扩",
"濶":"阔",
"闊":"阔",
"臘":"腊",
"蠟":"蜡",
"辢":"辣",
"來":"来",
"崍":"崃",
"徠":"徕",
"淶":"涞",
"萊":"莱",
"錸":"铼",
"賚":"赉",
"睞":"睐",
"賴":"赖",
"顂":"赖",
"瀨":"濑",
"癩":"癞",
"籟":"籁",
"蘭":"兰",
"嵐":"岚",
"攔":"拦",
"欄":"栏",
"惏":"婪",
"闌":"阑",
"藍":"蓝",
"讕":"谰",
"瀾":"澜",
"襤":"褴",
"斕":"斓",
"籃":"篮",
"鑭":"镧",
"覽":"览",
"攬":"揽",
"纜":"缆",
"欖":"榄",
"嬾":"懒",
"懶":"懒",
"爛":"烂",
"濫":"滥",
"瑯":"琅",
"鋃":"锒",
"蜋":"螂",
"閬":"阆",
"撈":"捞",
"勞":"劳",
"嘮":"唠",
"嶗":"崂",
"癆":"痨",
"鐒":"铹",
"銠":"铑",
"澇":"涝",
"耮":"耢",
"樂":"乐",
"鰳":"鳓",
"縲":"缧",
"鐳":"镭",
"誄":"诔",
"壘":"垒",
"淚":"泪",
"類":"类",
"纍":"累",
"稜":"棱",
"釐":"厘",
"棃":"梨",
"貍":"狸",
"離":"离",
"驪":"骊",
"犂":"犁",
"鸝":"鹂",
"灕":"漓",
"縭":"缡",
"蘺":"蓠",
"琍":"璃",
"瓈":"璃",
"鱺":"鲡",
"籬":"篱",
"蔾":"藜",
"禮":"礼",
"裡":"里",
"裏":"里",
"邐":"逦",
"鋰":"锂",
"鯉":"鲤",
"鱧":"鳢",
"厤":"历",
"曆":"历",
"歷":"历",
"厲":"厉",
"麗":"丽",
"勵":"励",
"嚦":"呖",
"壢":"坜",
"瀝":"沥",
"藶":"苈",
"櫪":"枥",
"癘":"疠",
"隷":"隶",
"隸":"隶",
"儷":"俪",
"櫟":"栎",
"鬁":"疬",
"癧":"疬",
"茘":"荔",
"轢":"轹",
"酈":"郦",
"慄":"栗",
"礪":"砺",
"礫":"砾",
"涖":"莅",
"蒞":"莅",
"糲":"粝",
"蠣":"蛎",
"躒":"跞",
"靂":"雳",
"倆":"俩",
"匲":"奁",
"奩":"奁",
"匳":"奁",
"籢":"奁",
"連":"连",
"簾":"帘",
"憐":"怜",
"漣":"涟",
"蓮":"莲",
"聯":"联",
"褳":"裢",
"亷":"廉",
"鰱":"鲢",
"鐮":"镰",
"斂":"敛",
"歛":"敛",
"璉":"琏",
"臉":"脸",
"襝":"裣",
"蘞":"蔹",
"練":"练",
"孌":"娈",
"煉":"炼",
"鍊":"炼",
"戀":"恋",
"殮":"殓",
"鏈":"链",
"瀲":"潋",
"涼":"凉",
"樑":"梁",
"糧":"粮",
"兩":"两",
"魎":"魉",
"諒":"谅",
"輛":"辆",
"遼":"辽",
"療":"疗",
"繚":"缭",
"鐐":"镣",
"鷯":"鹩",
"釕":"钌",
"獵":"猎",
"鄰":"邻",
"隣":"邻",
"臨":"临",
"痳":"淋",
"轔":"辚",
"粦":"磷",
"燐":"磷",
"鱗":"鳞",
"麐":"麟",
"凜":"凛",
"廩":"廪",
"懍":"懔",
"檁":"檩",
"恡":"吝",
"賃":"赁",
"藺":"蔺",
"躪":"躏",
"霛":"灵",
"靈":"灵",
"嶺":"岭",
"淩":"凌",
"鈴":"铃",
"櫺":"棂",
"欞":"棂",
"綾":"绫",
"蔆":"菱",
"齡":"龄",
"鯪":"鲮",
"領":"领",
"霤":"溜",
"劉":"刘",
"瀏":"浏",
"畱":"留",
"瑠":"琉",
"璢":"琉",
"餾":"馏",
"騮":"骝",
"癅":"瘤",
"鎦":"镏",
"栁":"柳",
"桺":"柳",
"綹":"绺",
"鋶":"锍",
"鷚":"鹨",
"龍":"龙",
"嚨":"咙",
"瀧":"泷",
"蘢":"茏",
"櫳":"栊",
"瓏":"珑",
"朧":"胧",
"礱":"砻",
"籠":"笼",
"聾":"聋",
"隴":"陇",
"壟":"垄",
"壠":"垄",
"攏":"拢",
"婁":"娄",
"僂":"偻",
"嘍":"喽",
"蔞":"蒌",
"樓":"楼",
"耬":"耧",
"螻":"蝼",
"髏":"髅",
"嶁":"嵝",
"摟":"搂",
"簍":"篓",
"瘺":"瘘",
"瘻":"瘘",
"鏤":"镂",
"嚕":"噜",
"擼":"撸",
"盧":"卢",
"廬":"庐",
"蘆":"芦",
"壚":"垆",
"罏":"垆",
"瀘":"泸",
"爐":"炉",
"鑪":"炉",
"櫨":"栌",
"臚":"胪",
"轤":"轳",
"鸕":"鸬",
"艫":"舻",
"顱":"颅",
"鱸":"鲈",
"鹵":"卤",
"滷":"卤",
"虜":"虏",
"擄":"掳",
"魯":"鲁",
"櫓":"橹",
"艣":"橹",
"艪":"橹",
"鑥":"镥",
"陸":"陆",
"錄":"录",
"賂":"赂",
"輅":"辂",
"淥":"渌",
"祿":"禄",
"濾":"滤",
"剹":"戮",
"轆":"辘",
"鷺":"鹭",
"氌":"氇",
"驢":"驴",
"閭":"闾",
"櫚":"榈",
"呂":"吕",
"侶":"侣",
"穭":"稆",
"鋁":"铝",
"屢":"屡",
"縷":"缕",
"褸":"褛",
"慮":"虑",
"綠":"绿",
"孿":"孪",
"巒":"峦",
"攣":"挛",
"欒":"栾",
"鸞":"鸾",
"臠":"脔",
"灤":"滦",
"鑾":"銮",
"亂":"乱",
"畧":"略",
"鋝":"锊",
"掄":"抡",
"侖":"仑",
"崙":"仑",
"倫":"伦",
"圇":"囵",
"淪":"沦",
"綸":"纶",
"輪":"轮",
"論":"论",
"羅":"罗",
"儸":"罗",
"玀":"猡",
"腡":"脶",
"蘿":"萝",
"邏":"逻",
"欏":"椤",
"鑼":"锣",
"籮":"箩",
"騾":"骡",
"驘":"骡",
"鏍":"镙",
"躶":"裸",
"臝":"裸",
"濼":"泺",
"絡":"络",
"犖":"荦",
"駱":"骆",
"媽":"妈",
"嬤":"嬷",
"蔴":"麻",
"蟇":"蟆",
"馬":"马",
"獁":"犸",
"瑪":"玛",
"碼":"码",
"螞":"蚂",
"榪":"杩",
"罵":"骂",
"駡":"骂",
"嘜":"唛",
"嗎":"吗",
"買":"买",
"蕒":"荬",
"勱":"劢",
"邁":"迈",
"麥":"麦",
"賣":"卖",
"脈":"脉",
"衇":"脉",
"顢":"颟",
"蠻":"蛮",
"饅":"馒",
"瞞":"瞒",
"鰻":"鳗",
"滿":"满",
"蟎":"螨",
"謾":"谩",
"縵":"缦",
"鏝":"镘",
"貓":"猫",
"氂":"牦",
"犛":"牦",
"錨":"锚",
"鉚":"铆",
"冐":"冒",
"貿":"贸",
"夘":"帽",
"戼":"帽",
"麼":"么",
"沒":"没",
"楳":"梅",
"槑":"梅",
"鎇":"镅",
"鶥":"鹛",
"黴":"霉",
"鎂":"镁",
"門":"门",
"捫":"扪",
"鍆":"钔",
"悶":"闷",
"燜":"焖",
"懣":"懑",
"們":"们",
"懞":"蒙",
"濛":"蒙",
"矇":"蒙",
"錳":"锰",
"夢":"梦",
"彌":"弥",
"瀰":"弥",
"禰":"祢",
"獼":"猕",
"謎":"谜",
"羋":"芈",
"瞇":"眯",
"覓":"觅",
"覔":"觅",
"祕":"秘",
"冪":"幂",
"謐":"谧",
"綿":"绵",
"緜":"绵",
"黽":"黾",
"緬":"缅",
"靦":"腼",
"靣":"面",
"麪":"面",
"麵":"面",
"鶓":"鹋",
"緲":"缈",
"玅":"妙",
"廟":"庙",
"哶":"咩",
"滅":"灭",
"衊":"蔑",
"瑉":"珉",
"緍":"缗",
"緡":"缗",
"閔":"闵",
"冺":"泯",
"閩":"闽",
"憫":"悯",
"湣":"愍",
"鰵":"鳘",
"鳴":"鸣",
"銘":"铭",
"謬":"谬",
"繆":"缪",
"謨":"谟",
"饃":"馍",
"饝":"馍",
"糢":"模",
"歿":"殁",
"驀":"蓦",
"鏌":"镆",
"謀":"谋",
"畝":"亩",
"鉬":"钼",
"幙":"幕",
"拏":"拿",
"挐":"拿",
"鎿":"镎",
"內":"内",
"納":"纳",
"鈉":"钠",
"廼":"乃",
"迺":"乃",
"嬭":"奶",
"難":"难",
"枏":"楠",
"柟":"楠",
"饢":"馕",
"撓":"挠",
"鐃":"铙",
"蟯":"蛲",
"堖":"垴",
"惱":"恼",
"腦":"脑",
"閙":"闹",
"鬧":"闹",
"訥":"讷",
"餒":"馁",
"嫰":"嫩",
"鈮":"铌",
"蜺":"霓",
"鯢":"鲵",
"妳":"你",
"擬":"拟",
"暱":"昵",
"膩":"腻",
"鮎":"鲇",
"鯰":"鲶",
"撚":"捻",
"輦":"辇",
"攆":"撵",
"唸":"念",
"孃":"娘",
"釀":"酿",
"鳥":"鸟",
"蔦":"茑",
"嫋":"袅",
"裊":"袅",
"嬝":"袅",
"揑":"捏",
"隉":"陧",
"聶":"聂",
"嚙":"啮",
"齧":"啮",
"囁":"嗫",
"鑷":"镊",
"鎳":"镍",
"顳":"颞",
"躡":"蹑",
"孼":"孽",
"寧":"宁",
"嚀":"咛",
"擰":"拧",
"獰":"狞",
"檸":"柠",
"聹":"聍",
"濘":"泞",
"紐":"纽",
"鈕":"钮",
"農":"农",
"辳":"农",
"儂":"侬",
"噥":"哝",
"濃":"浓",
"膿":"脓",
"衖":"弄",
"駑":"驽",
"釹":"钕",
"瘧":"疟",
"煖":"暖",
"煗":"暖",
"儺":"傩",
"諾":"诺",
"鍩":"锘",
"謳":"讴",
"歐":"欧",
"毆":"殴",
"甌":"瓯",
"鷗":"鸥",
"嘔":"呕",
"慪":"怄",
"漚":"沤",
"槃":"盘",
"盤":"盘",
"蹣":"蹒",
"龐":"庞",
"鉋":"刨",
"鑤":"刨",
"麅":"狍",
"砲":"炮",
"礮":"炮",
"皰":"疱",
"肧":"胚",
"賠":"赔",
"錇":"锫",
"珮":"佩",
"轡":"辔",
"噴":"喷",
"鵬":"鹏",
"掽":"碰",
"踫":"碰",
"紕":"纰",
"鈹":"铍",
"毘":"毗",
"羆":"罴",
"駢":"骈",
"諞":"谝",
"騗":"骗",
"騙":"骗",
"縹":"缥",
"飃":"飘",
"飄":"飘",
"貧":"贫",
"嬪":"嫔",
"頻":"频",
"顰":"颦",
"評":"评",
"凴":"凭",
"憑":"凭",
"蘋":"苹",
"缾":"瓶",
"鮃":"鲆",
"釙":"钋",
"潑":"泼",
"頗":"颇",
"鉕":"钷",
"廹":"迫",
"僕":"仆",
"撲":"扑",
"鋪":"铺",
"舖":"铺",
"鏷":"镤",
"樸":"朴",
"譜":"谱",
"鐠":"镨",
"悽":"凄",
"淒":"凄",
"棲":"栖",
"榿":"桤",
"慼":"戚",
"鏚":"戚",
"齊":"齐",
"臍":"脐",
"頎":"颀",
"騏":"骐",
"騎":"骑",
"棊":"棋",
"碁":"棋",
"蠐":"蛴",
"旂":"旗",
"蘄":"蕲",
"鰭":"鳍",
"豈":"岂",
"啓":"启",
"啟":"启",
"綺":"绮",
"氣":"气",
"訖":"讫",
"棄":"弃",
"薺":"荠",
"磧":"碛",
"憇":"憩",
"韆":"千",
"扡":"扦",
"遷":"迁",
"僉":"佥",
"釺":"钎",
"牽":"牵",
"慳":"悭",
"鉛":"铅",
"謙":"谦",
"諐":"愆",
"簽":"签",
"籤":"签",
"騫":"骞",
"蕁":"荨",
"鈐":"钤",
"錢":"钱",
"鉗":"钳",
"亁":"乾",
"乹":"乾",
"潛":"潜",
"淺":"浅",
"膁":"肷",
"譴":"谴",
"繾":"缱",
"塹":"堑",
"槧":"椠",
"嗆":"呛",
"羗":"羌",
"戧":"戗",
"槍":"枪",
"蹌":"跄",
"錆":"锖",
"鏘":"锵",
"鏹":"镪",
"彊":"强",
"強":"强",
"墻":"墙",
"牆":"墙",
"嬙":"嫱",
"薔":"蔷",
"檣":"樯",
"艢":"樯",
"搶":"抢",
"羥":"羟",
"繈":"襁",
"繦":"襁",
"熗":"炝",
"墝":"硗",
"磽":"硗",
"蹺":"跷",
"鍫":"锹",
"鍬":"锹",
"繰":"缲",
"喬":"乔",
"僑":"侨",
"蕎":"荞",
"橋":"桥",
"譙":"谯",
"癄":"憔",
"顦":"憔",
"鞽":"鞒",
"誚":"诮",
"陗":"峭",
"竅":"窍",
"翹":"翘",
"竊":"窃",
"愜":"惬",
"篋":"箧",
"鍥":"锲",
"親":"亲",
"欽":"钦",
"琹":"琴",
"懃":"勤",
"鋟":"锓",
"寢":"寝",
"唚":"吣",
"搇":"揿",
"撳":"揿",
"氫":"氢",
"輕":"轻",
"傾":"倾",
"鯖":"鲭",
"檾":"苘",
"頃":"顷",
"請":"请",
"慶":"庆",
"窮":"穷",
"煢":"茕",
"瓊":"琼",
"坵":"丘",
"秌":"秋",
"鞦":"秋",
"鰌":"鳅",
"鰍":"鳅",
"虯":"虬",
"毬":"球",
"賕":"赇",
"巰":"巯",
"區":"区",
"粬":"曲",
"麯":"曲",
"嶇":"岖",
"詘":"诎",
"敺":"驱",
"驅":"驱",
"軀":"躯",
"趨":"趋",
"鴝":"鸲",
"臒":"癯",
"齲":"龋",
"闃":"阒",
"覰":"觑",
"覷":"觑",
"覻":"觑",
"權":"权",
"詮":"诠",
"輇":"辁",
"銓":"铨",
"踡":"蜷",
"顴":"颧",
"綣":"绻",
"勸":"劝",
"卻":"却",
"愨":"悫",
"慤":"悫",
"確":"确",
"闋":"阕",
"闕":"阙",
"鵲":"鹊",
"搉":"榷",
"帬":"裙",
"裠":"裙",
"羣":"群",
"冄":"冉",
"讓":"让",
"蕘":"荛",
"饒":"饶",
"橈":"桡",
"擾":"扰",
"嬈":"娆",
"繞":"绕",
"熱":"热",
"認":"认",
"紉":"纫",
"姙":"妊",
"軔":"轫",
"靭":"韧",
"韌":"韧",
"飪":"饪",
"毧":"绒",
"絨":"绒",
"羢":"绒",
"榮":"荣",
"嶸":"嵘",
"蠑":"蝾",
"螎":"融",
"宂":"冗",
"銣":"铷",
"顬":"颥",
"縟":"缛",
"軟":"软",
"輭":"软",
"蕋":"蕊",
"橤":"蕊",
"蘂":"蕊",
"銳":"锐",
"叡":"睿",
"閏":"闰",
"潤":"润",
"篛":"箬",
"灑":"洒",
"颯":"飒",
"薩":"萨",
"顋":"腮",
"鰓":"鳃",
"賽":"赛",
"毿":"毵",
"傘":"伞",
"繖":"伞",
"糝":"糁",
"饊":"馓",
"顙":"颡",
"喪":"丧",
"騷":"骚",
"繅":"缫",
"鰠":"鳋",
"掃":"扫",
"澁":"涩",
"澀":"涩",
"嗇":"啬",
"銫":"铯",
"穡":"穑",
"殺":"杀",
"紗":"纱",
"鎩":"铩",
"鯊":"鲨",
"篩":"筛",
"曬":"晒",
"刪":"删",
"姍":"姗",
"釤":"钐",
"羶":"膻",
"閃":"闪",
"陝":"陕",
"訕":"讪",
"騸":"骟",
"繕":"缮",
"饍":"膳",
"贍":"赡",
"鱓":"鳝",
"鱔":"鳝",
"傷":"伤",
"殤":"殇",
"觴":"觞",
"坰":"垧",
"賞":"赏",
"緔":"绱",
"燒":"烧",
"紹":"绍",
"賒":"赊",
"虵":"蛇",
"捨":"舍",
"厙":"厍",
"設":"设",
"慴":"慑",
"懾":"慑",
"攝":"摄",
"灄":"滠",
"紳":"绅",
"詵":"诜",
"審":"审",
"讅":"审",
"諗":"谂",
"嬸":"婶",
"瀋":"渖",
"腎":"肾",
"滲":"渗",
"昇":"升",
"陞":"升",
"聲":"声",
"勝":"胜",
"澠":"渑",
"繩":"绳",
"聖":"圣",
"賸":"剩",
"屍":"尸",
"師":"师",
"蝨":"虱",
"詩":"诗",
"獅":"狮",
"溼":"湿",
"濕":"湿",
"釃":"酾",
"鯴":"鲺",
"時":"时",
"識":"识",
"實":"实",
"蝕":"蚀",
"塒":"埘",
"蒔":"莳",
"鰣":"鲥",
"駛":"驶",
"勢":"势",
"眎":"视",
"眡":"视",
"視":"视",
"試":"试",
"飾":"饰",
"昰":"是",
"柹":"柿",
"貰":"贳",
"適":"适",
"軾":"轼",
"鈰":"铈",
"諡":"谥",
"謚":"谥",
"釋":"释",
"壽":"寿",
"夀":"寿",
"獸":"兽",
"綬":"绶",
"書":"书",
"紓":"纾",
"樞":"枢",
"倐":"倏",
"儵":"倏",
"疎":"疏",
"攄":"摅",
"輸":"输",
"贖":"赎",
"藷":"薯",
"術":"术",
"樹":"树",
"竪":"竖",
"豎":"竖",
"庻":"庶",
"數":"数",
"潄":"漱",
"帥":"帅",
"閂":"闩",
"雙":"双",
"誰":"谁",
"稅":"税",
"順":"顺",
"說":"说",
"説":"说",
"爍":"烁",
"鑠":"铄",
"碩":"硕",
"絲":"丝",
"噝":"咝",
"鷥":"鸶",
"緦":"缌",
"螄":"蛳",
"廝":"厮",
"鍶":"锶",
"佀":"似",
"禩":"祀",
"飼":"饲",
"駟":"驷",
"竢":"俟",
"鬆":"松",
"慫":"怂",
"聳":"耸",
"訟":"讼",
"誦":"诵",
"頌":"颂",
"蒐":"搜",
"餿":"馊",
"颼":"飕",
"鎪":"锼",
"擻":"擞",
"藪":"薮",
"甦":"苏",
"蘇":"苏",
"囌":"苏",
"穌":"稣",
"訴":"诉",
"肅":"肃",
"謖":"谡",
"泝":"溯",
"遡":"溯",
"痠":"酸",
"雖":"虽",
"綏":"绥",
"隨":"随",
"嵗":"岁",
"歲":"岁",
"誶":"谇",
"孫":"孙",
"猻":"狲",
"蓀":"荪",
"飱":"飧",
"損":"损",
"筍":"笋",
"挱":"挲",
"簑":"蓑",
"縮":"缩",
"嗩":"唢",
"瑣":"琐",
"鎖":"锁",
"牠":"它",
"鉈":"铊",
"墖":"塔",
"獺":"獭",
"鰨":"鳎",
"撻":"挞",
"闥":"闼",
"駘":"骀",
"臺":"台",
"颱":"台",
"檯":"台",
"擡":"抬",
"鮐":"鲐",
"態":"态",
"鈦":"钛",
"貪":"贪",
"攤":"摊",
"灘":"滩",
"癱":"瘫",
"墰":"坛",
"壇":"坛",
"罈":"坛",
"壜":"坛",
"罎":"坛",
"曇":"昙",
"談":"谈",
"錟":"锬",
"譚":"谭",
"襢":"袒",
"鉭":"钽",
"嘆":"叹",
"歎":"叹",
"賧":"赕",
"湯":"汤",
"鐋":"铴",
"鏜":"镗",
"餳":"饧",
"餹":"糖",
"儻":"傥",
"燙":"烫",
"蹚":"趟",
"濤":"涛",
"絛":"绦",
"縚":"绦",
"縧":"绦",
"搯":"掏",
"韜":"韬",
"鞀":"鼗",
"鞉":"鼗",
"討":"讨",
"鋱":"铽",
"騰":"腾",
"謄":"誊",
"籐":"藤",
"銻":"锑",
"綈":"绨",
"嗁":"啼",
"緹":"缇",
"鵜":"鹈",
"題":"题",
"蹏":"蹄",
"躰":"体",
"體":"体",
"屜":"屉",
"薙":"剃",
"鬀":"剃",
"闐":"阗",
"條":"条",
"齠":"龆",
"鰷":"鲦",
"覜":"眺",
"糶":"粜",
"銚":"铫",
"貼":"贴",
"鉄":"铁",
"銕":"铁",
"鐵":"铁",
"厛":"厅",
"廳":"厅",
"聼":"听",
"聽":"听",
"烴":"烃",
"鋌":"铤",
"衕":"同",
"銅":"铜",
"統":"统",
"筩":"筒",
"慟":"恸",
"偸":"偷",
"媮":"偷",
"頭":"头",
"禿":"秃",
"圖":"图",
"凃":"涂",
"塗":"涂",
"釷":"钍",
"兎":"兔",
"團":"团",
"糰":"团",
"摶":"抟",
"頹":"颓",
"頽":"颓",
"穨":"颓",
"骽":"腿",
"蛻":"蜕",
"飩":"饨",
"臋":"臀",
"託":"托",
"拕":"拖",
"脫":"脱",
"馱":"驮",
"駝":"驼",
"鴕":"鸵",
"鼉":"鼍",
"橢":"椭",
"搨":"拓",
"籜":"箨",
"窪":"洼",
"媧":"娲",
"鼃":"蛙",
"襪":"袜",
"韤":"袜",
"膃":"腽",
"彎":"弯",
"灣":"湾",
"紈":"纨",
"翫":"玩",
"頑":"顽",
"輓":"挽",
"綰":"绾",
"盌":"碗",
"椀":"碗",
"萬":"万",
"亾":"亡",
"網":"网",
"徃":"往",
"輞":"辋",
"朢":"望",
"為":"为",
"爲":"为",
"韋":"韦",
"圍":"围",
"幃":"帏",
"溈":"沩",
"潙":"沩",
"違":"违",
"闈":"闱",
"潿":"涠",
"維":"维",
"濰":"潍",
"偉":"伟",
"偽":"伪",
"僞":"伪",
"緯":"纬",
"葦":"苇",
"煒":"炜",
"瑋":"玮",
"諉":"诿",
"韙":"韪",
"鮪":"鲔",
"衛":"卫",
"衞":"卫",
"謂":"谓",
"餧":"喂",
"餵":"喂",
"蝟":"猬",
"溫":"温",
"紋":"纹",
"聞":"闻",
"螡":"蚊",
"蟁":"蚊",
"閿":"阌",
"脗":"吻",
"穩":"稳",
"問":"问",
"甕":"瓮",
"罋":"瓮",
"撾":"挝",
"渦":"涡",
"萵":"莴",
"窩":"窝",
"蝸":"蜗",
"臥":"卧",
"齷":"龌",
"烏":"乌",
"汙":"污",
"汚":"污",
"鄔":"邬",
"嗚":"呜",
"誣":"诬",
"鎢":"钨",
"無":"无",
"吳":"吴",
"蕪":"芜",
"塢":"坞",
"隖":"坞",
"娬":"妩",
"嫵":"妩",
"廡":"庑",
"啎":"忤",
"憮":"怃",
"鵡":"鹉",
"務":"务",
"誤":"误",
"騖":"骛",
"霧":"雾",
"鶩":"鹜",
"誒":"诶",
"犧":"牺",
"晳":"晰",
"谿":"溪",
"錫":"锡",
"譆":"嘻",
"厀":"膝",
"習":"习",
"蓆":"席",
"襲":"袭",
"覡":"觋",
"璽":"玺",
"銑":"铣",
"戯":"戏",
"戲":"戏",
"繫":"系",
"係":"系",
"餼":"饩",
"細":"细",
"郤":"郄",
"鬩":"阋",
"潟":"舄",
"蝦":"虾",
"俠":"侠",
"峽":"峡",
"狹":"狭",
"硤":"硖",
"轄":"辖",
"鎋":"辖",
"嚇":"吓",
"廈":"厦",
"僊":"仙",
"縴":"纤",
"纖":"纤",
"秈":"籼",
"薟":"莶",
"躚":"跹",
"鍁":"锨",
"鮮":"鲜",
"閒":"闲",
"閑":"闲",
"絃":"弦",
"賢":"贤",
"鹹":"咸",
"嫺":"娴",
"嫻":"娴",
"啣":"衔",
"銜":"衔",
"癇":"痫",
"鷳":"鹇",
"鷴":"鹇",
"鷼":"鹇",
"顯":"显",
"險":"险",
"獫":"猃",
"蜆":"蚬",
"蘚":"藓",
"縣":"县",
"峴":"岘",
"莧":"苋",
"現":"现",
"綫":"线",
"線":"线",
"憲":"宪",
"餡":"馅",
"羨":"羡",
"獻":"献",
"鄉":"乡",
"鄕":"乡",
"薌":"芗",
"廂":"厢",
"緗":"缃",
"驤":"骧",
"鑲":"镶",
"詳":"详",
"亯":"享",
"響":"响",
"餉":"饷",
"饗":"飨",
"鯗":"鲞",
"嚮":"向",
"曏":"向",
"項":"项",
"梟":"枭",
"嘵":"哓",
"驍":"骁",
"綃":"绡",
"蕭":"萧",
"銷":"销",
"瀟":"潇",
"簫":"箫",
"嚻":"嚣",
"囂":"嚣",
"曉":"晓",
"篠":"筱",
"効":"效",
"傚":"效",
"嘯":"啸",
"歗":"啸",
"蠍":"蝎",
"協":"协",
"衺":"邪",
"脅":"胁",
"脇":"胁",
"挾":"挟",
"諧":"谐",
"擕":"携",
"攜":"携",
"擷":"撷",
"纈":"缬",
"鞵":"鞋",
"寫":"写",
"洩":"泄",
"瀉":"泻",
"紲":"绁",
"絏":"绁",
"緤":"绁",
"褻":"亵",
"謝":"谢",
"蠏":"蟹",
"訢":"欣",
"鋅":"锌",
"釁":"衅",
"興":"兴",
"陘":"陉",
"倖":"幸",
"兇":"凶",
"洶":"汹",
"胷":"胸",
"脩":"修",
"鵂":"鸺",
"饈":"馐",
"綉":"绣",
"繡":"绣",
"銹":"锈",
"鏽":"锈",
"須":"须",
"鬚":"须",
"頊":"顼",
"虛":"虚",
"噓":"嘘",
"許":"许",
"詡":"诩",
"敍":"叙",
"敘":"叙",
"卹":"恤",
"賉":"恤",
"勗":"勖",
"緒":"绪",
"續":"续",
"壻":"婿",
"漵":"溆",
"軒":"轩",
"諼":"谖",
"諠":"喧",
"萲":"萱",
"蕿":"萱",
"藼":"萱",
"蘐":"萱",
"懸":"悬",
"鏇":"旋",
"璿":"璇",
"選":"选",
"癬":"癣",
"絢":"绚",
"鉉":"铉",
"楥":"楦",
"鞾":"靴",
"學":"学",
"澩":"泶",
"鱈":"鳕",
"謔":"谑",
"勛":"勋",
"勳":"勋",
"塤":"埙",
"壎":"埙",
"燻":"熏",
"尋":"寻",
"廵":"巡",
"馴":"驯",
"詢":"询",
"潯":"浔",
"鱘":"鲟",
"訓":"训",
"訊":"讯",
"狥":"徇",
"遜":"逊",
"枒":"丫",
"壓":"压",
"鴉":"鸦",
"鵶":"鸦",
"椏":"桠",
"鴨":"鸭",
"啞":"哑",
"瘂":"痖",
"亞":"亚",
"訝":"讶",
"埡":"垭",
"婭":"娅",
"氬":"氩",
"嚥":"咽",
"懨":"恹",
"懕":"恹",
"煙":"烟",
"臙":"胭",
"閹":"阉",
"醃":"腌",
"訁":"讠",
"閆":"闫",
"嚴":"严",
"喦":"岩",
"巖":"岩",
"巗":"岩",
"鹽":"盐",
"閻":"阎",
"顏":"颜",
"顔":"颜",
"簷":"檐",
"兗":"兖",
"儼":"俨",
"厴":"厣",
"縯":"演",
"魘":"魇",
"鼴":"鼹",
"厭":"厌",
"彥":"彦",
"硯":"砚",
"艷":"艳",
"豔":"艳",
"騐":"验",
"驗":"验",
"諺":"谚",
"燄":"焰",
"鴈":"雁",
"灧":"滟",
"灩":"滟",
"釅":"酽",
"讞":"谳",
"饜":"餍",
"讌":"燕",
"醼":"燕",
"鷰":"燕",
"贋":"赝",
"贗":"赝",
"鴦":"鸯",
"揚":"扬",
"敭":"扬",
"颺":"扬",
"陽":"阳",
"楊":"杨",
"煬":"炀",
"瘍":"疡",
"養":"养",
"癢":"痒",
"樣":"样",
"殀":"夭",
"堯":"尧",
"餚":"肴",
"軺":"轺",
"窯":"窑",
"窰":"窑",
"謠":"谣",
"搖":"摇",
"遙":"遥",
"瑤":"瑶",
"鰩":"鳐",
"葯":"药",
"藥":"药",
"鷂":"鹞",
"燿":"耀",
"爺":"爷",
"鋣":"铘",
"埜":"野",
"壄":"野",
"業":"业",
"葉":"叶",
"頁":"页",
"鄴":"邺",
"亱":"夜",
"曄":"晔",
"燁":"烨",
"爗":"烨",
"謁":"谒",
"靨":"靥",
"毉":"医",
"醫":"医",
"吚":"咿",
"銥":"铱",
"儀":"仪",
"詒":"诒",
"迆":"迤",
"飴":"饴",
"貽":"贻",
"迻":"移",
"遺":"遗",
"頤":"颐",
"彜":"彝",
"彞":"彝",
"釔":"钇",
"艤":"舣",
"螘":"蚁",
"蟻":"蚁",
"義":"义",
"億":"亿",
"憶":"忆",
"藝":"艺",
"議":"议",
"異":"异",
"囈":"呓",
"讛":"呓",
"譯":"译",
"嶧":"峄",
"懌":"怿",
"繹":"绎",
"詣":"诣",
"驛":"驿",
"軼":"轶",
"誼":"谊",
"縊":"缢",
"瘞":"瘗",
"鎰":"镒",
"瞖":"翳",
"鐿":"镱",
"囙":"因",
"陰":"阴",
"隂":"阴",
"蔭":"荫",
"廕":"荫",
"慇":"殷",
"銦":"铟",
"瘖":"喑",
"陻":"堙",
"唫":"吟",
"婬":"淫",
"滛":"淫",
"銀":"银",
"齦":"龈",
"飲":"饮",
"隱":"隐",
"癮":"瘾",
"應":"应",
"鶯":"莺",
"鸎":"莺",
"嬰":"婴",
"嚶":"嘤",
"攖":"撄",
"纓":"缨",
"甖":"罂",
"罌":"罂",
"櫻":"樱",
"瓔":"璎",
"鸚":"鹦",
"鷹":"鹰",
"塋":"茔",
"滎":"荥",
"熒":"荧",
"瑩":"莹",
"螢":"萤",
"營":"营",
"縈":"萦",
"瀅":"滢",
"鎣":"蓥",
"瀠":"潆",
"蠅":"蝇",
"贏":"赢",
"潁":"颍",
"穎":"颖",
"癭":"瘿",
"暎":"映",
"喲":"哟",
"傭":"佣",
"擁":"拥",
"癰":"痈",
"雝":"雍",
"鄘":"墉",
"鏞":"镛",
"鱅":"鳙",
"詠":"咏",
"湧":"涌",
"惥":"恿",
"慂":"恿",
"踴":"踊",
"優":"优",
"憂":"忧",
"猶":"犹",
"郵":"邮",
"蓧":"莜",
"蕕":"莸",
"鈾":"铀",
"遊":"游",
"魷":"鱿",
"銪":"铕",
"祐":"佑",
"誘":"诱",
"紆":"纡",
"餘":"余",
"歟":"欤",
"魚":"鱼",
"娛":"娱",
"諛":"谀",
"漁":"渔",
"崳":"嵛",
"踰":"逾",
"覦":"觎",
"輿":"舆",
"與":"与",
"傴":"伛",
"嶼":"屿",
"俁":"俣",
"語":"语",
"齬":"龉",
"馭":"驭",
"訏":"吁",
"籲":"吁",
"嫗":"妪",
"飫":"饫",
"鬱":"郁",
"獄":"狱",
"鈺":"钰",
"預":"预",
"慾":"欲",
"諭":"谕",
"閾":"阈",
"禦":"御",
"鵒":"鹆",
"瘉":"愈",
"癒":"愈",
"蕷":"蓣",
"譽":"誉",
"鷸":"鹬",
"鳶":"鸢",
"鴛":"鸳",
"淵":"渊",
"員":"员",
"園":"园",
"圓":"圆",
"緣":"缘",
"黿":"鼋",
"猨":"猿",
"蝯":"猿",
"轅":"辕",
"櫞":"橼",
"遠":"远",
"願":"愿",
"約":"约",
"嶽":"岳",
"鑰":"钥",
"鈅":"钥",
"籥":"钥",
"悅":"悦",
"鉞":"钺",
"閱":"阅",
"閲":"阅",
"躍":"跃",
"粵":"粤",
"雲":"云",
"勻":"匀",
"紜":"纭",
"蕓":"芸",
"鄖":"郧",
"氳":"氲",
"隕":"陨",
"殞":"殒",
"運":"运",
"鄆":"郓",
"惲":"恽",
"暈":"晕",
"醖":"酝",
"醞":"酝",
"慍":"愠",
"韞":"韫",
"韻":"韵",
"蘊":"蕴",
"帀":"匝",
"襍":"杂",
"雜":"杂",
"災":"灾",
"烖":"灾",
"菑":"灾",
"載":"载",
"簮":"簪",
"偺":"咱",
"喒":"咱",
"欑":"攒",
"儹":"攒",
"攢":"攒",
"趲":"趱",
"暫":"暂",
"賛":"赞",
"贊":"赞",
"讚":"赞",
"鏨":"錾",
"瓚":"瓒",
"賍":"赃",
"贓":"赃",
"贜":"赃",
"駔":"驵",
"髒":"脏",
"臟":"脏",
"塟":"葬",
"蹧":"糟",
"鑿":"凿",
"棗":"枣",
"竈":"灶",
"皁":"皂",
"唕":"唣",
"譟":"噪",
"則":"则",
"擇":"择",
"澤":"泽",
"責":"责",
"嘖":"啧",
"幘":"帻",
"簀":"箦",
"賾":"赜",
"賊":"贼",
"譖":"谮",
"繒":"缯",
"鋥":"锃",
"贈":"赠",
"摣":"揸",
"齇":"齄",
"紥":"扎",
"紮":"扎",
"剳":"札",
"劄":"札",
"軋":"轧",
"牐":"闸",
"閘":"闸",
"鍘":"铡",
"詐":"诈",
"柵":"栅",
"搾":"榨",
"齋":"斋",
"債":"债",
"霑":"沾",
"氈":"毡",
"氊":"毡",
"譫":"谵",
"斬":"斩",
"盞":"盏",
"嶄":"崭",
"輾":"辗",
"佔":"占",
"戰":"战",
"棧":"栈",
"綻":"绽",
"驏":"骣",
"張":"张",
"麞":"獐",
"漲":"涨",
"帳":"帐",
"脹":"胀",
"賬":"账",
"釗":"钊",
"詔":"诏",
"趙":"赵",
"櫂":"棹",
"炤":"照",
"喆":"哲",
"輒":"辄",
"蟄":"蛰",
"謫":"谪",
"讁":"谪",
"轍":"辙",
"鍺":"锗",
"這":"这",
"淛":"浙",
"鷓":"鹧",
"貞":"贞",
"針":"针",
"鍼":"针",
"偵":"侦",
"湞":"浈",
"珎":"珍",
"楨":"桢",
"碪":"砧",
"禎":"祯",
"診":"诊",
"軫":"轸",
"縝":"缜",
"陣":"阵",
"鴆":"鸩",
"賑":"赈",
"鎮":"镇",
"爭":"争",
"徴":"征",
"崢":"峥",
"掙":"挣",
"猙":"狰",
"鉦":"钲",
"睜":"睁",
"錚":"铮",
"箏":"筝",
"証":"证",
"證":"证",
"諍":"诤",
"鄭":"郑",
"幀":"帧",
"癥":"症",
"巵":"卮",
"織":"织",
"梔":"栀",
"執":"执",
"妷":"侄",
"姪":"侄",
"職":"职",
"縶":"絷",
"蹠":"跖",
"躑":"踯",
"衹":"只",
"隻":"只",
"阯":"址",
"紙":"纸",
"軹":"轵",
"誌":"志",
"製":"制",
"祑":"帙",
"袠":"帙",
"幟":"帜",
"質":"质",
"櫛":"栉",
"摯":"挚",
"緻":"致",
"贄":"贽",
"輊":"轾",
"擲":"掷",
"鷙":"鸷",
"滯":"滞",
"騭":"骘",
"稺":"稚",
"穉":"稚",
"寘":"置",
"觶":"觯",
"躓":"踬",
"終":"终",
"鈡":"钟",
"鍾":"钟",
"鐘":"钟",
"腫":"肿",
"種":"种",
"塚":"冢",
"眾":"众",
"衆":"众",
"謅":"诌",
"週":"周",
"軸":"轴",
"箒":"帚",
"紂":"纣",
"呪":"咒",
"縐":"绉",
"晝":"昼",
"葤":"荮",
"皺":"皱",
"驟":"骤",
"硃":"朱",
"誅":"诛",
"諸":"诸",
"豬":"猪",
"銖":"铢",
"櫧":"槠",
"瀦":"潴",
"櫫":"橥",
"燭":"烛",
"屬":"属",
"煑":"煮",
"囑":"嘱",
"矚":"瞩",
"佇":"伫",
"竚":"伫",
"苧":"苎",
"註":"注",
"貯":"贮",
"駐":"驻",
"築":"筑",
"鑄":"铸",
"筯":"箸",
"專":"专",
"塼":"砖",
"甎":"砖",
"磚":"砖",
"顓":"颛",
"轉":"转",
"囀":"啭",
"賺":"赚",
"譔":"撰",
"饌":"馔",
"妝":"妆",
"粧":"妆",
"莊":"庄",
"樁":"桩",
"裝":"装",
"壯":"壮",
"狀":"状",
"騅":"骓",
"錐":"锥",
"墜":"坠",
"綴":"缀",
"縋":"缒",
"贅":"赘",
"諄":"谆",
"準":"准",
"槕":"桌",
"斮":"斫",
"斲":"斫",
"斵":"斫",
"濁":"浊",
"諑":"诼",
"鋜":"镯",
"鐲":"镯",
"茲":"兹",
"玆":"兹",
"貲":"赀",
"資":"资",
"緇":"缁",
"諮":"谘",
"輜":"辎",
"錙":"锱",
"齜":"龇",
"鯔":"鲻",
"姉":"姊",
"漬":"渍",
"眥":"眦",
"綜":"综",
"椶":"棕",
"蹤":"踪",
"騣":"鬃",
"鬉":"鬃",
"縂":"总",
"總":"总",
"傯":"偬",
"縱":"纵",
"糉":"粽",
"鄒":"邹",
"騶":"驺",
"諏":"诹",
"鯫":"鲰",
"鏃":"镞",
"詛":"诅",
"組":"组",
"躦":"躜",
"纘":"缵",
"篹":"纂",
"鉆":"钻",
"鑽":"钻",
"辠":"罪",
"罇":"樽",
"鱒":"鳟",
"串列":"串行",
"乙太":"以太",
"點陣圖":"位图",
"常式":"例程",
"通道":"信道",
"圖元":"像素",
"游標":"光标",
"光碟":"光盘",
"光碟機":"光驱",
"全形":"全角",
"西元":"公元",
"西曆":"公历",
"共用":"共享",
"相容":"兼容",
"記憶體":"内存",
"首碼":"前缀",
"開工廠":"办厂",
"載入":"加载",
"半形":"半角",
"變數":"变量",
"尾碼":"后缀",
"雜訊":"噪声",
"因數":"因子",
"線上":"在线",
"功能變數名稱":"域名",
"音效卡":"声卡",
"賓士":"奔驰",
"乳酪":"奶酪",
"字型大小":"字号",
"字形檔":"字库",
"欄位":"字段",
"字元":"字符",
"位元組":"字节",
"存檔":"存盘",
"定址":"寻址",
"章節附註":"尾注",
"鉅賈":"巨商",
"布希":"布什",
"非同步":"异步",
"匯流排":"总线",
"手電筒":"手电",
"列印":"打印",
"括弧":"括号",
"介面":"接口",
"控制項":"控件",
"許可權":"权限",
"毫安培":"毫安",
"浮水印":"水印",
"中文卡":"汉卡",
"大碗公":"海碗",
"碟片":"盘片",
"硬體":"硬件",
"矽油":"硅油",
"矽片":"硅片",
"矽石":"硅石",
"矽磚":"硅砖",
"矽肺":"硅肺",
"矽膠":"硅胶",
"矽藻":"硅藻",
"矽谷":"硅谷",
"矽酸":"硅酸",
"矽鋼":"硅钢",
"硬碟":"硬盘",
"磁片":"磁盘",
"磁軌":"磁道",
"程式":"程序",
"程式控制":"程控",
"埠":"端口",
"運算元":"算子",
"演算法":"算法",
"晶片":"芯片",
"片語":"词组",
"解碼":"译码",
"軟盤機":"软驱",
"快閃記憶體":"闪存",
"滑鼠":"鼠标",
"二極體":"二极管",
"三極體":"三极管",
"進位":"进制",
"互動式":"交互式",
"模擬":"仿真",
"優先順序":"优先级",
"感測":"传感",
"攜帶型":"便携式",
"資訊理論":"信息论",
"迴圈":"循环",
"防寫":"写保护",
"分散式":"分布式",
"解析度":"分辨率",
"丹唐":"丹顿",
"葉門":"也门",
"慣用":"习用",
"母音":"元音",
"數位":"数码",
"程式":"程序",
"軟體":"软件",
"網路":"网络",
"電腦":"计算机",
"存檔":"保存",
"伺服器":"服务器",
"」":"”",
"「":"“",
"『":"‘",
"』":"’",
"記憶體":"内存",
"預設":"默认",
"串列":"串行",
"乙太網":"以太网",
"點陣圖":"位图",
"常式":"例程",
"游標":"光标",
"光碟":"光盘",
"光碟機":"光驱",
"全形":"全角",
"共用":"共享",
"載入":"加载",
"半形":"半角",
"變數":"变量",
"雜訊":"噪声",
"因數":"因子",
"功能變數名稱":"域名",
"音效卡":"声卡",
"字型大小":"字号",
"字型檔":"字库",
"欄位":"字段",
"字元":"字符",
"存檔":"存盘",
"定址":"寻址",
"章節附註":"尾注",
"非同步":"异步",
"匯流排":"总线",
"括弧":"括号",
"介面":"接口",
"控制項":"控件",
"許可權":"权限",
"碟片":"盘片",
"矽片":"硅片",
"矽谷":"硅谷",
"硬碟":"硬盘",
"磁碟":"磁盘",
"磁軌":"磁道",
"程式控制":"程控",
"運算元":"算子",
"演算法":"算法",
"晶片":"芯片",
"晶元":"芯片",
"片語":"词组",
"軟碟機":"软驱",
"快閃記憶體":"快闪存储器",
"滑鼠":"鼠标",
"進位":"进制",
"互動式":"交互式",
"優先順序":"优先级",
"感測":"传感",
"攜帶型":"便携式",
"資訊理論":"信息论",
"迴圈":"循环",
"防寫":"写保护",
"分散式":"分布式",
"解析度":"分辨率",
"伺服器":"服务器",
"等於":"等于",
"區域網":"局域网",
"巨集":"宏",
"掃瞄器":"扫瞄仪",
"寬頻":"宽带",
"資料庫":"数据库",
"乳酪":"奶酪",
"鉅賈":"巨商",
"萬曆":"万历",
"永曆":"永历",
"辭彙":"词汇",
"母音":"元音",
"自由球":"任意球",
"頭槌":"头球",
"進球":"入球",
"顆進球":"粒入球",
"射門":"打门",
"蓋火鍋":"火锅盖帽",
"印表機":"打印机",
"打印機":"打印机",
"位元組":"字节",
"字節":"字节",
"列印":"打印",
"打印":"打印",
"硬體":"硬件",
"二極體":"二极管",
"二極管":"二极管",
"三極體":"三极管",
"三極管":"三极管",
"數位":"数码",
"數碼":"数码",
"軟體":"软件",
"軟件":"软件",
"網路":"网络",
"網絡":"网络",
"人工智慧":"人工智能",
"太空梭":"航天飞机",
"穿梭機":"航天飞机",
"網際網路":"因特网",
"互聯網":"因特网",
"機械人":"机器人",
"機器人":"机器人",
"行動電話":"移动电话",
"流動電話":"移动电话",
"調制解調器":"调制解调器",
"數據機":"调制解调器",
"短訊":"短信",
"簡訊":"短信",
"烏茲別克":"乌兹别克斯坦",
"查德":"乍得",
"乍得":"乍得",
"也門":"",
"葉門":"也门",
"伯利茲":"伯利兹",
"貝里斯":"伯利兹",
"維德角":"佛得角",
"佛得角":"佛得角",
"克羅地亞":"克罗地亚",
"克羅埃西亞":"克罗地亚",
"岡比亞":"冈比亚",
"甘比亞":"冈比亚",
"幾內亞比紹":"几内亚比绍",
"幾內亞比索":"几内亚比绍",
"列支敦斯登":"列支敦士登",
"列支敦士登":"列支敦士登",
"利比里亞":"利比里亚",
"賴比瑞亞":"利比里亚",
"加納":"加纳",
"迦納":"加纳",
"加彭":"加蓬",
"加蓬":"加蓬",
"博茨瓦納":"博茨瓦纳",
"波札那":"博茨瓦纳",
"卡塔爾":"卡塔尔",
"卡達":"卡塔尔",
"盧旺達":"卢旺达",
"盧安達":"卢旺达",
"危地馬拉":"危地马拉",
"瓜地馬拉":"危地马拉",
"厄瓜多爾":"厄瓜多尔",
"厄瓜多":"厄瓜多尔",
"厄立特里亞":"厄立特里亚",
"厄利垂亞":"厄立特里亚",
"吉布堤":"吉布提",
"吉布地":"吉布提",
"哈薩克":"哈萨克斯坦",
"哥斯達黎加":"哥斯达黎加",
"哥斯大黎加":"哥斯达黎加",
"圖瓦盧":"图瓦卢",
"吐瓦魯":"图瓦卢",
"土庫曼":"土库曼斯坦",
"聖盧西亞":"圣卢西亚",
"聖露西亞":"圣卢西亚",
"聖吉斯納域斯":"圣基茨和尼维斯",
"聖克里斯多福及尼維斯":"圣基茨和尼维斯",
"聖文森特和格林納丁斯":"圣文森特和格林纳丁斯",
"聖文森及格瑞那丁":"圣文森特和格林纳丁斯",
"聖馬力諾":"圣马力诺",
"聖馬利諾":"圣马力诺",
"圭亞那":"圭亚那",
"蓋亞那":"圭亚那",
"坦桑尼亞":"坦桑尼亚",
"坦尚尼亞":"坦桑尼亚",
"埃塞俄比亞":"埃塞俄比亚",
"衣索匹亞":"埃塞俄比亚",
"衣索比亞":"埃塞俄比亚",
"吉里巴斯":"基里巴斯",
"基里巴斯":"基里巴斯",
"塔吉克":"塔吉克斯坦",
"塞拉利昂":"塞拉利昂",
"塞普勒斯":"塞浦路斯",
"塞浦路斯":"塞浦路斯",
"塞舌爾":"塞舌尔",
"塞席爾":"塞舌尔",
"多明尼加共和國":"多米尼加",
"多明尼加":"多米尼加",
"多明尼加聯邦":"多米尼加联邦",
"多米尼克":"多米尼加联邦",
"安提瓜和巴布達":"安提瓜和巴布达",
"安地卡及巴布達":"安提瓜和巴布达",
"尼日利亞":"尼日利亚",
"奈及利亞":"尼日利亚",
"尼日爾":"尼日尔",
"尼日":"尼日尔",
"巴貝多":"巴巴多斯",
"巴巴多斯":"巴巴多斯",
"巴布亞新畿內亞":"巴布亚新几内亚",
"巴布亞紐幾內亞":"巴布亚新几内亚",
"布基納法索":"布基纳法索",
"布吉納法索":"布基纳法索",
"蒲隆地":"布隆迪",
"布隆迪":"布隆迪",
"希臘":"希腊",
"帛琉":"帕劳",
"義大利":"意大利",
"意大利":"意大利",
"所羅門群島":"所罗门群岛",
"索羅門群島":"所罗门群岛",
"汶萊":"文莱",
"斯威士蘭":"斯威士兰",
"史瓦濟蘭":"斯威士兰",
"斯洛文尼亞":"斯洛文尼亚",
"斯洛維尼亞":"斯洛文尼亚",
"新西蘭":"新西兰",
"紐西蘭":"新西兰",
"格林納達":"格林纳达",
"格瑞那達":"格林纳达",
"格魯吉亞":"乔治亚",
"喬治亞":"乔治亚",
"梵蒂岡":"梵蒂冈",
"毛里塔尼亞":"毛里塔尼亚",
"茅利塔尼亞":"毛里塔尼亚",
"毛里裘斯":"毛里求斯",
"模里西斯":"毛里求斯",
"沙地阿拉伯":"沙特阿拉伯",
"沙烏地阿拉伯":"沙特阿拉伯",
"波斯尼亞黑塞哥維那":"波斯尼亚和黑塞哥维那",
"波士尼亞赫塞哥維納":"波斯尼亚和黑塞哥维那",
"津巴布韋":"津巴布韦",
"辛巴威":"津巴布韦",
"宏都拉斯":"洪都拉斯",
"洪都拉斯":"洪都拉斯",
"特立尼達和多巴哥":"特立尼达和托巴哥",
"千里達托貝哥":"特立尼达和托巴哥",
"瑙魯":"瑙鲁",
"諾魯":"瑙鲁",
"瓦努阿圖":"瓦努阿图",
"萬那杜":"瓦努阿图",
"溫納圖":"瓦努阿图",
"科摩羅":"科摩罗",
"葛摩":"科摩罗",
"象牙海岸":"科特迪瓦",
"突尼西亞":"突尼斯",
"索馬里":"索马里",
"索馬利亞":"索马里",
"老撾":"老挝",
"寮國":"老挝",
"肯雅":"肯尼亚",
"肯亞":"肯尼亚",
"蘇利南":"苏里南",
"莫三比克":"莫桑比克",
"莫桑比克":"莫桑比克",
"萊索托":"莱索托",
"賴索托":"莱索托",
"貝寧":"贝宁",
"貝南":"贝宁",
"贊比亞":"赞比亚",
"尚比亞":"赞比亚",
"亞塞拜然":"阿塞拜疆",
"阿塞拜疆":"阿塞拜疆",
"阿拉伯聯合酋長國":"阿拉伯联合酋长国",
"阿拉伯聯合大公國":"阿拉伯联合酋长国",
"南韓":"韩国",
"馬爾代夫":"马尔代夫",
"馬爾地夫":"马尔代夫",
"馬爾他":"马耳他",
"馬利共和國":"马里共和国",
"即食麵":"方便面",
"快速面":"方便面",
"速食麵":"方便面",
"泡麵":"方便面",
"笨豬跳":"蹦极跳",
"绑紧跳":"蹦极跳",
"冷盤　　":"凉菜",
"冷菜":"凉菜",
"散钱":"零钱",
"谐星":"笑星",
"夜学":"夜校",
"华乐":"民乐",
"中樂":"民乐",
"屋价":"房价",
"計程車":"出租车",
"公車":"公共汽车",
"單車":"自行车",
"節慶":"节日",
"芝士":"乾酪",
"狗隻":"犬只",
"士多啤梨":"草莓",
"忌廉":"奶油",
"桌球":"台球",
"撞球":"台球",
"雪糕":"冰淇淋",
"衞生":"卫生",
"衛生":"卫生",
"賓士":"奔驰",
"平治":"奔驰",
"平治之亂":"平治之乱",
"平治之乱":"平治之乱",
"積架":"捷豹",
"福斯":"大众",
"福士":"大众",
"雪鐵龍":"雪铁龙",
"萬事得":"马自达",
"馬自達":"马自达",
"寶獅":"标志",
"拿破崙":"拿破仑",
"布殊":"布什",
"布希":"布什",
"柯林頓":"克林顿",
"克林頓":"克林顿",
"薩達姆":"萨达姆",
"海珊":"萨达姆",
"梵谷":"凡高",
"大衛碧咸":"大卫·贝克汉姆",
"米高奧雲":"迈克尔·欧文",
"卡佩雅蒂":"珍妮弗·卡普里亚蒂",
"沙芬":"马拉特·萨芬",
"舒麥加":"迈克尔·舒马赫",
"希特拉":"希特勒",
"黛安娜":"戴安娜",
"抽象":"抽象",
"演算法":"算法",
"註釋":"注释",
"應用程式":"应用程序",
"引數":"参数",
"陣列":"数组",
"程序集":"程序集",
"非同步":"异步",
"屬性":"属性",
"批次":"批量",
"區塊":"区块",
"布林值":"布尔值",
"快取":"缓存",
"字元":"字符",
"類別":"类",
"類別庫":"类库",
"程式碼":"代码",
"註解":"注释",
"元件":"组件",
"通訊":"通信",
"並行":"并发",
"併行":"并行",
"設定":"配置",
"常數":"常量",
"建構函數":"构造函数",
"建構子":"构造函数",
"建立":"创建",
"樣式表":"样式表",
"資料":"数据",
"資料結構":"数据结构",
"死結":"死锁",
"除錯":"调试",
"偵錯":"调试",
"宣告":"声明",
"委派":"委托",
"組件":"动态链接库文件",
"動態鏈結程式庫":"动态链接库文件",
"預設值":"缺省值",
"設計樣式":"设计模式",
"設計模式":"设计模式",
"分散式":"分布式",
"分散式交易":"分布式事务",
"封裝":"封装",
"列舉":"枚举",
"事件":"事件",
"異常":"异常",
"欄位":"字段",
"框架":"框架",
"函數":"函数",
"呼叫函數":"调用函数",
"泛型":"泛型",
"寫死":"硬编码",
"堆積":"堆",
"裝載":"装载",
"主機":"主机",
"實作":"实现",
"資訊":"信息",
"繼承":"继承",
"實體":"实例",
"執行個體":"实例",
"實體化":"实例化",
"具現化":"实例化",
"介面":"接口",
"迭代器":"迭代器",
"迴圈":"循环",
"巨集":"宏",
"訊息":"消息",
"詮釋資料":"元数据",
"元資料":"元数据",
"方法":"方法",
"中介軟體":"中间件",
"模組":"模块",
"訊息佇列":"消息队列",
"命名空間":"命名空间",
"物件導向":"面向对象",
"物件":"对象",
"運算子":"运算符",
"多載":"重载",
"覆寫":"重写",
"分頁":"分页",
"換頁":"分页",
"平行運算":"并行计算",
"參數":"参数",
"效能":"性能",
"效能最佳化":"性能优化",
"永續":"持久化",
"指標":"指针",
"多型":"多态",
"同名異式":"多态",
"行程; 程序":"进程",
"程式":"程序",
"程式設計師":"程序员",
"程式":"程序",
"屬性":"属性",
"佇列":"队列",
"重構":"重构",
"重建":"重构",
"參考型別":"引用类型",
"反射":"反射",
"註冊":"注册",
"反註冊":"注销",
"規則運算式":"正则表达式",
"傳回":"返回",
"回傳":"返回",
"複用":"复用",
"序列化":"序列化",
"原始碼":"源代码",
"陳述式":"语句",
"堆疊":"堆栈",
"靜態":"静态",
"字串":"字符串",
"強型別":"强类型",
"結構":"結構",
"送出":"提交",
"同步":"同步",
"執行緒":"线程",
"交易":"事务",
"型別":"类型",
"實值型別":"值类型",
"變數":"变量",
"指派":"赋值",
"存取":"访问",
"叢集索引":"聚集索引",
"連線":"联机",
"指標":"游标",
"資料":"数据",
"資料庫":"数据库",
"資料存取":"数据访问",
"離線":"脱机",
"欄位":"字段",
"索引":"索引",
"新增":"插入",
"映射":"映射",
"線上交易處理":"联机事务处理",
"主鍵":"主键",
"查詢":"查询",
"記錄":"记录",
"關聯(一對多)":"联系(一对多)",
"儲存":"存储",
"選取":"提取",
"撈取":"提取",
"SQL陳述式":"SQL语句",
"預存程序":"存储过程",
"資料表":"数据表",
"交易":"事务",
"觸發程序":"触发器",
"型別":"类型",
"檢視表":"视图",
"一筆資料":"一条记录",
"繫結":"綁定",
"緩衝":"缓冲",
"按鈕":"按钮",
"快取":"缓存",
"控制項":"控件",
"資料集":"数据集",
"事件處理常式":"事件处理程序",
"命名空間":"命名空间",
"前置詞":"前缀",
"檢視狀態":"视图状态",
"中斷點":"断点",
"建立":"创建",
"剪下":"剪切",
"項目":"項",
"功能表":"菜單",
"選單":"菜单",
"巡覽":"导航",
"新增":"新建",
"貼上":"粘贴",
"專案":"項目",
"方案":"解决方案",
"索引標籤":"选项卡",
"頁籤":"标签面板",
"工具欄":"菜单栏",
"工具列":"工具条",
"工具箱":"工具箱",
"視窗":"窗口",
"建置":"生成",
"參考":"引用",
"設定":"设置",
"清單":"列表",
"對應":"映射",
"啟動":"激活",
"轉接器":"适配器",
"加入":"添加",
"網址":"网址",
"網址列":"地址栏",
"審核":"审计",
"稽核":"审计",
"頻寬":"带宽",
"位元":"位",
"位元組":"字节",
"攝影機":"摄像头",
"光碟":"光盘",
"晶片":"芯片",
"客戶端":"客户端",
"雲端運算":"云计算",
"叢集":"集群",
"電腦":"计算机",
"處理器":"处理器",
"建立":"创建",
"對話框":"对话框",
"目錄":"目录",
"文件":"文档",
"下載":"下载",
"磁碟":"磁盘",
"模擬器":"仿真器",
"範例":"范例",
"可擴充性":"可扩展性",
"副檔名":"后缀",
"檔案":"文档",
"檔案副檔名":"文件扩展名",
"快閃記憶體":"闪存",
"資料夾":"文件夹",
"硬碟":"硬盘",
"連結":"链接",
"圖示":"图标",
"介面":"界面",
"整合":"集成",
"互動; 交談式":"交互",
"網際網路":"互联网",
"互通性":"互操作性",
"區域網路":"局域网",
"載入":"加载",
"記憶體":"内存",
"螢幕":"屏幕",
"滑鼠":"鼠标",
"滑鼠滾輪":"鼠标滚动轮",
"網路":"网络",
"離線":"脱机",
"線上":"在线",
"作業系統":"操作系统",
"封包":"数据包",
"磁區":"扇区",
"C槽":"C盘",
"路徑":"路径",
"外掛":"插件",
"效能":"性能",
"埠號":"端口号",
"列印":"打印",
"印表機":"打印机",
"捉圖":"截图",
"專案":"项目",
"專案管理":"项目管理",
"協定":"协议",
"唯讀":"只读",
"即時":"及时",
"註冊":"注册",
"機碼":"注册表",
"暫存器":"寄存器",
"回應":"响应",
"唯讀記憶體":"只读存储器",
"彈性":"可伸缩性",
"捲軸":"滚动条",
"伺服端":"服务器端",
"軟體":"软件",
"字尾":"后缀",
"純文字":"文本",
"調校":"调优",
"使用者":"用户",
"廣域網路":"广域网",
"萬用字元":"通配符",
"視窗":"窗口",
"精靈":"向导",
"簡訊":"短信",
"剪貼簿":"剪贴板",
"下拉式選單":"下拉菜单",
"企業流程再造":"业务流程重组",
"資訊長":"企业首席信息官",
"客戶關係管理":"客户关系管理",
"電子資料交換":"电子数据交换",
"企業資源規劃":"企业资源计划",
"来料质量控制":"进货检验",
"物料需求規劃":"物料需求计划",
"供應鏈管理":"供应链管理",
"服務導向架構":"面向服务架构",
"標準作業流程":"标准作业流程",
"工作流程":"工作流",
"簽核":"审批",
"電子簽核":"电子审批",
"審察":"审查",
"審校":"审校",
"部落格":"博客",
"衝突":"冲突",
"自訂":"自定义",
"客製":"定制",
"範例":"示例",
"批准":"审批",
"回饋":"反馈",
"裡":"里",
"遺失":"丢失",
"行銷":"营销",
"符合":"匹配",
"輔助文件":"帮助文档",
"唬爛":"乎悠",
"制定":"定制",
"相容性":"兼容性",
"支援":"支持",
"內建":"内置",
"建置":"构建",
}

class Jianti:
    def __init__(self, f_str):
        self.f_str = f_str

    def f2j(self):
        if table.has_key(self.f_str):
            return table[self.f_str]
        else:
            fstr = unicode(self.f_str,'utf-8')
            output = [table.get(char.encode('utf-8'), char.encode('utf-8')) for char in fstr]
            return "".join(output)
'''
j1 = Jianti('電子簽核')
j2 = Jianti('慇')
j3 = Jianti('詛門鉈')

print j1.f2j(),',',j2.f2j(),',',j3.f2j()
'''

