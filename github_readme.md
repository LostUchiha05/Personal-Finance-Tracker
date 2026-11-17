# 💰 Personal Finance Tracker CLI

A lightweight, command-line interface (CLI) application built with Python to track daily income and expenses. All transactions are automatically timestamped with the current date and stored locally in a structured JSON file.

---

## ✨ Features

* **Log Income & Expenses:** Quickly record financial transactions with an amount and a custom description.
* **Automatic Date Stamping:** Automatically tags every entry with the current day and month (e.g., `"17 Nov"`).
* **Filter & View Records:** View your entire transaction history or filter entries by a specific date.
* **Zero External Dependencies:** Built entirely using Python's standard library (`argparse`, `json`, `os`, `datetime`).
* **Auto-Initializing Storage:** Automatically creates and formats `Data.json` on the first run.

---

## 🛠️ Prerequisites

* **Python 3.6+** installed on your system.

---

## 🚀 Installation & Setup

1. **Clone the repository** (or download the source files into a single folder):
   ```bash
   git clone https://github.com/yourusername/finance-tracker-cli.git
   cd finance-tracker-cli
   ```

2. **Ensure the module import matches your filenames:**
   > **Note:** If your files are named `financeCLI_2.py` and `financeTracker_2.py`, ensure the import statement at the top of your CLI file matches your tracker filename (`from financeTracker_2 import ...`).

---

## 💻 Usage

Run the application from your terminal using `python financeCLI.py` (or `financeCLI_2.py`) followed by a command and its arguments.

### 1. Add Income
Record a new income entry using the `income` command along with `-a` (amount) and `-d` (description):
```bash
python financeCLI.py income -a 5000 -d "Monthly Salary"
```

### 2. Add Expense
Record a new expense entry using the `expense` command:
```bash
python financeCLI.py expense -a 250 -d "Groceries and Snacks"
```

### 3. View All Transactions
Run the `filter` command without any date flags to display all stored records:
```bash
python financeCLI.py filter
```

### 4. Filter Transactions by Date
Pass the `--Date` flag formatted as `"DD Mon"` (e.g., `"17 Nov"`) to view transactions from a specific day:
```bash
python financeCLI.py filter --Date "17 Nov"
```

---

## 📋 Command Reference

| Argument / Flag | Shorthand | Description | Required For |
| :--- | :--- | :--- | :--- |
| `commands` | *(positional)* | Mode of operation: `income`, `expense`, or `filter` | All commands |
| `--amount` | `-a` | Integer value representing the transaction amount | `income`, `expense` |
| `--Description` | `-d` | Text description explaining the nature of the transaction | `income`, `expense` |
| `--Date` | — | Date string (`"DD Mon"`) used to filter records | `filter` *(Optional)* |

---

## 📂 Data Structure (`Data.json`)

Transactions are stored as an array of JSON objects in `Data.json`:

```json
[
    {
        "id": "17 Nov",
        "amount": 5000,
        "Type": "Income",
        "Description": "Monthly Salary"
    },
    {
        "id": "17 Nov",
        "amount": 250,
        "Type": "Expense",
        "Description": "Groceries and Snacks"
    }
]
```

---

## 🔮 Future Improvements

* Add a `summary` command to calculate total income, total expenses, and net balance.
* Support floating-point numbers (`float`) for decimal amounts (cents/paise).
* Add a `--delete` or `--edit` flag to manage past entries.