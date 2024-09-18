# Importing the Required Libraries
from spellchecker import SpellChecker  # Step 1: Importing the SpellChecker class from the spellchecker library to perform spell-checking.

# Step 2: Define the SpellCheckerApp class which holds the functionality for our app.
class SpellCheckerApp:
    def __init__(self):
        # Step 3: Initialize an instance of the SpellChecker class.
        self.spell = SpellChecker()

    # Step 4: Function to correct the input text.
    def correct_text(self, text):
        words = text.split()  # Split the text into individual words.
        corrected_words = []  # This will hold the corrected words.

        # Step 5: Iterate over each word in the text.
        for word in words:
            corrected_word = self.spell.correction(word)  # Get the corrected word.
            # If the corrected word is different from the original, show a message.
            if corrected_word != word.lower():
                # Add emoji to indicate correction.
                print(f"🔍 Correcting '{word}' to '{corrected_word}' ✅")
                corrected_words.append(corrected_word)  # Append the corrected word.
            else:
                corrected_words.append(word)  # If no correction is needed, keep the word as is.

        # Step 6: Return the corrected text as a single string.
        return " ".join(corrected_words)

    # Step 7: Function to run the spell checker app.
    def run(self):
        # Add some design with emojis and spaces.
        print("\n✨✨✨  Welcome to the Spell Checker App!  ✨✨✨\n")  # Intro message with emojis.
        print("📝 Type any text, and I'll help you correct it! 📝\n")
        print("🔴 Type 'exit' to close the program 🔴\n")

        # Step 8: Infinite loop to keep the program running until the user exits.
        while True:
            text = input("✏️ Enter a text (or 'exit' to quit): ")  # Ask user for input.
            if text.lower() == 'exit':  # Check if the user wants to exit.
                print("\n👋 Closing the program... Goodbye! 👋\n")  # Exit message.
                break  # Break out of the loop to stop the program.
            
            # Correct the entered text.
            corrected_text = self.correct_text(text)
            print(f"\n✨ Corrected Text: {corrected_text} ✨\n")  # Display the corrected text with emojis.

# Step 9: Entry point of the program.
if __name__ == "__main__":
    # Start the app.
    SpellCheckerApp().run()











#TODO: GUI Based Below

# # Importing the Required Libraries
# from tkinter import *
# from spellchecker import SpellChecker  # Importing SpellChecker for spell checking.

# # Step 1: Define the SpellCheckerApp class for the GUI-based application.
# class SpellCheckerApp:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Spell Checker App ✨")  # Set the title of the window.
#         self.root.geometry("500x400")  # Set the window size.

#         # Step 2: Create a SpellChecker instance.
#         self.spell = SpellChecker()

#         # Step 3: Add GUI components like labels, text boxes, and buttons.
#         self.label = Label(self.root, text="Enter Text:", font=("Arial", 14))
#         self.label.pack(pady=10)  # Label for input text.

#         self.text_box = Text(self.root, height=8, width=40, font=("Arial", 12))  # Text box for user input.
#         self.text_box.pack(pady=10)

#         self.check_button = Button(self.root, text="Check Spelling 🔍", command=self.correct_text, font=("Arial", 12), bg="lightblue")
#         self.check_button.pack(pady=10)  # Button to trigger spell check.

#         self.result_label = Label(self.root, text="Corrected Text:", font=("Arial", 14))
#         self.result_label.pack(pady=10)  # Label for the corrected text.

#         self.result_box = Text(self.root, height=8, width=40, font=("Arial", 12), state="disabled", bg="lightgray")  # Text box to display corrected text.
#         self.result_box.pack(pady=10)

#     # Step 4: Function to correct the text entered in the text box.
#     def correct_text(self):
#         text = self.text_box.get("1.0", END)  # Get the text from the text box.
#         words = text.split()  # Split the text into individual words.
#         corrected_words = []  # List to store corrected words.

#         # Step 5: Iterate through the words and correct them.
#         for word in words:
#             corrected_word = self.spell.correction(word)  # Get the corrected word.
#             if corrected_word != word.lower():  # If the word is corrected, notify.
#                 corrected_words.append(corrected_word)
#             else:
#                 corrected_words.append(word)

#         # Step 6: Display the corrected text in the result text box.
#         corrected_text = " ".join(corrected_words)  # Join the corrected words into a string.
#         self.result_box.config(state="normal")  # Enable the result box to update the text.
#         self.result_box.delete("1.0", END)  # Clear any previous text in the result box.
#         self.result_box.insert(END, corrected_text)  # Insert the corrected text.
#         self.result_box.config(state="disabled")  # Disable the result box after updating.

# # Step 7: Run the application.
# if __name__ == "__main__":
#     root = Tk()  # Initialize the Tkinter window.
#     app = SpellCheckerApp(root)  # Create an instance of the SpellCheckerApp.
#     root.mainloop()  # Run the main loop to keep the window open.
