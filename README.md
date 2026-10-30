# ☁️ Serverless Web Application on AWS

A fully functional serverless web application built using AWS services. The application provides a web-based greeting experience with a serverless backend, allowing users to interact with the application without managing traditional servers.

## 🚀 Project Overview

This project demonstrates how to build and deploy a scalable, highly available, and cost-efficient web application using AWS serverless technologies.

The frontend is hosted on Amazon S3 and delivered through Amazon CloudFront, while the backend is powered by AWS Lambda and Amazon API Gateway.

## 🏗️ Architecture

**AWS Architecture Components:**

1. **Amazon S3** – Hosts the static frontend files (HTML, CSS, JavaScript).
2. **Amazon CloudFront** – Distributes frontend content globally through a CDN.
3. **Amazon API Gateway** – Exposes REST API endpoints to handle frontend requests.
4. **AWS Lambda** – Executes backend business logic without managing servers.
5. **Amazon DynamoDB** – Stores application data and visitor information.
6. **Amazon Route 53 (Optional)** – Can be used for custom domain and DNS management.

### Architecture Diagram

```text
              Users
                |
                v
          CloudFront
                |
                v
          Amazon S3
         (Frontend)
                |
                | API Request
                v
         API Gateway
           (REST API)
                |
                v
          AWS Lambda
      (GreetingVisitorFunction)
                |
                v
           DynamoDB
        (Data Storage)
```

## ✨ Features

- Serverless web application architecture.
- Static website hosting using Amazon S3.
- Global content delivery using CloudFront.
- REST API integration using Amazon API Gateway.
- Backend processing using AWS Lambda.
- Database integration with Amazon DynamoDB.
- Scalable and cost-efficient infrastructure.
- No EC2 instance or traditional server management required.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| HTML, CSS, JavaScript | Frontend development |
| Amazon S3 | Static website hosting |
| Amazon CloudFront | Content delivery |
| Amazon API Gateway | REST API management |
| AWS Lambda | Serverless backend |
| Amazon DynamoDB | NoSQL database |
| Amazon Route 53 | Optional DNS management |

## ⚙️ Application Workflow

1. A user accesses the web application through the CloudFront distribution.
2. CloudFront retrieves the frontend content hosted in Amazon S3.
3. The user interacts with the application.
4. The frontend sends an HTTP POST request to the `/greet` endpoint.
5. API Gateway receives the request and invokes the Lambda function.
6. `GreetingVisitorFunction` processes the request.
7. DynamoDB is used for application data storage.
8. The backend returns a response through API Gateway.
9. The frontend displays the response to the user.

## 🔧 AWS Configuration

### 1. Amazon S3
- Created an S3 bucket for frontend hosting.
- Uploaded website files.
- Configured the bucket for static website hosting.

### 2. Amazon CloudFront
- Created a CloudFront distribution.
- Configured Amazon S3 as the origin.
- Enabled HTTPS content delivery.

### 3. AWS Lambda
- Created the `GreetingVisitorFunction`.
- Implemented the backend application logic.
- Configured the required execution permissions.

### 4. Amazon API Gateway
- Created a REST API.
- Configured the `POST /greet` route.
- Integrated the route with `GreetingVisitorFunction`.
- Deployed the API.

### 5. Amazon DynamoDB
- Configured the database for application data storage.
- Integrated the backend with DynamoDB.

## 📁 Project Structure

```text
serverless-web-application/
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── backend/
│   └── lambda/
│       └── GreetingVisitorFunction/
│
├── screenshots/
│   ├── application.png
│   ├── s3-bucket.png
│   ├── cloudfront.png
│   ├── api-gateway.png
│   └── lambda.png
│
└── README.md
```

*Adjust the folder structure to match the actual repository.*

## 🌐 Deployment

The application is deployed using AWS services:

- Frontend: Amazon S3
- Content Delivery: Amazon CloudFront
- Backend: AWS Lambda
- API: Amazon API Gateway
- Database: Amazon DynamoDB

## 📸 Screenshots

Add screenshots of your completed project here.

### Application Interface
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/e408bcfb-1d52-4faa-8c8e-fb82fce0d7e4" />


### Amazon S3
<img width="953" height="901" alt="Screenshot 2026-10-30 121354" src="https://github.com/user-attachments/assets/eb2bb67b-71be-49d6-babc-82d347e76f02" />


### CloudFront Distribution
<img width="1148" height="716" alt="Screenshot 2026-10-30 123724" src="https://github.com/user-attachments/assets/56e4eba2-6a2a-428e-b234-9b02969cb739" />


### API Gateway
<img width="972" height="907" alt="Screenshot 2026-10-30 145112" src="https://github.com/user-attachments/assets/55c1c69b-f418-4a24-8606-75395a8922e0" />


### AWS Lambda
<img width="1917" height="927" alt="Screenshot 2026-10-30 141138" src="https://github.com/user-attachments/assets/6558113f-89c8-4ca6-8ac4-9a1370f9ebd4" />


## 🎯 Key Learnings

Through this project, I gained practical experience in:

- Building serverless architectures on AWS.
- Hosting static websites using Amazon S3.
- Configuring CloudFront distributions.
- Creating REST APIs using API Gateway.
- Integrating Lambda functions with API Gateway.
- Working with DynamoDB.
- Understanding AWS IAM permissions.
- Deploying and troubleshooting cloud applications.

## 🔮 Future Enhancements

- Configure a custom domain using Route 53.
- Implement CI/CD automation using AWS CodePipeline or GitHub Actions.
- Add monitoring and logging using Amazon CloudWatch.
- Improve application security and access controls.

## 👩‍💻 Author

**Charinika**

Aspiring Cloud & DevOps Engineer

GitHub: [@charinika](https://github.com/charinika)

---

⭐ If you find this project useful, consider giving this repository a star!
