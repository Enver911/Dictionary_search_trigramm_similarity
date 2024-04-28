import json
from string import ascii_uppercase


def trigram_similarity(word_check, rating=0.5):
    """
    Trigram similarity between two strings is determined by the number of matching character triplets in both strings.
    The algorithm can be generalized to n-grams, where n=1, 2, ...

    The lines are then divided into triplets (trigrams). Finally, the similarity is calculated using the formula:

    s = 2*m / (a ​​+ b).

    Here:

    m - number of matching trigrams
    a - number of trigrams in string1
    b - number of trigrams in string2
    
    ---------------------------------
    
    Триграммное сходство (trigram similarity) между двумя строками определяется числом совпадающих символьных триплетов в обоих строках. 
    Алгоритм можно обобщить на n-граммы, где n=1, 2, ...

    Затем строки разделяются на триплеты (триграммы). Окончательно, сходство вычисляется по формуле:

    s = 2*m / (a + b).

    Здесь:

    m - число совпадающих триграмм
    a - число триграмм в string1
    b - число триграмм в string2
    """
    dict_eng = {}
    dict_rus = {}

    with open(file="dictionary_eng.json", encoding="utf-8", mode="r") as file_input: # unserialize into dict "dictionary_rus.json"
        dict_eng = json.load(file_input)
        
    with open(file="dictionary_rus.json", encoding="utf-8", mode="r") as file_input: # unserialize into dict "dictionary_eng.json"
        dict_rus = json.load(file_input)
    
    
    word_check = " " + word_check.upper() + " " 
    
    if set(word_check.strip()).issubset(set(ascii_uppercase)): # checking for word language
        dict_check = dict_eng
    else:
        dict_check = dict_rus 
        
    word_trigrams = [word_check[i: i + 3] for i in range(len(word_check) - 2)] #word trigrams list
    dict_trigrams = {} # dictionary {dict_word: trigrams list}
    
    for word_dict in dict_check:
        word_dict = " " + word_dict.upper() + " "
        dict_trigrams[word_dict] = [word_dict[i: i + 3] for i in range(len(word_dict) - 2)] #dict trigrams
    
    word_ratings = [] # list [[dict_word, rating], ...] where rating = 2 * matches / (len(word_trigrams) + len(dict_word_trigrams))

    for dict_word, dict_word_trigrams in dict_trigrams.items():
        matches = sum(trigram in dict_word_trigrams for trigram in word_trigrams)
        word_rating = 2 * matches / (len(word_trigrams) + len(dict_word_trigrams))
        word_ratings += [[dict_word, word_rating]]
        
    word_ratings_sorted = sorted(word_ratings, key=lambda row: row[1], reverse=True) # reverse sort by rating
    
    # filtred dict with similar words
    result = {word[0].strip(): dict_check.get(word[0].strip())  for word in word_ratings_sorted if word[1] >= rating} or \
             {word[0].strip(): dict_check.get(word[0].strip())  for word in word_ratings_sorted[:5]}
    
    return result


word = ""
while word not in ("exit", "stop", "exit()", "stop()"):
    word = input('Input word for Trigram similarity search in rus and eng dictionaries ("exit" or "stop" to exit):\n')
    
    for key, value in trigram_similarity(word).items():
        print(f"{key}: {value}")
        print("-" * 100)
    


