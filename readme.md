# Price Comparator

A **simple web interface** to help you find the **cheapest product** across:

- **Amazon**
- **Flipkart**
- **Zepto**
- **Blinkit**

---

## 🔍 What It Does

- Uses **Google's Gemini LLM** to decide whether a product is likely available on each platform  
- Then **scrapes** the relevant websites for results  
- Ranks all products based on their **Price-to-Rating ratio**  
- Presents the best value options in a clean interface

---

## How to Run

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Start the Flask server:
   ```bash
   python app.py
   ```

3. Open your browser and go to:
   ```
   http://localhost:5000
   ```

---

## Tech Stack

- **Flask** – backend framework  
- **Selenium / Requests + BeautifulSoup** – for web scraping  
- **Google Gemini API** – to intelligently select sources  
- **HTML/CSS/JS** – for the frontend UI

---

## Notes

- The scraper may break if site structures change (especially Amazon/Flipkart)  
- Use responsibly. Some sites have scraping protections and TOS against it  

