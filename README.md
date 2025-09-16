# SecureCheck: A Python-SQL Digital Ledger for Police Post Logs

## 📜 Project Overview
SecureCheck is a centralized system for logging, tracking, and analyzing vehicle traffic stop data. This project uses Python for data processing, MySQL for database management, and Streamlit for creating an interactive web dashboard. The goal is to move from inefficient manual logging to a real-time, data-driven system to enhance security and operational efficiency.

---

## ✨ Features
- **Data Processing**: Cleans and prepares raw traffic stop data using Python's pandas library.
- **SQL Database**: Stores the cleaned data in a MySQL database for efficient querying.
- **Interactive Dashboard**: A web-based dashboard built with Streamlit that allows users to:
  - View key metrics like total stops, total arrests, and arrest rate.
  - Filter data by driver gender, race, and violation type.
  - Visualize insights through interactive charts and graphs.

---

## 💻 Technologies Used
- **Python**: Core language for data processing and web application.
- **Pandas**: For data manipulation and cleaning.
- **SQLAlchemy**: To connect Python with the MySQL database.
- **MySQL**: Relational database for storing traffic stop records.
- **Streamlit**: For building the interactive web dashboard.
- **Plotly**: For creating interactive data visualizations.

---

## 🚀 Getting Started

Follow these instructions to get a copy of the project up and running on your local machine.

### Prerequisites
- Python 3.8+
- MySQL Server installed and running.
- Git (for cloning the repository).

### Installation & Setup

1.  **Clone the Repository**
    ```sh
    git clone [https://github.com/your-username/securecheck.git](https://github.com/your-username/securecheck.git)
    cd securecheck
    ```

2.  **Create a Virtual Environment**
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install Dependencies**
    ```sh
    pip install pandas sqlalchemy pymysql streamlit plotly
    ```

4.  **Set up the MySQL Database**
    - Open your MySQL client (e.g., MySQL Workbench, terminal).
    - Create a new database named `securecheck`.
      ```sql
      CREATE DATABASE securecheck;
      ```
    - **Important**: Update the database credentials (`username` and `password`) in both `traffic_stops_project.ipynb` and `dashboard.py`.

5.  **Run the Jupyter Notebook**
    - Place your `traffic_stops (2).xlsx` data file in the project's root directory.
    - Launch Jupyter Notebook:
      ```sh
      jupyter notebook
      ```
    - Open `traffic_stops_project.ipynb` and run all the cells. This will clean the data and populate your `securecheck` database.

6.  **Launch the Streamlit Dashboard**
    - Open your terminal in the project directory.
    - Run the following command:
      ```sh
      streamlit run dashboard.py
      ```
    - Your web browser will open with the interactive dashboard.
