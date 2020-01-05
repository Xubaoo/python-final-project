import pandas as pd
from flask import Flask
from flask import render_template, request, redirect
from pyecharts.charts import EffectScatter, Bar, Line, WordCloud, Map, Grid
from pyecharts.charts import Scatter
import numpy as np
from pyecharts.charts import Geo
from pyecharts import options as opts
from pyecharts.globals import ChartType, SymbolType, ThemeType
from pyecharts.charts import Bar, Tab, Line, Map, Timeline

app = Flask(__name__)


@app.route('/')
def index():
    data1 = pd.read_csv(r"./static/data/country_females.csv")
    data2 = pd.read_csv(
        r"./static/data/country_males.csv")
    data3 = pd.read_csv(
        r"./static/data/data_1.csv")
    data4 = pd.read_csv(
        r"./static/data/mental.csv")
    data1_x = data1.columns.values
    data2_x = data2.columns.values
    data3_x = data3.columns.values
    data4_x = data4.columns.values

    data1_y = data1.values.tolist()
    data2_y = data2.values.tolist()
    data3_y = data3.values.tolist()
    data4_y = data4.values.tolist()
    return render_template("index.html", data1_x=data1_x[1:], data2_x=data2_x[1:], data3_x=data3_x[1:],
                           data4_x=data4_x[1:], data1_y=data1_y, data2_y=data2_y, data3_y=data3_y, data4_y=data4_y,
                           a=1)


@app.route('/word1')
def index_bar():
    df = pd.read_csv("./static/data/country_females.csv")
    tl = Timeline()
    for i in range(2014, 2018):
        map0 = (
            Map()
                .add(
                "女性患病率", list(zip(list(df.Country), list(df["{}".format(i)]))), "world", is_map_symbol_show=False
            )
                .set_global_opts(
                title_opts=opts.TitleOpts(title="{}年女性患病率".format(i), subtitle="",
                                          subtitle_textstyle_opts=opts.TextStyleOpts(color="red", font_size=18,
                                                                                     font_style="italic")),
                visualmap_opts=opts.VisualMapOpts(min_=10, max_=20)

            )
        )
        tl.add(map0, "{}年".format(i))
    return render_template('index.html',
                           myechart=tl.render_embed(),
                           text='''
                           女性心理健康患病率在国家和地区间的分布大致同男性的差不多。
                           经济较发达的欧洲、美洲及大洋洲的心理健康患病率的比例较高
                           且四年间的变化趋势也趋于稳定，这与经济和社会发展水平有着密切联系，
                           随着社会医疗保障体系的完善，心理健康患病率正趋于稳定和下降趋势。''')


@app.route('/word2')
def index_word():
    df = pd.read_csv("./static/data/country_males.csv")
    tl = Timeline()
    for i in range(2014, 2018):
        map0 = (
            Map()
                .add(
                "男性患病率", list(zip(list(df.Country), list(df["{}".format(i)]))), "world", is_map_symbol_show=False
            )
                .set_global_opts(
                title_opts=opts.TitleOpts(title="{}年女性患病率".format(i), subtitle="",
                                          subtitle_textstyle_opts=opts.TextStyleOpts(color="red", font_size=18,
                                                                                     font_style="italic")),
                visualmap_opts=opts.VisualMapOpts(min_=10, max_=20)

            )
        )
        tl.add(map0, "{}年".format(i))
    return render_template('index.html',
                           myechart=tl.render_embed(),
                           text='''
                           由地图可知2014年-2017年亚洲、俄罗斯及部门南美洲地区的男性心理健康患病率
                           比欧洲、美国、澳洲要低，由此可见发达国家和地区患心理健康疾病的比例也比欠
                           发达的国家和地区高。且四年间的变化率不大，相对于较稳定趋势。''')


@app.route('/index_scatter12')
def index_scatter12():
    data = pd.read_csv("./static/data/mental.csv")
    columns = data.columns.values
    data_y = data["males"].values.tolist()
    data_x = data["Country"].values.tolist()
    c = (
        Scatter()
            .add_xaxis(data_x)
            .add_yaxis("各国男性患病率", data_y)
            .set_global_opts(
            title_opts=opts.TitleOpts(title="各国男性患病率"),
            visualmap_opts=opts.VisualMapOpts(min_=min(data_y), max_=max(data_y)),
        )
    )
    return render_template('index.html',
                           myechart=c.render_embed(),
                           text='''
                           由男女性心理健康患病率的散点图对比分析可知，男性的患病率集中在10%-15%之间，
                           最高的比例也未超过18%；而女性的患病率多集中在11%-17%之间，且最高的患病比例已超过20%，
                           可见这种疾病在女性中比在男性中更为常见。这与女性在社会中所处地位较低，
                           心理和生理健康都比男性要脆弱，社会上应对女性的心理健康提供更多的保障。''')


