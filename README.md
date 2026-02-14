# Gold Price Tracker

## A simple interactive Power BI dashboard showing the prices of Gold and SnP 500 from the year 1968 to 2025.

The data was obtained using Yahoo Finance Python API for all of SnP 500. The Yahoo Finance API was able to provide data from 2000 to 2025.
The data from 1968 to 2000 was obtained from https://sdbullion.com/gold-price (LMBA).
Simple mathematical operations were performed to calculate the High and Low prices of gold which were not available for the years between 1968 and 2000.

Technologies used:
Python, Yahoo Finance API, Power BI, DAX, PostgreSQL



The dashboard shows a line chart plotting prices of Gold and SnP 500 from the year 1968 to 2025.

![Page 1 Base_001](https://github.com/user-attachments/assets/3718383d-7395-43db-aea3-585d38837c7c)




The chart can also be filtered by 5-year intervals.

![Page 1 Year Filtered_001](https://github.com/user-attachments/assets/0487d1f4-3e7e-4be4-b776-da8364a0f585)





Another chart shows the maximum opening and closing price of Gold per year from 1968 to 2025.
It also shows the maximum difference between opening and closing price on a day per year.

![Page 2 Base_001](https://github.com/user-attachments/assets/141b1264-9161-4e21-8e6b-24cb0c9db08b)



The above charts can also be filtered by 5-year intervals as shown below.

![Page 2 Year Filtered_001](https://github.com/user-attachments/assets/958ccfe5-01fd-468a-ba8c-74d197e71891)



The below chart shows a 5 Year seasonal plot for gold prices from the year 1985 to 2025.
It can be observed that there were not any big increases in prices until year 2005 with the highest jump, of more than 2000 USD observed from year 2020 to 2025.

![Page 3 Base_001](https://github.com/user-attachments/assets/3b3bf27b-5a25-4d4f-bb16-218c62ba2e1b)



The last chart shows a 1Y rolling returns plotted for both Gold and SnP 500

![Page 4 Base_001](https://github.com/user-attachments/assets/f95b0894-042e-4c0a-b4ec-e83b5b15cf16)



The above chart can be filtered by 5 year interval groups.

![Page 4 Year Filtered_001](https://github.com/user-attachments/assets/5cf379ba-455b-4b10-a245-ebf054306342)





