import argparse

from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types


def print_result(annotations):
    score = annotations.document_sentiment.score
    magnitude = annotations.document_sentiment.magnitude
    file=open('sentiment.txt','w',encoding="utf-8")
    for index, sentence in enumerate(annotations.sentences):
        sentence_sentiment = sentence.sentiment.score
        file.write('Sentence {} has a sentiment score of {}'.format(
            index, sentence_sentiment)+'\n')
    file.close()
    print('Sentiments written to file.')
    print('Overall Sentiment: score of {} with magnitude of {}'.format(
        score, magnitude))
    return 0


def analyze(tweets):
    """Run a sentiment analysis request on text within a passed filename."""
    client = language.LanguageServiceClient()

    with open('tweets.txt', 'r',encoding="utf-8") as review_file:
        # Instantiates a plain text document.
        content = review_file.read()

    document = types.Document(
        content=content,
        type=enums.Document.Type.PLAIN_TEXT)
    annotations = client.analyze_sentiment(document=document)

    # Print the results
    print_result(annotations)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument(
        'tweets',
        help='The filename of the tweets file you\'d like to analyze.')
    args = parser.parse_args()
    analyze(args.tweets)
