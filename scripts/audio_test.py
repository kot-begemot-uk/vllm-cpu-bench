#!/usr/bin/python
# SPDX-License-Identifier: Apache-2.0
'''Trivial openai transcription client'''


from argparse import ArgumentParser
import httpx
from openai import OpenAI

HELP='''
    --media file in any supported audio format
    --url defaults to http://localhost:8000/v1
    --model defaults to openai/whisper-tiny
'''

def sync_openai(media=None, url="http://localhost:8000/v1", model="openai/whisper-tiny"):
    '''Transcribe the supplied file'''


    client = OpenAI(
        base_url=url,
        api_key="EMPTY",
    )

    if media is None:
        raise RuntimeError("No media supplied")
    with open(media, "rb") as f:
        transcription = client.audio.transcriptions.create(
            file=f,
            model=model,
            language="en",
            response_format="json",
            temperature=0.0)
        return transcription.text

def main():
    '''submit audio for transcode'''

    aparser = ArgumentParser(description=main.__doc__)
    aparser.add_argument(
        '--media',
        help='media file - any supported format',
        type=str)

    aparser.add_argument(
        '--url',
        help='openai server url',
        type=str)

    aparser.add_argument(
        '--model',
        help='llm model to use',
        type=str)

    args = vars(aparser.parse_args())

    if args["media"] is None:
        print(HELP)
    else:
        print("Transcription:", sync_openai(**args))

if __name__ == "__main__":
    main()
