from flask import Flask, render_template, request,url_for, redirect
import datetime as dt  

app = Flask(__name__)

# rute awal web 
@app.route("/")
def index():
    waktu_sekrang =  dt.date.today()
    return f"""
    <!DOCTYPE html>
    <html>
        <head>
            <title>Menu Awal</title>
         </head>
        <body>
            <div class="waktu_sekarang">
            <h1>Flask Import Datetime</h1>
            <p>Tanggal Sekarang {waktu_sekrang}</p>
            </div>
            
            <section class="index2_jarak_umur">
            <h3>Input Jarak Umur?</h3>
            <button>
            <a href="{url_for('index2')}">Input Jarak</a>
            </button>
            </section>

            <section class="index3_umur">
            <h3>Input Umur?</h3>
                <button>
                <a href="{url_for('index3')}">Input Umur</a>
                </button>
            </section>

            <section class="source">
            <h3>Source Code</h3>
                <button>
                <a href="{url_for('index4')}">Source Code</a>
                </button>
            </section>
        </body>
    </html>
    """

# input jarak dari function index2 
# ini menggunakan render_template
@app.route("/inputtes",methods=["GET","POST"])
def index2():
    waktu_sekarang = dt.date.today()
    if request.method == "POST":
        tahun = int(request.form["tahun"])
        bulan = int(request.form["bulan"])
        tanggal  = int(request.form['tanggal'])
    
        full_data = dt.date(tahun,bulan,tanggal)
        selisih_waktu = waktu_sekarang - full_data

        # return ke hasil function index2_hasil_jarak lewat render_template
        return render_template("index2.html",full_data=full_data,selisih_waktu=selisih_waktu)
    return f"""
    <!DOCTYPE html>
    <html>
        <head>
            <title>Input Jarak</title>
        </head>
        <body>
            <div class="waktu_sekarang">
            <h1>Input Jarak Umur</h1>
            <p>Tanggal Sekarang {waktu_sekarang}</p>
            </div>

            <!-- metode POST yang di kirim ke file rute index2 -->
            <form method="POST">   
                
                <input type="number" name="tahun" placeholder="Masukan Tahun"><br>

                 <input type="number" name="bulan" placeholder="Masukan Bulan"><br>

                  <input type="number" name="tanggal" placeholder="Masukan hari"><br>
                <input type="submit" value="kirim"> 


                <section class="waktu_sekarang">
                    <h3>Kembali Ke Menu Awal</h3>
                    <button>
                        <a href="{url_for('index')}">Menu Awal</a>
                    </button>
                </section>
            </form>
        </body>
    </html>

"""
 

##############################################################################################################################################
# OPSIONAL JIKA MENGGUNAKAN redirect(url_for('nama function')) maka gunakan kode ini
# hasil_jarak_setelah_input 
#@app.route("/hasil_jarak")
#def index2_hasil_jarak():     
    # hasil input tanggal lahir yang dibungkus function index2 
    #full_data = request.args.get('full_data')
  
    # hasil selisih / jarak dikirim ke index2.html
    #selisih_waktu = request.args.get('selisih_waktu')
    # dikirim ke function index2.html
    #return render_template('index2.html',full_data=full_data,selisih_waktu=selisih_waktu)
##############################################################################################################################################


    



# bagian hitung umur  
# ini menggunakan redirect url_for
@app.route("/inputtes2",methods=["GET","POST"])
def index3():
        hri_ini = dt.date.today()
        if request.method == "POST":
            tahun = int(request.form["tahun"])
            bulan = int(request.form["bulan"])
            tanggal  = int(request.form['tanggal'])
    
            full_data = dt.date(tahun,bulan,tanggal)
            waktu_sekarang = dt.date.today()
            selisih_waktu = waktu_sekarang - full_data
            umur_anda = selisih_waktu.days // 365
            #return render_template("index3.html",data_lahir=full_data,umur_lu=umur_anda)
            return redirect(url_for('hasil_umur',umur_anda=umur_anda,full_data=full_data))
        return f"""
        <!DOCTYPE html>
        <html>
            <head>
                <title>Input Umur</title>
            </head>
            <body>
            <div class="waktu_sekarang">
            <h1>Input Umur</h1>
            <p>Tanggal Sekarang {hri_ini}</p>
            </div>
            
            <form method="POST">
            <input type="number" name="tahun" placeholder="Masukan Tahun"><br>
             <input type="number" name="bulan" placeholder="Masukan Bulan"><br>
              <input type="number" name="tanggal" placeholder="Masukan Tanggal"><br>
              <input type="submit" value="kirim">
            </form>

                <section class="waktu_sekarang">
                    <h3>Kembali Ke Menu Awal</h3>
                    <button>
                        <a href="{url_for('index')}">Menu Awal</a>
                    </button>
            </section>
            </body>
        </html>
        

        """


# hasil redirect url for dari index3 
# mengirim parameter full data dan umur anda kesini
@app.route('/hasil_umur_user')
def hasil_umur():
    hasil_umur = request.args.get('full_data')
    umur_user = request.args.get('umur_anda')
    
    return render_template('index3.html',hasil_umur=hasil_umur,umur_user=umur_user)


# rute about untuk html
@app.route("/about")
def index4():
    return render_template("about.html")
        


if __name__ =='__main__':

    app.run(debug=True)
    




















































































































