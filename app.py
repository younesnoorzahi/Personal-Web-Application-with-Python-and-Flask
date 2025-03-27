from flask import Flask, render_template, request, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)  # For form security

# Contact form class
class ContactForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    message = TextAreaField('Message', validators=[DataRequired()])
    submit = SubmitField('Send Message')

# Sample data - you would replace this with your own information
personal_info = {
    'name': 'Your Name',
    'title': 'Web Developer & Python Enthusiast',
    'bio': 'I am a passionate web developer with expertise in Python and web technologies.',
    'skills': ['Python', 'Flask', 'HTML/CSS', 'JavaScript', 'SQL', 'Git'],
    'projects': [
        {
            'name': 'Project 1',
            'description': 'A web application built with Flask and SQLAlchemy.',
            'link': '#'
        },
        {
            'name': 'Project 2',
            'description': 'Data analysis project using Pandas and Matplotlib.',
            'link': '#'
        },
        {
            'name': 'Project 3',
            'description': 'REST API built with Flask-RESTful.',
            'link': '#'
        }
    ]
}

# Routes
@app.route('/')
def home():
    return render_template('index.html', info=personal_info)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        # In a real application, you would process the form data here
        # For example, send an email or save to a database
        print(f"Message from {form.name.data} ({form.email.data}): {form.message.data}")
        flash('Your message has been sent successfully!', 'success')
        return redirect(url_for('home'))
    return render_template('contact.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)

# Note: In a production environment, you would:
# 1. Use a proper database instead of in-memory data
# 2. Configure email sending for the contact form
# 3. Set up proper error handling
# 4. Use environment variables for sensitive information