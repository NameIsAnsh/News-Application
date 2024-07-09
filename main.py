import tkinter as tk

import Functions as fn
root= tk.Tk()
m = tk.Text(root, width=120, height=30)

def displaynews(func):
    m.delete(1.0,tk.END)
    news= func
    if news['totalResults']==0:
        m.tag_configure("b", font=("Arial", 18, "bold"), justify="center")
        m.delete(1.0, tk.END)

        m.insert(tk.END, 'Articles not found!!', 'b')
    if isinstance(news, dict) and "articles" in news:

        for article in news['articles']:
            title= article.get('title')
            description= article.get('description')
            m.tag_configure("b", font=("Arial", 22, "bold"))
            m.tag_configure("bo", font=("Arial", 16))
            m.tag_configure("bol", font=("Arial", 12))
            url=article.get('url')
            m.insert(tk.END,f'\n{title}','b')
            m.insert(tk.END, f'\nDescription: \n{description}','bo')
            m.insert(tk.END, f'\n\nSource:\t{url}','bol')
            m.insert(tk.END, '\n\n'+'----'*30+'\n')
def search():

    topic=w2.get().strip()

    if topic:
        news= fn.headlines()
        m.delete(1.0, tk.END)

        for article in news['articles']:
            title= article.get('title')
            if topic.lower() in title.lower():
                
                description= article.get('description')
                m.tag_configure("b", font=("Arial", 22, "bold"))
                m.tag_configure("bo", font=("Arial", 16))
                m.tag_configure("bol",foreground='blue', font=("Arial", 12))
                url=article.get('url')
                m.insert(tk.END,f'\n{title}','b')
                m.insert(tk.END, f'\nDescription: \n{description}','bo')
                m.insert(tk.END, f'\n\nSource:\t{url}','bol')
                m.insert(tk.END, '\n\n'+'----'*30+'\n')

    else:
        m.tag_configure("bl", font=("Arial", 18, "bold"),justify="center")
        m.delete(1.0, tk.END)

        m.insert(tk.END,'Articles not found!!','bl')
def topheadlines():
    displaynews(fn.headlines())
m.pack(fill = tk.BOTH, expand=True,padx=20,pady=20)


w2=tk.Entry(root)
w2.pack(padx=0)


w = tk.Button(root, text='Search:',command=search)
w1= tk.Button(root, text='Get Top Headlines!',command=topheadlines)
root.title("Newsapp")
w.pack()
w1.pack()

root.mainloop()