@app.route('/index_scatter11')
def index_scatter11():
    data = pd.read_csv("./static/data/mental.csv")
    columns = data.columns.values
    data_y = data["females"].values.tolist()
    data_x = data["Country"].values.tolist()
    c = (
        Scatter()
            .add_xaxis(data_x)
            .add_yaxis("各国女性患病率", data_y)
            .set_global_opts(
            title_opts=opts.TitleOpts(title="各国男性患病率"),
            visualmap_opts=opts.VisualMapOpts(min_=min(data_y), max_=max(data_y)),
        )
    )
    return render_template('index.html',
                           myechart=c.render_embed(),
                           text='''
                           由男女性心理健康患病率的散点图对比分析可知，男性的患病率集中在10%-15%之间，
                           最高的比例也未超过18%；而女性的患病率多集中在11%-17%之间，且最高的患病比例已超过20%，
                           可见这种疾病在女性中比在男性中更为常见。这与女性在社会中所处地位较低，
                           心理和生理健康都比男性要脆弱，社会上应对女性的心理健康提供更多的保障。''')


@app.route('/bar')
def index_scatter():
    df = pd.read_csv("./static/data/data_1.csv")
    columns = df.columns.values.tolist()
    tl = Timeline()
    for i in range(2007, 2017):
        bar = (
            Bar()
                .add_xaxis(columns[1:])
                .add_yaxis("男性", list(df.iloc[0])[1:])
                .add_yaxis("女性", list(df.iloc[1])[1:])
                .set_global_opts(title_opts=opts.TitleOpts("中国男女性心理健康障碍患病率".format(i)))
        )
        tl.add(bar, "{}年".format(i))
    return render_template('index.html',
                           myechart=tl.render_embed(),
                           text='''
                           由我们国家2007年到2017年男女性心理健康患病率对比可知，女性虽还是比男性患病率
                           比率高一点点，但两者已经不断趋平，且总体上患病率也逐年下降。这说明，
                           我们国家的医疗普及水平，以及对心理健康的关怀程度不断提升，让国民心理健康得到更多保障。''')


@app.route('/duibi')
def index_scatter1():
    df = pd.read_csv("./static/data/data_1.csv")
    bar = (
        Bar()
            .add_xaxis(list(df.set_index('指标').columns))
            .add_yaxis("中国男性", list(df.iloc[0])[1:])
            .add_yaxis("中国女性", list(df.iloc[1])[1:])
            .add_yaxis("美国男性", list(df.iloc[2])[1:])
            .add_yaxis("美国女性", list(df.iloc[3])[1:])
            .set_global_opts(title_opts=opts.TitleOpts(title="对比图1"))
    )
    line = (
        Line()
            .add_xaxis(list(df.set_index('指标').columns))
            .add_yaxis("中国男性", list(df.iloc[0])[1:])
            .add_yaxis("中国女性", list(df.iloc[1])[1:])
            .add_yaxis("美国男性", list(df.iloc[2])[1:])
            .add_yaxis("美国女性", list(df.iloc[3])[1:])
            .set_global_opts(
            title_opts=opts.TitleOpts(title="对比图2", pos_top="60%"),
            legend_opts=opts.LegendOpts(pos_top="60%"),
        )
    )

    grid = (
        Grid()
            .add(bar, grid_opts=opts.GridOpts(pos_bottom="60%"))
            .add(line, grid_opts=opts.GridOpts(pos_top="60%"))
    )
    return render_template('index.html', myechart=grid.render_embed(),
                           text='''由中美心理健康患病率对比图可知，美国男女性的心理健康患病率远高于中国男女性。
                           这或许与国家的福利制度、经济发展水平有着密切的联系。且美国女性的心理健康患病比例逐年
                           与美国男性的比例拉大，而相反中国以及逐渐趋平甚至降低。
                           综上，我们发现在大多数国家中，这种疾病在女性中比在男性中更为常见，这种情况因疾病类型而异：
                           平均而言，抑郁症，焦虑症，进食障碍和躁郁症在女性中更为普遍。
                           精神分裂症患病率的性别差异在各个国家参差不齐，
                           但在男性中通常更为常见。酒精和药物滥用疾病在男性中更为常见。
                           国家对国民的心理健康关注程度刻不容缓。''' )


@app.route('/wordX')
def word():
    prevention = request.args.get("city")
    if prevention == "1":
        return redirect("/index_scatter12")
    elif prevention == "2":
        return redirect("/index_scatter11")
    elif prevention == "3":
        return redirect("/word2")
    else:
        return redirect("/word1")


if __name__ == '__main__':
    app.run(debug=True)
