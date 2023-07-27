import tensorflow
import pickle

class TaylorLM:

    def __init__(self):
    
        # loading the tokenizer
        with open('tokenizer.pickle', 'rb') as handle:
            self.tokenizer = pickle.load(handle)
        print("tokenizer loaded successfully")
        
        # loading the trained model
        self.model = tensorflow.keras.models.load_model('taylor_blstm_model')
        print("trained model loaded successfully")
        
    def finish_sentence(self, user_input):
    
        # the test document
        test_corpus = [user_input]

        # tokenizing the test corpuses
        tokenized_test_corpus = self.tokenizer.texts_to_sequences(test_corpus)[0]
        
        # we will loop until the model generates an <EOS> token
        eos_index = self.tokenizer.word_index["eos"]

        # looping to generate the sentence
        index = 0
        while index != eos_index and len(tokenized_test_corpus) <= 20:
            
            # making prediction to get the next word probs, pred are softmax probabilities
            pred = self.model.predict([tokenized_test_corpus])[0]
            
            # getting the word with the highest prob
            index = int(tensorflow.argmax(pred))

            # appending it to the list.
            tokenized_test_corpus.append(index)

        output_sentence = self.tokenizer.sequences_to_texts([tokenized_test_corpus])[0]

        output_sentence = output_sentence.replace(" eos", "")

        return output_sentence
