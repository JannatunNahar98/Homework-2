"""
CS5760 Natural Language Processing - Homework 2
Part II, Q1: Bigram Language Model
"""

from collections import Counter

corpus = [
    ["<s>", "I", "love", "NLP", "</s>"],
    ["<s>", "I", "love", "deep", "learning", "</s>"],
    ["<s>", "deep", "learning", "is", "fun", "</s>"],
]


def build_counts(sentences):
    """Build unigram and bigram frequency counts."""
    unigram_counts = Counter()
    bigram_counts = Counter()

    for sentence in sentences:
        unigram_counts.update(sentence)

        for i in range(len(sentence) - 1):
            bigram_counts[(sentence[i], sentence[i + 1])] += 1

    return unigram_counts, bigram_counts


def bigram_probability(previous_word, next_word,
                       unigram_counts, bigram_counts):
    """Calculate MLE P(next_word | previous_word)."""
    denominator = unigram_counts[previous_word]

    if denominator == 0:
        return 0.0

    return bigram_counts[(previous_word, next_word)] / denominator


def sentence_probability(sentence, unigram_counts, bigram_counts):
    """Calculate the probability of a tokenized sentence."""
    probability = 1.0

    for i in range(len(sentence) - 1):
        probability *= bigram_probability(
            sentence[i],
            sentence[i + 1],
            unigram_counts,
            bigram_counts
        )

    return probability


def main():
    unigram_counts, bigram_counts = build_counts(corpus)

    print("UNIGRAM COUNTS")
    print("-" * 40)

    for word, count in unigram_counts.items():
        print(f"{word}: {count}")

    print()
    print("BIGRAM COUNTS")
    print("-" * 40)

    for (previous, next_word), count in bigram_counts.items():
        print(f"({previous}, {next_word}): {count}")

    print()
    print("MLE BIGRAM PROBABILITIES")
    print("-" * 40)

    for (previous, next_word), count in bigram_counts.items():
        probability = bigram_probability(
            previous,
            next_word,
            unigram_counts,
            bigram_counts
        )
        print(f"P({next_word} | {previous}) = {probability:.4f}")

    s1 = ["<s>", "I", "love", "NLP", "</s>"]
    s2 = ["<s>", "I", "love", "deep", "learning", "</s>"]

    p1 = sentence_probability(s1, unigram_counts, bigram_counts)
    p2 = sentence_probability(s2, unigram_counts, bigram_counts)

    print()
    print("SENTENCE PROBABILITIES")
    print("-" * 40)
    print("S1: <s> I love NLP </s>")
    print(f"P(S1) = {p1:.6f}")

    print()
    print("S2: <s> I love deep learning </s>")
    print(f"P(S2) = {p2:.6f}")

    if p1 > p2:
        print()
        print("Preferred sentence: S1")
        print("Reason: P(S1) is greater than P(S2).")
    elif p2 > p1:
        print()
        print("Preferred sentence: S2")
        print("Reason: P(S2) is greater than P(S1).")
    else:
        print()
        print("Both sentences have the same probability.")


if __name__ == "__main__":
    main()
