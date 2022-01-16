from flask import Flask
app = Flask(__name__)

@app.route('/caesar/<word>/<int:shift>')
def roming(word, shift):
    enctyption = ""
    text = word
    for i in text:
        if i.isupper():
            i_index = ord(i) - ord("A")
            new_index = (i_index + shift) % 26
            new_unicode = new_index + ord("A")
            new_charatcer = chr(new_unicode)
            enctyption = enctyption + new_charatcer
        else:
            enctyption += i
    return "Исходный - {} шифр - {}".format(text, enctyption)

if __name__ == '__main__':
     app.run(debug=True)
