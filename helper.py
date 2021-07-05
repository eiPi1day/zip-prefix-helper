import zipfile
import argparse
import os
from struct import pack


def zip_dir(path, ziph):
    for root, dirs, files in os.walk(path):
        for file in files:
            ziph.write(os.path.join(root, file), os.path.relpath(os.path.join(root, file), path))


def create_zip(zip_path, output_path, prefix, sample):
    prefix_content = b""
    if sample is not None:
        assert os.path.isfile(sample), "not a file path"
        temp = b""
        with open(sample, "rb") as f:
            for line in f:
                temp += line
        if prefix < 0:
            prefix = len(temp)
            prefix_content = temp
        else:
            prefix_content = temp[:prefix]
        print("using file prefix of", f"'{sample}'", "with length :", prefix)
        print("file prefix:", prefix_content)
    elif prefix > 0:
        print("file prefix length:", prefix)
    else:
        print("prefix length can't be negative")
        return

    with zipfile.ZipFile(f'{output_path}', 'w', zipfile.ZIP_DEFLATED) as z:
        # zip file
        if os.path.isfile(zip_path):
            z.write(zip_path, os.path.basename(zip_path))
        elif os.path.isdir(zip_path):
            zip_dir(zip_path, z)
        # Changing Local Header Offset
        for info in z.infolist():
            print("Changing Local Header Offset of", f"'{info.filename}'")
            info.header_offset += prefix
        print("done")
    # Changing offset of Central Dir
    print("Changing Central Dir Offset")
    zip_content = b""
    with open(f'{output_path}', "rb") as f:
        for line in f:
            zip_content += line
    zip_content = zip_content[:-6] + \
                  pack("<I", int.from_bytes(zip_content[-6:-2], byteorder="little") + prefix) + \
                  zip_content[-2:]
    with open(f'{output_path}', "wb") as f:
        f.write(prefix_content + zip_content)
    print("All Done")
    os.system(f"xxd {output_path}")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-z", "--zip-path", required=True, help="set a path to one target file or folder")
    parser.add_argument("-p", "--prefix", type=int, required=True,
                        help="set prefix len you want to add to original zip")
    parser.add_argument("-s", "--sample", help="set path to sample of prefix file")
    parser.add_argument("-o", "--output", required=True, help="set output zip path")
    args = parser.parse_args()
    create_zip(zip_path=args.zip_path, output_path=args.output, prefix=args.prefix, sample=args.sample)
