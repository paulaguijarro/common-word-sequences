FROM python:3.9

COPY requirements.txt /common_word_sequence/requirements.txt
WORKDIR /common_word_sequence
RUN pip install -r requirements.txt
COPY common_word_sequences/ docs/ ./

ENTRYPOINT ["python", "com_word_seq.py"]
# Not using CMD so we can use the stdin:
# i.e: echo "word1 word2 word2" | docker run -i common_word_sequences -t 10
# CMD ["-f", "war-and-peace.txt"]
# CMD ["python", "com_word_seq.py", "-f", "war-and-peace.txt"]
