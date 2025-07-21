# 🗞️ NewsApp – GUI for Live News Headlines

This is a lightweight Python desktop GUI app that displays **live news headlines** using a public news API, built with `tkinter`. It allows users to:

- View top headlines  
- Search news articles by keyword  
- Read titles, descriptions, and source URLs — directly in the interface

---

## 📌 Features

- 🔥 Get the latest top headlines  
- 🔍 Keyword-based article search  
- 🖥️ Simple GUI using `tkinter`  
- 📃 Clean article formatting: bold titles, readable descriptions, and source links  

---

## 📂 File Structure

```
NewsApp/
├── app.py                    # Main GUI application
├── Functions.py              # API interaction logic
└── 1.md                      # Project documentation (this file)
```

---

## 📊 Tech Stack

- Python 3.x  
- tkinter for the GUI  
- requests or similar (in Functions.py) for API calls  

---

## ⚙️ Setup & Installation

1. Clone the repository:
```
git clone https://github.com/yourusername/NewsApp.git
cd NewsApp
```

2. Install required dependencies:
```
pip install requests
```

3. Configure your `Functions.py` with your News API key. Example:
```python
# Functions.py
import requests

def headlines():
    url = 'https://newsapi.org/v2/top-headlines?country=in&apiKey=YOUR_API_KEY'
    return requests.get(url).json()
```

4. Run the app:
```
python app.py
```

---

## 🧪 How to Use

- 📰 Click **“Get Top Headlines!”** to fetch and display the latest news  
- 🔍 Enter a keyword and click **“Search:”** to find news articles by topic  
- 🧼 The app clears previous results before showing new ones  
- ❗ If no articles are found, it shows a clear "not found" message  

---

## 🧱 Limitations

- Source URLs are displayed as plain text (not clickable)  
- No error handling for network failures or invalid API responses  
- GUI can freeze briefly during API calls (no threading)  
- No filters for country, category, or language  

---

## 🚀 Future Enhancements

- Make URLs clickable using the `webbrowser` module  
- Add dropdowns for country/category/language filtering  
- Implement threading to keep the UI responsive  
- Add scrollbars for long article lists  
- Replace raw `tkinter` widgets with `ttk` for modern UI design  

---

