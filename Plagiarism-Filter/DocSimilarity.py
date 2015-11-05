import random
import string
import os


class SimilarityReporter:


	def __init__(self, base_corpus, input_corpus):

		self.base_words = self.make_words_list(base_corpus)
		self.input_words = self.make_words_list(input_corpus)

		self.base_doubles = self.loadDoubles(self.base_words)
		self.input_doubles = self.loadDoubles(self.input_words)

		self.base_triples = self.loadTriples(self.base_words)
		self.input_triples = self.loadTriples(self.input_words)

		self.stop_words = ['a', 'an', 'and', 'are', 'as', 'at', 'be', 'by',
						   'for', 'from', 'has', 'he', 'in', 'is', 'it', 'its',
						   'of', 'on', 'that', 'the', 'to', 'was', 'were',
						   'will', 'with']

	def make_words_list(self, corpus):
		words = []
		for word in corpus.split():
			words.append(\
				''.join(char for char in word if char not in string.punctuation)\
				.strip())
		return words

	def loadDoubles(self, corpus):

		pairs = {}
		for i in range(len(corpus) - 1):
			first, second = corpus[i], corpus[i+1]
			key = first
			if key in pairs:
				pairs[key].append(second)
			else:
				pairs[key] = [second]

		return pairs

	def loadTriples(self, corpus):

		triples = {}

		for i in range(len(corpus) - 2):
			first, second, third = corpus[i], corpus[i+1], corpus[i+2]
			key = (first, second)

			if key in triples:
				triples[key].append(third)
			else:
				triples[key] = [third]

		return triples

	def getSimilarityIndexSingles(self):
		
		matches = 0
		attempts = 0

		for word in self.base_words:
			if word not in self.stop_words:
				if word in self.input_words:
					matches += 1
				attempts += 1

		print('Single word matches: {}/{} matches, {} match percentage'\
			  .format(matches, attempts,
			   round(((float(matches) / attempts) * 100), 3)))
		
		return matches / attempts

	def getSimilarityIndexDoubles(self):

		matches = 0
		attempts = 0

		for key in self.input_doubles.keys():
			if key in self.base_doubles.keys():

				for next_word in self.input_doubles[key]:

					if next_word in self.base_doubles[key]:
						matches += 1
			attempts += 1


		print('Two-word sequence similarity: {}/{} matches, {} match percentage'\
			  .format(matches, attempts,
			   round(((float(matches) / attempts) * 100), 3)))

		return matches / attempts

	def getSimilarityIndexTriples(self):

		matches = 0
		attempts = 0

		for key in self.input_triples.keys():
			if key in self.base_triples.keys():

				for next_word in self.input_triples[key]:

					if next_word in self.base_triples[key]:
						matches += 1
			attempts += 1

		print('Three-word sequence similarity: {}/{} matches, {} match percentage'\
			  .format(matches, attempts,
			  		  round(((float(matches) / attempts) * 100), 3)))

		return matches / attempts


	def printReport(self):

		print('Generating similarity indexes.....\n')


		similarityIndex = .2 * self.getSimilarityIndexSingles() +\
						  .3 * self.getSimilarityIndexDoubles() +\
						  .5 * self.getSimilarityIndexTriples()

		print('Weighted similarity index: {:.3f}\n'.format(similarityIndex))

		if similarityIndex < .3:
			print('The .two documents are not very similar. It is unlikely that any plagiarism occurred.')
		elif similarityIndex < .622:
			print('This essay contains commonalities with the base essay. A careful review of the two would be a good choice.')
		else:
			print('These two documents are very similar. It is highly likely that the document in question is plagiarized.')


if __name__ == '__main__':

	
	base_path = input('Enter the path to the base document\n(Current directory is: {})\n'
		.format(os.getcwd()))
	input_path = input('Enter the path to document to be analyzed\n'
		.format(os.getcwd()))
	
	try:
		base_corpus = open(base_path, 'r').read()
		input_corpus = open(input_path, 'r').read()
	except FileNotFoundError:
		print('Invalid Files. Double check your filenames!\n')
		os._exit(1)

	my_mcc = SimilarityReporter(base_corpus, input_corpus)
	my_mcc.printReport()
