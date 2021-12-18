# Common Word Sequences

Program executable from the command line that when given text(s) will return a list of the n most common x word sequences.

## Basic requirements

The program accepts as arguments a list of one or more file paths.

```bash
python common_word_sequences/com_word_seq.py -f docs/text-examples/origin-of-species.txt
python common_word_sequences/com_word_seq.py -f docs/text-examples/origin-of-species.txt docs/text-examples/moby-dick.txt
```

Ouput example:

```text
❯ python common_word_sequences/com_word_seq.py -f docs/text-examples/origin-of-species.txt

Processing text...

+---------------------------------------+
|  Top 100 most common 3-word sequences |
+------------------------------+--------+
| Word Sequence                | Count  |
+------------------------------+--------+
| of the same                  |  310   |
| the same species             |  125   |
| conditions of life           |  120   |
| in the same                  |  113   |
| from each other              |  103   |
| species of the               |   95   |
| of natural selection         |   94   |
| on the other                 |   87   |
| the other hand               |   79   |
| the case of                  |   78   |
| some of the                  |   73   |
| of the world                 |   72   |
| parts of the                 |   70   |
| through natural selection    |   69   |
| with respect to              |   68   |
| in the case                  |   67   |
| the theory of                |   66   |
| it may be                    |   64   |
| the inhabitants of           |   63   |
| the species of               |   63   |
| of the species               |   63   |
| that of the                  |   60   |
| the same genus               |   60   |
| individuals of the           |   59   |
| forms of life                |   57   |
| as far as                    |   56   |
| part of the                  |   55   |
| the number of                |   54   |
| those of the                 |   54   |
| in this case                 |   51   |
| the nature of                |   50   |
| more or less                 |   50   |
| on the same                  |   50   |
| at the same                  |   50   |
| to each other                |   50   |
| in regard to                 |   49   |
| nature of the                |   49   |
| to the same                  |   49   |
| as in the                    |   48   |
| and in the                   |   47   |
| it has been                  |   47   |
| a state of                   |   47   |
| the individuals of           |   47   |
| one of the                   |   47   |
| nearly the same              |   47   |
| in which the                 |   47   |
| state of nature              |   46   |
| each other in                |   46   |
| we can understand            |   46   |
| the principle of             |   46   |
| inhabitants of the           |   45   |
| the amount of                |   45   |
| from a common                |   44   |
| will have been               |   44   |
| are descended from           |   43   |
| might have been              |   43   |
| by natural selection         |   43   |
| in a state                   |   42   |
| the same manner              |   42   |
| which have been              |   42   |
| and on the                   |   42   |
| to believe that              |   42   |
| animals and plants           |   41   |
| would have been              |   41   |
| we have seen                 |   41   |
| respect to the               |   40   |
| and of the                   |   40   |
| it would be                  |   40   |
| to have been                 |   40   |
| the same time                |   40   |
| the conditions of            |   39   |
| there is no                  |   39   |
| of the most                  |   39   |
| in some degree               |   39   |
| varieties of the             |   39   |
| belonging to the             |   39   |
| could be given               |   38   |
| members of the               |   38   |
| as well as                   |   38   |
| it is that                   |   38   |
| on the theory                |   38   |
| each other and               |   37   |
| it is not                    |   36   |
| that it is                   |   36   |
| species belonging to         |   36   |
| the process of               |   36   |
| the present day              |   35   |
| the power of                 |   35   |
| of life and                  |   35   |
| in order to                  |   35   |
| reason to believe            |   35   |
| from the same                |   33   |
| believe that the             |   33   |
| for instance the             |   33   |
| the sterility of             |   33   |
| of the sea                   |   33   |
| and this is                  |   32   |
| so as to                     |   32   |
| habits of life               |   32   |
| in relation to               |   32   |
+------------------------------+--------+
```

### How to run common-word-sequences

Install python requirements:

```bash
python3 -m venv venv # Create a virtual environment
source venv/bin/activate; pip install -r requirements.txt # Install requirements
```

or use the [Makefile](Makefile) provided:

```bash
make install
```

See program usage and options running the --help option:

``` text
❯ python common_word_sequences/com_word_seq.py --help
usage: com_word_seq.py [-h] [-f [FILE ...]] [-t TOP] [-w WORDS]

Given text(s) will return a list of the most common word sequences.

optional arguments:
  -h, --help            show this help message and exit
  -f [FILE ...], --file [FILE ...]
                        Path to file(s) to process. If no file is specified, stdin will be used.
  -t TOP, --top TOP     Number of top results to return. If no value is specified, 100 will be used.
  -w WORDS, --words WORDS
                        Number of words in each n-gram. If no value is specified, 3 will be used.
```

The program accepts parameters for the number of top results to return and the number of words in each n-gram. If no value is specified, the default values (words=3, top=100) will be used.

Examples:

``` text
❯ python common_word_sequences/com_word_seq.py -f docs/text-examples/origin-of-species.txt
❯ python common_word_sequences/com_word_seq.py -f docs/text-examples/origin-of-species.txt -t 10
❯ python common_word_sequences/com_word_seq.py -f docs/text-examples/origin-of-species.txt -t 10 -w 4
```

The program also accepts input from stdin.

