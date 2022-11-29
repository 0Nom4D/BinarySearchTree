from sources.searching import LinearCount, BinaryCount, BTree
from typing import List
from time import sleep
from re import findall
from os import stat

import pytest

def openFile(filename: str) -> List[str]:
    word_list = []

    def isEmpty(filename: str) -> bool:
        return stat(filename).st_size == 0

    if isEmpty(filename):
        return []
    with open(filename) as fd:
        for line in fd:
            word_list += findall(r"((?!^-)[\w-]+)", line)
        if len(word_list) == 0:
            return []
    fd.close()
    return word_list


class TestSearchingAlgorithm:

    ## File Opening Tests
    def test_fileOpeningParsing(self):
        wordList = openFile('tests/testFiles/tiny_text.txt')
        assert wordList == ['Extraordinary', 'scene', 'at', 'the', 'nou', 'camp']

    def test_fileOpeningParsingWithPunctation(self):
        wordList = openFile('tests/testFiles/tiny_text_with_punctuation.txt')
        assert wordList == [
            'Messi', 'Oh', 'Messi', 'WHAAAAAAATTTT', 'MESSI',
            'ARE', 'YOU', 'KIDDING', 'ME', 'A', 'work',
            'of', 'art', 'This', 'man', 'is',
            'absolutely', 'midlane', 'to', 'pure', 'footballing', 'magic'
            ]

    def test_fileOpeningMediumFile(self):
        wordList = openFile('tests/testFiles/lyrics_Ronaldo_Ziak.txt')
        assert len(wordList) == 504

    ## Linear Couting Tests
    @pytest.mark.benchmark(group='Tiny Text')
    def test_LinearCountOnTinyText(self, benchmark):
        wordList = openFile('tests/testFiles/tiny_text.txt')
        result = benchmark.pedantic(LinearCount, iterations=10, args=[wordList, 'CAMP'])
        assert result == 1

    @pytest.mark.benchmark(group='Tiny Text With Punctuation')
    def test_LinearCountOnTinyTextWithPunctuation(self, benchmark):
        wordList = openFile('tests/testFiles/tiny_text_with_punctuation.txt')
        result = benchmark.pedantic(LinearCount, iterations=10, args=[wordList, 'Messi'])
        assert result == 3

    @pytest.mark.benchmark(group='Song Lyrics')
    def test_LinearCountOnSongLyrics(self, benchmark):
        wordList = openFile('tests/testFiles/lyrics_Ronaldo_Ziak.txt')
        result = benchmark.pedantic(LinearCount, iterations=10, args=[wordList, 'Ronaldo'])
        assert result == 4

    @pytest.mark.benchmark(group='Lorem Ipsum')
    def test_LinearCountOnLoremIpsum(self, benchmark):
        wordList = openFile('tests/testFiles/lorem_ipsum.txt')
        result = benchmark.pedantic(LinearCount, iterations=10, args=[wordList, 'SED'])
        assert result == 3310

    @pytest.mark.benchmark(group='Bible')
    def test_LinearCountOnBible(self, benchmark):
        wordList = openFile('tests/testFiles/bible.txt')
        result = benchmark.pedantic(LinearCount, iterations=10, args=[wordList, 'SHALL'])
        assert result == 9840

    @pytest.mark.benchmark(group='Bible Ten Times')
    def test_LinearCountOnTenTimesBible(self, benchmark):
        wordList = openFile('tests/testFiles/10_times_bible.txt')
        result = benchmark.pedantic(LinearCount, iterations=10, args=[wordList, 'SHALL'])
        assert result == 98400

    ## Binary Tree Search Couting Tests
    @pytest.mark.benchmark(group='Tiny Text')
    def test_BinaryCountOnTinyText(self, benchmark):
        wordList = openFile('tests/testFiles/tiny_text.txt')
        bTree = BTree()

        for word in wordList:
            bTree.insertInTree(word)
        result = benchmark.pedantic(BinaryCount, iterations=10, args=[bTree, 'CAMP'])
        assert result == 1

    @pytest.mark.benchmark(group='Tiny Text With Punctuation')
    def test_BinaryCountOnTinyTextWithPunctuation(self, benchmark):
        wordList = openFile('tests/testFiles/tiny_text_with_punctuation.txt')
        bTree = BTree()

        for word in wordList:
            bTree.insertInTree(word)
        result = benchmark.pedantic(BinaryCount, iterations=10, args=[bTree, 'Messi'])
        assert result == 3

    @pytest.mark.benchmark(group='Song Lyrics')
    def test_BinaryCountOnSongLyrics(self, benchmark):
        wordList = openFile('tests/testFiles/lyrics_Ronaldo_Ziak.txt')
        bTree = BTree()

        for word in wordList:
            bTree.insertInTree(word)
        result = benchmark.pedantic(BinaryCount, iterations=10, args=[bTree, 'Ronaldo'])
        assert result == 4

    @pytest.mark.benchmark(group='Lorem Ipsum')
    def test_BinaryCountOnLoremIpsum(self, benchmark):
        wordList = openFile('tests/testFiles/lorem_ipsum.txt')
        bTree = BTree()

        for word in wordList:
            bTree.insertInTree(word)
        result = benchmark.pedantic(BinaryCount, iterations=10, args=[bTree, 'SED'])
        assert result == 3310

    @pytest.mark.benchmark(group='Bible')
    def test_BinaryCountOnBible(self, benchmark):
        wordList = openFile('tests/testFiles/bible.txt')
        bTree = BTree()

        for word in wordList:
            bTree.insertInTree(word)
        result = benchmark.pedantic(BinaryCount, iterations=10, args=[bTree, 'SHALL'])
        assert result == 9840

    @pytest.mark.benchmark(group='Bible Ten Times')
    def test_BinaryCountOnTenTimesBible(self, benchmark):
        wordList = openFile('tests/testFiles/10_times_bible.txt')
        bTree = BTree()

        for word in wordList:
            bTree.insertInTree(word)
        result = benchmark.pedantic(BinaryCount, iterations=10, args=[bTree, 'SHALL'])
        assert result == 98400

    ## Binary Tree Search Couting Tree With Tree Indexing
    @pytest.mark.benchmark(group='Tiny Text')
    def test_BinaryCountOnTinyTextWithIndexing(self, benchmark):
        wordList = openFile('tests/testFiles/tiny_text.txt')
        bTree = BTree()

        result = benchmark.pedantic(BinaryCount, iterations=10, args=[bTree, 'CAMP', wordList])
        assert result == 1

    @pytest.mark.benchmark(group='Tiny Text With Punctuation')
    def test_BinaryCountOnTinyTextWithPunctuationWithIndexing(self, benchmark):
        wordList = openFile('tests/testFiles/tiny_text_with_punctuation.txt')
        bTree = BTree()

        result = benchmark.pedantic(BinaryCount, iterations=10, args=[bTree, 'Messi', wordList])
        assert result == 3

    @pytest.mark.benchmark(group='Song Lyrics')
    def test_BinaryCountOnSongLyricsWithIndexing(self, benchmark):
        wordList = openFile('tests/testFiles/lyrics_Ronaldo_Ziak.txt')
        bTree = BTree()

        result = benchmark.pedantic(BinaryCount, iterations=10, args=[bTree, 'Ronaldo', wordList])
        assert result == 4

    @pytest.mark.benchmark(group='Lorem Ipsum')
    def test_BinaryCountOnLoremIpsumWithIndexing(self, benchmark):
        wordList = openFile('tests/testFiles/lorem_ipsum.txt')
        bTree = BTree()

        result = benchmark.pedantic(BinaryCount, iterations=10, args=[bTree, 'SED', wordList])
        assert result == 3310

    @pytest.mark.benchmark(group='Bible')
    def test_BinaryCountOnBibleWithIndexing(self, benchmark):
        wordList = openFile('tests/testFiles/bible.txt')
        bTree = BTree()

        result = benchmark.pedantic(BinaryCount, iterations=10, args=[bTree, 'SHALL', wordList])
        assert result == 9840

    @pytest.mark.benchmark(group='Bible Ten Times')
    def test_BinaryCountOnTenTimesBibleWithIndexing(self, benchmark):
        wordList = openFile('tests/testFiles/10_times_bible.txt')
        bTree = BTree()

        result = benchmark.pedantic(BinaryCount, iterations=10, args=[bTree, 'SHALL', wordList])
        assert result == 98400
