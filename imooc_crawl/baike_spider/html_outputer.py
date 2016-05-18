# coding:utf-8

class HtmlOutputer(object):

    def __init__(self):
        self.datas=[]

    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    def output_html(self):
        fout = open("output.html", "w")

        fout.write(r"<html>")
        fout.write(r"<meta charset='utf-8'>")
        fout.write(r"<body>")
        fout.write(r"<table>")

        for data in self.datas:
            fout.write(r"<tr>")
            fout.write(r"<td>%s</td>" % data['title'].encode('utf-8'))
            fout.write(r"<td>%s</td>" % data['url'])
            fout.write(r"<td>%s</td>" % data['summary_node'].encode('utf-8'))
            fout.write(r"</tr>")

        fout.write(r"</table>")
        fout.write(r"</body>")
        fout.write(r"</html>")

        fout.close()