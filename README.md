# RapidFire - Real-Time Quiz Application   🔗 [Live Link](http://65.2.190.143:8000/account/host-login/)

Say goodbye to boring, outdated quizzes, and hello to the future of interactive and engaging quizzes with RapidFire

`RapidFire` - `Real-Time` Quiz Application! Our application is perfect for anyone who wants to create and conduct engaging quizzes in `real-time`. 
With our user-friendly platform, you can easily `customize` your quizzes with your own questions. 
The application is highly customizable, making it ideal for use in `schools`, `colleges`, `contests`, and other educational events. 
RapidFire - Real-Time Quiz Application offers real-time updates, making the quiz more interactive and engaging for participants. 

Our state-of-the-art technology ensures real-time updates, so participants can see quiz questions and results as they happen. And with our robust security protocols, you can rest assured that your quizzes are secure and reliable.

Whether you're a teacher, contest organizer, or quiz enthusiast, RapidFire - Real-Time Quiz Application is the perfect tool for conducting fun, engaging, and interactive quizzes. Get started today and revolutionize the way you conduct quizzes!

Get started today and revolutionize the way you conduct quizzes!

## Demo 🎦🎥

https://user-images.githubusercontent.com/52989607/220909411-949604b7-fb7d-49b3-affa-0e844370bdd2.mp4

## Purpose and Goals 🎯

The purpose of the RapidFire - Real-Time Quiz Application is to provide an engaging and interactive platform for creating and conducting multiple-choice quizzes in real-time. 
Our application is designed to be user-friendly, highly customizable, and accessible for everyone. Whether you're a teacher, student, or quiz enthusiast, 
our application makes it easy for you to create and manage quizzes on the fly.

The goals of this project are to:

- Provide a fun, interactive, and engaging platform for creating and conducting multiple-choice quizzes in real-time.
- Offer a user-friendly and highly customizable interface that allows quiz creators to tailor their quizzes to their specific needs.
- Enable real-time updates to make the quiz more exciting and interactive for participants.
- Provide advanced security protocols to ensure a safe and secure environment for conducting quizzes.
- Become the go-to platform for conducting multiple-choice quizzes in real-time, for use in schools, colleges, and contests.

## What we have Developed 🔨⚒️

For students and contestants, we have developed a mobile application using React Native -> [Application Github Link](https://github.com/yogesh2k21/RapidFire-Frontend), a popular cross-platform mobile app development framework. By leveraging React Native, we are able to create a highly responsive and interactive mobile app that works seamlessly on both iOS and Android platforms. React Native also offers a range of customizable features and native-like performance, making it an ideal framework for creating the RapidFire mobile app. With our React Native-based mobile app, participants can easily and conveniently take part in quizzes from their smartphones, making it more accessible and user-friendly.

For quiz hosts or teachers, we have developed a web portal using Django, a popular Python-based web development framework. Our web portal is accessible from any web browser, making it easy to use and accessible from any device. Using the web portal, quiz hosts can easily create and customize quizzes, upload questions, and set up multiple-choice questions. They can also manage the quiz in real-time, including starting and ending the quiz, tracking participants' progress, and viewing quiz results even after Quiz Ends. With our Django-based web portal, quiz hosts can conduct quizzes seamlessly and efficiently, making it an ideal tool for use in schools, colleges, and contests.

## How its Works 🏃‍♂️🏃‍♀️

The host creates a quiz and sends a unique quiz ID to the participants, which they can enter on their phones to connect to the quiz.

The quiz application has two modes: automatic and custom. In the automatic mode, there is no limit to the number of participants and questions are read and thrown from an Excel sheet. The host selects the questions and the questions are sent to the participants' phones in real-time. 

In the custom mode,there is a limit of 5 participants, and the host needs to wait until all 5 participants are connected before sending questions and after everyone connected host has to thrown manually by typing them into the web portal. In both modes, the participants can answer multiple-choice questions in real-time and see their results as the quiz progresses. The application is user-friendly, accessible from any device, and employs the latest security protocols to ensure a secure and reliable experience.

## Screenshots

![Screenshot (317)](https://user-images.githubusercontent.com/52989607/220836694-2cf22e6f-1b53-48bd-94cb-3909fd1dfb9d.png)
<p align="center">
Home Page
</p>

![Screenshot (318)](https://user-images.githubusercontent.com/52989607/220836810-97e61068-0258-4e78-99f5-4b58398a8c34.png)
<p align="center">
Excel Sheet
</p>

![Screenshot (319)](https://user-images.githubusercontent.com/52989607/220836848-3cab7483-deaa-4ea5-949b-340fa7452c0a.png)
<p align="center">
Custom MCQ Quiz
</p>

![Screenshot (320)](https://user-images.githubusercontent.com/52989607/220836867-f8fb874d-1fd3-4bd5-8560-e152a229cc7d.png)
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

## Authentication with Django Channels and Websockets 🔐

To ensure that only authorized users can access and participate in quizzes, we implemented token authentication using Django Channels and Websockets. This allows us to verify the identity of participants before they can join a quiz.
Using token authentication in Django Channels is a common approach for securing WebSocket connections. It's good practice to authenticate WebSocket connections in order to restrict access to certain functionality to authenticated users only.

When a user logs in or registers, a token is generated for that user. This token is then stored in the browser's localStorage, and is used to authenticate the user when they connect to a quiz using the mobile app or web portal.

`ws://localhost:8000/?token=fkdsahjkfshiadjkfhoasdfk"`

The link we provided appears to be a WebSocket URL for a local development server running on port 8000 with a token query parameter. This type of URL is typically used to establish a WebSocket connection between a client (such as a browser) and a server that supports WebSocket communication.

With token authentication in place, we can ensure that only authorized users can access and participate in quizzes, and that quiz results are recorded accurately and securely.

To provide secure authentication for our host portal, we've implemented a dual-layer approach. Users can log in using traditional session-based authentication for the regular site. However, for WebSocket connections used for real-time functionality, we utilize Django Token authentication to ensure end-to-end encryption and secure communication.

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

To set up and install our containerized RapidFire backend using Docker, follow these steps:

- Clone the GitHub repository to your local machine
- Navigate to the project directory
- Run the following command to build the Docker containers: `docker-compose build`
- Start the containers using the following command: `docker-compose up`
- Open a web browser and navigate to `http://localhost:8000` to access the e-commerce platform.

Note: The entire application has been containerized using Docker, ensuring that the application is portable and can be easily deployed on any system with Docker installed. If you make any changes to the code, you may need to rebuild the containers and restart the application. You can do this by running the `docker-compose down` command followed by `docker-compose up`.

## Hosting & Deployment ☁️

This RapidFire platform's backend has been hosted on Amazon EC2 as part of my journey to learn about AWS and containerized using Docker.
By using Docker, the application has been packaged into a container that can be easily moved between development, testing, and production environments.
AWS provides a wide range of cloud computing services, and hosting this application on EC2 has been a great opportunity to dive deeper into the platform. 
By hosting on EC2, I was able to gain hands-on experience with cloud computing and improve my skills in this area.

## END

Thank you for taking the time to review this RapidFire platform project. Your feedback and support are greatly appreciated. If you have any questions or comments, please feel free to reach out.

