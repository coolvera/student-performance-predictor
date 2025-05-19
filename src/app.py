from flask import Flask, render_template, request
import joblib
import os

app = Flask(__name__)

# Load the model
model = joblib.load('models/performance_model.joblib')

# Ethnicity mapping (replace with your actual categories)
ethnicity_map = {
    0: "Group A",
    1: "Group B",
    2: "Group C",
    3: "Group D",
    4: "Group E"
}

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get form data
        math_score = float(request.form['math_score'])
        reading_score = float(request.form['reading_score'])
        writing_score = float(request.form['writing_score'])
        
        # Make prediction
        prediction = model.predict([[math_score, reading_score, writing_score]])
        predicted_ethnicity = ethnicity_map[prediction[0]]
        
        return render_template('index.html', 
                             prediction=predicted_ethnicity,
                             math_score=math_score,
                             reading_score=reading_score,
                             writing_score=writing_score)
    
    return render_template('index.html', prediction=None)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)