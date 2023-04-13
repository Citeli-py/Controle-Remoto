import random, socket, qrcode, os

def getToken():
    with open("token.txt", "r") as f:
        token = f.readlines()
        f.close()
    return token[0]

def getIp():
    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)
    return ip

def getUrl():
    return "http://" + getIp() + '/token=' + getToken()

def gerarQrcode():
    img = qrcode.make(getUrl())
    img.save('static/qrcode.png')

def gerarToken():
    token = [str(random.randint(0, 9)) for i in range(10)]
    token = "".join(token)
    
    with open("token.txt", 'w') as f:
        f.write(token)
        f.close()

def showQrcode():
    os.system(f"start {getUrl()}/qrcode")