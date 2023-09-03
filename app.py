from flask import Flask, render_template, request, send_file, redirect, url_for, session
from image_generate import generate_wish_card_image
import os
app = Flask(__name__)

app.secret_key = '0889704444a2a2816ddc707e55435d40'
if not os.path.exists("static/generated_cards"):
    os.makedirs("static/generated_cards")

#only if reverse proxy
# from werkzeug.middleware.proxy_fix import ProxyFix
# app.wsgi_app = ProxyFix(
#     app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1
# )


@app.route('/',methods=['GET'])
def home():
    return render_template('index.html',name="home")

@app.route('/generate_card',methods=['POST'])
def generate_card():
    if request.method == "POST":
        template = request.form.get('template')
        recipient = request.form.get('recipient')
        sender = request.form.get('sender')
        session['sender'] = sender
        if (generate_wish_card_image(image=template,sender=sender,receiver=recipient)):
            return redirect(url_for('thanks'))
        else:
            return 'error!!! Go back <a href="/">home</a>'
            
@app.route('/thanks',methods=['GET'])
def thanks():
    if (session.get('sender')):
        return render_template('thanks.html',context=f"static/generated_cards/card_{session.get('sender').lower()}.png")
    else:
        return 'error!!! Go back <a href="/">home</a>'

@app.route('/download')
def download_image():
    image_path = 'static/image.jpg'
    return send_file(image_path, as_attachment=True)

if __name__ == "__main__":
    app.run('0.0.0.0',port=5021,debug=False)