from flask import Flask, render_template, abort, url_for

app = Flask(__name__)

# 项目数据
projects = {
    "autonomous-sorting-robot": {
        "title": "Autonomous Sorting and Transport Robot",
        "overview": "An autonomous mobile robot designed for shape and color-based sorting tasks. Powered by dual STM32 MCUs, it features an integrated camera system, PID tracking, and encoder-based locomotion. This project represents an early application of embodied intelligence, demonstrating effective perception-action coordination in real-world scenarios.",
        "media_folder": "autonomous-sorting-robot",
        "images": [
            "images/1.jpg",
            "images/2.jpg",
            "images/3.png",
            "images/4.png"
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
        "overview": "Built control software on STM32 for a scorpion-inspired sampling robot with LiDAR and motor modules.",
        "media_folder": "bionic-scorpion",
        "images": [
            "images/1.png",
            "images/2.png",
            "images/3.gif",
            "images/4.gif",
            "images/5.gif"
        ],
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
    
    # 根据项目类型选择不同的模板
    template_map = {
        "autonomous-sorting-robot": "autonomous_robot_demo.html",
        "snake-robot": "snake_robot_demo.html",
        "defect-detection": "defect_detection_demo.html",
        "bionic-scorpion": "bionic_scorpion_demo.html"
    }
    
    template = template_map.get(project_key, "project_template.html")
    return render_template(template, project=project, image_urls=image_urls, video_url=video_url)

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