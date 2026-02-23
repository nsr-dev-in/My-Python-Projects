# 🔗 QuickLink: Streamlit URL Shortener

A sleek, lightweight web application that transforms long, cumbersome URLs into manageable, short links using the TinyURL API.

---

## 📝 Overview

**QuickLink** is a user-friendly tool built with Python and Streamlit. It addresses the common problem of sharing long web addresses by providing a clean interface to generate shortened versions instantly. This project demonstrates the integration of third-party APIs with a modern web frontend, making link sharing more efficient and aesthetically pleasing.

## ✨ Features

* **Instant Shortening:** Converts long URLs to TinyURL links in seconds.
* **Clean Web Interface:** Built with Streamlit for a responsive and intuitive user experience.
* **Validation:** Built-in checks to ensure users provide a URL before processing.
* **One-Click Action:** Simple "Shorten URL" button functionality.
* **Success Alerts:** Clear visual feedback once the short link is generated.

## 🛠 Technologies Used

* **Python:** The core programming language.
* **Streamlit:** For the web application framework and UI.
* **PyShorteners:** A Python libary to interact with various URL shortening APIs.
* **TinyURL API:** The underlying service used to generate short links.

## 📂 Project Structure

```text
QuickLink/
├── app.py              # Main application file
├── requirements.txt    # Project dependencies
├── README.md           # Project documentation
└── .gitignore          # Files to ignore in Git

```

## ⚙️ Installation & Setup

Follow these steps to get the project running on your local machine:

1. **Clone the repository:**
```bash
git clone https://github.com/yourusername/quicklink-url-shortener.git
cd quicklink-url-shortener

```


2. **Create a virtual environment (Optional but recommended):**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

```


3. **Install the required packages:**
```bash
pip install pyshorteners streamlit pyperclip

```



## 🚀 How to Run

Once the dependencies are installed, launch the application using Streamlit:

```bash
streamlit run app.py

```

## 🎮 How to Use

1. Launch the app in your browser (usually at `http://localhost:8501`).
2. Locate the **"Enter the URL"** input box.
3. Paste your long URL (e.g., `https://www.example.com/very/long/path/to/page`).
4. Click the **"Shorten URL"** button.
5. Copy your new short link from the success message!

## 🧠 Concepts Learned

* **API Integration:** Utilizing the `pyshorteners` library to communicate with external web services.
* **State Management:** Handling user inputs and button triggers within a reactive web framework.
* **Error Handling:** Implementing basic validation to manage empty input fields.
* **Web Deployment Basics:** Structuring a Python script to function as a standalone web app.

## 📸 Example Usage

> **Input:** `https://www.google.com/search?q=how+to+build+a+url+shortener+with+python`
> **Output:** `https://tinyurl.com/2p8vx9zk`

## 🚀 Future Improvements

* [ ] **Copy to Clipboard:** Add a button to copy the short link automatically.
* [ ] **History Log:** Keep a session-based list of recently shortened links.
* [ ] **QR Code Generator:** Automatically generate a QR code for the shortened URL.
* [ ] **Custom Aliases:** Allow users to request specific keywords for their links.

## 🤝 Contributing

Contributions make the open-source community an amazing place to learn and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project.
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`).
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`).
4. Push to the Branch (`git push origin feature/AmazingFeature`).
5. Open a Pull Request.

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.

## 👤 Author

**Your Name**

* GitHub: [@yourusername](https://github.com/yourusername)
* LinkedIn: [Your Name](https://linkedin.com/in/yourprofile)

## ⭐ Support

If you found this project helpful, please consider giving it a **Star**! It helps others find the repository and keeps the motivation high.
