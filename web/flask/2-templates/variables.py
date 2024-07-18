from flask import Flask, render_template

app = Flask(__name__)


# 객체 정의 예시
class MyObject:
    def somemethod(self):
        return "Object Method Value"


@app.route("/")
def index():
    mydict = {"key": "Dictionary Value"}
    mylist = ["list0", "list1", "list2", "list3", "list4"]
    myintvar = 2
    myobj = MyObject()
    return render_template(
        "variables.html", mydict=mydict, mylist=mylist, myintvar=myintvar, myobj=myobj
    )


if __name__ == "__main__":
    app.run(debug=True)
