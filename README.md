# Simple ATM Application with Tkinter

This repository contains a simple ATM (Automated Teller Machine) application implemented in Python using Tkinter for the graphical user interface (GUI).

## Overview

This ATM application allows users to perform various banking operations such as:

- Log in with a 4-digit PIN
- View account balance
- Withdraw cash
- Deposit cash
- Change PIN
- Return card and log out

The application maintains account information in a text file named `account.txt`. Each account entry in the file consists of the PIN, account balance, and account holder's name, separated by commas.

## Features

- Graphical user interface (GUI) built with Tkinter for a user-friendly experience.
- Error handling and validation for PIN entry, withdrawal amount, deposit amount, and PIN change.
- Persistence of account data through file I/O operations.
- Simple and intuitive navigation through the ATM menu options.

## Getting Started

To run the ATM application locally, follow these steps:

1. Clone this repository to your local machine:

```bash
git clone https://github.com/your-username/atm-application.git
