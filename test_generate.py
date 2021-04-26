import unittest
from crossword import *
from generate import *

class TestGenerate(unittest.TestCase):
    def test_enforce_node_consistency(self):
        # Parse command-line arguments
        structure = "data/structure1.txt"
        words = "data/words1.txt"

        # Generate crossword
        crossword = Crossword(structure, words)
        creator = CrosswordCreator(crossword)
        creator.enforce_node_consistency()

    def test_revise(self):
        # Parse command-line arguments
        structure = "data/structure1.txt"
        words = "data/words1.txt"

        # Generate crossword
        crossword = Crossword(structure, words)
        creator = CrosswordCreator(crossword)
        creator.enforce_node_consistency()
        vs = list(creator.domains.keys())
        creator.revise(vs[0], vs[1])

    def test_arc3(self):
        # Parse command-line arguments
        structure = "data/structure1.txt"
        words = "data/words1.txt"

        # Generate crossword
        crossword = Crossword(structure, words)
        creator = CrosswordCreator(crossword)
        creator.enforce_node_consistency()
        creator.ac3()


if __name__ == "__main__":
    unittest.main()
