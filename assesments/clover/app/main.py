from app.file_utils import FileUtils
from app.parser import Parser


def main():
    data_files: dict[str, str] = FileUtils.files(directory="data", extension="txt")
    specs_files: dict[str, str] = FileUtils.files(directory="specs", extension="csv")
    parser = Parser()
    for file in data_files:
        if file in specs_files:
            print(f"Processing {file}")
            parser.load(data_path=data_files[file], spec_path=specs_files[file])
        else:
            print(f"file [{file}] has no specification file associated.")


if __name__ == "__main__":
    main()
