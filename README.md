# Multiplication Table Generator

A simple and interactive web application built using **Streamlit** that generates multiplication tables for any number entered by the user.

## Features

* User-friendly interface
* Generates multiplication table from 1 to 10
* Number input validation
* Supports numbers from 0 to 1000
* Fast and interactive execution using Streamlit

## Technologies Used

* Python
* Streamlit

## Project Structure

```bash
📁 Multiplication-Table-Generator
│── app.py
│── README.md
```

## Installation

1. Clone the repository

```bash
git clone https://github.com/your-username/Multiplication-Table-Generator.git
```

2. Move into the project folder

```bash
cd Multiplication-Table-Generator
```

3. Install required libraries

```bash
pip install streamlit
```

## Run the Application

```bash
streamlit run app.py
```

## Code Example

```python
import streamlit as st

st.title("Welcome to Table World")

n = st.number_input(
    "Enter a number",
    min_value=0,
    max_value=1000
)

if st.button("Submit"):
    for i in range(1, 11):
        st.write(f"{n} * {i} = {n*i}")
```

## How It Works

1. Enter a number in the input field
2. Click the **Submit** button
3. The app displays the multiplication table from 1 to 10

## Future Improvements

* Add custom table range
* Add dark/light mode
* Download table as PDF
* Add colorful UI design
* Support multiple tables at once

## Author

Paresh Prajapati
AI & ML Student | Python Developer
