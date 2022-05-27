# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}
def read_file_content(filename):
    # [assignment] Add your code here 
    filenames = open(filename, "r")
    file = filenames.read()
    return file

#read_file_content("c:/Users/sanmi/Downloads/Reading-Text-Files/Reading-Text-Files/story.txt")


def count_words(text_file):
    text = read_file_content(text_file)
    words = text.split()
    counts = dict()

    for word in words:
        if word in counts:
            counts[word] += 1

        else :
            counts[word] = 1

    return counts


    # [assignment] Add your code here
print(count_words("c:/Users/sanmi/Downloads/Reading-Text-Files/Reading-Text-Files/story.txt"))

    #return {"as": 10, "would": 20}
