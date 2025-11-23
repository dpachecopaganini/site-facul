from flask import Flask, render_template, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "secret-key-politicia"

# 10 imagens com respostas corretas
imagens = [
    {"arquivo": "img3.jpeg", "correta": "ia"},
    {"arquivo": "img4.jpg", "correta": "ia"},
    {"arquivo": "img5.jpeg", "correta": "ia"},
    {"arquivo": "img7.jpeg", "correta": "ia"},
    {"arquivo": "img1.jpg", "correta": "ia"},
    {"arquivo": "img2.png", "correta": "real"},
    {"arquivo": "img6.jpeg", "correta": "real"},
    {"arquivo": "img8.jpeg", "correta": "real"},
    {"arquivo": "img9.jpeg", "correta": "real"},
    {"arquivo": "img10.png", "correta": "real"},
]

#     Imanges novas para adicionar futuramente
#    {"arquivo": "img11.png", "correta": "ia"},
#    {"arquivo": "img12.png", "correta": "ia"},
#    {"arquivo": "img13.png", "correta": "real"},
#    {"arquivo": "img14.png", "correta": "real"},
#    {"arquivo": "img15.png", "correta": "real"},
 
@app.route("/")
def index():
    session["fase"] = 1
    session["score"] = 0
    return render_template("index.html")

@app.route("/game")
def game():
    fase = session.get("fase", 1)
    if fase > len(imagens):
        return redirect(url_for("forms"))  # redireciona pro formulário antes do final

    imagem_atual = imagens[fase - 1]["arquivo"]
    return render_template("game.html", imagem=imagem_atual, fase=fase)

@app.route("/responder/<resposta>")
def responder(resposta):
    fase = session.get("fase", 1)
    if fase > len(imagens):
        return redirect(url_for("forms"))

    correta = imagens[fase - 1]["correta"]
    if resposta == correta:
        session["score"] = session.get("score", 0) + 1

    session["fase"] = fase + 1
    return redirect(url_for("game"))

@app.route("/forms")
def forms():
    return render_template("forms.html")

@app.route("/final")
def final():
    score = session.get("score", 0)
    total = len(imagens)
    return render_template("final.html", score=score, total=total)

@app.route("/sobre")
def sobre():
    return render_template("sobre.html")

@app.route("/politica")
def politica():
    return render_template("politica.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
