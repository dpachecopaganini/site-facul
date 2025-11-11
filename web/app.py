from flask import Flask, render_template, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "secret-key-facemesh"

# 10 imagens e suas respostas corretas
imagens = [
    {"arquivo": "img1.jpg", "correta": "real"},
    {"arquivo": "img2.jpg", "correta": "ia"},
    {"arquivo": "img3.jpg", "correta": "real"},
    {"arquivo": "img4.jpg", "correta": "ia"},
    {"arquivo": "img5.jpg", "correta": "ia"},
    {"arquivo": "img6.jpg", "correta": "real"},
    {"arquivo": "img7.jpg", "correta": "ia"},
    {"arquivo": "img8.jpg", "correta": "real"},
    {"arquivo": "img9.jpg", "correta": "ia"},
    {"arquivo": "img10.jpg", "correta": "real"},
]

@app.route("/")
def index():
    session["fase"] = 1
    session["score"] = 0
    return render_template("index.html")

@app.route("/game")
def game():
    fase = session.get("fase", 1)
    if fase > len(imagens):
        return redirect(url_for("final"))

    imagem_atual = imagens[fase - 1]["arquivo"]
    return render_template("game.html", imagem=imagem_atual, fase=fase)

@app.route("/responder/<resposta>")
def responder(resposta):
    fase = session.get("fase", 1)

    # Evita erro se ultrapassar a última fase
    if fase > len(imagens):
        return redirect(url_for("final"))

    correta = imagens[fase - 1]["correta"]

    # Compara resposta do jogador com a correta
    if resposta == correta:
        session["score"] = session.get("score", 0) + 1

    # Avança para próxima fase
    session["fase"] = fase + 1

    return redirect(url_for("game"))

@app.route("/final")
def final():
    score = session.get("score", 0)
    total = len(imagens)
    return render_template("final.html", score=score, total=total)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
