from flask import Flask, jsonify, request, abort
from flask_cors import CORS


# configuration
DEBUG = True


MOOCs = [
    {
        'title': 'Coursera',
        'courses':
        [
            {"title": "DeepLearning", "acronym": "DL", "weeks": ["Week-1", "Week-2", "Week-3", "Week-4"], "weeks_info":
                [
                    {"week_title": "Week-1", "videos": ['01_Welcome.mp4', "02_What is a neural network.mp4",
                                                        "03_Supervised Learning with Neural Networks.mp4"]},
                    {"week_title": "Week-2", "videos": ['01_Binary_Classification.mp4', '02_Logistic_Regression.mp4']},
                    {"week_title": "Week-3", "videos": ['Grad Descent']},
                    {"week_title": "Week-4", "videos": ['Results']},
                ]
             },

            {"title": "Cryptography", "acronym": "Crypto", "weeks": ["Week-1", "Week-2", "Week-3"], "weeks_info":
                [
                    {"week_title": "Week-1", "videos": ['Introduction', "Why cryptography"]},
                    {"week_title": "Week-2", "videos": ['DES']},
                    {"week_title": "Week-3", "videos": ['AES']},
                ]
             }

        ]
    },
    {
        'title': 'Stepik',
        'courses':
        [
            {"title": "Web: Flask", "acronym": "Flask", "weeks": ["Week-1", "Week-2"], "weeks_info":
                [
                    {"week_title": "Week-1", "videos": ['Introduction', "Flask vs Django", "Hello World"]},
                    {"week_title": "Week-2", "videos": ['app routes']},
                ]
             },

            {"title": "JavaScript for beginners", "acronym": "JS", "weeks": ["Week-1", "Week-2", "Week-3"], "weeks_info":
                [
                    {"week_title": "Week-1", "videos": ['Introduction', "Basics"]},
                    {"week_title": "Week-2", "videos": ['Some cases']},
                    {"week_title": "Week-3", "videos": ['Angular', 'React', 'Vue.js']},
                ]
             }

        ]
    }
]


# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


@app.route('/', methods=['GET'])
def get_moocs():
    moocs_titles = []
    for i in range(len(MOOCs)):
        moocs_titles.append(MOOCs[i]['title'])
    response_object = {'status': 'success', 'moocs': moocs_titles}
    return jsonify(response_object)


@app.route('/<mooc>', methods=['GET'])
def get_courses(mooc):
    for i in range(len(MOOCs)):
        if MOOCs[i]['title'] == mooc:
            courses_needed = [x for x in MOOCs[i]['courses']]
            response_object = {'status': 'success', 'courses': courses_needed}
            return jsonify(response_object)
    abort(404)


@app.route('/<mooc>/<course>', methods=['GET'])
def get_materials(mooc, course):
    for i in range(len(MOOCs)):
        if MOOCs[i]['title'] == mooc:
            found_courses = MOOCs[i]['courses']
            for j in range(len(found_courses)):
                if found_courses[j]['acronym'] == course:
                    response_object = {'status': 'success', 'courseMaterial': found_courses[j]}
                    return jsonify(response_object)
    abort(404)


@app.route('/<mooc>/<course>/<week_number>', methods=['GET'])
def get_week_materials(mooc, course, week_number):
    return str(mooc) + "   " + str(course) + "   week:" + str(week_number)


if __name__ == '__main__':
    app.run()