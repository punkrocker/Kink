import argparse
from download import download_video


def download_channel(chanenl_name):
    url = 'https://www.kink.com/search?type=shoots&channelIds=' + chanenl_name + '&sort=published'
    pass


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Personal information')
    parser.add_argument('--channel', dest='channel', type=str, help='Name of the candidate')

    args = parser.parse_args()
    download_channel(args.channel)
