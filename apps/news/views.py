from django.shortcuts import render, HttpResponse, loader
import pymysql
from pyecharts.charts import Line, Bar
# Create your views here.

def news(request):
    # coon = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd=' ', db='local', charset='utf8');
    sql = "SELECT * from people"
    # cur = coon.cursor(cursor=pymysql.cursors.DictCursor)
    # cur.execute(sql)
    # result = cur.fetchall()
    # print(result)
    # cur.close()
    # coon.close()
    result = set_sql(sql)
    return HttpResponse(result)

# 链接本地数据库查询数据
def set_sql(sql):
    coon = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd=' ', db='local', charset='utf8');
    cur = coon.cursor(cursor=pymysql.cursors.DictCursor)
    cur.execute(sql)
    result = cur.fetchall()
    # print(result)
    cur.close()
    coon.close()
    return result

def zhu(request):
    # // 导入柱状图 - Bar

    # // 设置行名
    columns = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    # // 设置数据
    data1 = [2.0, 4.9, 7.0, 23.2, 25.6, 76.7, 135.6, 162.2, 32.6, 20.0, 6.4, 3.3]
    data2 = [2.6, 5.9, 9.0, 26.4, 28.7, 70.7, 175.6, 182.2, 48.7, 18.8, 6.0, 2.3]
    # // 设置柱状图的主标题与副标题
    bar = Bar("柱状图", "一年的降水量与蒸发量")
    # // 添加柱状图的数据及配置项
    bar.add("降水量", columns, data1, mark_line=["average"], mark_point=["max", "min"])
    bar.add("蒸发量", columns, data2, mark_line=["average"], mark_point=["max", "min"])
    # // 生成本地文件（默认为.html文件）
    # bar.render()
    return render(request, bar.render)

def line():
    attr = ['教师', '教授', '副教授', '博导', '硕导', '国家级奖项', '省部级奖项', '院士', '荣誉学者', '专利']
    v1 = [100, 20, 15, 50, 40, 200, 200, 4, 5, 100]
    v2 = [150, 30, 40, 50, 30, 250, 200, 1, 2, 110]
    line = Line(width=1834, height=400)
    line.add('北京大学', attr, v1,
             mark_point=['average', 'max', 'min'],  # 标注点：平均值，最大值，最小值
             mark_point_symbol='diamond',  # 标注点：钻石形状
             mark_point_textcolor='#40ff27')  # 标注点：标注文本颜色
    line.add('清华大学', attr, v2,
             mark_point=['average', 'max', 'min'],
             mark_point_symbol='arrow',
             xaxis_name_size=20,
             yaxis_name_size=20,
             )
    return line

def university_picture(request):
    template = loader.get_template('search/test.html')
    l = line()  # 生成图像实例
    context = dict(
        myechart=l.render_embed(),  # 必须要有
        host=REMOTE_HOST,  # 若前端加载了对应的echarts库，可以不需要这一句和下一句
        script_list=l.get_js_dependencies(),  # 以上两句代码的目的是下载该图标对应的一些echarts库
    )
    return HttpResponse(template.render(context, request))
