from convokit.transformer import Transformer
from convokit.model import Corpus

import nltk

class Tokenizer(Transformer):
	'''
		tokenizes utterances. stores tokens as space-separated string.

		:param verbosity: frequency to print status messages while tokenizing. 
	'''
	def __init__(self, verbosity: int=0):
		self.verbosity = verbosity
	
	def _print_output(self, i):
		return (self.verbosity > 0) and (i > 0) and (i % self.verbosity == 0)
		
	def transform(self, corpus: Corpus):
		'''
			tokenizes each utterance, and stores tokens as a space-separated string entry in the utterance metadata.

			:param corpus: the Corpus to tokenize utterances for.
			:type corpus: Corpus
		'''
		for idx, utterance in enumerate(corpus.iter_utterances()):
			if self._print_output(idx):
				print(idx, 'utterances tokenized')
			utterance.add_meta('tokens', ' '.join(nltk.word_tokenize(utterance.text)))
		return corpus