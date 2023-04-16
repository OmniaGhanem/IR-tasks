docs = [
    "new home sales top forecasts",
    "home sales rise in July",
    "increase in home sales in July",
    "July new home sales rise"
]
inverted_index = {}

for doc_id, doc in enumerate(docs):
    tokens = doc.split()

    for token in tokens:
        if token not in inverted_index:
            inverted_index[token] = []
        inverted_index[token].append(doc_id)

term = input("Enter a word/term: ")
if term in inverted_index:
    postings_list = inverted_index[term]
else:
    postings_list = []

print(postings_list)