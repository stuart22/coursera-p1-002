def get_length(dna):
    """ (str) -> int

    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    """
    return  len(dna)

def is_longer(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    """
    return len(dna1) > len(dna2)

def count_nucleotides(dna, nucleotide):
    """ (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    """
    return dna.count(nucleotide)


def contains_sequence(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False

    """
    return dna2 in dna1



def is_valid_sequence(dna):
    """
    (str) -> bool
    """
    bool=true
    for letter in dna
        if letter not in ['A' ,"T", "C", "G"]:
            bool = false
    return bool


def insert_sequence(dna1, dna2, ind)

    return dna1[0:ind] + dna2 + dna1[ind+1:]



def get_complement(nucleotide):
    """(str) -> (str)

    Return the complement of the nucleotide

    """


    if nucleotide = 'A'
        return comp = 'T'
    elif nucleotide = 'T'
        return comp = 'A'
    elif nucleotide = 'C'
        return comp = 'G'
    elif nucleotide = 'G'
        return comp = 'C'

    print(comp)




def get_complementary_sequence(dna):
    """(str) -> (str)

        Return the complement of the sequence

    """
    complementary_sequence = ""
    for letter in dna:
        complementary_sequence += get_complement(letter)
    return

