# -*- coding: utf-8 -*-

class Special_words:
    def __init__(self):
        self.status = "Called"
    
    def tw_sector(self):
        tw_sec=['中正區', '中正', '大同區', '大同', '中山區', '中山', '松山區', '松山', '大安區', '大安', '萬華區'
        , '萬華', '信義區', '信義', '士林區', '士林', '北投區', '北投', '內湖區', '內湖', '南港區', '南港', '文山區'
        , '文山', '板橋區', '板橋', '新莊區', '新莊', '中和區', '中和', '永和區', '永和', '土城區', '土城', '樹林區'
        , '樹林', '三峽區', '三峽', '鶯歌區', '鶯歌', '三重區', '三重', '蘆洲區', '蘆洲', '五股區', '五股', '泰山區'
        , '泰山', '林口區', '林口', '八里區', '八里', '淡水區', '淡水', '三芝區', '三芝', '石門區', '石門', '金山區'
        , '金山', '萬里區', '萬里', '汐止區', '汐止', '瑞芳區', '瑞芳', '貢寮區', '貢寮', '平溪區', '平溪', '雙溪區'
        , '雙溪', '新店區', '新店', '深坑區', '深坑', '石碇區', '石碇', '坪林區', '坪林', '烏來區', '烏來', '桃園區'
        , '桃園', '中壢區', '中壢', '平鎮區', '平鎮', '八德區', '八德', '楊梅區', '楊梅', '蘆竹區', '蘆竹', '大溪區'
        , '大溪', '龍潭區', '龍潭', '龜山區', '龜山', '大園區', '大園', '觀音區', '觀音', '新屋區', '新屋', '復興區'
        , '復興', '中區', '東區', '南區', '西區', '北區','北屯區', '北屯', '西屯區', '西屯', '南屯區', '南屯', '太平區'
        , '太平', '大里區', '大里', '霧峰區', '霧峰', '烏日區', '烏日', '豐原區', '豐原', '后里區', '后里', '石岡區'
        , '石岡', '東勢區', '東勢', '新社區', '新社', '潭子區', '潭子', '大雅區', '大雅', '神岡區', '神岡', '大肚區'
        , '大肚', '沙鹿區', '沙鹿', '龍井區', '龍井', '梧棲區', '梧棲', '清水區', '清水', '大甲區', '大甲', '外埔區'
        , '外埔', '大安區', '大安', '和平區', '和平', '中西區', '中西', '東區', '南區', '北區', '安平區', '安平'
        , '安南區', '安南', '永康區', '永康', '歸仁區', '歸仁', '新化區', '新化', '左鎮區', '左鎮', '玉井區', '玉井'
        , '楠西區', '楠西', '南化區', '南化', '仁德區', '仁德', '關廟區', '關廟', '龍崎區', '龍崎', '官田區', '官田'
        , '麻豆區', '麻豆', '佳里區', '佳里', '西港區', '西港', '七股區', '七股', '將軍區', '將軍', '學甲區', '學甲'
        , '北門區', '北門', '新營區', '新營', '後壁區', '後壁', '白河區', '白河', '東山區', '東山', '六甲區', '六甲'
        , '下營區', '下營', '柳營區', '柳營', '鹽水區', '鹽水', '善化區', '善化', '大內區', '大內', '山上區', '山上'
        , '新市區', '新市', '安定區', '安定', '楠梓區', '楠梓', '左營區', '左營', '鼓山區', '鼓山', '三民區', '三民'
        , '鹽埕區', '鹽埕', '前金區', '前金', '新興區', '新興', '苓雅區', '苓雅', '前鎮區', '前鎮', '旗津區', '旗津'
        , '小港區', '小港', '鳳山區', '鳳山', '大寮區', '大寮', '鳥松區', '鳥松', '林園區', '林園', '仁武區', '仁武'
        , '大樹區', '大樹', '大社區', '大社', '岡山區', '岡山', '路竹區', '路竹', '橋頭區', '橋頭', '梓官區', '梓官'
        , '彌陀區', '彌陀', '永安區', '永安', '燕巢區', '燕巢', '田寮區', '田寮', '阿蓮區', '阿蓮', '茄萣區', '茄萣'
        , '湖內區', '湖內', '旗山區', '旗山', '美濃區', '美濃', '內門區', '內門', '杉林區', '杉林', '甲仙區', '甲仙'
        , '六龜區', '六龜', '茂林區', '茂林', '桃源區', '桃源', '那瑪夏區', '那瑪夏', '仁愛區', '仁愛', '中正區', '中正'
        , '信義區', '信義', '中山區', '中山', '安樂區', '安樂', '暖暖區', '暖暖', '七堵區', '七堵', '東區', '北區'
        ,'香山區', '香山', '東區', '西區', '竹北市', '竹北', '竹東鎮', '竹東', '新埔鎮', '新埔', '關西鎮', '關西'
        , '湖口鄉', '湖口', '新豐鄉', '新豐', '峨眉鄉', '峨眉', '寶山鄉', '寶山', '北埔鄉', '北埔', '芎林鄉', '芎林'
        , '橫山鄉', '橫山', '尖石鄉', '尖石', '五峰鄉', '五峰', '苗栗市', '苗栗', '頭份市', '頭份', '竹南鎮', '竹南'
        , '後龍鎮', '後龍', '通霄鎮', '通霄', '苑裡鎮', '苑裡', '卓蘭鎮', '卓蘭', '造橋鄉', '造橋', '西湖鄉', '西湖'
        , '頭屋鄉', '頭屋', '公館鄉', '公館', '銅鑼鄉', '銅鑼', '三義鄉', '三義', '大湖鄉', '大湖', '獅潭鄉', '獅潭'
        , '三灣鄉', '三灣', '南庄鄉', '南庄', '泰安鄉', '泰安', '彰化市', '員林市', '員林', '和美鎮', '和美'
        , '鹿港鎮', '鹿港', '溪湖鎮', '溪湖', '二林鎮', '二林', '田中鎮', '田中', '北斗鎮', '北斗', '花壇鄉', '花壇'
        , '芬園鄉', '芬園', '大村鄉', '大村', '永靖鄉', '永靖', '伸港鄉', '伸港', '線西鄉', '線西', '福興鄉', '福興'
        , '秀水鄉', '秀水', '埔心鄉', '埔心', '埔鹽鄉', '埔鹽', '大城鄉', '大城', '芳苑鄉', '芳苑', '竹塘鄉', '竹塘'
        , '社頭鄉', '社頭', '二水鄉', '二水', '田尾鄉', '田尾', '埤頭鄉', '埤頭', '溪州鄉', '溪州', '南投市', '南投'
        , '埔里鎮', '埔里', '草屯鎮', '草屯', '竹山鎮', '竹山', '集集鎮', '集集', '名間鄉', '名間', '鹿谷鄉', '鹿谷'
        , '中寮鄉', '中寮', '魚池鄉', '魚池', '國姓鄉', '國姓', '水里鄉', '水里', '信義鄉', '信義', '仁愛鄉', '仁愛'
        , '斗六市', '斗六', '斗南鎮', '斗南', '虎尾鎮', '虎尾', '西螺鎮', '西螺', '土庫鎮', '土庫', '北港鎮', '北港'
        , '林內鄉', '林內', '古坑鄉', '古坑', '大埤鄉', '大埤', '莿桐鄉', '莿桐', '褒忠鄉', '褒忠', '二崙鄉', '二崙'
        , '崙背鄉', '崙背', '麥寮鄉', '麥寮', '臺西鄉', '臺西', '東勢鄉', '東勢', '元長鄉', '元長', '四湖鄉', '四湖'
        , '口湖鄉', '口湖', '水林鄉', '水林', '太保市', '太保', '朴子市', '朴子', '布袋鎮', '布袋', '大林鎮', '大林'
        , '民雄鄉', '民雄', '溪口鄉', '溪口', '新港鄉', '新港', '六腳鄉', '六腳', '東石鄉', '東石', '義竹鄉', '義竹'
        , '鹿草鄉', '鹿草', '水上鄉', '水上', '中埔鄉', '中埔', '竹崎鄉', '竹崎', '梅山鄉', '梅山', '番路鄉', '番路'
        , '大埔鄉', '大埔', '阿里山鄉', '阿里山', '屏東市', '屏東', '潮州鎮', '潮州', '東港鎮', '東港', '恆春鎮', '恆春'
        , '萬丹鄉', '萬丹', '長治鄉', '長治', '麟洛鄉', '麟洛', '九如鄉', '九如', '里港鄉', '里港', '鹽埔鄉', '鹽埔'
        , '高樹鄉', '高樹', '萬巒鄉', '萬巒', '內埔鄉', '內埔', '竹田鄉', '竹田', '新埤鄉', '新埤', '枋寮鄉', '枋寮'
        , '新園鄉', '新園', '崁頂鄉', '崁頂', '林邊鄉', '林邊', '南州鄉', '南州', '佳冬鄉', '佳冬', '琉球鄉', '琉球'
        , '車城鄉', '車城', '滿州鄉', '滿州', '枋山鄉', '枋山', '霧臺鄉', '霧臺', '瑪家鄉', '瑪家', '泰武鄉', '泰武'
        , '來義鄉', '來義', '春日鄉', '春日', '獅子鄉', '獅子', '牡丹鄉', '牡丹', '三地門鄉', '三地門', '宜蘭市'
        , '頭城鎮', '頭城', '羅東鎮', '羅東', '蘇澳鎮', '蘇澳', '礁溪鄉', '礁溪', '壯圍鄉', '壯圍', '員山鄉', '員山'
        , '冬山鄉', '冬山', '五結鄉', '五結', '三星鄉', '三星', '大同鄉', '大同', '南澳鄉', '南澳', '花蓮市', '花蓮'
        , '鳳林鎮', '鳳林', '玉里鎮', '玉里', '新城鄉', '新城', '吉安鄉', '吉安', '壽豐鄉', '壽豐', '光復鄉', '光復'
        , '豐濱鄉', '豐濱', '瑞穗鄉', '瑞穗', '富里鄉', '富里', '秀林鄉', '秀林', '萬榮鄉', '萬榮', '卓溪鄉', '卓溪'
        , '臺東市', '成功鎮', '成功', '關山鎮', '關山', '長濱鄉', '長濱', '池上鄉', '池上', '東河鄉', '東河'
        , '鹿野鄉', '鹿野', '卑南鄉', '卑南', '大武鄉', '大武', '綠島鄉', '綠島', '太麻里鄉', '太麻里', '海端鄉', '海端'
        , '延平鄉', '延平', '金峰鄉', '金峰', '達仁鄉', '達仁', '蘭嶼鄉', '蘭嶼', '馬公市', '馬公', '湖西鄉', '湖西'
        , '白沙鄉', '白沙', '西嶼鄉', '西嶼', '望安鄉', '望安', '七美鄉', '七美', '金城鎮', '金城', '金湖鎮', '金湖'
        , '金沙鎮', '金沙', '金寧鄉', '金寧', '烈嶼鄉', '烈嶼', '烏坵鄉', '烏坵', '南竿鄉', '南竿', '北竿鄉', '北竿'
        , '莒光鄉', '莒光', '東引鄉', '東引']
        return tw_sec


    def special_location(self):
        location = ["橋","國小","國中","大學","廟","宮","苑","寺","溪","河","派出所","車站","捷運站","公所","政府","行政中心","院","山"]
        return location
        # ,"大遠百","新光三越","sogo","家樂福","costco","賓士"
    def address(self):
        address = ["縣","市","里","路","段","巷","弄","號","公路"]
        return address