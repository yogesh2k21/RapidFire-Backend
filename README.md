# IQ Tester - Real-Time Quiz Application   🔗 [Live Link](http://65.2.190.143:8000/)

Say goodbye to boring, outdated quizzes, and hello to the future of interactive and engaging quizzes with IQ Tester

`IQ Tester` - `Real-Time` Quiz Application! Our application is perfect for anyone who wants to create and conduct engaging quizzes in `real-time`. 
With our user-friendly platform, you can easily `customize` your quizzes with your own questions. 
The application is highly customizable, making it ideal for use in `schools`, `colleges`, `contests`, and other educational events. 
IQ Tester - Real-Time Quiz Application offers real-time updates, making the quiz more interactive and engaging for participants. 

Our state-of-the-art technology ensures real-time updates, so participants can see quiz questions and results as they happen. And with our robust security protocols, you can rest assured that your quizzes are secure and reliable.

Whether you're a teacher, contest organizer, or quiz enthusiast, IQ Tester - Real-Time Quiz Application is the perfect tool for conducting fun, engaging, and interactive quizzes. Get started today and revolutionize the way you conduct quizzes!

Get started today and revolutionize the way you conduct quizzes!

https://user-images.githubusercontent.com/52989607/177797914-d17ae50e-a83a-491e-8224-e3c74796960f.mp4

## Purpose and Goals 🎯

The purpose of the IQ Tester - Real-Time Quiz Application is to provide an engaging and interactive platform for creating and conducting multiple-choice quizzes in real-time. 
Our application is designed to be user-friendly, highly customizable, and accessible for everyone. Whether you're a teacher, student, or quiz enthusiast, 
our application makes it easy for you to create and manage quizzes on the fly.

The goals of this project are to:

- Provide a fun, interactive, and engaging platform for creating and conducting multiple-choice quizzes in real-time.
- Offer a user-friendly and highly customizable interface that allows quiz creators to tailor their quizzes to their specific needs.
- Enable real-time updates to make the quiz more exciting and interactive for participants.
- Provide advanced security protocols to ensure a safe and secure environment for conducting quizzes.
- Become the go-to platform for conducting multiple-choice quizzes in real-time, for use in schools, colleges, and contests.

## What we have Developed 🔨⚒️

For students and contestants, we have developed a mobile application using React Native -> [Application Github Link](https://github.com/yogesh2k21/IQ-Tester-Frontend), a popular cross-platform mobile app development framework. By leveraging React Native, we are able to create a highly responsive and interactive mobile app that works seamlessly on both iOS and Android platforms. React Native also offers a range of customizable features and native-like performance, making it an ideal framework for creating the IQ Tester mobile app. With our React Native-based mobile app, participants can easily and conveniently take part in quizzes from their smartphones, making it more accessible and user-friendly.

For quiz hosts or teachers, we have developed a web portal using Django, a popular Python-based web development framework. Our web portal is accessible from any web browser, making it easy to use and accessible from any device. Using the web portal, quiz hosts can easily create and customize quizzes, upload questions, and set up multiple-choice questions. They can also manage the quiz in real-time, including starting and ending the quiz, tracking participants' progress, and viewing quiz results even after Quiz Ends. With our Django-based web portal, quiz hosts can conduct quizzes seamlessly and efficiently, making it an ideal tool for use in schools, colleges, and contests.

## How its Works 🏃‍♂️🏃‍♀️

The quiz application has two modes: automatic and custom. In the automatic mode, there is no limit to the number of participants and questions are read and thrown from an Excel sheet. The host selects the questions and the questions are sent to the participants' phones in real-time. 

In the custom mode,there is a limit of 5 participants, and the host needs to wait until all 5 participants are connected before sending questions and after everyone connected host has to thrown manually by typing them into the web portal. In both modes, the participants can answer multiple-choice questions in real-time and see their results as the quiz progresses. The application is user-friendly, accessible from any device, and employs the latest security protocols to ensure a secure and reliable experience.

## Screenshots

![Screenshot (300)](https://user-images.githubusercontent.com/52989607/219969855-818c332b-f8d8-4e25-9402-48df959d3e68.png)
<p align="center">
Home Page
</p>

![Screenshot (295)](https://user-images.githubusercontent.com/52989607/219969879-867860a9-6cf8-4df7-acf0-c49ee42b2fb2.png)
<p align="center">
Excel Sheet
</p>


![Screenshot (296)](https://user-images.githubusercontent.com/52989607/219969888-9d1229f6-ba4d-4b3c-a05e-655151ced622.png)
<p align="center">
Custom MCQ Quiz
</p>


![Screenshot (297)](https://user-images.githubusercontent.com/52989607/219969899-6db8e1a1-3265-4adb-aec3-44ce5ab6b6cb.png)
<p align="center">
Old quizes Details
</p>


## Features 📜

Features of our platform:

For the web portal:

- Create and customize quizzes with your own questions and answers
- Import questions from an Excel sheet
- Set up multiple-choice questions in real-time
- Real-time updates allow participants to see quiz questions and results as they happen
- Manage the quiz in real-time, including starting and ending the quiz, tracking participants' progress, and viewing quiz results
- Secure and reliable with token-based authentication for web socket connection
- Easy-to-use and intuitive, no tech expertise required
- Accessible from any web browser on any device

For the mobile app:

- Participate in quizzes on the go with the mobile app
- Real-time updates allow participants to see quiz questions and results as they happen
- Multiple-choice questions for engaging and interactive quizzes
- Secure and reliable with token-based authentication for web socket connection
- User-friendly and intuitive, no tech expertise required
- Accessible from any device with the mobile app installed

## Tools ⚒️ and Tech Stack 🧑‍💻

Tech Stack used in our platform:

- Django web framework for backend development
- Django Channels for WebSocket implementation
- Django REST Framework for building APIs
- Redis for in-memory data storage and cache
- SQLite for lightweight database management
- ASGI server for web protocol handling
- TailwindCSS for styling and UI design

##  Requirements 🏗️

Requirements to run our e-commerce platform:

- Docker installed on your system
- At least 4 GB of RAM available
- A web browser, such as Google Chrome, Mozilla Firefox, or Microsoft Edge
- A stable internet connection

Note: The application has been tested on Linux and macOS, but it should also run on Windows with Docker installed. The required packages and dependencies are included in the Docker containers, so you do not need to install anything manually on your system.

## Installation & Setup 🏭

To set up and install our containerized IQ Tester backend using Docker, follow these steps:

- Clone the GitHub repository to your local machine
- Navigate to the project directory
- Run the following command to build the Docker containers: `docker-compose build`
- Start the containers using the following command: `docker-compose up`
- Open a web browser and navigate to `http://localhost:8000` to access the e-commerce platform.

Note: The entire application has been containerized using Docker, ensuring that the application is portable and can be easily deployed on any system with Docker installed. If you make any changes to the code, you may need to rebuild the containers and restart the application. You can do this by running the `docker-compose down` command followed by `docker-compose up`.

## Hosting & Deployment ☁️

This IQ Tester platform's backend has been hosted on Amazon EC2 as part of my journey to learn about AWS and containerized using Docker.
By using Docker, the application has been packaged into a container that can be easily moved between development, testing, and production environments.
AWS provides a wide range of cloud computing services, and hosting this application on EC2 has been a great opportunity to dive deeper into the platform. 
By hosting on EC2, I was able to gain hands-on experience with cloud computing and improve my skills in this area.

## END

Thank you for taking the time to review this IQ Tester platform project. Your feedback and support are greatly appreciated. If you have any questions or comments, please feel free to reach out.

