# 🖥️ Process Monitor with Calendar Integration

A Python-based system process monitor that tracks application usage and automatically logs the data to Google Calendar, helping you understand your computer usage patterns and manage your time more effectively.

<div align="center">

![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)
![SQLite](https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white)
![Google Calendar](https://img.shields.io/badge/Google_Calendar-4285F4?style=for-the-badge&logo=google-calendar&logoColor=white)

</div>

## 📚 Table of Contents
- [Features](#features)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Technical Details](#technical-details)
- [Contributing](#contributing)

## ✨ Features

- **Real-time Process Monitoring**: Tracks active applications and windows in real-time
- **Time Tracking**: Records application start and end times accurately
- **Google Calendar Integration**: Automatically logs application usage to your Google Calendar
- **SQLite Database**: Maintains local storage of process data
- **Efficient Updates**: Updates calendar entries only when applications are closed
- **Lightweight**: Minimal system resource usage

## 🗂️ Project Structure

```
process-monitor/
├── calendar/
│   ├── mainnn.py         # Main process monitoring script
│   ├── pi.py            # Process information handling
│   ├── prog.py          # Program core logic
│   └── updateTable.py   # Database update operations
├── list.txt             # Configuration file for tracked applications
├── mydb.sqlite          # SQLite database for storing process data
└── test.py             # Testing module
```

## 🚀 Installation

1. Clone the repository
```bash
git clone https://github.com/Sethuram2003/EventTracker_googleCalendar.git
cd process-monitor
```

2. Install required dependencies
```bash
pip install psutil
pip install google-auth-oauthlib
pip install google-auth-httplib2
pip install google-api-python-client
```

3. Set up Google Calendar API
- Create a project in Google Cloud Console
- Enable Google Calendar API
- Download credentials.json and place it in the project directory

## ⚙️ Configuration

1. Configure the `list.txt` file with applications you want to track:
```text
chrome.exe
code.exe
discord.exe
# Add more applications as needed
```

2. Set up Google Calendar credentials:
- Run the script first time to authenticate
- Follow the OAuth2 flow to grant calendar access

## 📖 Usage

1. Start the monitor:
```bash
python calendar/mainnn.py
```

2. The system will:
- Monitor specified applications
- Track their usage time
- Update Google Calendar when applications are closed

3. View your calendar to see application usage logs

## 🔧 Technical Details

### Components

- **mainnn.py**
  - Main entry point
  - Handles process monitoring loop
  - Manages calendar integration

- **pi.py**
  - Process information gathering
  - System interaction logic

- **prog.py**
  - Core program logic
  - Event handling
  - Time tracking calculations

- **updateTable.py**
  - Database operations
  - Table updates
  - Data persistence

### Database Schema

```sql
CREATE TABLE IF NOT EXISTS processes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    process_name TEXT,
    start_time DATETIME,
    end_time DATETIME,
    duration INTEGER
);
```

### Calendar Integration

- Uses Google Calendar API v3
- Creates events with:
  - Application name as title
  - Usage duration
  - Start and end timestamps
  - Category color coding

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Commit changes
4. Push to the branch
5. Open a Pull Request

## 📝 Notes

- Ensure Python 3.6+ is installed
- Keep Google Calendar API credentials secure
- Regular database maintenance recommended
- Monitor system resource usage

## ⚠️ Requirements

- Python 3.6+
- SQLite3
- Google Calendar API access
- Internet connection for calendar updates
- Windows OS (for process monitoring)

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

---
<div align="center">

Created with ❤️ by Sethuram

</div>
