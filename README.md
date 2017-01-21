# homz
- homz allows you to load a .txt file of words (separated by line-breaks), generate all the possible homonyms/homophones that exist within the dataset you provided, and then search for a word in the generated data to find all the best matches.
- homz relies on the [JellyFish](https://github.com/jamesturk/jellyfish) python library to perform [Match Rating](https://en.wikipedia.org/wiki/Match_rating_approach) comparisons, and also to generate [Jaro-Winkler distance](https://en.wikipedia.org/wiki/Jaro–Winkler_distance) scores.

# Usage
```
% git clone https://github.com/cameronehrlich/homz.git
% cd homz
% pip install -r requirements.txt
% python
>>> import homz
>>> words = homz.words_from_file('homonyms.txt')
>>> data = homz.generate_data(words)
>>> homonyms = homz.search(data, 'base')
>>> print(homonyms)
[u'based', u'bases', u'baste', u'basses', u'basque', u'braise', u'bass', u'bask', u'bale', u'bate']
```
