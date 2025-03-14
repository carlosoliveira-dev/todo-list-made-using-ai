from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

tasks = []

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify(tasks)

@app.route("/tasks", methods=["POST"])
def add_task():
    data = request.get_json()
    if "task" in data:
        task = {"id": len(tasks) + 1, "task": data["task"]}
        tasks.append(task)
        return jsonify(task), 201
    return jsonify({"error": "Task content is required"}), 400

@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task["id"] != task_id]
    return jsonify({"message": "Task deleted"})

if __name__ == "__main__":
    app.run(debug=True)
