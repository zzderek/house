# encoding:utf-8
# python3.0

from source.save import saveData
from source.common import getHtml
from source.report import reportData
import configparser
import webbrowser
import os


# ------主函数------
# delete()
if __name__ == '__main__':
    # 获取参数
    config = configparser.ConfigParser()
    config.read("config.ini")

    # 清除数据
    save = saveData(config)
    save.deleteOldData()

    # 贝壳找房 广州二手房2室3室 100-300w
    beike1 = getHtml('''https://gz.ke.com/ershoufang/tianhe/l2l3bp100ep300/''')
    beike2 = getHtml('''https://gz.ke.com/ershoufang/yuexiu/l2l3bp100ep300/''')
    beike3 = getHtml('''https://gz.ke.com/ershoufang/liwan/l2l3bp100ep300/''')
   # beike4 = getHtml('''https://gz.ke.com/ershoufang/haizhu/pg3co32ba80ea100bp211219/''')
    beike4 = getHtml('''https://gz.ke.com/ershoufang/haizhu/l2l3bp100ep300/''')
    beike5 = getHtml('''https://gz.ke.com/ershoufang/panyu/l2l3bp100ep300/''')
    beike6 = getHtml('''https://gz.ke.com/ershoufang/huangpugz/l2l3bp100ep300/''')
    beike7 = getHtml('''https://gz.ke.com/ershoufang/baiyun/l2l3bp100ep300/''')
    # 源码为遍历
    # beike_htmls = [beike1, beike2, beike3,beike4,beike5,beike6,beike7]
    # for beike_html in beike_htmls:
    #     save.beike_save(beike_html)
    save.beike_save(beike1,'天河')
    save.beike_save(beike2,'越秀')
    save.beike_save(beike3,'荔湾')
    save.beike_save(beike4,'海珠')
    save.beike_save(beike5,'番禺')
    save.beike_save(beike6,'黄埔')
    save.beike_save(beike7,'白云')

    # 链家 广州二手房 2室3室 100-300w
    lianjia1 = getHtml('''https://gz.lianjia.com/ershoufang/tianhe/l2l3bp100ep300/''')
    lianjia2 = getHtml('''https://gz.lianjia.com/ershoufang/yuexiu/l2l3bp100ep300/''')
    lianjia3 = getHtml('''https://gz.lianjia.com/ershoufang/liwan/l2l3bp100ep300/''')
    lianjia4 = getHtml('''https://gz.lianjia.com/ershoufang/haizhu/l2l3bp100ep300/''')
    lianjia5 = getHtml('''https://gz.lianjia.com/ershoufang/panyu/l2l3bp100ep300/''')
    lianjia6 = getHtml('''https://gz.lianjia.com/ershoufang/huangpugz/l2l3bp100ep300/''')
    lianjia7 = getHtml('''https://gz.lianjia.com/ershoufang/baiyun/l2l3bp100ep300/''')
    # lianjia_htmls = [lianjia1, lianjia2, lianjia3,lianjia4,lianjia5,lianjia6,lianjia7]
    # for lianjia_html in lianjia_htmls:
    #     save.lianjia_save(lianjia_html)
    save.lianjia_save(lianjia1,'天河')
    save.lianjia_save(lianjia2,'越秀')
    save.lianjia_save(lianjia3,'荔湾')
    save.lianjia_save(lianjia4,'海珠')
    save.lianjia_save(lianjia5,'番禺')
    save.lianjia_save(lianjia6,'黄埔')
    save.lianjia_save(lianjia7,'白云')

    # 58同城 高新园区 80-120W 3室 精装修
 #   tongcheng1 = getHtml('''http://gz.58.com/baiyun/ershoufang/?PGTID=0d00000c-0000-099e-5f9d-eb7cd9b2d735&ClickID=1&huansuanyue=200_600&bunengdaikuan=0&area=60_100''')
 #   tongcheng2 = getHtml('''http://gz.58.com/tianhe/ershoufang/pn2/?huansuanyue=200_600&bunengdaikuan=0&area=60_100&PGTID=0d300000-0000-0b90-1e0b-bf894f74b13a&ClickID=1''')
 #   tongcheng3 = getHtml('''http://gz.58.com/yuexiu/ershoufang/pn3/?huansuanyue=200_600&bunengdaikuan=0&area=60_100&PGTID=0d300000-0000-08f9-ba56-6673c850e2b8&ClickID=1''')
 #   tongcheng3 = getHtml('''http://gz.58.com/liwan/ershoufang/pn3/?huansuanyue=200_600&bunengdaikuan=0&area=60_100&PGTID=0d300000-0000-08f9-ba56-6673c850e2b8&ClickID=1''')
 #   tongcheng3 = getHtml('''http://gz.58.com/haizhu/ershoufang/pn3/?huansuanyue=200_600&bunengdaikuan=0&area=60_100&PGTID=0d300000-0000-08f9-ba56-6673c850e2b8&ClickID=1''')
 #   tongcheng3 = getHtml('''http://gz.58.com/panyu/ershoufang/pn3/?huansuanyue=200_600&bunengdaikuan=0&area=60_100&PGTID=0d300000-0000-08f9-ba56-6673c850e2b8&ClickID=1''')
 #   tongcheng3 = getHtml('''http://gz.58.com/huangpugz/ershoufang/pn3/?huansuanyue=200_600&bunengdaikuan=0&area=60_100&PGTID=0d300000-0000-08f9-ba56-6673c850e2b8&ClickID=1''')
    # print(str(tongcheng1.encode('GB18030')))
 #   tongcheng_htmls = [tongcheng1, tongcheng2, tongcheng3]
 #   for tongcheng_html in tongcheng_htmls:
 #       save.tongcheng_save(tongcheng_html)

    # 安居客 （例：北京 200-600万 60-100平 按最新排序） 根据自己需求添加链接
 #   anjuke1 = getHtml('''https://guangzhou.anjuke.com/sale/tianhe/o5/?from_area=60&to_area=100&from_price=200&to_price=600''')
 #   anjuke2 = getHtml('''https://guangzhou.anjuke.com/sale/yuexiu/o5-p2/?from_area=60&to_area=100&from_price=200&to_price=600#filtersort''')
 #   anjuke3 = getHtml('''https://guangzhou.anjuke.com/sale/huangpugz/o5-p3/?from_area=60&to_area=100&from_price=200&to_price=600#filtersort''')
 #   anjuke3 = getHtml('''https://guangzhou.anjuke.com/sale/panyu/o5-p3/?from_area=60&to_area=100&from_price=200&to_price=600#filtersort''')
 #   anjuke3 = getHtml('''https://guangzhou.anjuke.com/sale/baiyun/o5-p3/?from_area=60&to_area=100&from_price=200&to_price=600#filtersort''')
 #   anjuke3 = getHtml('''https://guangzhou.anjuke.com/sale/liwan/o5-p3/?from_area=60&to_area=100&from_price=200&to_price=600#filtersort''')
 #   anjuke3 = getHtml('''https://guangzhou.anjuke.com/sale/haizhu/o5-p3/?from_area=60&to_area=100&from_price=200&to_price=600#filtersort''')
 #   anjuke_htmls = [anjuke1, anjuke2, anjuke3]
 #   for anjuke_html in anjuke_htmls:
 #       save.anjuke_save(anjuke_html)

    # # 赶集 高新园区 80-120W 3室 精装修
    # ganji1 = getHtml('''http://dl.ganji.com/fang5/gaoxinyuanqu/b80e120h3q2/''')
    # ganji2 = getHtml('''http://dl.ganji.com/fang5/gaoxinyuanqu/b80e120h3o2q2/''')
    # ganji3 = getHtml('''http://dl.ganji.com/fang5/gaoxinyuanqu/b80e120h3o3q2/''')
    # ganji_htmls = [ganji1, ganji2, ganji3]
    # for ganji_html in ganji_htmls:
    #     ganji_save(ganji_html)

    print("生成报告中...")
    rep = reportData()
    reportFileName = rep.get_report()
    webbrowser.open('''file:///''' + os.path.dirname(__file__) + '''/reports/''' + reportFileName)

    print("OVER!!!")
