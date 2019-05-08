#!/usr/bin/env python3

import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('stunts_path', type=str, help='Path to Stunts',
                        default=r'D:\y-c-drive\games\STUNTS')
    parser.add_argument('beamng_path', type=str, help='Path to BeamNG',
                        default=r'D:\SteamLibrary\SteamApps\common\BeamNG.drive')
    parser.add_argument('stunts_tracks', type=str, nargs='+', help='Stunts track filenames to convert',
                        default='default.trk')
