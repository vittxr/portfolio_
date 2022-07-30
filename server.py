from flask import Flask, redirect, render_template, request, url_for 
from flask_mail import Mail, Message 
from config import config

app = Flask(__name__)
app.config.from_object(config['default'])

mail = Mail(app)

@app.route("/")
def index(): 
    mail_response = request.args.get("mail_response")
    if mail_response: 
        return render_template("index.html", mail_response=mail_response)
        
    return render_template("index.html")

@app.route("/sendMail", methods=["POST"])
def sendMail():
    if request.form: 
        sender_name=request.form.get("name")
        sender_email=request.form.get("email")
        msg_content = request.form.get("msg_content")

        msg = Message("Email do Portfolio", sender="vitor.roberto3022@outlook.com", recipients=["vitor.roberto3022@gmail.com"])

        msg.body = f"""
                     message: {msg_content}
                     enviado por -> name: {sender_name}  email: {sender_email}
                   """

        with app.app_context():
            mail.send(msg)

        return redirect(url_for("index", mail_response="Email enviado com sucesso! Obrigado pelo contato :)."))
    return redirect(url_for("index", mail_response="Algo deu errado. Tente novamente, por favor"))
    
if __name__ == '__main__':
    app.run(debug=1)