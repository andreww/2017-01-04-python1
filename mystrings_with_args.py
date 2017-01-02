def num_of_vowels ( word ):
    return(sum([i in 'aeiou' for i in word]))

if __name__ == "__main__":

    import sys
    print("argv[0] is", sys.argv[0])
    print("argv[1] is", sys.argv[1])

    print(num_of_vowels(sys.argv[1]))
