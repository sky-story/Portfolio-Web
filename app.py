from flask import Flask, render_template, abort, url_for, request, session, redirect
from translations import translations
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)  # 添加密钥用于session

# 项目数据
projects_data = {
    "autonomous-sorting-robot": {
        "title": "Autonomous Sorting and Transport Robot",
        "title_zh": "自主分拣运输机器人",
        "overview": "An autonomous mobile robot designed for shape and color-based sorting tasks. Powered by dual STM32 MCUs, it features an integrated camera system, PID tracking, and encoder-based locomotion. This project represents an early application of embodied intelligence, demonstrating effective perception-action coordination in real-world scenarios.",
        "overview_zh": "一个基于形状和颜色的自主移动分拣机器人。采用双STM32微控制器，集成了相机系统、PID跟踪和编码器驱动。该项目展示了早期具身智能的应用，在实际场景中实现了有效的感知-动作协调。",
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
        "title_zh": "多运动模式蛇形机器人路径与步态规划",
        "overview": "Developed a modular snake-like robot with multiple gaits (serpentine, rolling, undulation) for environment-adaptive motion planning. Implemented SLAM-based localization and 2D occupancy grid mapping using ROS, Gmapping, and LiDAR for real-time navigation. National Student Research Training Program (SRTP) project.",
        "overview_zh": "开发了一个具有多种步态（蜿蜒、、侧向蜿蜒、行波、侧向翻滚）的模块化蛇形机器人，用于环境自适应运动规划。使用ROS、Gmapping和激光雷达实现了基于SLAM的定位和二维占用栅格地图构建，用于实时导航。国家级大学生创新创业训练计划项目。",
        "media_folder": "snake-robot",
        "images": [
            "images/1.jpg"
        ],
        "video": "videos/demo.mp4",
        "github_url": ""
    },
    "defect-detection": {
        "title": "Vision-Based Surface Defect Detection with Edge Deployment",
        "title_zh": "基于视觉的表面缺陷检测与边缘部署",
        "overview": "Developed a real-time defect detection system for aluminum parts, integrating image acquisition, live inference, and display modules. Fine-tuned YOLOv5 model, deployed to edge devices using TensorRT, achieving 2× speedup in inference.",
        "overview_zh": "开发了一套铝合金零件表面缺陷实时检测系统，集成了图像采集、实时推理和显示模块。基于YOLOv5模型进行微调，使用TensorRT进行边缘设备部署，实现2倍推理加速。",
        "media_folder": "defect-detection",
        "images": [
            "images/1.jpg"
        ],
        "video": "videos/demo.mp4",
        "github_url": "https://github.com/sky-story/Vision-Based-Surface-Defect-Detection-with-Edge-Deployment"
    },
    "bionic-scorpion": {
        "title": "Bionic Scorpion Sampling Robot",
        "title_zh": "仿生蝎子采样机器人",
        "overview": "Built control software on STM32 for a scorpion-inspired sampling robot with LiDAR and motor modules.",
        "overview_zh": "基于STM32开发了仿生蝎子采样机器人的控制软件，集成了激光雷达和电机模块。",
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

# 翻译数据
translations = {
    'en': {
        # 导航栏
        'nav_home': 'Home',
        'nav_projects': 'Projects',
        'nav_skills': 'Skills',
        'nav_contact': 'Contact',
        
        # 首页
        'welcome_title': 'Welcome to My Portfolio',
        'education_title': "Master's Student in Computer Science & Data Science",
        'research_focus': 'Researching Embodied AI and Object-Goal Navigation',
        'about_me': 'About Me',
        'about_me_content': 'I am a dual-degree Master\'s student pursuing Computer Science at the University of Washington and Data Science at Tsinghua University. My research focuses on Embodied AI, particularly in object-goal navigation and multi-strategy decision-making approaches. I am passionate about developing intelligent systems that can understand and interact with their environment effectively, combining theoretical foundations with practical implementations.',
        'education': 'Education',
        'uw': 'University of Washington',
        'uw_degree': 'Master of Computer Science - Robotics Track',
        'uw_period': 'Sept 2024 - June 2026',
        'tsinghua': 'Tsinghua University',
        'tsinghua_degree': 'Master in Data Science and Information Technology',
        'tsinghua_period': 'Sept 2023 - June 2026',
        'swjtu': 'Southwest Jiaotong University',
        'swjtu_degree': "Bachelor's in Measurement, Control Technology and Instruments",
        'swjtu_period': 'Sept 2019 - June 2023',
        'awards': 'Awards & Recognition',
        'award_1': 'Tsinghua University Comprehensive Excellence Scholarship (First Class) - 2024',
        'award_2': 'Outstanding Graduate of Sichuan Province (Top 1%) - 2023',
        'award_3': 'National Scholarship, Ministry of Education of China - 2022',
        
        # 项目页面
        'projects_title': 'Projects',
        'view_demo': 'View Demo',
        'computer_vision': 'Computer Vision',
        'pid_control': 'PID Control',
        'edge_computing': 'Edge Computing',
        'robotics': 'Robotics',
        
        # 项目标题和描述
        'autonomous_robot_title': 'Autonomous Sorting and Transport Robot',
        'autonomous_robot_desc': 'Built a mobile robot for shape-color based sorting using dual STM32 MCUs, integrating camera, PID tracking, and encoder-based locomotion. Early application of embodied intelligence for perception-action coordination.',
        
        'snake_robot_title': 'Path and Gait Planning for Multi-Locomotion Snake Robot',
        'snake_robot_desc': 'Developed a modular snake-like robot with multiple gaits (serpentine, rolling, undulation) for environment-adaptive motion planning. Implemented SLAM-based localization and 2D occupancy grid mapping using ROS, Gmapping, and LiDAR.',
        
        'defect_detection_title': 'Vision-Based Surface Defect Detection with Edge Deployment',
        'defect_detection_desc': 'Developed a real-time defect detection system for aluminum parts, integrating image acquisition, live inference, and display modules. Fine-tuned YOLOv5 model, deployed to edge devices using TensorRT, achieving 2× speedup in inference.',
        
        'bionic_scorpion_title': 'Bionic Scorpion Sampling Robot',
        'bionic_scorpion_desc': 'Built control software on STM32 for a scorpion-inspired sampling robot with LiDAR and motor modules. 2nd Prize (Top 10%) in Sichuan Province at China\'s Mechanical Innovation Design Competition.',
        
        # 项目相关
        'achievement': 'Achievement',
        'outstanding_project': 'Outstanding Graduation Project',
        'outstanding_project_desc': 'Recognized as an outstanding graduation project at the university level, demonstrating excellence in innovation and technical implementation.',
        'tech_specs': 'Technical Specifications',
        'model_arch': 'Model Architecture',
        'model_arch_desc': 'High-precision defect detection model based on YOLOv5',
        'deployment': 'Deployment',
        'deployment_desc': 'Edge device deployment solution optimized with TensorRT',
        'performance': 'Performance',
        'performance_desc': '2× inference speedup compared to standard deployment',
        'application': 'Application',
        'application_desc': 'Real-time surface defect detection for aluminum parts',
        'system_photo': 'System Photo',
        'system_arch': 'System Architecture',
        'inference_accel_enabled': 'Inference Acceleration Enabled',
        'inference_accel_disabled': 'Inference Acceleration Disabled',
        'detection_result_after': 'Detection Result (After Acceleration)',
        'detection_result_before': 'Detection Result (Before Acceleration)'
    },
    'zh': {
        # 导航栏
        'nav_home': '首页',
        'nav_projects': '项目',
        'nav_skills': '技能',
        'nav_contact': '联系',
        
        # 首页
        'welcome_title': '欢迎来到我的作品集',
        'education_title': '计算机科学&数据科学硕士在读',
        'research_focus': '研究具身智能与目标导航',
        'about_me': '关于我',
        'about_me_content': '我是一名华盛顿大学和清华大学联合培养的双学位硕士。我的研究专注于具身智能，特别是具身导航方向。我热衷于开发能够有效理解和与环境交互的智能系统，注重把理论知识和前沿技术应用到实际中。',
        'education': '教育经历',
        'uw': '华盛顿大学',
        'uw_degree': '计算机科学硕士 - 机器人方向',
        'uw_period': '2024年9月 - 2026年6月',
        'tsinghua': '清华大学',
        'tsinghua_degree': '数据科学与信息技术硕士',
        'tsinghua_period': '2023年9月 - 2026年6月',
        'swjtu': '西南交通大学',
        'swjtu_degree': '测控技术与仪器学士',
        'swjtu_period': '2019年9月 - 2023年6月',
        'awards': '获奖情况',
        'award_1': '清华大学综合优秀奖学金（一等） - 2024',
        'award_2': '四川省优秀毕业生（前1%） - 2023',
        'award_3': '国家奖学金 - 2022',
        
        # 项目页面
        'projects_title': '项目',
        'view_demo': '查看演示',
        'computer_vision': '计算机视觉',
        'pid_control': 'PID控制',
        'edge_computing': '边缘计算',
        'robotics': '机器人技术',
        
        # 项目标题和描述
        'autonomous_robot_title': '自主分拣运输机器人',
        'autonomous_robot_desc': '开发了一个基于形状和颜色的自主移动分拣机器人。采用双STM32微控制器，集成了相机系统、PID跟踪和编码器驱动。该项目展示了早期具身智能的应用，在实际场景中实现了有效的感知-动作协调。',
        
        'snake_robot_title': '多运动模式蛇形机器人路径与步态规划',
        'snake_robot_desc': '开发了一个具有多种步态（蜿蜒、、侧向蜿蜒、行波、侧向翻滚）的模块化蛇形机器人，用于环境自适应运动规划。使用ROS、Gmapping和激光雷达实现了基于SLAM的定位和二维占用栅格地图构建，用于实时导航。',
        
        'defect_detection_title': '基于视觉的表面缺陷检测与边缘部署',
        'defect_detection_desc': '开发了一套铝合金零件表面缺陷实时检测系统，集成了图像采集、实时推理和显示模块。基于YOLOv5模型进行微调，使用TensorRT进行边缘设备部署，实现2倍推理加速。',
        
        'bionic_scorpion_title': '仿生蝎子采样机器人',
        'bionic_scorpion_desc': '基于STM32开发了仿生蝎子采样机器人的控制软件，集成了激光雷达和电机模块。在四川省机械创新设计大赛中获得二等奖（前10%）。',
        
        # 项目相关
        'achievement': '成就',
        'outstanding_project': '校级优秀毕业设计',
        'outstanding_project_desc': '被评为校级优秀毕业设计，展示了在创新和技术实现方面的卓越成就。',
        'tech_specs': '技术规格',
        'model_arch': '模型架构',
        'model_arch_desc': '基于YOLOv5的高精度缺陷检测模型',
        'deployment': '部署方案',
        'deployment_desc': '使用TensorRT优化的边缘设备部署方案',
        'performance': '性能表现',
        'performance_desc': '相比标准部署实现2倍推理加速',
        'application': '应用场景',
        'application_desc': '铝合金零件表面缺陷实时检测',
        'system_photo': '系统实物图',
        'system_arch': '系统架构图',
        'inference_accel_enabled': '启用推理加速',
        'inference_accel_disabled': '未启用推理加速',
        'detection_result_after': '加速后检测结果',
        'detection_result_before': '加速前检测结果'
    }
}

@app.route('/project/<project_key>')
def project_demo(project_key):
    project = projects_data.get(project_key)
    if not project:
        abort(404)
    image_urls = [url_for('static', filename=f'projects/{project["media_folder"]}/{img}') for img in project["images"]]
    video_url = url_for('static', filename=f'projects/{project["media_folder"]}/{project["video"]}') if project.get("video") else None
    
    # 根据项目类型和语言选择不同的模板
    template_map = {
        "autonomous-sorting-robot": {
            "en": "projects/autonomous_robot/demo.html",
            "zh": "projects/autonomous_robot/demo_zh.html"
        },
        "snake-robot": {
            "en": "projects/snake_robot/demo.html",
            "zh": "projects/snake_robot/demo_zh.html"
        },
        "defect-detection": {
            "en": "projects/defect_detection/demo.html",
            "zh": "projects/defect_detection/demo_zh.html"
        },
        "bionic-scorpion": {
            "en": "projects/bionic_scorpion/demo.html",
            "zh": "projects/bionic_scorpion/demo_zh.html"
        }
    }
    
    lang = session.get('lang', 'en')
    template = template_map.get(project_key, {}).get(lang, "project_template.html")
    return render_template(template, project=project, image_urls=image_urls, video_url=video_url, lang=lang, t=translations[lang])

@app.route('/')
def index():
    lang = session.get('lang', 'en')
    return render_template('main/index.html', lang=lang, t=translations[lang])

@app.route('/about')
def about():
    lang = session.get('lang', 'en')
    return render_template('main/about.html', lang=lang, t=translations[lang])

@app.route('/projects')
def projects():
    lang = session.get('lang', 'en')
    return render_template('projects/projects.html', lang=lang, t=translations[lang])

@app.route('/skills')
def skills():
    lang = session.get('lang', 'en')
    template = 'main/skills_zh.html' if lang == 'zh' else 'main/skills.html'
    return render_template(template, lang=lang, t=translations[lang])

@app.route('/contact')
def contact():
    lang = session.get('lang', 'en')
    template = 'main/contact_zh.html' if lang == 'zh' else 'main/contact.html'
    return render_template(template, lang=lang, t=translations[lang])

@app.route('/defect-detection')
def defect_detection():
    lang = session.get('lang', 'en')
    project = projects_data['defect-detection']
    t = translations[lang]
    return render_template('defect_detection_demo.html', project=project, t=t, lang=lang)

@app.route('/defect-detection-zh')
def defect_detection_zh():
    lang = session.get('lang', 'zh')
    project = projects_data['defect-detection']
    t = translations[lang]
    return render_template('defect_detection_demo_zh.html', project=project, t=t, lang=lang)

@app.route('/autonomous-sorting-robot')
def autonomous_robot():
    lang = session.get('lang', 'en')
    project = projects_data['autonomous-sorting-robot']
    t = translations[lang]
    return render_template('autonomous_robot_demo.html', project=project, t=t, lang=lang)

@app.route('/autonomous-sorting-robot-zh')
def autonomous_robot_zh():
    lang = session.get('lang', 'zh')
    project = projects_data['autonomous-sorting-robot']
    t = translations[lang]
    return render_template('autonomous_robot_demo_zh.html', project=project, t=t, lang=lang)

@app.route('/snake-robot')
def snake_robot():
    lang = session.get('lang', 'en')
    project = projects_data['snake-robot']
    t = translations[lang]
    return render_template('snake_robot_demo.html', project=project, t=t, lang=lang)

@app.route('/snake-robot-zh')
def snake_robot_zh():
    lang = session.get('lang', 'zh')
    project = projects_data['snake-robot']
    t = translations[lang]
    return render_template('snake_robot_demo_zh.html', project=project, t=t, lang=lang)

@app.route('/switch_language/<lang>')
def switch_language(lang):
    if lang in ['en', 'zh']:
        session['lang'] = lang
        # 获取当前页面的URL
        current_url = request.referrer or url_for('index')
        
        # 处理项目页面的语言切换
        if '/autonomous-sorting-robot' in current_url:
            if lang == 'zh':
                return redirect(url_for('autonomous_robot_zh'))
            else:
                return redirect(url_for('autonomous_robot'))
        elif '/defect-detection' in current_url:
            if lang == 'zh':
                return redirect(url_for('defect_detection_zh'))
            else:
                return redirect(url_for('defect_detection'))
        elif '/snake-robot' in current_url:
            if lang == 'zh':
                return redirect(url_for('snake_robot_zh'))
            else:
                return redirect(url_for('snake_robot'))
        
    return redirect(request.referrer or url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001) 