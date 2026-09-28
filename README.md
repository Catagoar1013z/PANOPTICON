\# PANOPTICON



\## AI-Assisted Cybersecurity Monitoring System



\*\*Independent Technical Project · 2026\*\*



Panopticon is an independent cybersecurity prototype developed to explore how artificial intelligence and machine learning can support the detection and analysis of potentially suspicious activity.



The project combines \*\*rule-based security analysis\*\* with \*\*unsupervised machine-learning anomaly detection\*\* to evaluate activity, assess potential risk, and generate practical security recommendations.



The name \*Panopticon\* was inspired by the concept of continuous observation and awareness, reflecting the project's objective of monitoring activity and identifying unusual patterns.



\---



\## Project Objective



Panopticon was developed as a practical exploration of the intersection between \*\*Computer Science, Artificial Intelligence, and Cybersecurity\*\*.



The current prototype aims to:



\* Identify potentially suspicious activity through predefined security rules.

\* Detect unusual activity patterns using machine-learning techniques.

\* Combine rule-based and machine-learning results into a risk assessment.

\* Generate explanations and security recommendations based on the analysis.

\* Provide a practical environment for experimenting with cybersecurity concepts and Python-based systems.



\---



\## System Architecture



The current analysis pipeline follows this structure:



```text

Activity Data

&#x20;    │

&#x20;    ├───────────────┐

&#x20;    ▼               ▼

Rule-Based       Machine Learning

Detection        Anomaly Detection

&#x20;    │               │

&#x20;    └───────┬───────┘

&#x20;            ▼

&#x20;       Risk Engine

&#x20;            │

&#x20;            ▼

&#x20;     Risk Assessment

&#x20;            │

&#x20;            ▼

&#x20;    Security Advisor

&#x20;            │

&#x20;            ▼

&#x20;Explanation \& Recommendations

```



The system is exposed through a \*\*FastAPI\*\* backend. The `/analyze` endpoint receives activity information including request count, failed login attempts, and duration, then processes the data through the detection and assessment pipeline.



\---



\## Core Components



\### Rule-Based Detection



The rule-based detector evaluates predefined security conditions.



For example, repeated failed login attempts or an unusually high number of requests can be classified as potentially suspicious.



The detector returns:



\* Suspicious activity status

\* Risk level

\* Reason for the classification



\### Machine-Learning Anomaly Detection



Panopticon uses \*\*Isolation Forest\*\*, an unsupervised machine-learning algorithm implemented through scikit-learn.



The model is trained on activity data and evaluates new observations to determine whether they differ from the patterns observed during training.



\### Risk Engine



The risk engine combines the results from the rule-based detector and the machine-learning model.



It produces:



\* Risk level

\* Logical confidence level

\* Explanation of the combined assessment



\### Security Advisor



The advisor converts the analysis into practical security guidance.



Depending on the detected situation, recommendations may include reviewing authentication logs, monitoring unusual activity, or checking for unauthorized access.



\---



\## Technologies



\* \*\*Python\*\*

\* \*\*FastAPI\*\*

\* \*\*NumPy\*\*

\* \*\*scikit-learn\*\*

\* \*\*pytest\*\*

\* \*\*HTML\*\*

\* \*\*Git / GitHub\*\*



\---



\## Testing



The project includes an automated test suite covering the main detection, machine-learning, risk-assessment, advisor, and data-generation components.



Current test result:



\*\*10 tests passed\*\*



```text

============================================================

10 passed in 1.89s

============================================================

```



The tests are intended to verify that the main components behave as expected as the project continues to evolve.



\---



\## Project Structure



```text

PANOPTICON/

│

├── advisor/

│   └── advisor.py

│

├── ai/

│   ├── anomaly\_model.py

│   └── \_\_init\_\_.py

│

├── backend/

│   └── main.py

│

├── data/

│   ├── dataset.py

│   └── generator.py

│

├── detection/

│   ├── detector.py

│   ├── risk\_engine.py

│   └── \_\_init\_\_.py

│

├── tests/

│   ├── test\_advisor.py

│   ├── test\_anomaly\_model.py

│   ├── test\_detector.py

│   ├── test\_generator.py

│   └── test\_risk\_engine.py

│

├── index.html

├── .gitignore

└── README.md

```



\---



\## Current Scope



Panopticon is currently an \*\*independent prototype and learning project\*\*, rather than a production cybersecurity system.



Its current purpose is to provide a practical environment for experimenting with:



\* Security monitoring concepts

\* Rule-based detection

\* Machine-learning anomaly detection

\* Risk assessment

\* Explainable security recommendations

\* Python and API development



The project is still under development, and its current results should be understood within the scope of the prototype and its limited training data.



\---



\## Future Development



Future development may include expanding the available datasets, introducing additional security scenarios, improving anomaly-detection methods, strengthening the evaluation methodology, and testing the system with more realistic cybersecurity data.



The project may also evolve toward a more comprehensive monitoring interface and additional security-analysis capabilities.



\---



\## Author



\*\*Catalina Gomez Arias\*\*



Independent Computer Science Project

2026



