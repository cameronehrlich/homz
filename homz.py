import jellyfish
import codecs

def words_from_file(file_path='homonyms.txt'):
	words = []
	with codecs.open('words/' + file_path, 'r', 'UTF-8') as f:
	    for line in f:
	    	word = line.strip().lower()
	    	words.append(unicode(word))
	return words

def generate_data(words):
	word_dict = {}
	for i, w1 in enumerate(words):
		matching_words = []
		for j, w2 in enumerate(words):
			if w1 == w2:
				continue
			else:
				is_match_rating_true = jellyfish.match_rating_comparison(w1, w2)
				if is_match_rating_true:
					jaro_winkler_score = jellyfish.jaro_winkler(w1,w2)
					if jaro_winkler_score > 0.0:
						word_score = (w2, jaro_winkler_score)
						matching_words.append(word_score)
				if j == len(words)-1:
					sorted_matching_words = sorted(matching_words, key=lambda tup: tup[1], reverse=True)
					word_dict[w1] = sorted_matching_words
	return word_dict

def search(data, word, count=10):
	all_homz = data[word]
	output = []
	if len(all_homz) > 0:
		for h in all_homz:
			output.append(h[0])
			if len(output) >= count:
				return output

def save_data(obj, name):
    with open('data/' + name + '.pkl', 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)

def load_data(name):
    with open('data/' + name + '.pkl', 'rb') as f:
        return pickle.load(f)
