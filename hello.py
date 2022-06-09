from turtle import color
from flask import Flask , render_template 
app=Flask(__name__)



@app.route('/play') 
def show_user_profile():
     return render_template('index.html')
    

@app.route('/play/<id>') 
def show_user_profile1(id):
     return render_template('index1.html',num=int(id))


     
@app.route('/play/<id>/<color>')
def show_user_profile2(id,color):

    return  render_template('index2.html' , num=int(id), color=color)


if __name__=="__main__":
    app.run(debug=True)