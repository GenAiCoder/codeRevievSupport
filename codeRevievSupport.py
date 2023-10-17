#from github import Github
#import requests
from tkinter import Tk, Entry, Text, Button, Label, Scrollbar, END

# Funkcje związane z logiką działania

def get_last_commit_code(repo_url):
    return ["First line of code", "secound line of code"]

def send_code_to_gpt(code):
    return '''{
    "comments": [
        {
            "lineNumber": 1,
            "comment": "Początek pliku, importy"
        },
        {
            "lineNumber": 5,
            "comment": "Funkcja główna programu"
        },
        {
            "lineNumber": 12,
            "comment": "Pętla przetwarzająca dane"
        },
        {
            "lineNumber": 18,
            "comment": "Zapis wyników do pliku"
        }
    ]
}'''

def add_comments_on_github(comments):
    # ... (dodaj komentarze do repozytorium)
    pass


class CodeReviewerGUI:
    def __init__(self):
        self.window = Tk()
        self.window.title("Code Reviewer")

        Label(self.window, text="GitHub Repository URL:").pack(pady=10)
        self.repo_entry = Entry(self.window, width=50)
        self.repo_entry.pack(pady=10)

        get_comments_button = Button(self.window, text="Get Comments", command=self.fetch_comments)
        get_comments_button.pack(pady=10)

        Label(self.window, text="Comments:").pack(pady=10)
        self.comments_text = Text(self.window, height=15, width=50)
        self.comments_text.pack(pady=10)

        scrollbar = Scrollbar(self.window, command=self.comments_text.yview)
        scrollbar.pack(side="right", fill="y")
        self.comments_text.config(yscrollcommand=scrollbar.set)

        

        submit_button = Button(self.window, text="Submit Comments to GitHub", command=self.submit_to_github)
        submit_button.pack(pady=10)

    def run(self):
        self.window.mainloop()

    def fetch_comments(self):
        repo_url = self.repo_entry.get()
        code = get_last_commit_code(repo_url)
        comments = send_code_to_gpt(code)
        self.comments_text.insert(END, comments + '\n\n')
            
    def submit_to_github(self):
        comments = self.comments_text.get("1.0", END).strip().split('\n\n')
        add_comments_on_github(comments)

if __name__ == "__main__":
    gui = CodeReviewerGUI()
    gui.run()