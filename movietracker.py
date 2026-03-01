from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time

# -----------------------------
# Setup Chrome Options
# -----------------------------
chrome_options = Options()

# Uncomment below line for headless mode (optional)
# chrome_options.add_argument("--headless")

chrome_options.add_argument("--start-maximized")

# Setup WebDriver
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=chrome_options
)

# -----------------------------
# Open IMDb Top 250 Page
# -----------------------------
url = "https://www.imdb.com/chart/top/"
driver.get(url)

time.sleep(5)  # Wait for page to load

# -----------------------------
# Scrape Data
# -----------------------------
movies = driver.find_elements(By.XPATH, '//li[contains(@class,"ipc-metadata-list-summary-item")]')

movie_data = []

rank = 1

for movie in movies:
    try:
        title = movie.find_element(By.TAG_NAME, "h3").text
        rating = movie.find_element(By.XPATH, './/span[contains(@class,"ipc-rating-star")]').text
        
        # Extract year from title
        # Example format: "1. The Shawshank Redemption (1994)"
        if "(" in title:
            year = title.split("(")[-1].replace(")", "")
            name = title.split(". ")[1].split(" (")[0]
        else:
            year = "N/A"
            name = title

        movie_data.append([rank, name, year, rating])
        rank += 1

    except:
        continue

# -----------------------------
# Close Browser
# -----------------------------
driver.quit()

# -----------------------------
# Save to CSV
# -----------------------------
df = pd.DataFrame(movie_data, columns=["Rank", "Movie Name", "Year", "IMDb Rating"])

df.to_csv("imdb_top_250_movies.csv", index=False)

print("Data successfully saved to imdb_top_250_movies.csv")