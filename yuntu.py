import matplotlib.pyplot as plt
import jieba
from wordcloud import WordCloud,ImageColorGenerator
from PIL import Image
import numpy as np
# 读入txt文本数据
text = open(r'元尊.txt', "r",encoding="utf-8").read()

# 结巴分词
seg_list = jieba.cut(text,cut_all=False)
result = "/".join(seg_list)

image = Image.open(r'C:\Users\Administrator\Desktop\timg (1).jpg')
graph = np.array(image)

#生成词云图
wc = WordCloud(font_path=r"D:\weiruan.ttf", background_color='white',max_font_size=50,mask=graph)  # ,min_font_size=10)#,mode='RGBA',colormap='pink')
#generate（文本）从文本生成wordcloud。
wc.generate(result)
#从背景图片生成颜色值
image_color = ImageColorGenerator(graph)
wc.recolor(color_func=image_color)
wc.to_file("wordcloud1.png")
#显示图片
plt.figure("词云图")  # 指定所绘图名称
plt.imshow(wc)  # 以图片的形式显示词云
plt.axis("off")  # 关闭图像坐标系
plt.show()

