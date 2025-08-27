# buzzline-01-schroder

**Course:** Streaming Data  
**Project by:** Justin Schroder  
**Date:** August 27, 2025  
**GitHub:** [github.com/SchroderJ-pixel](https://github.com/SchroderJ-pixel)

![Python 3.11](https://img.shields.io/badge/Python-3.11-blue?logo=python&logoColor=white)

---

## 📌 Project Overview
This project demonstrates **streaming analytics in Python**.  
It uses generators to emit continuous social media–style comments (my custom theme is Taylor Swift getting engaged),  
and a consumer that watches the log file in real time for alerts, keyword matches, and summaries.

## Task 1. Set Up Your Machine & GitHub

This course requires **Python 3.11**.  
Make sure it’s installed on your system (other versions may not work with the tools we’ll use later, like Kafka).  
If you already have multiple versions of Python, that’s fine — just make sure you can switch between them when needed.  

Also create a **GitHub account** (mine is [github.com/SchroderJ-pixel](https://github.com/SchroderJ-pixel)) if you don’t already have one.  
We’ll use GitHub throughout the course to store and share projects.  

⚠️ Setup is critical — missing or incomplete steps here will block the rest of the project. Double-check before moving on.  

---

## Task 2. Initialize Your Project

1. Copy this template repository into your own GitHub account.  
2. Name your repo: **buzzline-01-schroder** (replace with your own name if you’re not me).  
3. Clone it down to your local machine.  
4. Create and activate a virtual environment in the root of the project.  

   **Windows PowerShell**
   ```shell
   py -3.11 -m venv .venv
   .venv\Scripts\activate

## Task 3. Run the Producer (Terminal 1)

Time to generate streaming data.  
My producer is customized to create **Taylor Swift engagement comments** that get written to the project log file every few seconds.  

Open a terminal in VS Code, activate your `.venv`, and run:

**Windows**
```shell
.venv\Scripts\activate
py -m producers.basic_producer_schroder
```
## Task 4. Run the Consumer (Terminal 2)

Next, we’ll monitor the log file in real time.  
The consumer reads new comments as they are written, raises alerts, and tracks keyword mentions.  

Open a **new terminal** in VS Code, activate your `.venv`, and run:

**Windows**
```shell
.venv\Scripts\activate
py -m consumers.basic_consumer_schroder
```

## Save Space
To save disk space, you can delete the .venv folder when not actively working on this project.
We can always recreate it, activate it, and reinstall the necessary packages later. 
Managing Python virtual environments is a necessary and valuable skill. 
We will get a good amount of practice. 

## License
This project is licensed under the MIT License as an example project. 
You are encouraged to fork, copy, explore, and modify the code as you like. 
See the [LICENSE](LICENSE.txt) file for more.
