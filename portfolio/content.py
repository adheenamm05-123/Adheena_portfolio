"""Portfolio content for Adheena M M. The dashboard database is seeded from these defaults."""

PROFILE = {'name': 'Adheena M M',
 'location': 'Kerala, India',
 'email': '',
 'github': '',
 'linkedin': '',
 'instagram': '',
 'whatsapp': '',
 'resume': '',
 'tagline': 'Turning raw data into meaningful decisions.',
 'roles': ['Data Analyst', 'Machine Learning Enthusiast', 'Python Developer', 'AI Application Builder'],
 'intro': 'Data Analyst and Machine Learning enthusiast building AI-powered applications — from RAG chatbots '
          'to predictive models — with Python, SQL, and Power BI.',
 'about_heading': 'Turning data into insight.\nBuilding AI-powered solutions.',
 'skills_heading': 'Tools & technologies',
 'projects_heading': 'Featured projects',
 'journey_heading': 'Education & learning journey',
 'services_heading': 'Certifications & education',
 'contact_heading': "Let's build something with data.",
 'contact_intro': 'Open to Data Analyst, ML Engineer, and AI-related opportunities.',
 'explore_label': 'Explore my work',
 'connect_label': "Let's connect",
 'contact_button': 'Send message'}

ABOUT = ["I'm a Computer Science graduate passionate about Data Analytics, Machine Learning, and Artificial "
 'Intelligence. I enjoy solving real-world problems using data-driven solutions and continuously improving '
 'my technical skills through practical projects.',
 'My expertise spans Python, SQL, Power BI, Machine Learning, Data Visualization, and Streamlit application '
 "development. I'm interested in opportunities where I can contribute, learn, and grow as a Data Analyst or "
 'AI Engineer.']

STATS = [{'label': 'Featured ML / AI projects', 'value': 5},
 {'label': 'Certifications completed', 'value': 4},
 {'label': 'Core focus areas', 'value': 3}]

SKILLS = [{'cat': 'Programming', 'icon': 'code-2', 'items': [('Python', 80), ('SQL', 75)]},
 {'cat': 'Data Analysis',
  'icon': 'chart-no-axes-combined',
  'items': [('Pandas', 75),
            ('NumPy', 70),
            ('Excel', 70),
            ('Power BI', 75),
            ('Data Cleaning', 80),
            ('Data Visualization', 75)]},
 {'cat': 'Machine Learning',
  'icon': 'brain-circuit',
  'items': [('Scikit-learn', 75), ('Classification', 70), ('Regression', 70), ('Model Evaluation', 70)]},
 {'cat': 'AI & NLP',
  'icon': 'bot',
  'items': [('NLP', 65), ('TF-IDF', 70), ('RAG Basics', 60), ('Gemini API', 60)]},
 {'cat': 'Tools & Platforms',
  'icon': 'wrench',
  'items': [('Git', 65),
            ('GitHub', 65),
            ('Streamlit', 75),
            ('VS Code', 80),
            ('Jupyter Notebook', 80),
            ('MySQL', 70),
            ('Tableau', 60)]}]

