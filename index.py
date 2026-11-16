from flask import Flask, jsonify, render_template, request

app = Flask(__name__, template_folder='../templates')

@app.get('/')
def home():
    return render_template('index.html')

@app.post('/recommend')
def recommend():
    theme = (request.get_json(silent=True) or {}).get('theme', '')
    tips = {
        'هادئ وعصري': 'استخدمي مساحات بيضاء وألوانًا طبيعية.',
        'فاخر': 'استخدمي لونًا داكنًا مع لمسات ذهبية.',
        'مرح وشبابي': 'استخدمي ألوانًا زاهية وأشكالًا مرحة.',
        'تقني': 'استخدمي خطوطًا واضحة وعناصر هندسية.'
    }
    return jsonify(recommendation=tips.get(theme, 'اختاري أسلوبًا مناسبًا لهوية مشروعك.'))

if __name__ == '__main__':
    app.run(debug=True)
