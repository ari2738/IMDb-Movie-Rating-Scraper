🎬 IMDb Movie Rating Scraper

📌 Description

The IMDb Movie Rating Scraper is a Python-based automation tool that extracts movie data from the IMDb Top 250 list using Selenium and Chrome WebDriver. The scraper dynamically loads JavaScript content and collects movie rank, title, release year, and IMDb rating, then exports the data into a structured CSV file for analysis.

This project demonstrates practical web scraping, browser automation, and structured data handling using Python.

🚀 Key Features

✔ Dynamic Web Scraping using Selenium

✔ Extracts Top 250 movie rankings

✔ Collects Movie Name, Year, and IMDb Rating

✔ Handles JavaScript-rendered content

✔ Exports structured data into CSV format

✔ Optional Headless Mode (runs without opening browser)

✔ Easily extendable to scrape cast, genre, etc.

⚙️ Working

The script launches Chrome using Selenium WebDriver.

It opens the IMDb Top 250 movies page.

It waits for the page to fully load dynamic content.

It extracts movie details such as rank, name, year, and rating.

The extracted data is stored in a list.

The list is converted into a Pandas DataFrame.

Finally, the data is exported into a CSV file (imdb_top_250_movies.csv).
