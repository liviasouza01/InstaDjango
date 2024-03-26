Insta clone
=============

This is a project proposed by Loomi to check Django backend knowledge

Installation
------------

1. Clone the repository: `git clone https://github.com/liviasouza01/InstaDjango.git`
2. Navigate to the project directory
3. Activate virtual environment: `source venv/bin/activate`
4. Install dependencies: `pip3 install -r requirements.txt`
5. Migrate the project: `python3 manage.py migrate`

Obs.: insta_clone path has the settings.py

Usage
-----

1. Run the server: `python3 manage.py runserver`
2. Open your browser and navigate to `http://localhost:8000`
3. Try http://localhost:8000/admin (user: livia ; password: livia)

Make adjustments if you're using Windows.

Features
--------

- **User Authentication**: Users can securely authenticate into the system using their credentials.
  
- **Data Management**: The system provides robust data management capabilities, allowing users to create, read, update, and delete various types of data.
  
- **POSSIBLE Integration with External Services**: Integration with popular social media platforms, such as Facebook and Twitter, enables users to share content seamlessly.
  
- **Real-time Messaging**: Users can engage in real-time messaging with other users within the system, facilitating instant communication.
  
- **Customization Options**: The system offers customization options, allowing users to personalize their profiles, settings, and preferences.
  
- **Enhanced Security Measures**: Implementations of encryption, authentication protocols, and access controls ensure the security and integrity of user data.
  
- **Scalability and Performance**: The system is designed to handle large volumes of data and user interactions while maintaining optimal performance.


Contributing
------------

1. Fork the repository
2. Create a new branch: `git checkout -b feature-branch`
3. Make changes and commit them: `git commit -am 'Add new feature'`
4. Push to the branch: `git push origin feature-branch`
5. Submit a pull request

License
-------

This project is licensed under the MIT License. See the LICENSE file for details.
