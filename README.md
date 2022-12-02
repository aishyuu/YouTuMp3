# YouTuMp3
Download mp3 files from youtube links

I was motivated to do this because I no longer have spotify premium and I want to listen to music without having to copy and paste links and wait to do each step for one song only. I also want to have a streamlined way of downloading whole Youtube playlists.

__Features__
1. Can download a single song or a whole playlist
2. Can search for terms rather than youtube links
3. All saves in a custom folder that can be sorted by dates
4. Has a GUI version so you can download your favorite music with an interface

__Libraries Used__
1. sys
2. argparse
3. os
4. datetime
5. re
6. pytube

## How to use YouTuMp3

### Non-GUI
Once downloaded, run one of the following commands on your terminal

**For Single Song**
```
python youtump3.py -s *link or search term*
```

**For Playlist**
```
python youtump3.py -p *link*
```

### GUI

*coming soon*


* * *

MIT License

Copyright (c) 2022

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.