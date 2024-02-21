<div align="center" >

<a href="https://SwiftChat.pythonanywhere.com/">
<img width=100 src="./static/chat/icon.png">
</a>

# [SwiftChat](https://SwiftChat.pythonanywhere.com/)

[SwiftChat](https://SwiftChat.pythonanywhere.com/) is a web application built with Django that enables users to engage in real-time conversations by entering a chat room through its unique ID. The app leverages AJAX technology to facilitate the seamless exchange of messages, providing an interactive and dynamic user experience.

<img align="center" height="500px" src="https://github.com/AzeemIdrisi/SwiftChat/assets/112647789/3236952b-6a96-48d3-b90d-09cfe6b9fb3a">

<img align="center" height="500px" src="https://github.com/AzeemIdrisi/SwiftChat/assets/112647789/54d9f77f-6a64-4b2d-becf-f1360813be3e">
    
</div>

## Features

- **Real-time Messaging**: Experience instant message updates without the need for page refreshes, thanks to the integration of AJAX.

- **Room-based Communication**: Users can join chat rooms by entering a specific room ID, allowing for organized and private conversations.

- **User-friendly Interface**: The app boasts an intuitive and clean interface, making it easy for users to navigate and participate in conversations.

## Installation

To run the Django Chat App locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/AzeemIdrisi/SwiftChat.git
   ```

2. Navigate to the project directory:
   ```bash
   cd SwiftChat
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Apply migrations:
   ```bash
   python manage.py migrate
   ```

5. Start the development server:
   ```bash
   python manage.py runserver
   ```

6. Visit `http://localhost:8000` in your web browser to access the Django Chat App.

## Usage

1. Access the application through the provided URL.

2. Enter a unique room ID to create or join a chat room.

3. Start sending and receiving messages in real-time.

## Technologies Used

- **Django**: The web framework that forms the backbone of the application.

- **AJAX**: Asynchronous JavaScript and XML technology for real-time message updates.

- **SQLite**: The default database system used for data storage.

<!-- ## Contributing

Contributions are welcome! If you'd like to enhance the Django Chat App or report issues, please follow the guidelines outlined in the [CONTRIBUTING.md](CONTRIBUTING.md) file.

## License

This project is licensed under the [MIT License](LICENSE), granting you the freedom to modify and distribute the application.

## Acknowledgments

Special thanks to the Django community and contributors for their valuable insights and contributions to the project.

Feel free to reach out with any questions or feedback! -->
