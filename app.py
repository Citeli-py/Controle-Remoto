from flask import Flask, render_template, redirect, url_for, request
from utils import getToken, getUrl, showQrcode
from threading import Thread
from shortcuts import Default

app = Flask("Controle Remoto")
TOKEN = getToken()
controler = Default()

@app.route(f'/token={TOKEN}/')
def index():
  return render_template('index.html', token=TOKEN)


@app.route(f'/token={TOKEN}/pause')
def pause():
  controler.pause()
  print(f"\nRequested PAUSE from {request.remote_addr}\n")
  return redirect(url_for("index"))


@app.route(f'/token={TOKEN}/increase_volume')
def increase_volume():
  controler.aumentarVolume()
  print(f"\nRequested VOLUME+ from {request.remote_addr}\n")
  return redirect(url_for("index"))


@app.route(f'/token={TOKEN}/decrease_volume')
def decrease_volume():
  controler.diminuirVolume()
  print(f"\nRequested VOLUME- from {request.remote_addr}\n")
  return redirect(url_for("index"))


@app.route(f'/token={TOKEN}/fullscreen')
def fullscreen():
  controler.fullScreen()
  print(f"\nRequested FULLSCREEN from {request.remote_addr}\n")
  return redirect(url_for("index"))

@app.route(f'/token={TOKEN}/qrcode')
def qrcodepage():
  print(f"\nRequested QRCODE from {request.remote_addr}\n")
  return render_template("qrcode.html")


if __name__ == "__main__":
  showQR_Thread = Thread(target=showQrcode())
  appRun_Thread = Thread(target=app.run(host='0.0.0.0', port=80))

  print("Running in " + getUrl())
  showQR_Thread.start()
  appRun_Thread.start()