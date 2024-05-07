
<h3>Trigram similarity function (search algorithm)</h3>

<h4>
trigram_similarity(word_check, rating: float = 0.5) -> dict {"word": "description", ...} returns words with descriptions found in dictionaries

<h5>
  Trigram similarity between two strings is determined by the number of matching character triplets in both strings.
  <br>
  The algorithm can be generalized to n-grams, where n=1, 2, ...
  <br>
  The lines are then divided into triplets (trigrams). Finally, the similarity is calculated using the formula:
  <br>
  s = 2*m / (a ​​+ b).
  <br><br>
  Here:
  <br>
  m - number of matching trigrams
  <br>
  a - number of trigrams in string1
  <br>
  b - number of trigrams in string2
</h5>

---------------------------------
﻿
<h3>Функция триграммного сходства (поисковой алгоритм)</h3>

<h5>
  Триграммное сходство (trigram similarity) между двумя строками определяется числом совпадающих символьных триплетов в обоих строках. 
  <br>
  Алгоритм можно обобщить на n-граммы, где n=1, 2, ...
  <br>
  Затем строки разделяются на триплеты (триграммы). Окончательно, сходство вычисляется по формуле:
  <br>
  s = 2*m / (a + b).
  <br><br>
  Здесь:
  <br>
  m - число совпадающих триграмм
  <br>
  a - число триграмм в string1
  <br>
  b - число триграмм в string2
  <br>
</h5>
