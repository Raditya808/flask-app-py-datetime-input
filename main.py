from flask import Flask, render_template, request
import datetime as dt  

app = Flask(__name__)

@app.route("/")
def index():
    waktu_sekrang =  dt.date.today()
    return render_template("index.html",waktu=waktu_sekrang)

@app.route("/inputtes",methods=["GET","POST"])
def index2():
    if request.method == "POST":
        tahun = int(request.form["tahun"])
        bulan = int(request.form["bulan"])
        hari  = int(request.form['hari'])
    
        full_data = dt.date(tahun,bulan,hari)
        waktu_sekarang = dt.date.today()
        selisih_waktu = waktu_sekarang - full_data
        return render_template("index2.html",data_lahir=full_data,dtful=selisih_waktu,flldata=waktu_sekarang)
    return render_template("index2.html")
  
        
@app.route("/inputtes2",methods=["GET","POST"])
def index3():
        hri_ini = dt.date.today()
        if request.method == "POST":
            tahun = int(request.form["tahun"])
            bulan = int(request.form["bulan"])
            hari  = int(request.form['hari'])
    
            full_data = dt.date(tahun,bulan,hari)
            waktu_sekarang = dt.date.today()
            selisih_waktu = waktu_sekarang - full_data
            umur_anda = selisih_waktu.days // 365
            return render_template("index3.html",data_lahir=full_data,umur_lu=umur_anda)
        return render_template("index3.html",hari_ini=hri_ini)

@app.route("/about")
def index4():
    return render_template("about.html")
        


if __name__ =='__main__':

    app.run(debug=True)
    




















































































































