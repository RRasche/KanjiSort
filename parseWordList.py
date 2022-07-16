filename = "core6000.htm"
with open(filename, 'r', encoding='utf-8') as file:
	data = file.read()
	
data = data.split("</tr>")
kanji = []
for i in range(len(data)):
    line = data[i]
    line = line.split("</td>")[0].split(">")[-1]
    kanji.append(line)
with open("wordlist.txt", 'w', encoding='utf-8') as file:
    for word in kanji:
        file.write(word + " ")
