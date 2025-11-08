from flask import Flask, render_template

app = Flask(__name__)

# Home Page
@app.route('/')
def home():
    return render_template('index.html')

# Jobs Page
@app.route('/jobs')
def jobs():
    return render_template('jobs.html')

# Resume Analyzer Page
@app.route('/resume-analyzer')
def analyzer():
    return render_template('resume-analyzer.html')

# Resume Builder Page
@app.route('/resume-builder')
def builder():
    return render_template('resume-builder.html')

# Courses Page
@app.route('/courses')
def courses():
    return render_template('courses.html')

# Internships Page
@app.route('/internships')
def internships():
    return render_template('internships.html')

# Career Predictor Page
@app.route('/career-predictor')
def predictor():
    return render_template('career-predictor.html')

# Run the Flask App
if __name__ == '__main__':
    app.run(debug=True)
