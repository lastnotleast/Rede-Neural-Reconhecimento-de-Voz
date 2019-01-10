from app import app, db, login_manager
from flask import render_template, flash, redirect, url_for, request, send_from_directory, Response, make_response, send_file, session

from flask_login import login_user, logout_user, user_loaded_from_header
from app.models.forms import LoginForm
from app.models.tables import User
from flask import jsonify
from app.controllers.GravarAudio import Audio, RecordingThread, RNA
import time
from pybrain.tools.customxml.networkreader import NetworkReader
global Captar_audio
from flask_login import current_user
Captar_audio = None
global_frame = None
global global_imagem
global_imagem = "/static/img/CadeadoFechado.png"
rede = NetworkReader.readFrom('treinamento.xml')
@login_manager.user_loader
def load_user(id):
    return User.query.filter_by(id=id).first()


@app.route('/')
@app.route('/imagem/<imagem>')
def index(imagem=None):
    if current_user.is_authenticated:
        if imagem is not None:
            imagem = "/static/img/"+ imagem
            return render_template('index.html', global_imagem=imagem)
        else:
            return render_template('index.html', global_imagem=global_imagem)
    else:
        print(User)
        return redirect(url_for("login"))




@app.route('/record_status', methods=['POST'])
def record_status():
    global Captar_audio
    if Captar_audio == None:
        Captar_audio = Audio(rede)

    json = request.get_json()

    status = json['status']

    if status == "true":
        Captar_audio.start_record()
        return jsonify(result="started")
    else:
        Captar_audio.stop_record()
        return jsonify(result="stopped")


def video_stream():
    global Captar_audio
    global global_frame

    if Captar_audio == None:
        teste = RecordingThread(rede)

    while True:
        frame = teste.get_frame()
        global global_imagem
        global_imagem = frame

        if frame != None:
            global_frame = "/img/CadeadoFechado.png"
            yield (frame)
        else:
            yield (global_frame)

@app.route('/video_viewer')
def video_viewer():
    return Response(video_stream())

@app.route("/login", methods=["GET","POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        usuario = User.query.filter_by(username=form.username.data).first()
        print(usuario.password)
        if usuario and usuario.password == form.password.data:
            login_user(usuario)
            flash('Login realizado com sucessso')
            return redirect(url_for("index"))
        else:
            flash('Login invalido')
    return render_template('login.html', form=form)

@app.route("/logout")
def logout():
    logout_user()
    flash('Usuário deslogado com sucesso')
    return redirect(url_for("index"))


@app.route("/teste")
def mudarImagem():

    teste = RNA(rede)
    teste.start()
    time.sleep(2)
    frame = teste.get_frame()
    print(frame)
    imagem = "/static/img/" + frame
    global global_imagem
    global_imagem = imagem
    return redirect(url_for("index"))

