# Portfolio Mockup with Email Form Integration

This project is a portfolio website mockup featuring a secure email form that allows users to submit their email addresses. The form is powered by Python's `smtplib` library, and sensitive information, such as the email password, is securely handled using environment variables.

## Features
- Email form with basic validation for user input.
- Sends email using Python's `smtplib` over SSL.
- Environment variables (`.env` file) are used for securely managing sensitive information.
  
## Technologies Used
- Python
- `smtplib` for email functionality
- `ssl` for secure communication
- Environment variables for security (`os` module)
- HTML/CSS for the front-end form

## Setup Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/portfolio-mockup.git
   cd portfolio-mockup
