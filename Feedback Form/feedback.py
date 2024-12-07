import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.scrolled import ScrolledText
import json
from datetime import datetime
from ttkbootstrap.style import Bootstyle
from PIL import Image, ImageTk
import os

class FeedbackForm:
    def __init__(self):
        # Create a custom theme
        self.root = ttk.Window(themename="superhero")
        self.root.title("✨ Feedback Form")
        self.root.geometry("900x800")
        
        # Set background color
        style = ttk.Style()
        style.configure('Custom.TFrame', background='#2c3e50')
        
        self.center_window()
        
        # Create main container with gradient effect
        self.main_frame = ttk.Frame(self.root, padding="30", style='Custom.TFrame')
        self.main_frame.pack(fill=BOTH, expand=YES)
        
        self.create_header()
        self.create_form()
        
        # Add hover effects
        self.add_hover_effects()
        
        # Add animation for initial load
        self.animate_form_elements()
    
    def animate_form_elements(self):
        """Animate form elements on startup"""
        children = self.main_frame.winfo_children()
        for i, child in enumerate(children):
            child.pack_forget()
            self.root.after(100 * i, lambda w=child: w.pack(fill=X, pady=5))

    def center_window(self):
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width - 900) // 2
        y = (screen_height - 800) // 2
        self.root.geometry(f"900x800+{x}+{y}")
        
    def create_header(self):
        # Header withmodern design
        header_frame = ttk.Frame(self.main_frame)
        header_frame.pack(fill=X, pady=(0, 30))
        
        # Add a decorative line
        ttk.Separator(header_frame, orient='horizontal').pack(fill=X, pady=(0, 20))
        
        title = ttk.Label(
            header_frame,
            text="✨ Share Your Experience ✨",
            font=("Helvetica", 32, "bold"),
            bootstyle="inverse-primary",
        )
        title.pack(pady=10)
        
        subtitle = ttk.Label(
            header_frame,
            text="Your feedback helps us improve",
            font=("Helvetica", 14),
            bootstyle="inverse-secondary",
        )
        subtitle.pack()
        
        # Add another decorative line
        ttk.Separator(header_frame, orient='horizontal').pack(fill=X, pady=(20, 0))
        
    def create_form(self):
        # Modern form container with card-like appearance
        form_frame = ttk.Frame(self.main_frame, padding=20)
        form_frame.pack(fill=BOTH, expand=YES)
        
        # Add a pulsing effect to the form fields
        self.add_field_effects(form_frame)
        
        # Name field with icon and validation
        name_frame = ttk.Frame(form_frame)
        name_frame.pack(fill=X, pady=(0, 15))
        ttk.Label(name_frame, text="👤 Full Name", font=("Helvetica", 12, "bold"), 
                 bootstyle="inverse-primary").pack(anchor=W, pady=(0, 5))
        self.name_entry = ttk.Entry(name_frame, width=50, font=("Helvetica", 11))
        self.name_entry.pack(fill=X, ipady=5)
        
        # Add validation
        self.name_entry.bind('<FocusOut>', self.validate_name)
        
        # Email field with validation
        email_frame = ttk.Frame(form_frame)
        email_frame.pack(fill=X, pady=(0, 15))
        ttk.Label(email_frame, text="📧 Email Address", font=("Helvetica", 12, "bold"),
                 bootstyle="inverse-primary").pack(anchor=W, pady=(0, 5))
        self.email_entry = ttk.Entry(email_frame, width=50, font=("Helvetica", 11))
        self.email_entry.pack(fill=X, ipady=5)
        
        # Add validation
        self.email_entry.bind('<FocusOut>', self.validate_email)
        
        # Enhanced star rating with hover effects
        self.create_enhanced_rating(form_frame)
        
        # Category with modern dropdown
        ttk.Label(form_frame, text="📑 Feedback Category", font=("Helvetica", 12, "bold"),
                 bootstyle="inverse-primary").pack(anchor=W, pady=(15, 5))
        self.category_var = tk.StringVar()
        categories = ["General Feedback", "Product Review", "Customer Service", "Website Experience", "Bug Report"]
        self.category_combo = ttk.Combobox(
            form_frame, 
            values=categories,
            textvariable=self.category_var,
            font=("Helvetica", 11),
            state="readonly"
        )
        self.category_combo.pack(fill=X, ipady=5)
        self.category_combo.set("General Feedback")
        
        # Feedback text area with modern styling
        ttk.Label(form_frame, text="💭 Your Message", font=("Helvetica", 12, "bold"),
                 bootstyle="inverse-primary").pack(anchor=W, pady=(15, 5))
        self.feedback_text = ScrolledText(
            form_frame,
            height=6,
            width=50,
            font=("Helvetica", 11),
            wrap=tk.WORD
        )
        self.feedback_text.pack(fill=BOTH, expand=YES, pady=(0, 20))
        
        # Submit button with hover effect
        self.submit_btn = ttk.Button(
            form_frame,
            text="Submit Feedback 📤",
            command=self.submit_feedback,
            bootstyle="success-outline",
            width=25,
            cursor="hand2"
        )
        self.submit_btn.pack(pady=20)

    def validate_name(self, event):
        name = self.name_entry.get().strip()
        if len(name) < 2:
            self.show_validation_error("Name must be at least 2 characters long")
            self.name_entry.configure(bootstyle="danger")
        else:
            self.name_entry.configure(bootstyle="success")

    def validate_email(self, event):
        email = self.email_entry.get().strip()
        if '@' not in email or '.' not in email:
            self.show_validation_error("Please enter a valid email address")
            self.email_entry.configure(bootstyle="danger")
        else:
            self.email_entry.configure(bootstyle="success")

    def show_validation_error(self, message):
        error_label = ttk.Label(
            self.main_frame,
            text=message,
            bootstyle="danger",
            font=("Helvetica", 10)
        )
        error_label.pack(pady=5)
        self.root.after(2000, error_label.destroy)

    def create_enhanced_rating(self, parent):
        rating_frame = ttk.Frame(parent)
        rating_frame.pack(fill=X, pady=(0, 15))
        
        ttk.Label(rating_frame, text="⭐ Rate Your Experience", 
                 font=("Helvetica", 12, "bold"),
                 bootstyle="inverse-primary").pack(anchor=W, pady=(0, 5))
        
        self.rating_var = tk.StringVar()
        stars_frame = ttk.Frame(rating_frame)
        stars_frame.pack(fill=X)
        
        # Create interactive stars with hover effects
        self.star_buttons = []
        for i in range(1, 6):
            btn = ttk.Button(
                stars_frame,
                text="★",
                command=lambda x=i: self.set_rating(x),
                bootstyle="primary-link",
                width=5,
                cursor="hand2"
            )
            btn.pack(side=LEFT, padx=5)
            
            # Add hover effects
            btn.bind('<Enter>', lambda e, x=i: self.on_star_hover(x))
            btn.bind('<Leave>', lambda e: self.on_star_leave())
            
            self.star_buttons.append(btn)

    def on_star_hover(self, rating):
        """Highlight stars on hover"""
        for i, btn in enumerate(self.star_buttons):
            if i < rating:
                btn.configure(bootstyle="warning-link")

    def on_star_leave(self):
        """Reset star colors when mouse leaves"""
        current_rating = int(self.rating_var.get()) if self.rating_var.get() else 0
        for i, btn in enumerate(self.star_buttons):
            if i < current_rating:
                btn.configure(bootstyle="warning-link")
            else:
                btn.configure(bootstyle="primary-link")

    def add_field_effects(self, parent):
        """Add visual effects to form fields"""
        style = ttk.Style()
        
        # Add focus effects
        style.configure('Custom.TEntry',
                       fieldbackground='#34495e',
                       foreground='white',
                       insertcolor='white')
        
        style.map('Custom.TEntry',
                 fieldbackground=[('focus', '#2c3e50')],
                 foreground=[('focus', '#2ecc71')])

    def set_rating(self, rating):
        self.rating_var.set(str(rating))
        # Update star colors
        for i, child in enumerate(self.main_frame.winfo_children()[1].winfo_children()[3].winfo_children()[1].winfo_children()):
            if i < rating:
                child.configure(bootstyle="warning-link")
            else:
                child.configure(bootstyle="primary-link")

    def add_hover_effects(self):
        # Add hover effects for buttons and entries
        style = ttk.Style()
        
        style.configure('TEntry', foreground='white')
        style.map('TEntry',
                 foreground=[('focus', 'white')],
                 fieldbackground=[('focus', '#34495e')])
        
        style.map('TButton',
                 background=[('active', '#2ecc71')],
                 foreground=[('active', 'white')])

    def show_animated_success(self):
        success_window = ttk.Toplevel(self.root)
        success_window.title("")
        success_window.geometry("400x200")
        
        # Center the success window
        success_window.geometry(f"+{self.root.winfo_x() + 250}+{self.root.winfo_y() + 275}")
        
        # Add animation effect
        for i in range(5):
            label = ttk.Label(
                success_window,
                text="🎉 Thank you for your feedback! 🎉",
                font=("Helvetica", 14, "bold"),
                bootstyle="success"
            )
            label.pack(pady=20)
            label.after(100 * i, lambda l=label: l.pack_forget())
        
        final_label = ttk.Label(
            success_window,
            text="🎉 Thank you for your feedback! 🎉",
            font=("Helvetica", 14, "bold"),
            bootstyle="success"
        )
        final_label.pack(pady=20)
        
        ttk.Button(
            success_window,
            text="Close",
            command=success_window.destroy,
            bootstyle="success-outline",
            cursor="hand2"
        ).pack(pady=10)
        
        success_window.after(2000, success_window.destroy)

    def submit_feedback(self):
        feedback_data = {
            "name": self.name_entry.get(),
            "email": self.email_entry.get(),
            "rating": self.rating_var.get(),
            "category": self.category_var.get(),
            "feedback": self.feedback_text.get("1.0", tk.END).strip(),
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        
        try:
            with open("feedback_data.json", "a") as f:
                json.dump(feedback_data, f)
                f.write("\n")
            
            # Show success message
            self.show_animated_success()
            
            # Clear form
            self.name_entry.delete(0, tk.END)
            self.email_entry.delete(0, tk.END)
            self.rating_var.set("")
            self.category_combo.set("General Feedback")
            self.feedback_text.delete("1.0", tk.END)
            
        except Exception as e:
            # Show error message
            error_window = ttk.Toplevel(self.root)
            error_window.title("Error")
            error_window.geometry("300x150")
            error_window.geometry(f"+{self.root.winfo_x() + 250}+{self.root.winfo_y() + 275}")
            
            ttk.Label(
                error_window,
                text="An error occurred while submitting feedback.",
                font=("Helvetica", 12),
                bootstyle="danger"
            ).pack(pady=20)
            
            ttk.Button(
                error_window,
                text="OK",
                command=error_window.destroy,
                bootstyle="danger-outline"
            ).pack()
    
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = FeedbackForm()
    app.run()
