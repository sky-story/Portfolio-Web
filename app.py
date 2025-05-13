from flask import Flask, render_template, abort, url_for

app = Flask(__name__)

# 项目数据
projects = {
    "autonomous-sorting-robot": {
        "title": "Autonomous Sorting and Transport Robot",
        "overview": "A mobile robot for shape-color based sorting using dual STM32 MCUs, integrating camera, PID tracking, and encoder-based locomotion. Early application of embodied intelligence for perception-action coordination. 2nd Prize (Top 5%) at China National Mechanical Engineering Innovation Competition (Logistics Track).",
        "media_folder": "autonomous-sorting-robot",
        "images": [
            "images/1.jpg",
            "images/2.jpg"
        ],
        "video": "videos/demo.mp4",
        "github_url": "https://github.com/sky-story/Autonomous-Sorting-and-Transport-Robot"
    },
    "snake-robot": {
        "title": "Path and Gait Planning for Multi-Locomotion Snake Robot",
        "overview": "Developed a modular snake-like robot with multiple gaits (serpentine, rolling, undulation) for environment-adaptive motion planning. Implemented SLAM-based localization and 2D occupancy grid mapping using ROS, Gmapping, and LiDAR for real-time navigation. National Student Research Training Program (SRTP) project.",
        "media_folder": "snake-robot",
        "images": [
            "images/1.jpg"
        ],
        "video": "videos/demo.mp4",
        "github_url": ""
    },
    "defect-detection": {
        "title": "Vision-Based Surface Defect Detection with Edge Deployment",
        "overview": "Developed a real-time defect detection system for aluminum parts, integrating image acquisition, live inference, and display modules. Fine-tuned YOLOv5 model, deployed to edge devices using TensorRT, achieving 2× speedup in inference.",
        "media_folder": "defect-detection",
        "images": [
            "images/1.jpg"
        ],
        "video": "videos/demo.mp4",
        "github_url": "https://github.com/sky-story/Vision-Based-Surface-Defect-Detection-with-Edge-Deployment"
    },
    "bionic-scorpion": {
        "title": "Bionic Scorpion Sampling Robot",
        "overview": "Built control software on STM32 for a scorpion-inspired sampling robot with LiDAR and motor modules. 2nd Prize (Top 10%) in Sichuan Province at China's Mechanical Innovation Design Competition.",
        "media_folder": "bionic-scorpion",
        "images": [
            "images/1.jpg"
        ],
        "video": "videos/demo.mp4",
        "github_url": "https://github.com/sky-story/Bionic-Scorpion-Sampling-Robot"
    }
}

@app.route('/project/<project_key>')
def project_demo(project_key):
    project = projects.get(project_key)
    if not project:
        abort(404)
    image_urls = [url_for('static', filename=f'projects/{project["media_folder"]}/{img}') for img in project["images"]]
    video_url = url_for('static', filename=f'projects/{project["media_folder"]}/{project["video"]}') if project.get("video") else None
    return render_template('project_demo.html', project=project, image_urls=image_urls, video_url=video_url)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/projects')
def projects_page():
    return render_template('projects.html', projects=projects)

@app.route('/skills')
def skills():
    return render_template('skills.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001) 