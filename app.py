from flask import Flask, render_template, request
import smtplib
from email.message import EmailMessage

app = Flask(__name__)

EMAIL = "scoutme51@gmail.com"
PASSWORD = "APP_PASSWORD_KAMU"
TUJUAN = "android@support.whatsapp.com"


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/kirim", methods=["POST"])
def kirim():
    nomor = request.form.get("nomor", "").strip()

    if not nomor:
        return "Nomor WhatsApp wajib diisi."

    pesan = f"""LAPORAN SPAM

Saya melaporkan nomor {nomor} karena mengirimkan pesan spam dan berbagai tautan yang tidak diminta, termasuk tautan mencurigakan, promosi yang tidak diinginkan, judi online, penipuan, dan konten lainnya yang mengganggu pengguna.

PERMINTAAN TINDAKAN SEGERA

Mohon WhatsApp segera meninjau nomor tersebut dan menindaklanjuti laporan ini dengan tegas. Mohon berikan tindakan berupa pembatasan, penandaan sebagai spam, atau pemblokiran (banned) terhadap nomor tersebut sesuai prosedur yang berlaku.

Mohon laporan ini diproses dan ditindaklanjuti sesegera mungkin.

Terima kasih.
"""

    msg = EmailMessage()
    msg["Subject"] = "LAPORAN SPAM"
    msg["From"] = EMAIL
    msg["To"] = TUJUAN
    msg.set_content(pesan)

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(EMAIL, PASSWORD)
            server.send_message(msg)

        return """
        <!DOCTYPE html>
        <html lang="id">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Berhasil</title>
            <style>
                body {
                    margin: 0;
                    min-height: 100vh;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    font-family: Arial, sans-serif;
                    background: #f5f5f5;
                }

                .box {
                    width: 90%;
                    max-width: 430px;
                    background: white;
                    padding: 35px;
                    border-radius: 20px;
                    text-align: center;
                    box-shadow: 0 8px 30px rgba(0,0,0,0.15);
                }

                h2 {
                    color: #25d366;
                }

                a {
                    display: inline-block;
                    margin-top: 15px;
                    padding: 12px 25px;
                    background: #25d366;
                    color: white;
                    text-decoration: none;
                    border-radius: 10px;
                }
            </style>
        </head>
        <body>
            <div class="box">
                <h2>✓ Laporan Berhasil Dikirim</h2>
                <p>Nomor: {}</p>
                <a href="/">Kembali</a>
            </div>
        </body>
        </html>
        """.format(nomor)

    except Exception as e:
        return f"Terjadi error: {e}"


if __name__ == "__main__":
    app.run(debug=True)
