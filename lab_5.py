import re
import csv



print("Task №1")
text = open('task1-en.txt').read().strip()

print("Part 1 (Все конструкции 'Fig. #') -------------")
pictures = re.findall(r"\bFig. \d+\b", text)
for picture in pictures:
    print(picture)

print("Part 2 (Все слова из четырёх букв) ------------")
words = re.findall(r"\b[a-zA-Z]{4}\b", text)
for word in words:
    print(word)



print("Task №2")
print("Стили и ширина всех шрифтов task2.html:")
with open('task2.html', 'r', encoding='utf-8') as file:
    text2 = file.read()
styles = re.findall(r"font-style: \w+", text2)
wights = re.findall(r"font-weight: \w+", text2)
for num in range(len(styles)):
    print(f'№{num+1} - {styles[num]}; {wights[num]}')



print("Task №3")
text3 = open('task3.txt').read().strip()
ids = re.findall(r"(?<=\s)\d+(?=\s)", text3)
surnames = re.findall(r"(?<=\s)[A-Z][a-z]+(?=\s)", text3)
emails = re.findall(r"\w+@\w+", text3)
dates = re.findall(r"\d{4}-\d{2}-\d{2}", text3)
links = re.findall(r"\shttps?://[^\s']+", text3)
with open('ans_3.cvs', 'w', newline='') as csvfile:
    answer = csv.writer(csvfile)
    csv_result = zip(ids, surnames, emails, dates, links)
    for row in csv_result:
        answer.writerow(row)
print("Данные отсортированы и помещены в файл ans_3.csv")



print("Extra Task ")
text4 = open('task_add.txt').read().strip()

print("Секретные ссылки:")
links_1 = re.findall(r"\shttps?://[a-z]+.[a-z]+", text4)
for link in links_1:
    print(link)

print("Секретные почты:")
emails_1 = re.findall(r"[a-zA-Z0-9_.+-]+@[a-z]+\.ru", text4)
emails_2 = re.findall(r"[a-zA-Z0-9_.+-]+@[a-z]+\.now", text4)
emails_3 = re.findall(r"[a-zA-Z0-9_.+-]+@[a-z]+\.ter", text4)
emails_4 = re.findall(r"[a-zA-Z0-9_.+-]+@[a-z]+\.le", text4)
for email in emails_1:
    print(link)
for email in emails_2:
    print(link)
for email in emails_3:
    print(link)
for email in emails_4:
    print(link)

print("Секретные даты:")
dates_1 = re.findall(r"\d{2}\W\d{2}\W\d{4}", text4)
dates_2 = re.findall(r"\d{4}\W\d{2}\W\d{2}", text4)
for date in dates_1:
    print(date)
for date in dates_2:
    print(date)

