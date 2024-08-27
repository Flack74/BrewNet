# ☕ **BrewNet** – *Find Your Perfect Café Spot* 🔌🛜

**BrewNet** is your go-to café discovery platform where you can explore, rate, and share cafés based on coffee quality, Wi-Fi strength, and power socket availability. Whether you're on the hunt for a cozy nook to sip your latte or a workspace with blazing-fast Wi-Fi, **BrewNet** has you covered, complete with emoji-based ratings!

https://brewnet.onrender.com/

## ✨ **Features**

- **Add a Café**: Easily submit your favorite café spots with:
  - **Café Name** 📍
  - **Google Maps Location (URL)** 🌐
  - **Opening & Closing Times** 🕒
  - **Ratings** using fun emojis: Coffee ☕, Wi-Fi 🛜, and Power 🔌
  
- **Browse Cafés**: See a comprehensive list of all added cafés with quick access to their details.

## 🛠️ **Tech Stack**

- **Backend**: Flask, WTForms
- **Frontend**: HTML, CSS, Bootstrap 5
- **Data Storage**: CSV
- **Styling**: Custom CSS for a sleek and responsive design

## 🚀 **Getting Started**

1. **Clone the Repository**:

    ```bash
    git clone https://github.com/your-username/brewnet.git
    cd brewnet
    ```

2. **Create a Virtual Environment and Install Dependencies**:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    pip install -r requirements.txt
    ```

3. **Run the Application**:

    ```bash
    python main.py
    ```

4. **Explore BrewNet**:

    Open your browser and navigate to [http://127.0.0.1:5000](http://127.0.0.1:5000) to explore.

## 💻 **How to Use BrewNet**

1. **Home Page**: Start by exploring the landing page with options to add or browse cafés.
2. **Add a Café**: Share a new café by filling in the form and rating it with emojis. 📝
3. **Browse Cafés**: View all available cafés and access their details, including location links and ratings.

## 📁 **Project Structure**

```plaintext
brewnet/
│
├── static/
│   ├── css/
│   │   └── styles.css          # Custom styling for the project
│   ├── coffee.png              # Coffee-related image used in the project
│   └── coffee2.png             # Another coffee image for visual appeal
│
├── templates/
│   ├── add.html                # Form page for adding new cafés
│   ├── base.html               # Base template for consistent styling
│   ├── cafes.html              # Page displaying all listed cafés
│   └── index.html              # Landing page
│
├── cafe-data.csv               # Data storage for café submissions
├── main.py                     # Main Flask application
├── requirements.txt            # Python dependencies
└── README.md                   # Project documentation (You are here!)
```

## 🌟 **Why BrewNet?**

With BrewNet, you’re not just discovering cafés – you’re building a community of coffee lovers, remote workers, and digital nomads. The simple and playful design, paired with practical functionality, makes it easy to find the ideal café for your needs.

## 🌐 **Contributing**

Contributions are welcome! Feel free to fork the repository, submit pull requests, and suggest new features.
