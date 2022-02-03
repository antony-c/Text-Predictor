class Word_Data:

    @staticmethod
    def predict(word, data):  # Returns up to 3 predicted words following input
        def sort_options(options):  # Sorts potential words by weight
            sort_lambda = lambda item: item[1]
            sorted_options = sorted(options, key=sort_lambda, reverse=True)

            return {k: v for k, v in sorted_options}

        def padded(list): # Pad list to 3 elements
            for i in range(3 - len(list)):
                list.append("")
            return list

        # If word is not in database, give no predictions
        if word not in data:
            return ["", "", ""]

        word_options = sort_options(data[word].items())

        # If less than or equal to 3 predictions, return all predictions
        if len(word_options) <= 3:
            return padded([option for option in word_options])

        # Otherwise, return top 3 weighted predictions
        enum_options = enumerate(word_options)
        return [option for i, option in enum_options if i < 3]

    @staticmethod
    def check_spelling(word, data):
        return word in data
