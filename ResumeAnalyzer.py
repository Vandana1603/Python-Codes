import tkinter as tk
from tkinter import filedialog, messagebox

KEYWORDS = ["Python", "Machine Learning", "Data Analysis", "Communication", "Leadership"]

def evaluate_resume(text):
    word_count = len(text.split())
    keywords_found = [kw for kw in KEYWORDS if kw.lower() in text.lower()]
    feedback = []

    if word_count < 100:
        feedback.append("🔍 Your resume seems short. Consider adding more detail.")
    if not keywords_found:
        feedback.append("⚠️ No relevant keywords found. Try including industry-specific terms.")
    if "Objective" not in text:
        feedback.append("💡 Consider adding an 'Objective' section to clarify your goals.")

    return {
        "word_count": word_count,
        "keywords_found": keywords_found,
        "feedback": feedback
    }

def upload_resume():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if not file_path:
        return

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            resume_text = file.read()
    except UnicodeDecodeError:
        try:
            with open(file_path, "r", encoding="windows-1252") as file:
                resume_text = file.read()
        except Exception as e:
            messagebox.showerror("Error", f"Could not read file:\n{e}")
            return

    status_label.config(text="Analyzing resume...")
    root.update_idletasks()

    results = evaluate_resume(resume_text)

    output_text = f"Resume Summary\n\n"
    output_text += f" Word Count: {results['word_count']}\n"
    output_text += f" Keywords Found: {', '.join(results['keywords_found']) if results['keywords_found'] else 'None'}\n\n"
    output_text += " Suggestions:\n"
    if results["feedback"]:
        for tip in results["feedback"]:
            output_text += f"{tip}\n"
    else:
        output_text += "🎉 Excellent! Your resume is well-optimized."

    result_display.delete("1.0", tk.END)
    result_display.insert(tk.END, output_text)
    status_label.config(text="Analysis complete ✅")

# GUI Setup
root = tk.Tk()
root.title("Resume Analyzer")
root.geometry("600x500")

upload_button = tk.Button(root, text="📂 Upload Resume", command=upload_resume, font=("Arial", 12))
upload_button.pack(pady=10)

status_label = tk.Label(root, text="Waiting for resume upload...", font=("Arial", 10))
status_label.pack()

result_display = tk.Text(root, wrap=tk.WORD, font=("Arial", 11))
result_display.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

root.mainloop()