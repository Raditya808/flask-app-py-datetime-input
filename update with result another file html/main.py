from flask import Flask, render_template, request, redirect, url_for
import datetime as dt 

app = Flask(__name__)



# rute tampilan web pertama tidak ada slash variabel 
@app.route("/")
def index():
    waktu_sekrang = dt.date.today()
    return render_template("index.html",waktu=waktu_sekrang)


# rute kedua menghitung jarak antarq tanggal hari ini dan user 
@app.route("/inputtes",methods=["GET","POST"])
def index2():
     if request.method == "POST":
        tahun = int(request.form["tahun"])
        bulan = int(request.form["bulan"])
        hari = int(request.form['hari'])

        full_data = dt.date(tahun,bulan,hari)
        waktu_sekarang = dt.date.today()
        selisih_waktu = waktu_sekarang - full_data

         #  mengitim data menggunakan syntax redirect url_for di rute hasil_jarak
        return redirect(url_for('hasil_jarak', 
                                data_lahir=full_data, 
                                dtful=selisih_waktu, 
                                flldata=waktu_sekarang)) 
 
     return render_template("index2.html")



# bagian menghitung umur dari user 
@app.route("/inputtes2",methods=["GET","POST"])
def index3():
    hri_ini = dt.date.today()
    if request.method == "POST":
        tahun = int(request.form["tahun"])
        bulan = int(request.form["bulan"])
        hari = int(request.form['hari'])

        full_data = dt.date(tahun,bulan,hari)
        waktu_sekarang = dt.date.today()
        selisih_waktu = waktu_sekarang - full_data
        umur_anda = selisih_waktu.days // 365

        # mengirim data menggunakan syntax redirect url_for du rute hasil_umur
        return redirect(url_for('hasil_umur', 
                            full_data=full_data, 
                            umur_anda=umur_anda))

    return render_template("index3.html",hari_ini=hri_ini)


# rute web about dengan mengirim render template lewat html file
@app.route("/about")
def index4():
    return render_template("about.html")


# rute web hasil_jarak
@app.route("/hasil_jarak")
def hasil_jarak():
    # menerima data dari rute index2
    # membuat parameter variabel yang nentinya di kirim ke html
    # ke hasil hasil_jarak.html
    data_lahir = request.args.get('data_lahir') # menerima parameter variabek dari rute index2 
    dtful = request.args.get('dtful') # menerima parameter variabek dari rute index2 
    flldata = request.args.get('flldata') # menerima parameter variabek dari rute index2 

    # mengirim rute ke file htmll hasil_jarak.html
    return render_template("hasil_jarak.html", data_lahir=data_lahir, dtful=dtful, flldata=flldata) # membuat parameter yang sama yang akan di kirim ke kode html hasil_jarak.html



@app.route("/hasil_umur")
def hasil_umur():
    # menerima data dari rute index3
    full_data = request.args.get('full_data') # menerima parameter variabel dari rute index3 
    umur_lu = request.args.get('umur_anda') # menerima parameter variabel dari rute index3 

    return render_template("hasil_umur.html", full_data=full_data, umur_lu=umur_lu)







if __name__ =='__main__':
    app.run(debug=True)
