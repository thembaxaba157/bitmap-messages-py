# 🖼️ Bitmap Messages – Python ASCII Art Generator

A Python program that turns text into ASCII art using a bitmap pattern. Inspired by **The Big Book of Small Python Projects**, this app creatively maps user input onto a character-based image.

---

## 🧠 Description

This project takes a **bitmap image made of characters** (like `*`, `.`, or whitespace) and replaces non-space characters with repeating letters from a user-provided message. The result is a customized ASCII art image!

> Spaces remain blank. All other characters (like `*`, `.`) get replaced by letters from your message, creating a dynamic text-based visual.

You can experiment with any bitmap to produce your own art.

---

## 🖼️ Example Output (Snippet)

For the message `hello`, a few lines of the output may look like:

```
 hellohellohellohellohellohellohellohellohellohellohellohellohellohel
   lohellohellohe   h  loh ll  e      lohellohellohellohellohellohel
  llohellohellohellohel oh ll h  l hellohellohellohellohellohello e 
 el      ohellohellohelloh       lohellohellohellohellohellohel     
          hellohellohel          lo  l ohel oh llohellohelloh l     
           ellohello            llohell   llohellohellohel o e      
            llohello           ellohellohellohellohellohel  h       
   l        l ohel ohe         ellohellohelloh llohel  he l
               hell  e         ellohellohelloh   ohe loh  l
                 llohel         llohellohello    oh   oh  l
                 llohello        lohellohelloh    h  lo ell
                   ohellohe         ellohell          o ell hell
                   ohellohel         llohel  h        ohel oh l oh
                   ohellohel         llohel o e           loh l   e
                     ellohe          llohe lo             lohel   e
                     elloh            lohe l            ellohell
                    hello             lohe              ellohello
                    hell              lo                 llohell   l
                    hel                                       l    l
                    he     l                    l
hellohellohellohellohellohellohellohellohellohellohellohellohellohel

```

*(output varies by message and bitmap)*

---

## 📁 Project Structure

```text
bitmap-messages-py/
├── bitmap_mes.py     # Main Python script
├── bitmap.txt        # Bitmap pattern file
└── README.md         # Project documentation
```

---

## ▶️ How to Run

1. Clone the repo:
   ```bash
   git clone https://github.com/thembaxaba157/bitmap-messages-py.git
   cd bitmap-messages-py
   ```

2. Run the script:
   ```bash
   python3 bitmap_mes.py
   ```

3. Enter any message when prompted:
   ```
   Enter the message to display with the bitmap.
   > CODE4LIFE
   ```

4. See the customized ASCII output in the terminal!

---

## ✏️ Customization Tips

- **Change the message**: Try names, quotes, etc.
- **Change the bitmap**: Modify `bitmap.txt` with your own shapes using `*`, `.`, or any non-space character.
- **Try emojis**: Add emojis to your message for fun results (may depend on terminal support).

---

## 📜 License

MIT License — feel free to use, remix, and learn from this.

---

## 👨‍💻 Author

Coded by [@thembaxaba157](https://github.com/thembaxaba157), inspired by Al Sweigart's Python book.

---

⭐️ *If you liked this, try combining it with your own ASCII patterns!*
