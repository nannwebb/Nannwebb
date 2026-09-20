from flask import Flask, render_template, request
import smtplib
from email.message import EmailMessage

app = Flask(__name__)

EMAIL = "scoutme51@gmail.com"
PASSWORD = "hpyf grxp bddk jtaf"
TUJUAN = "android@support.whatsapp.com"

JUMLAH_KIRIM = 100


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/kirim", methods=["POST"])
def kirim():
    nomor = request.form.get("nomor", "").strip()
    subjek = request.form.get("subjek", "").strip()
    isi = request.form.get("isi", "").strip()

    pesan = f"""Halo Tim Support WhatsApp,

Saya ingin melaporkan sebuah akun WhatsApp.

Nomor WhatsApp yang dilaporkan:
{nomor}

Isi laporan:
{isi}

Mohon pihak WhatsApp meninjau laporan ini sesuai kebijakan yang berlaku.

Terima kasih.
"""

    msg = EmailMessage()
    msg["Subject"] = subjek
    msg["From"] = EMAIL
    msg["To"] = TUJUAN
    msg.set_content(pesan)

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(EMAIL, PASSWORD)
            server.send_message(msg)

        return "Laporan berhasil dikirim 1×."

    except Exception as e:
        return f"Terjadi error: {e}"


if __name__ == "__main__":
    app.run(debug=True)