PROJECTS = [{'id': 'ai-document-search',
  'title': 'AI Document Search (RAG Chatbot)',
  'short': 'An intelligent document search app using Retrieval-Augmented Generation. Users upload PDFs and '
           'ask natural-language questions to get context-aware answers.',
  'tags': ['Python', 'LangChain', 'FAISS', 'Gemini', 'Streamlit'],
  'live': '',
  'github': '',
  'screenshots': [],
  'features': ['PDF upload and text extraction',
               'Document chunking and embeddings',
               'Semantic retrieval for question answering',
               'Conversational responses grounded in uploaded documents'],
  'challenges': ['Building a reliable document ingestion and chunking workflow',
                 'Connecting retrieval results to generated answers'],
  'explanation': 'A RAG workflow that extracts text from uploaded PDFs, splits it into chunks, creates '
                 'vector embeddings, retrieves relevant context and generates answers.'},
 {'id': 'student-placement',
  'title': 'Student Placement Prediction',
  'short': 'ML model predicting student placements from academic performance and skill-related features, '
           'benchmarked across multiple algorithms.',
  'tags': ['Python', 'KNN', 'Decision Tree', 'Naive Bayes', 'SVM', 'SMOTE'],
  'live': '',
  'github': '',
  'screenshots': [],
  'features': ['Data cleaning and preprocessing',
               'Feature engineering',
               'Comparison of multiple classification algorithms',
               'Class-imbalance handling with SMOTE'],
  'challenges': ['Comparing models fairly', 'Handling imbalanced target classes'],
  'explanation': 'A supervised machine-learning classification project using KNN, Decision Tree, Naive Bayes '
                 'and SVM, with model evaluation.'},
 {'id': 'hospital-er-dashboard',
  'title': 'Hospital Emergency Room Dashboard',
  'short': 'Interactive Power BI dashboard analyzing emergency room operations — patient flow, wait times, '
           'and department performance.',
  'tags': ['Power BI', 'DAX', 'Data Modeling'],
  'live': '',
  'github': '',
  'screenshots': [],
  'features': ['Patient-flow analysis',
               'Waiting-time analysis',
               'Department performance analysis',
               'KPI dashboard'],
  'challenges': ['Organizing operational data into useful metrics', 'Designing an interactive dashboard'],
  'explanation': 'A Power BI dashboard using data modeling and DAX to explore emergency-room operations.'},
 {'id': 'jobfit-ai',
  'title': 'Resume Matcher (JobFit AI)',
  'short': 'AI-powered app that compares resumes against job descriptions, scoring fit and surfacing missing '
           'skills.',
  'tags': ['Python', 'Gemini API', 'Streamlit'],
  'live': '',
  'github': '',
  'screenshots': [],
  'features': ['Resume text extraction',
               'Skill extraction',
               'Job-description analysis',
               'ATS-style matching score and missing-skill insights'],
  'challenges': ['Extracting useful skills from resume text',
                 'Comparing resume skills with job requirements'],
  'explanation': 'A Streamlit application that parses resume content, extracts skills, compares them with '
                 'job requirements and provides matching feedback.'},
 {'id': 'sentiment-analysis',
  'title': 'Sentiment Analysis',
  'short': 'NLP pipeline classifying customer reviews by sentiment to surface product feedback trends.',
  'tags': ['Python', 'TF-IDF', 'Scikit-learn'],
  'live': '',
  'github': '',
  'screenshots': [],
  'features': ['Text preprocessing', 'TF-IDF vectorization', 'Sentiment classification'],
  'challenges': ['Preparing text for machine-learning models', 'Representing text as numerical features'],
  'explanation': 'An NLP classification pipeline that transforms review text using TF-IDF and predicts '
                 'sentiment with Scikit-learn.'}]

JOURNEY = [{'period': 'Education', 'title': 'BSc Computer Science', 'text': 'University of Calicut.'},
 {'period': 'Training',
  'title': 'Data Science Training',
  'text': 'Completed Data Science training at Luminar Technolab, Kochi.'},
 {'period': 'Internship',
  'title': 'Data Science Intern — Luminar Technolab',
  'text': 'Worked on data cleaning, preprocessing, exploratory data analysis, model building and '
          'evaluation.'}]

SERVICES = [['HackerRank — Python (Basic)', 'award', 'Python Basic certification.'],
 ['HackerRank — SQL (Basic)', 'award', 'SQL Basic certification.'],
 ['HackerRank — SQL (Intermediate)', 'award', 'SQL Intermediate certification.'],
 ['Luminar Technolab — Data Science', 'graduation-cap', 'Data Science course certification.']]

CONTEXT = {"p": PROFILE, "about": ABOUT, "stats": STATS, "skills": SKILLS, "projects": PROJECTS, "journey": JOURNEY, "services": SERVICES}
