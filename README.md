# Crawler

A Python-based automation tool designed to scrape member information from QQ group pages and send automated email notifications to those members.

## Features

- **Member Scraping**: Automatically extracts member details (Nickname, QQ number, Gender, Q-age, Join Date, and Last Activity) from `qun.qq.com`.
- **Data Export**: Saves scraped member information into a `QQ.csv` file.
- **Email Automation**: Integrated SMTP utility to send customized emails to the scraped contacts.
- **Bulk Mailing**: Ability to read email lists from a text file and send mass communications.

## Installation

### Prerequisites

- Python 3.x
- Google Chrome Browser
- [ChromeDriver](https://chromedriver.chromium.org/downloads) (Ensure the version matches your installed Chrome version)

### Dependencies

Install the required Python libraries using pip:

```bash
pip install selenium lxml
```

## Usage

### 1. Scraping QQ Group Members
Run the main crawler to extract data from a specific QQ group:

```bash
python -m com.CrawlerQQ
```
- You will be prompted to enter one or more QQ group numbers (separated by commas).
- The script will launch a Chrome browser, navigate to the member list, scroll to load data, and save the results to `QQ.csv`.
- **Note**: Ensure `chromedriver.exe` is in the project root directory or added to your system PATH.

### 2. Sending Emails from a File
To send emails to a list of addresses stored in a text file:

```bash
python -m com.ReadFileSendMail
```
- Provide the path to your `.txt` file containing one email address per line.

## Configuration

To use the email functionality, you must configure your SMTP settings in `com/SendMailUtil.py`. Update the following variables:

```python
mail_host = "smtp.163.com"  # Your SMTP server
mail_user = "your_email@163.com"
mail_pass = "your_smtp_password"
sender = "your_email@163.com"
```

## Project Structure

- `com/CrawlerQQ.py`: Main logic for browser automation and data parsing.
- `com/SendMailUtil.py`: SMTP utility class for handling email transmission.
- `com/ReadFileSendMail.py`: Utility to send emails to a list extracted from a file.
- `com/Test.py`: Test suite for verifying email functionality.