Examples:

``` text
cat docs/text-examples/apostrophe-vs-single-quote.txt | python common_word_sequences/com_word_seq.py 
cat docs/text-examples/origin-of-species.txt | python common_word_sequences/com_word_seq.py -t 10
echo "word1 word2 word2" | docker run -i common_word_sequences
```

### How to run test for common-word-sequences

Install python test requirements:

```bash
python3 -m venv venv # Create a virtual environment
source venv/bin/activate
pip install -r requirements.txt # Install requirements
pip install -r common_word_sequences/tests/requirements.txt
```

Run the test suite and see the coverage report:

```text
venv/bin/pytest --cov=common_word_sequences


❯ venv/bin/pytest --cov=common_word_sequences
===================== test session starts ======================
platform darwin -- Python 3.9.0, pytest-6.2.5, py-1.11.0, pluggy-1.0.0
plugins: cov-3.0.0
collected 8
common_word_sequences/tests/test_ngram_tool.py ....
common_word_sequences/tests/test_utils.py ...

---------- coverage: platform darwin, python 3.9.0-final-0 -----------
Name                                             Stmts   Miss  Cover
--------------------------------------------------------------------
common_word_sequences/com_word_seq.py               27     27     0%
common_word_sequences/resources/__init__.py          0      0   100%
common_word_sequences/resources/ngram_tool.py       32      5    84%
common_word_sequences/tests/__init__.py              0      0   100%
common_word_sequences/tests/test_ngram_tool.py      34      0   100%
common_word_sequences/tests/test_utils.py           20      0   100%
common_word_sequences/utils/__init__.py              0      0   100%
common_word_sequences/utils/styles.py                5      0   100%
common_word_sequences/utils/texts.py                25     12    52%
--------------------------------------------------------------------
TOTAL                                              143     44    69%

=====================8 passed in 0.32s =====================
```

Or use the [Makefile](Makefile) provided:

```text
make test
```

### Next steps and improvements

At this version, file inputs are processed one at a time. In a next iteration, we could improve performance by running each file on it's own thread.

Improve test coverage.

### Bugs and issues

Not issues known at this time.

## Extra requirements

### Docker

There is a [Dockerfile](Dockerfile) for building the image. Text file examples are attached to the Docker image for testing purposes.

For building the image:

```bash
docker build -t common_word_sequences .
```

Or use the [Makefile](Makefile) provided:

```text
make docker-build

or execute:

make docker-run
```

Usage examples:

```bash
docker run common_word_sequences -w 2 -t 10  -f text-examples/apostrophe-vs-single-quote.txt
echo "word1 word2 word2" | docker run -i common_word_sequences -t 10
cat text-examples/apostrophe-vs-single-quote.txt| docker run -i common_word_sequences -t 10
```

### Processing large files

Concurrent processing of multiple files has not been implemented for this iteration.

Considering performance, changed from `zip` to `nltk ngrams` library.

From 3.06 minutes using zip to 2.37 minutes using ngrams:

```text
~❯ python common_word_sequences/com_word_seq.py -t 10 -f big-file.txt # Using zip

Processing text...

+------------------------------------+
| Top 10 most common 3-word sequences |
+-------------------------+----------+
| Word Sequence           |  Count   |
+-------------------------+----------+
| the sperm whale         |  86000   |
| of the whale            |  77000   |
| one of the              |  64000   |
| the white whale         |  59000   |
| of the sea              |  56000   |
| out of the              |  56000   |
| part of the             |  53000   |
| a sort of               |  51000   |
| of the sperm            |  43000   |
| it was a                |  32000   |
+-------------------------+----------+

took 3m 6s

~❯ python common_word_sequences/com_word_seq.py -t 10 -f big-file.txt # Using nltk ngrams

Processing text...

+------------------------------------+
| Top 10 most common 3-word sequences |
+-------------------------+----------+
| Word Sequence           |  Count   |
+-------------------------+----------+
| the sperm whale         |  86000   |
| of the whale            |  77000   |
| one of the              |  64000   |
| the white whale         |  59000   |
| of the sea              |  56000   |
| out of the              |  56000   |
| part of the             |  53000   |
| a sort of               |  51000   |
| of the sperm            |  43000   |
| it was a                |  32000   |
+-------------------------+----------+

took 2m 37s
```

### Unicode characters

```text
~❯ docker run common_word_sequences -f origin_of_species.txt  -f text-examples/unicode.txt -t 10

Processing text...

+----------------------------------------+
|  Top 10 most common 3-word sequences   |
+--------------------------------+-------+
| Word Sequence                  | Count |
+--------------------------------+-------+
| danish da quizdeltagerne       |   1   |
| da quizdeltagerne spiste       |   1   |
| quizdeltagerne spiste jordbær  |   1   |
| spiste jordbær med             |   1   |
| jordbær med fløde              |   1   |
| med fløde mens                 |   1   |
| fløde mens cirkusklovnen       |   1   |
| mens cirkusklovnen wolther     |   1   |
| cirkusklovnen wolther spillede |   1   |
| wolther spillede på            |   1   |
+--------------------------------+-------+
```

### Follow up questions

See [follow up questions](docs/follow-up-questions.md)
