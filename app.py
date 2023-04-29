from flask import Flask, request, render_template, jsonify, send_file, session
from flask_cors import CORS
from functionality import read_report as read
from functionality import get_one_report_result as process
from functionality import filling_report as create_report

app = Flask(__name__)

CORS(app)  #Cross-Origin Resource Sharing

@app.route('/', methods= ['GET', 'POST'])
def get_message():
#  print("Got request in main function")
 return render_template("index.html")

@app.route('/upload_file', methods=['POST'])
def upload_static_file():
    # print("Got request in static files")
    # print(request.files)
    files = request.files.getlist('files[]')
    report_final =[]
    for f in files:
        f.save(f.filename)
        report_single = process(read(f.filename))
        report_final.append(report_single)
        # print("create file success")
        pass
    file_name = create_report(report_final)
    session["file_name_key"] = file_name
    print(file_name)
    resp = {"success": True, "response": "files saved!"}
    return jsonify(resp), 200

@app.route("/return_formed_file", methods = ["GET"])
def return_formed_file():
    # print("function worked")
    file_name = session.get("file_name_key")
    # print(file_name)
    return send_file(file_name, as_attachment=True)

if __name__ == "__main__":
    app.secret_key = "my_key"
    app.config["session_type"] = "my_session"
    app.run(host='0.0.0.0', debug=True)
