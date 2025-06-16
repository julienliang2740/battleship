# 🛳️ Terminal Battleship

A classic game of **Battleship**, reimagined for the terminal — featuring an **infinitely resizable** and **expandable** board. Whether you want a quick 10x10 match or a sprawling naval war, this version scales to your command. Built for smooth play directly from your terminal, no GUI required.

## 🚀 Features

- 🔄 **Resizable Board** – Play on any size grid, from traditional to massive  
- 🧠 **Simple Logic, Deep Strategy** – Classic Battleship rules that reward good guesses and bluffing  
- 💻 **Terminal-Based** – Lightweight, fast, and distraction-free  

## 🕹️ Usage

```bash
git clone https://github.com/julienliang2740/battleship.git
cd battleship
python main.py

## ⚙️ Customizing the Board Size
To change the board dimensions:

Open the scenario file (currently scenarios/default.json) 
Modify the length and height fields to set your desired board size.

You can also create your own scenario files — just make sure they follow the same format as default.json. Then you can load them into the game manually or modify the code to use them by default.

