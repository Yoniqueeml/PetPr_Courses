import uuid
from flask import Flask, jsonify, request
from flask_cors import CORS

MOOCS = [
    {
        'id': uuid.uuid4().hex,
        'title': 'Coursera',
    },
    {
        'id': uuid.uuid4().hex,
        'title': 'Stepik',
    },
]

Courses = {'Coursera': {'DeepLearning': {'1': ['01_Welcome', '02_What is a neural network', '03_Supervised Learning with Neural Networks', '04_Why is Deep Learning taking off', '05_About this Course', '07_Course Resources'], '2': ['CatRecognition']},
                        'Cryptography': {'1': ['Introduction', 'Cesar']}}}

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


@app.route('/', methods=['GET'])
def get_courses():
    response_object = {'status': 'success'}
    response_object['sites'] = MOOCS
    return jsonify(response_object)


@app.route('/<site>', methods=['GET'])
def get_materials(site):
    for i in Courses.keys():
        if (str(i) == str(site)):
            return jsonify(Courses[i])
    return 'nothing'


@app.route('/<site>/<course>', methods=['GET'])
def get_week_materials(site, course):
    for i in Courses.keys():
        if (str(i) == str(site)):
            for k in Courses[i]:
                if (str(course) == k):
                        print(Courses[i][k])
                        return jsonify(Courses[i][k])


if __name__ == '__main__':
    app.run()
